from auto_complete.auto_complete_data import AutoCompleteData
from string_utils import *


def manage_completions(completions, score):
    n = len(completions)
    texts = [SENTENCES[comp[0]] for comp in completions]
    return set([AutoCompleteData(texts[i][0], texts[i][1], completions[i][1], score) for i in range(n)])


def get_5_leaves(trie, res):

    res += trie[ind(END)]

    if len(res) >= SUM_COMPLETE:
        return res[:SUM_COMPLETE]

    for child in trie[1:]:
        if child is not None:
            res = get_5_leaves(child, res)

    return res[:5]


def get_completions(trie, sub_seq):
    level, res = trie, []

    if len(sub_seq) == 0:
        return res

    for ch in sub_seq:
        level = level[ind(ch)]
        if level is None:
            return []

    return get_5_leaves(level, [])


def get_replaced(sub_seq, index, trie, sum_to_find):
    if len(sub_seq) == 0:
        return []

    res = []
    for ch in ALPHABET:
        res += get_completions(trie, sub_seq[:index] + ch + sub_seq[index + 1:])
        if len(res) >= sum_to_find:
            return res[:sum_to_find]
    return res


def get_deleted(sub_seq, index, trie, sum_to_find):
    if len(sub_seq) == 0:
        return []

    res = get_completions(trie, sub_seq[:index] + sub_seq[index + 1:])
    return res[:sum_to_find]


def get_append(sub_seq, index, trie, sum_to_find):
    if len(sub_seq) == 0:
        return []

    res = []
    for ch in ALPHABET:
        res += get_completions(trie, sub_seq[:index] + ch + sub_seq[index:])
        if len(res) >= sum_to_find:
            return res[:sum_to_find]
    return res


def get_best_complete(sub_seq, trie):

    best_score = 2 * len(sub_seq)
    replace_score = DECREMENT_SCORE["replace"]
    add_remove_score = DECREMENT_SCORE["add_or_remove"]

    # find compatible completions
    res = set(manage_completions(get_completions(trie, sub_seq), best_score))

    lack = SUM_COMPLETE - len(res)
    replace_index, add_remove_index = len(sub_seq) - 1, len(sub_seq) - 1

    while lack > 0 and (replace_index > -1 or add_remove_index > -1):
        if replace_index >= 0:
            replace_dec = replace_score[-1] if replace_index >= len(replace_score)\
                else replace_score[replace_index]
        else:
            replace_dec = best_score

        if add_remove_index >= 0:
            add_remove_dec = add_remove_score[-1] if add_remove_index >= len(add_remove_score)\
                else add_remove_score[add_remove_index]
        else:
            add_remove_dec = best_score

        if replace_dec < add_remove_dec and replace_index > -1:
            replace_i = get_replaced(sub_seq, replace_index, trie, lack)
            lack = SUM_COMPLETE - len(res)
            replace_index -= 1
            res.update(manage_completions(replace_i, best_score - replace_dec))

        else:
            delete_i = get_deleted(sub_seq, add_remove_index, trie, lack)
            res.update(manage_completions(delete_i, best_score - add_remove_dec))
            lack = SUM_COMPLETE - len(res)

            if lack > 0:
                append_i = get_deleted(sub_seq, add_remove_index, trie, lack)
                res.update(manage_completions(append_i, best_score - add_remove_dec))
                lack = SUM_COMPLETE - len(res)
            add_remove_index -= 1

    return sorted(list(res), reverse=True)



