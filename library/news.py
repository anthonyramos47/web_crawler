

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
