import unittest
from library import news, data_manager
from library.sites_spider import news_spider
from library.utils import word_count_str


class TestSum(unittest.TestCase):

    def test_sort_desc(self):

        print("Test Sorting Descending")

        site1 = news(title  = "Short Title 1", order = 2, score = 100, comments = 500 ) 
        site2 = news(title  = "This is a Long Title for Testing 1", order = 3, score = 110, comments = 120 ) 
        site3 = news(title  = "Short Title 2", order = 4, score = 10, comments = 5 ) 
        site4 = news(title  = "This is a Long Title for Testing 2", order = 5, score = 0, comments = 1 ) 
        site5 = news(title  = "This is a Long Title for Testing 3", order = 1, score = 250, comments = 580 ) 

        sites = [site1, site2, site3, site4, site5]

        spider = news_spider("TESTURL", sites)
        
        data_news = spider.news 

        dat_man = data_manager(data_news)
        dat_man.sort_news_desc("comments")

        sorted_sites_comm_desc = list(map(lambda site: site.title , dat_man.op_data ))

        dat_man.clear_op_data()
        dat_man.sort_news_desc("score")

        sorted_sites_score_desc = list(map(lambda site: site.title, dat_man.op_data ))

        correct_sites_comm_desc = list(map(lambda site: site.title , [site5, site1, site2, site3, site4 ]))
        correct_sites_score_desc = list(map(lambda site: site.title , [site5, site2, site1, site3, site4 ]))

        self.assertEqual(sorted_sites_comm_desc, correct_sites_comm_desc, "Wrong Descending Order Comments")
        self.assertEqual(sorted_sites_score_desc, correct_sites_score_desc,"Wrong Descending Order Scores")

    def test_sort_asc(self):

        print("Test Sorting Ascending")

        site1 = news(title  = "Short Title 1", order = 2, score = 100, comments = 500 ) 
        site2 = news(title  = "This is a Long Title for Testing 1", order = 3, score = 110, comments = 120 ) 
        site3 = news(title  = "Short Title 2", order = 4, score = 10, comments = 5 ) 
        site4 = news(title  = "This is a Long Title for Testing 2", order = 5, score = 0, comments = 1 ) 
        site5 = news(title  = "This is a Long Title for Testing 3", order = 1, score = 250, comments = 580 ) 

        sites = [site1, site2, site3, site4, site5]

        spider = news_spider("TESTURL", sites)
        
        data_news = spider.news 

        dat_man = data_manager(data_news)
        dat_man.sort_news_asc("comments")

        sorted_sites_comm_asc = list(map(lambda site: site.title , dat_man.op_data ))

        dat_man.clear_op_data()
        dat_man.sort_news_asc("score")

        sorted_sites_score_asc = list(map(lambda site: site.title, dat_man.op_data ))

        correct_sites_comm_asc = list(map(lambda site: site.title , [site4, site3, site2, site1, site5]))
        
        correct_sites_score_asc = list(map(lambda site: site.title , [site4, site3, site1, site2, site5]))

        self.assertEqual(sorted_sites_comm_asc, correct_sites_comm_asc, "Wrong Ascending Order Comments")
        self.assertEqual(sorted_sites_score_asc, correct_sites_score_asc,"Wrong Ascending Order Scores")


    def test_filter_title(self):

        print("Test Filtering")
        #spider = news_spider("https://news.ycombinator.com")

        site1 = news(title  = "Short Title 1", order = 2, score = 100, comments = 500 ) 
        site2 = news(title  = "This is a Long Title for Testing 1", order = 3, score = 110, comments = 120 ) 
        site3 = news(title  = "Short Title 2", order = 4, score = 10, comments = 5 ) 
        site4 = news(title  = "This is a Long Title for Testing 2", order = 5, score = 0, comments = 1 ) 
        site5 = news(title  = "This is a Long Title for Testing 3", order = 1, score = 250, comments = 580 ) 

        sites = [site1, site2, site3, site4, site5]

        sites_short = set(map(lambda site: site.title ,[site1, site3]))
        sites_long = set(map(lambda site: site.title ,[site2, site4, site5]))

        spider = news_spider("TESTURL", sites)
        
        data_news = spider.news 

        dat_man = data_manager(data_news)
        dat_man.filter_news("title", lambda x : word_count_str(x) < 5 )
    
        filter_sites_short = set(map(lambda site: site.title , dat_man.op_data ))

        dat_man.clear_op_data()
        dat_man.filter_news("title", lambda x : word_count_str(x) > 5 )

        filter_sites_long = set(map(lambda site: site.title, dat_man.op_data))


        self.assertEqual(filter_sites_long, sites_long, "Wrong Filtering Long Strings")
        self.assertEqual(filter_sites_short, sites_short, "Wrong Filtering Short Strings")


if __name__ == '__main__':
    unittest.main()