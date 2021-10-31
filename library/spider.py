"""Module spider.
Define a generic spider class that extract information from a url using 
BeautifulSoup library
"""
import requests
from bs4 import BeautifulSoup as BS

class spider():
    """
        Class Spider to read URL and Interpret HTML
    """
    def __init__(self, url : str) -> None:
        """ Constructor: 
            Input: url: str -> String with the ulr to read
        """
        # Set Url
        self.url = url 
        # Set Soup (Reader and Manager of HTML file)
        self.soup = self.create_soup()

    def create_soup(self):
        """ Function to create a soup.
        """
        # Read Soup if possible, otherwise return None 
        try :
            soup = BS(requests.get(self.url).content, "html.parser")
        except:
            soup = None
        return soup
        