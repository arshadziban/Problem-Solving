# Group Anagrams
from collections import defaultdict

def group_anagrams(words):
    anagram_dict = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word))  
        anagram_dict[sorted_word].append(word)

    return list(anagram_dict.values())

# Example usage
words = ["listen", "silent", "rat", "tar", "god", "dog", "evil", "vile", "live"]
print(group_anagrams(words))
