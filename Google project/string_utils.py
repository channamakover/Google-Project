import re

from constants import *


def ind(ch):
    """ :return index of char in trie node """
    ch = ch.lower()
    if ch.isalpha():
        return ord(ch) - ord("a") + NUM_SPECIAL_CH
    elif ch.isnumeric():
        return ord(ch) - ord("0") + NUM_ALPHAS + NUM_SPECIAL_CH
    if ch == " ":
        return SPACE_INDEX
    return END_INDEX


def char(index):
    """ :return char represented by index in trie node """
    if index == SPACE_INDEX:
        return " "
    if index == END_INDEX:
        return END
    if index < NUM_ALPHAS + NUM_SPECIAL_CH:
        return chr(index + ord("a"))
    return chr(index + ord("0"))


def get_all_suffixes(s):
    """generator function to generate all suffixes of a string"""
    for i in range(len(s) - 1):
        yield s[i:], i


def generic_string(s):
    """
    remove extra spaces, ignore cases, ignore comets
    :param s: string
    :return: generic string
    """
    s = "".join([ch for ch in s if ch.isnumeric() or ord("a") <= ord(ch.lower()) <= ord("z") or ch == " "])
    return re.sub(' +', ' ', s) + END
