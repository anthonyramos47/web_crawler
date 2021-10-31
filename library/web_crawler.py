from os import name, write
from spider import *
import csv


def word_count_str(string):
    words = string.split(' ')
    return len(words)        

def extract_num(string: str)-> list:
    return int(''.join(filter(str.isdigit, string)))

def extract_num_str(string: str):
    return  str(''.join(filter(str.isdigit, string)))


class news():
    """ Class news. Describe one entry of Website https://news.ycombinator.com
        attributes:
            title: str
            order: int
            score: int
            comments: int
    """
    def __init__(self, title: str, order: int, score: int, comments: int )-> None:
        self.title = title
        self.order = order 
        self.score = score 
        self.comments = comments

    def __str__(self) -> str:
        return "{}> Title: {}\n    Score:{}\t Comments: {}\n".format(self.order, self.title, self.score, self.comments)


class data_manager():
    """ Class to manage data. This class will manage the filters and the sorters
    """
    def __init__(self, data: list) -> None:
        # Raw data imported 
        self.data = data  
        # Attribute where we store all modified data
        self.op_data = self.data

    def sort_news_asc(self, attrib: str)-> None:
        """ Ascending Sort according to attribute of data
        """
        self.op_data.sort(key=lambda ky: getattr(ky,attrib))

    def sort_news_desc(self, attrib: str)-> None :
        """ Descending Sort according to attribute of data
        """
        self.op_data.sort(key=lambda ky: getattr(ky,attrib), reverse= True)  
           
    def filter_news(self,attrib: str, __boolF)-> None:
        """ Method to filter data w.r.t attribute "attrib", and function __boolF (data.attrib -> bool)
        """
        self.op_data = filter(lambda new: __boolF(getattr(new, attrib)), self.op_data)

    def save_file(self, data: str, name_file: str)-> None:
        """ Method to save data in file. 
        """
        file_to_save = open(name_file+"_"+data+".txt", "w")
        for el in getattr(self, data):
            file_to_save.write(str(el))

    def save_csv(self, data: str, name_file: str )-> None:
        """  Method to save csv file of data. 
        """
        header = ["Rank", "Title", "Score", "Comments"]
        data = list(map( lambda n : [n.order, n.title, n.score, n.comments] , getattr(self,data)))
        with open(name_file+"_"+data+".csv", 'w', encoding= 'UTF8', newline='') as f:
            write = csv.writer(f)
            write.writerow(header)
            write.writerows(data)

    def show_data(self, attrib):
        """ Method to print the data. 
        """
        for el in getattr(self, attrib):
            print(el)
        

class news_spider(spider):
    """ Class news_spider to extract data from website. Inherited from class spider
        url: str
        news: list of news class
    """

    def __init__(self, url : str, news = []) -> None:
        spider.__init__(self, url)
        self.news = news
        self.calc = self.news

    def set_news(self)-> None:
        """ Setter of news
        """
        self.news = self.get_News()

    def dic_scores(self)-> dict:
        """ Create Dictionary of the form {"id": score: int}
        """
        # Create the dictionary
        dic = {} 
        # Filter with class "score"
        filt_class = self.soup.find_all(class_="score")
        # For all elements in filt class
        for el in filt_class:
            # Get the Id
            id = extract_num_str(el.attrs["id"])
            # Get the value of score
            val = extract_num(el.get_text())
            # Store information in dictionary
            dic[id] = val
        # Return Dictionary
        return dic

    def dic_comments(self)-> dict:
        """ Create Dictionary of the form {"id": comments: int}
        """
        # Create the dictionary
        dic = {}
        # Filter with href with string comments
        filt_class = self.soup.find_all("a", \
                href= lambda href:  href and "item?id" in href,\
                string = lambda text : "comments" in text.lower())
        # For all elements in filt class
        for el in filt_class:
            # Get the Id
            id = extract_num_str(el.attrs["href"])
            # Get the value of comments
            val = extract_num(el.get_text())
             # Store information in dictionary
            dic[id] = val
        # Return Dictionary
        return dic


    def get_News(self)-> list:
        """ Function to extract all the news entries in the webpage. 
        """

        # From the soup extract all the elements with class athing
        sites = self.soup.find_all("tr", class_="athing")
        # Get dictionary of id comments
        dic_scs = self.dic_comments()
        # Get dictionary of id scores
        dic_com = self.dic_scores()
        
        # Initialize list of news
        ls = []
        
        # For element in sites
        for pg in sites:
            # Get id
            id = pg.attrs["id"]
            # Get title
            title_n = pg.find("a", class_="titlelink").get_text() 
            # Get rank
            rank_n = extract_num(pg.find("span", class_="rank").get_text())
            # Get number of comments from dictionary of comments
            comm_n = self.set_val_news(dic_com, id)
            # Get scores of dictionary of scores
            score_n = self.set_val_news(dic_scs, id)
            # Append news to list
            ls.append(news(title= title_n, order= rank_n, comments= comm_n, score= score_n ))
        # Return list
        return ls

    def set_val_news(self, dic: dict, id: int) -> int:
        """ Set values of news from dictionary at id.
            Input: 
                dic: dict
                id: int
            Output:
                val int                
        """
        # In case no value found on dictionary assign value of 0
        try:
            val = dic[id]
        except:
            val = 0

        # Return value
        return val

    def show_sites(self)-> str:
        """ Function to show the list of news extracted from URL.
        """
        string = ""
        for el in self.news:
            string += str(el)+"\n"
        return string
    
    def __str__(self) -> str:
        return self.show_sites()    


def main():

    URL = "https://news.ycombinator.com"

    spidy = news_spider(URL)
    spidy.set_news()
    list_news = spidy.news
    dat_man = data_manager(list_news)
    dat_man.filter_news("title", lambda t: word_count_str(t) < 5 )
    dat_man.save_csv("op_data", "Filter_data")
    

main()