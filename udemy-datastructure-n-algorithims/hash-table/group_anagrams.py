from typing import List


def group_anagrams(strings: List) -> List:
    checker = {}
    output = []
    for string in strings:
        index = 0
        for c in string:
            index += ord(c)

        if not checker.get(index):
            checker[index] = []
        checker[index].append(string)

    for _, v in checker.items():
        output.append(v)
    return output


if __name__ == "__main__":

    print("1st set:")
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

    print("\n2nd set:")
    print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

    print("\n3rd set:")
    print(
        group_anagrams(
            ["listen", "silent", "triangle", "integral", "garden", "ranged"]
        )
    )

    """
        EXPECTED OUTPUT:
        ----------------
        1st set:
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

        2nd set:
        [['abc', 'cba', 'bac'], ['foo'], ['bar']]

        3rd set:
        [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

    """
