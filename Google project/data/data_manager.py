import json
import os


def build_data(path, data):
    path = os.getcwd() + path
    lines = []
    i = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            print(file)
            with open(os.path.join(root, file), encoding='utf') as f:
                for line in f:
                    try:
                        data.analyze_line(line, i)
                        lines.append((line.replace("\n", ""), file))
                        i += 1
                    except MemoryError:
                        return lines, i - 1
    return lines, i


def save_data(data_dict, path):
    with open(os.getcwd() + path, "w") as json_file:
        json.dump(data_dict, json_file)


def load_data(path):
    with open(os.getcwd() + path, "r") as json_file:
        return json.load(json_file)
