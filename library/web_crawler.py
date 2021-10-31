from os import name, write
from .spider import *
import csv


def word_count_str(string):
    words = string.split(' ')
    return len(words)        

def extract_num(string: str)-> list:
    return int(''.join(filter(str.isdigit, string)))

def extract_num_str(string: str):
    return  str(''.join(filter(str.isdigit, string)))


class news():

    def __init__(self, title: str, order: int, score: int, comments: int )-> None: 
        self.title = title
        self.order = order 
        self.score = score 
        self.comments = comments

    def __str__(self) -> str:
        return "{}> Title: {}\n    Score:{}\t Comments: {}\n".format(self.order, self.title, self.score, self.comments)


class news_spider(spider):
    def __init__(self, url : str, news = []) -> None:
        spider.__init__(self, url)
        self.news = news
        self.calc = self.news

    def set_news(self)-> None:
        self.news = self.get_News()

    def dic_scores(self)-> dict:
        dic = {}
        filt_class = self.soup.find_all(class_="score")
        for el in filt_class:
            id = extract_num_str(el.attrs["id"])
            val = extract_num(el.get_text())
            dic[id] = val
        return dic

    def dic_comments(self)-> dict:
        dic = {}
        filt_class = self.soup.find_all("a",  href= lambda href:  href and "item?id" in href, string = lambda text : "comments" in text.lower())
        for el in filt_class:
            id = extract_num_str(el.attrs["href"])
            val = extract_num(el.get_text())
            dic[id] = val
        return dic


    def get_News(self)-> list:

        pages = self.soup.find_all("tr", class_="athing")
        dic_scs = self.dic_comments()
        dic_com = self.dic_scores()
        
        ls = []
        for pg in pages:
            id = pg.attrs["id"]
            title_n = pg.find("a", class_="titlelink").get_text() 
            rank_n = extract_num(pg.find("span", class_="rank").get_text())
            comm_n = self.set_val_news(dic_com, id)
            score_n = self.set_val_news(dic_scs, id)
            ls.append(news(title= title_n, order= rank_n, comments= comm_n, score= score_n ))

        return ls

    def set_val_news(self, dic: dict, id: int) -> int:
        try:
            val = dic[id]
        except:
            val = 0
        return val

    def __str__(self) -> str:
        return self.show_pages(self.news)
    

    def show_pages(self, ls_news: str)-> str:
        string = ""
        for el in ls_news:
            string += str(el)+"\n"
        return string

    def print_pages(self, ls_news: str)-> None:
        print(self.show_pages(ls_news))

    def save_pages(self, ls_news: news, name_file: str)-> None:
        file_to_save = open(name_file, "w")
        file_to_save.write(self.show_pages(ls_news))

    def save_csv(self, ls_news: news, name_file: str )-> None:
        header = ["Rank", "Title", "Score", "Comments"]
        data = list(map( lambda n : [n.order, n.title, n.score, n.comments] , ls_news))
        with open(name_file+str(".csv"), 'w', encoding= 'UTF8', newline='') as f:
            write = csv.writer(f)
            write.writerow(header)
            write.writerows(data)


def main():

    URL = "https://news.ycombinator.com"

    spidy = news_spider(URL)
    spidy.set_news()
    ls_news = spidy.news
    filt = spidy.filter_news(ls_news, "title", lambda x : word_count_str(x) > 5)
    sort = spidy.sort_news_desc(filt, "score")
    spidy.save_pages(sort,"Desc_order.txt")
    spidy.save_csv(sort, "Desc_order")
    

main()