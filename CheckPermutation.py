# This is question 1.2

def check_permutation(word_one, word_two):
    is_permutation = False
    word_one_list = []
    word_two_list = []

    for c in word_one:
        word_one_list.append(ord(c))

    for c in word_two:
        word_two_list.append(ord(c))

    word_one_list.sort()
    word_two_list.sort()

    if word_one_list == word_two_list:
        is_permutation = True

    return is_permutation


word1 = input("Enter 1st word: ")
word2 = input("Enter 2nd word: ")
print(check_permutation(word1, word2))

# Time Complexity is 0(n)
