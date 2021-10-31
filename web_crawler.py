""" Web Crawler Data Filtering and Sortering.
    Input: type of sorting, argument to sort, filter operation for words in title, type of output fle, name output file

    python web_crawler.py <Type of Sorting> <Argument to Sort> <Condition Number of Words> <Type of Output File> <Name of Output File>
"""
from library.sites_spider import * 
from library.data_manager import data_manager

import argparse

parser = argparse.ArgumentParser(description='Software to Filter Data extracted from Webpage: "https://news.ycombinator.com" ')
parser.add_argument('cond_words', type=str, help='Number of Word condition on title. Example: "< 5", "> 8", "<= 9", ">= 10" ')
parser.add_argument('type', type=str, help='Type of sorting (asc/ desc)',choices=['asc', 'desc'])
parser.add_argument('arg', type=str, help='Argument to Sort', choices=['order', 'score', 'comments'])
parser.add_argument('f_t', type=str, help='Type of Output File',choices=['csv', 'txt', 'out'])
parser.add_argument('name', type=str, help='Name of Output File')




def main():
    # paser 
    args = parser.parse_args()

    type_order = args.type
    arg_sort = args.arg
    file_type = args.f_t
    file_name = args.name
    condition_words = args.cond_words

    # Define URL of webpage
    URL = "https://news.ycombinator.com"

    # Initialize news_spider class
    spidy = news_spider(URL)
    # Set news of the site
    spidy.set_news()
    # Get list of news sites
    list_news = spidy.news
    # Initialize Data Manager
    dat_man = data_manager(list_news)
    # Filter Tittles with more than 5 words and order ascendingly by comments 
    dat_man.filt_title_words_sort(arg= arg_sort, opt= type_order, filter_text= condition_words)
    # Save data in csv and txt 
    if file_type == "csv":
        dat_man.save_csv("op_data", file_name)
    else:
        dat_man.save_file("op_data", file_name+"."+file_type)
   

if __name__ == "__main__":
    main()