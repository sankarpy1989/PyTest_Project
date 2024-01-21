import itertools
import operator

# Infinite Iterators

# 1) count(start, step)

for i in itertools.count(4, 2):
    if i > 10:
        break
    else:
        print(i)

# 2) cycle(iterable)

l = ["Jai", "Siri", "Anvitha"]
cycle_values = itertools.cycle(l)
for i in range(8):
    print(next(cycle_values))


# 3) repeat(element, n)

for i in itertools.repeat(123, 4):
    print(i)


# Combinatorics Iterators

# 1) product()

print(list(itertools.product("ABC", repeat=2)))
#
print(list(itertools.product([1, 2, 3], [7, 8, 9])))
#
print(list(itertools.product("AB", "CD", repeat=2)))


# 2) permutations(iterable, group_size)

l = [1, 2, 3]
print(list(itertools.permutations(l, 2)))

print(list(itertools.permutations(l)))


# 3) combinations(iterable, size)

l = [1, 2, 3, 4]
print(list(itertools.combinations(l, 2)))

print(list(itertools.combinations(l, 3)))


# # 4) combinations_with_replacement(iterable, size)

l = [1, 2, 3]
print(list(itertools.combinations_with_replacement(l, 2)))

print(list(itertools.combinations_with_replacement(l, 3)))

# 3) Terminating iterators

# 1) accumulate(iterable[, func])
# data = [1, 2, 3, 4, 5]
# result = itertools.accumulate(data, operator.mul)
# for each in result:
#     print(each)

# 2) chain(*iterables)
# list_one = ['a', 'b', 'c']
# list_two =['d', 'e', 'f']
# list_three = ['1', '2', '3']
#
# result = itertools.chain(list_one, list_two, list_three)
#
# for element in result:
#     print(element)

# 3) chain.from_iterable(iterable)
# creating 3 iterables
# l1 = [1, 2, 3, 4]
#
# l2 = [2, 4, 6, 8]
#
# l3 = [3, 9, 12, 15]
#
# # creating a list of lists as a single iterator
# l = [l1, l2, l3]
#
# print("All values in the chain are : ", end="")
# print(list(itertools.chain.from_iterable(l)))

# 4) compress(data, selectors)
# names = ['Alice', 'James', 'Matt']
# have_flu = [True, True, False]
#
# result = itertools.compress(names, have_flu)
#
# for element in result:
#     print(element)

# 5) dropwhile(predicate, iterable)

# my_list = [0, 0, 1, 2, 0]
#
# result = itertools.dropwhile(lambda x: x == 0, my_list)
#
# for elements in result:
#     print(elements)

# 6) filterfalse(predicate, iterable)
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
# result = itertools.filterfalse(lambda x: x<5, data)
# for each in result:
#     print(each)

# 7) groupby(iterable, key=None)
# robots = [
#     {"name": "blaster", "faction": "autobot"},
#     {"name": "galvatron", "faction": "decepticon"},
#     {"name": "jazz", "faction": "autobot"},
#     {"name": "metroplex", "faction": "autobot"},
#     {"name": "megatron", "faction": "decepticon"},
#     {"name": "starcream", "faction": "decepticon"},
# ]
# for key, group in itertools.groupby(robots, key=lambda x: x['faction']):
#     print(key)
#     print(list(group))

# 8) islice(iterable, start, stop[, step])
# colors = ['red', 'orange', 'yellow', 'green', 'blue',]
# few_colors = itertools.islice(colors, 2)
# for each in few_colors:
#     print(each)
# 9) pairwise(),
# 10) starmap(function, iterable)
# import operator
# data = [(2, 6), (8, 4), (7, 3)]
# result = itertools.starmap(operator.mul, data)
# for each in result:
#     print(each)

# 11) takewhile(predicate, iterable)
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
# result = itertools.takewhile(lambda x: x<5, data)
# for each in result:
#     print(each)
# 12) tee(iterable, n=2)
# colors = ['red', 'orange', 'yellow', 'green', 'blue']
# alpha_colors, beta_colors = itertools.tee(colors)
# for each in alpha_colors:
#     print(each)
# 13) zip_longest(*iterables, fillvalue=None)
colors = ['red', 'orange', 'yellow', 'green', 'blue',]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
for each in itertools.zip_longest(colors, data, fillvalue=None):
    print(each)