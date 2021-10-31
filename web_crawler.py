
from library.sites_spider import * 
from library.data_manager import data_manager


def main():

    URL = "https://news.ycombinator.com"

    spidy = news_spider(URL)
    spidy.set_news()
    list_news = spidy.news
    dat_man = data_manager(list_news)
    dat_man.filt_tit_more_5_com_asc()
    dat_man.save_csv("op_data", "Filter_more")
    

if __name__ == "__main__":
    main()