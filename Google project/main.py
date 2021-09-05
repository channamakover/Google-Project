from data.data_builder import DataBuilder
from data.data_manager import *
from auto_complete import *


def prepare_data(path):
    data = DataBuilder()
    try:
        sentences, sum_lines = build_data(path, data)
        print("complete reading sentences")
        print(f"read {sum_lines} lines")
        save_data(sentences, "/data/sentences.json")
    except MemoryError:
        pass

    save_data(data.get_trie(), "/data/data.json")


def start():
    while True:
        sub_seq = input("The system is ready, insert your text:")
        while sub_seq[-1] != END_INPUT:
            completes = get_best_complete(sub_seq, TRIE)
            print("here are {} suggestions:".format(len(completes)))
            for i in range(len(completes)):
                print(f"{i + 1}.", completes[i])
            sub_seq += input("\n" + sub_seq)


if __name__ == '__main__':
    # prepare_data("/2021-archive/python-3.8.4-docs-text/c-api")
    start()
