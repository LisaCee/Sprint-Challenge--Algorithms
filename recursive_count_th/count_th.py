'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) < 2:
        return 0
    else:
        count = 0
        i = 0
        if word[i:i+2] == "th":
            count += 1
            i += 2
        else:
            count(word)
    return count
