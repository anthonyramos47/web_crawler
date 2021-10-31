"""Module data_manager.
Here is encoded the class data_manager, that allow us to perform operations 
on the data extracted with the spider class
"""
from .news import news
from .utils import comparator, parse_logic_op, word_count_str
import csv

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
        self.op_data = list(filter(lambda new: __boolF(getattr(new, attrib)), self.op_data))

    def save_file(self, data: str, name_file: str)-> None:
        """ Method to save data in file. 
        """
        file_to_save = open(name_file, "w")
        for el in getattr(self, data):
            file_to_save.write(str(el))

    def save_csv(self, data: str, name_file: str )-> None:
        """  Method to save csv file of data. 
        """
        header = ["Rank", "Title", "Score", "Comments"]
        data_mat = list(map( lambda n : [n.order, n.title, n.score, n.comments] , getattr(self,data)))
        with open(name_file+".csv", 'w', encoding= 'UTF8', newline='') as f:
            write = csv.writer(f)
            write.writerow(header)
            write.writerows(data_mat)
    
    def show_data(self, attrib):
        """ Method to print the data. 
        """
        for el in getattr(self, attrib):
            print(el)

    def clear_op_data(self):
        self.op_data = self.data
        
    ##--------------------------------METHODS TO SOLVE CHALLENGE----------------------------------#
    def filt_title_words_sort(self, arg: str, opt: str, filter_text: str):
        """ Method to filter data with more than 5 words in title and ascending order by score
        """
        operation, num = parse_logic_op(filter_text)

        # Filter titles with more than 5 words
        self.filter_news("title", lambda t: comparator(word_count_str(t), num, operation) )
        # Sort data by score 
        if opt.lower() == "asc": 
            self.sort_news_asc(arg)
        elif opt.lower() == "desc":
            self.sort_news_desc(arg)