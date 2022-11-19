import pandas as pd

strings = pd.read_csv('data/day5.csv', header =  None)[0].tolist()
nice = 0
banned_pairs = ['ab', 'cd', 'pq', 'xy']
vowles = ['a', 'e', 'i', 'o', 'u']

for s in strings:
    
    char_pairs = [s[i:i+2] for i in range(len(s)-1)]
    
    double = False
    for ch in char_pairs:
        if ch[0] == ch[1]:
            double = True
    
    char = [s[i] for i in range(len(s))]   
    vowel_test = [1 for x in char if x in vowles]

    if not any(x in char_pairs for x in banned_pairs) and \
        sum(vowel_test) >= 3 and \
           double:
               
               nice += 1

print(nice)

#RegEx solution!!!!      

#%% Part 2

import re

sum(1 for s in strings \
    if re.findall(r'(..).*\1', s) and \
        re.findall(r'(.).\1', s)
        )
