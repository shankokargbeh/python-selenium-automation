# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z and it's not a palindrome.

# o(n)
def is_almost_palindrome(s):
    for i in range(len(s)):
        curstr = s[:i] + s[i + 1:]
        if curstr == curstr[::-1]:
            return True
    return False

print(is_almost_palindrome("radkar"))
print(is_almost_palindrome("radario"))