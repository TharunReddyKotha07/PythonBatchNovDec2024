import cProfile

data_list = list(range(10_000_000))
cProfile.run("9_999_999 in data_list")  # O(N)


data_set = set(range(10_000_000))
cProfile.run("9_999_999 in data_set")  # O(1)

print()


# But, creating a set is a bit slower than creating a list
print("CREATING A LIST")
cProfile.run("list(range(10_000_000))")  # 0.370 sec

print("CREATING A SET")
cProfile.run("set(range(10_000_000))")  # 0.770 s


"""
NOTE:
    -- When we have MORE reads, go for set/dict
    -- When we have MORE writes, go for List/np.array
    - when only one time writing, but need to preserve order, go with tuples
    

"""