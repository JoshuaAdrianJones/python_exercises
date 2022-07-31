import numbers
from typing import List

def sortList(list_of_numbers: List[float]):
    """
    given a list of numbers return the same numbers in order from smallest to largest
    """
    sorted_list = sorted(list_of_numbers)
    return sorted_list