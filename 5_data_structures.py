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
numbers.sort() # sort work inplace so we don't need to assign it to another variable

numbers.sort(reverse=True)

nsort = sorted(numbers) # this will not modify numbers

items = [
  ("product1", 10),
  ("product2", 11),
  ("product3", 12),
]
items.sort() # This will not change anything!
items.sort(key = lambda x: x[1]) # sort only takes keyword arguments!


