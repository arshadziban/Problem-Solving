#  Write a Python program that creates all possible strings using the letters
#  'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.

import random
c_list = ['a', 'e', 'i', 'o', 'u']
random.shuffle(c_list)


print(''.join(c_list))