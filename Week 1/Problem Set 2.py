s = 'azcbobobegghakl'
needle = "bob"
count = 0

#you're ignoring the variable that's there. enumerate() allows you to iterate over the positions and characters of the string but we're not using the characters. Hence, we're only iterating over each of the positions in the string. You can also write for i, c in enumerate(haystack): to iterate over each position i and each character c (at the same time) of the string. 
for i, letter in enumerate(s):
    if s[i:i + len(needle)] == needle:
        count += 1

print ('Number of times bob occurs is: %d' % count)