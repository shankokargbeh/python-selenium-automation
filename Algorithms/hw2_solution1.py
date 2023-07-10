def split_in_half(s):
    length = len(s)
    half = length // 2
    add = 0
    if length % 2:
        add = 1
        left = s[:half + add]
        right = s[half + add:]
        return right + left
test_string_odd = "bbbcaaa"
test_string_even = "aaabbb"
print(split_in_half(test_string_odd))
print(split_in_half(test_string_even))
