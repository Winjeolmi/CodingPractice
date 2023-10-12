# This is question 1.1

word = input()
word_set = set(word)

if len(word) == len(word_set):
    print("True")
else:
    print("False")

# Time complexity would be O(n)
