# as The function


def in_range(start, end, step=1):
    index = start
    if step == 0:
        raise ValueError
    if not int(step) or not int(start) or not int(end):
        raise ValueError
    while index < end if step > 0 else index > end:
        yield index
        index += step
    else:
        if (step > 0 and start >= end) or (step < 0 and start <= end):
            return []

#------------------------------------------------------------------------------------------------------------------------
# as The class


class In_Range:
    def __init__(self, start, end, step):
        self.start_point = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_point >= self.end:
            raise StopIteration
        crnt_point = self.start_point
        self.start_point += self.step
        return crnt_point


x = In_Range(1, 10, 5)
for i in x:
    print(i)
print(x)


