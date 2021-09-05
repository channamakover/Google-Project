from data.data_manager import load_data


def load():
    sentences = load_data("/data/sentences.json")
    trie = load_data("/data/data.json")
    return sentences, trie


NUM_CHARS = 38

NUM_ALPHAS = 26

NUM_SPECIAL_CH = 2

SPACE_INDEX = 1

END_INDEX = 0

MAX_SUB_SEQ = 20

SUM_COMPLETE = 5

END = "$"

END_INPUT = "#"

ALPHABET = [" "] + [chr(code) for code in range(ord("a"), ord("z") + 1)]

SENTENCES, TRIE = load()

DECREMENT_SCORE = {
    "replace": [5, 4, 3, 2, 1],
    "add_or_remove": [10, 8, 6, 4, 2]
}
