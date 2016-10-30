s = 'azcbobobegghakl'
vowel = ['a' , 'e' , 'i' , 'o' , 'u'] 
count = 0
for letter in s:
    if letter in vowel:
        count += 1
    
print ('Number of vowels: %d' % count)
    