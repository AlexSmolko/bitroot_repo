from _collections_abc import Iterable


def with_index(iterable, start=0):
    if not isinstance(iterable, Iterable):
        raise TypeError(f"{iterable} should be an iterable by itself")
    if start >= len(iterable):
        raise ValueError
    n_indx = start
    for item in iterable:
        yield n_indx, item
        n_indx += 1


our_list = [13, 26, 52, 104, 208, 416, 832, 1664]

for count, element in with_index(our_list, 1):
    print(count, element)

