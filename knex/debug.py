from typing import List

__debug_list = []


def init_debug(debug_list: List[str]= []):
    global __debug_list
    __debug_list = debug_list


def debug(name: str):
    global __debug_list
    return name in __debug_list or 'all' in __debug_list