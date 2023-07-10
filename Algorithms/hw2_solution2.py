def unique_char_str(s):
    lenstr = len(s)
    lenset = len(set(s))
    return lenset == lenstr



test_data_pos = "abcde" #true
test_data_neg = "abcdee" #false
print(unique_char_str(test_data_pos))
print(unique_char_str(test_data_neg))
