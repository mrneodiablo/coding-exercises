if __name__ == "__main__":
    my_set = {1, 2, 3, 4, 5}
    print(my_set)
    my_set.add(5)
    print(my_set)
    my_set.remove(1)
    print(my_set)

    other_set = {3, 10, 5, 6}
    union_set = my_set.union(other_set)
    print(union_set)
