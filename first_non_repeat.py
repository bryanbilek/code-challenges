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

#summary: keep a count of the chars in a hash table & put them in order into a list so we can reference the first char in our list that has a count of 1, thus the first non-repeating char

def first_not_repeating_character(s):
    # chars dict to store the chars as a key with their count as a value
    chars = {}
    # non_repeat to send the values in s that dont have a count already
    non_repeat = []
    # for each char in s, if is in chars dict, add it's count by 1

    for char in s:
        if char in chars:
            chars[char] += 1
        else:
    # otherwise add it to chars dict with a count of 1 & append that char to our non_repeat list
            chars[char] = 1
            non_repeat.append(char)
    # for each character in non_repeat list, because appended in order we can look up the count & the first character with a count of 1 will be returned
    for char in non_repeat:
        if chars[char] == 1:
            return char
    # if none of the conditions were met then we return the last edge case
    return '_'

#Time complexity: O(n) - linear because our main for loop would change based on the input size of s

#Space complexity: O(n) - linear because we created a dict as well as an array that would change sizes based on the input size of s
