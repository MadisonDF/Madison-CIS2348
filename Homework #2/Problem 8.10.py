# Madison Fletcher
# 1868748
word = input()
word2 = word.replace(' ', '')
if word2 == word2[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
