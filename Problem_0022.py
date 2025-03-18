# Longest Substring Without Repeating Characters
def length_of_longest_substring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1  

        char_index[s[right]] = right  
        max_length = max(max_length, right - left + 1)  

    return max_length

# Example Usage
s = "abcabcbb"
print(length_of_longest_substring(s)) 
