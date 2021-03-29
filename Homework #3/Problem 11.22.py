# Madison Fletcher
# 1868748

count = {}
words = str(input())
word = words.split()
for x in word:
    frequency = word.count(x)
    print(x, frequency)
