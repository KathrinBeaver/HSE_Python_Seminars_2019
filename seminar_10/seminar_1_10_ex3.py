# map
words = ["dog", "frog", "cat", "tiger"]
print(list(map(len, words)))    # [3, 4, 3, 5]

print(list(map(lambda x, y: x * y, [1, 2], [3, 4, 5]))) # [3, 8]

# zip
a = [1, 2]
b = [3, 4]
print(list(zip(a, b))) # [(1, 3), (2, 4)]