def is_anagram(word1, word2):
    # return count_is_anagram(word1, word2)
    return sort_is_anagram(word1, word2)


def count_is_anagram(word1, word2):
    letter_count = {}
    word1 = word1.lower()
    word2 = word2.lower()
    for letter in word1:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    for letter in word2:
        if letter not in letter_count or letter_count[letter] == 0:
            return False
        else:
            letter_count[letter] -= 1
    return not any(letter_count.values())


def sort_is_anagram(word1, word2):
    word1 = sorted(word1.lower())
    word2 = sorted(word2.lower())

    return word1 == word2
