"""
Purpose: Profiling with memory profiler

    pip install memory_profiler psutil

"""

from memory_profiler import profile


@profile
def func1():
    mylist1 = []
    for i in range(10_000):
        mylist1.append(i)


@profile
def memory_intensive():
    small_list = [None] * 10
    big_list = [None] * 10000000
    del big_list
    return small_list


@profile
def my_func():
    a = [1] * (10**6)
    b = [2] * (2 * 10**7)
    del b
    return a


@profile(precision=4)
def my_func2():
    a = [1] * (10**6)
    b = [2] * (2 * 10**7)
    del b
    return a


if __name__ == "__main__":
    func1()
    memory_intensive()
    my_func()
    my_func2()

# Assignment : TRy for a method in a class, and entire class


from memory_profiler import profile


class MemoryTest:
    @profile
    def method_one(self):
        my_list = [i for i in range(10_000)]
        del my_list

    @profile
    def method_two(self):
        big_list = [None] * 10_000_000
        del big_list


@profile  # Profiling the entire class
class MemoryTestWholeClass:
    def __init__(self):
        self.data = [1] * (10**6)

    def process_data(self):
        big_data = [2] * (2 * 10**7)
        del big_data

    def finalize(self):
        self.data = None


if __name__ == "__main__":
    # Profiling individual methods
    tester = MemoryTest()
    tester.method_one()
    tester.method_two()

    # Profiling the entire class
    whole_tester = MemoryTestWholeClass()
    whole_tester.process_data()
    whole_tester.finalize()
