# lists:

letters = ["a", "b", "c"]
nested_lists = [[0, 1], [2, 3]]

l = [0] * 100
x = [[0] * 100 for _ in range(10)]

# this is different from:
y = [[0] *100] * 10

combined = letters + l

# convert iterable to list:
numbers = list(range(10))

chars = list("hello world!')
len(chars)

# accessing items:
letters[0]
letters[-1]

letters[0] = "A"

# slicing a string:
letters[0:3]
letters[:3]
letters[1:]

letters[::2]

numbers = list(range(20))
numbers[::2]

# return elements in reverse order:
numbers[::-1]

# list unpacking:
numbers = [1,2,3]
first, second, third = numbers

numbers = [1,2,3, 4, 4, 4]
first, second, *other = numbers
first, *other, last = numbers

# loop over lists:
for l in letters:
  print(l)

for i, l in enmuerate(letters):
  print(i, l)

items = [0, "a"]
items = (0, "a")
index, letter = items

# Adding/removing items from list:
letters.append("d")
letters.insert(0, "-")

# remove the last item
letters.pop()
letters.pop(0) # remove first item

letters.remove("b") # remove first occurrence of "b"
del letters[0]
del letters[0:3]

letters.clear() # Remove all items in a list.

# finding items:
letters.index("a")
letters.index("z") # this will get error if "z" is not in the list

if "d" in letters:
  letter.index("d")

letters.count("d")

# sorting lists:
numbers = [3, 51, 2, 8, 6]
numbers.sort() # sort work in place so we don't need to assign it to another variable

numbers.sort(reverse=True)

nsort = sorted(numbers) # this will not modify numbers

items = [
  ("product1", 10),
  ("product2", 11),
  ("product3", 12),
]
items.sort() # This will not change anything!
items.sort(key=lambda x: x[1]) # sort only takes keyword arguments!

# lambda functions:
lambda: parameter: expression

# map functions:
prices = []
for item in items:
  prices.append(item[1])

prices = list(map(lambda x: x[1], items))

# filter function:
prices = list(filter(lambda x: x[1]>11, items))

# list comprehensions:
prices = [item[1] for item in items]
prices = [item[1] for item in items if item[1] > 11]

# zip functions:
list1 = [1,2,3]
list2 = [11,22,33]

combined_list = list(zip(list1, list2))
combined_list = list(zip("ABC", list1, list2))

# stack: LIFO last in first out
stack = [1, 2, 3]
stack.append(4)
stack.pop()

# check if stack is empty:
if not stack:
  print("stack is empty")

if stack:
  print(stack[-1]) # is stack is empty, we will have an error

# queue: FIFO first in first out
queue = [1, 2, 3]
queue.pop(0)

# every time we remove the first item, all the following items must be moved forward. So we use deque:
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

if not queue:
  print("queue is empty")

# tuple: a read-only list, cannot modify or add/remove elements to/from it
point = 1, 2
point = (1, 2)
point = 1,
point = ()
print(type(point))

point = (1, 2) + (3, 4) # (1, 2, 3, 4)
point = (1, 2) * 3 # (1, 2, 1, 2, 1, 2)

point = tuple([1, 2])
t = tuple("hello world")

point = (1, 2, 3)
point[:2]

x, y, z = point

if 10 in point:
  print("exists")

point[0] = 10 # This will throw an error as a tuple is immutable.

# swap two variables:
x = 10
y = 11

z = x
x = y
y = z

# Swap x and y by using tuple
x, y = y, x

a, b = 1, 2

# arrays: dealing with large sequences of numbers.
from array import array

numbers = array("i", [1, 2, 3])
numbers.append(4)
numbers.insert(0, 0)
numbers.pop()
numbers.remove(3)

# objects in array are typed. cannot add floats or strings to int array.

# sets:

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 4}
second.add(5)
second.remove(5)
len(second)

first | second # union of two sets
first & second # intersection of two sets
first - second # in first but not second
first ^ second # either in first or second but not both

# sets do not support indexing as it is unordered:
first[0] # ERROR

if 1 in first:
  print("yes")

# dictionary:


