# Write a function to check whether two given strings are anagram of each other or not.
# An anagram of a string is another string that contains the same characters, only the order
# of characters can be different. For example, “abcd” and “dabc” are an anagram of each other.

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        print("False")
        return

    if sorted(s1) == sorted(s2):
        print("True")
    else:
        print("False")

    # return sorted(s1) == sorted(s2)

# is_anagram("abcd", "adcb")  # True
# is_anagram("abcde", "adcbe")  # True
#
# is_anagram("abcd", "aabc")  # False
# is_anagram("abcd", "abbc")  # False

is_anagram("abcd", "abc")  # False
# is_anagram("abcd", "1234")  # False
#
# is_anagram("", "")  # True
#
# is_anagram("abcd", "Abcd")  # False