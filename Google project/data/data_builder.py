from dataclasses import dataclass
from typing import List

from string_utils import *


@dataclass
class Completion:
    sentence_index: int
    offset: int


def empty_array():
    arr = [None] * NUM_CHARS
    arr[ind(END)] = []
    return arr


class DataBuilder:

    def __init__(self):
        self.__trie = empty_array()
        # self.sum_lines = 0
        # print("building")
        # for i in range(len(data)):
        #     try:
        #         self.analyze_line(data[i][0], i)
        #         self.sum_lines += 1
        #         print(i)
        #
        #     except MemoryError as e:
        #         raise e

    def analyze_line(self, sentence, index):
        """
        add all suffix of sentence to dict
        :param sentence: String
        :param index: index of sentence in array
        """
        try:

            # generate a generic string from sentence
            sentence = generic_string(sentence)

            # insert all suffixes into the trie
            for sub_seq, offset in get_all_suffixes(sentence):
                comp = (index, offset)
                level = self.__trie

                for ch in sub_seq[:-1]:
                    if level[ind(ch)] is None:
                        level[ind(ch)] = empty_array()
                    level = level[ind(ch)]

                if len(level[ind(END)]) < SUM_COMPLETE:
                    level[ind(END)].append(comp)

        except MemoryError as e:
            raise e

    def get_trie(self):
        return self.__trie
