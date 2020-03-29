def count_number(word):
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    return count


print(count_number('banana'))
