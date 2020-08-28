# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

# Example

# For s = "abacabad", the output should be
# first_not_repeating_character(s) = 'c'.

# There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

# For s = "abacabaabacaba", the output should be
# first_not_repeating_character(s) = '_'.

# There are no characters in this string that do not repeat.

# [execution time limit] 4 seconds (py3)

# [input] string s

# A string that contains only lowercase English letters.

# [output] char

# The first non-repeating character in s of '_' if there are no characters that do not repeat.


def first_not_repeating_character(s):
    # chars dict to store the chars as a key with their count as a value
    # non_repeat to send the values in s that dont have a count already
    chars = {}
    non_repeat = []
    # for each char in s, if is in chars dict, add it's count by 1
    # otherwise add it to chars dict with a count of 1 & append that char to our non_repeat list
    for char in s:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
            non_repeat.append(char)
    # for each character in non_repeat list, if the char value(count) is 1, return it
    for char in non_repeat:
        if chars[char] == 1:
            return char
    # if none of the conditions were met then we return the last edge case
    return '_'
