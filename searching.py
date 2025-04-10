import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return

    with open(file_path) as file:
        data = json.load(file)
        return data[field]


# best O(n) worst O(n)
def linear_search(seq: list[int], to_find: int) -> dict[str: list[int], str: int]:
    output = {"positions" : [],
              "count" : 0}

    for pos, number in enumerate(seq):
        if number == to_find:
            output["positions"].append(pos)
            output["count"] += 1

    return output


def pattern_search(seq: str, pattern: str) -> set[int]:
    output = set()

    for i in range(len(seq)):
        if i >= len(seq) - len(pattern):
            break

        if seq[i:i + len(pattern)] == pattern:
            output.add(i)

    return output


def binary_search(seq: list[int], to_find: int) -> int | None:
    left = 0
    right = len(seq)

    while left < right:

        middle = (left + right) // 2

        if seq[middle] == to_find and seq[middle - 1] == to_find:
            right -= 1
        elif seq[middle] == to_find:
            return middle
        elif to_find < seq[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return


def main():
    print(read_data("sequential.json", "ordered_numbers"))
    # print(linear_search(read_data("sequential.json", "unordered_numbers"), 9))
    # print(pattern_search(read_data("sequential.json", "dna_sequence"), "ATA"))

    number = 14
    print("moja funkcia:\t\t", binary_search(read_data("sequential.json", "ordered_numbers"), number))
    print("index of funkcia:\t", read_data("sequential.json", "ordered_numbers").index(number))

if __name__ == '__main__':
    main()