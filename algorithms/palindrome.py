def is_palindrome(word: str):
    return word == word[::-1]


if __name__ == '__main__':
    print(is_palindrome('osso'))
    print(is_palindrome('amar'))