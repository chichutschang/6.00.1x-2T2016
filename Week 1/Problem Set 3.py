#s = 'azcbobobegghakl'
i = 0
temp = s[i]
longest = s[i]

for i in range(1, len(s)):
            
    if s[i-1] <= s[i]:
        temp += s[i]
    
    else:
        temp = s[i]   
    
    if len(temp) > len(longest):
        longest = temp                
                                                                
print ('Longest substring in alphabetical order is: %s' % longest)