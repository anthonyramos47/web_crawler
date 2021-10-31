""" Utils functions.
"""

def word_count_str(string)-> int:
    words = string.split(' ')
    return len(words)        

def extract_num(string: str)-> list:
    return int(''.join(filter(str.isdigit, string)))

def extract_num_str(string: str)-> str:
    return  str(''.join(filter(str.isdigit, string)))
