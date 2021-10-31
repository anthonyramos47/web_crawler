""" Utils functions.
"""
import operator

# Dic of operations avaliable for comparison
operations = {
    "<": operator.lt,
    "<=": operator.le,
    ">": operator.gt,
    ">=": operator.ge
}

def parse_logic_op(string: str)-> tuple:
    """ Function to parse a string of the type "< 5", ">= 6", ">= 8". 
    Ouput: operation:str , number: int.
    """
    num = extract_num(string)
    op = extract_op(string)
    return op, num

def comparator(el1:int , el2: int, read_op: str)-> bool:
    """ Function that transform operation in str to real comparison operation. 
    Input: el1: int, el2: int, read_op: str
    Output: Bool
    """
    # Get operation from dictionary of operations
    operation = operations[read_op]
    # Return operation output
    return operation(el1, el2)

def word_count_str(string)-> int:
    """ Function to count the words in a string.
    """
    words = string.split(' ')
    return len(words)        

def extract_op(string: str)-> list:
    """ Function to extract the order operation from a string.
    """
    return str(''.join(filter(lambda st: st in operations , string)))

def extract_num(string: str)-> list:
    """ Function to extract and convert to int num from string.
    Output: Number: int
    """
    return int(''.join(filter(str.isdigit, string)))

def extract_num_str(string: str)-> str:
    """ Function to extract number from string.
    Output: string with the number
    """
    return  str(''.join(filter(str.isdigit, string)))
