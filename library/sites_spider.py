#from os import name, write
from .spider import *
from .news import news
from .utils import extract_num, extract_num_str, word_count_str

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