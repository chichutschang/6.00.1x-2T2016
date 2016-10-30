low = 0
high = 100
mid = int((low + high) /2)

print ("Please think of a number between " + str(low) + " and " + str(high)+ "!")
print ("Is your secret number " + str(mid) + " ?")
var = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while mid >= 1 and mid < 100:
    
    if var == 'c':
        print ("Game over. Your secret number was: " + str(mid))  
        break
        
    elif var == 'l':        
        low = mid
        mid = int((high + low) / 2)
        print ("Is your secret number " + str(mid) +"?")
        var = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
                                    
    elif var == 'h':
        high = mid
        mid = int((low + high) / 2)
        print ("Is your secret number " + str(mid) +"?")
        var = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
                                                                  
    else:
        print ("Sorry, I didn't understand your input")
        print ("Is your secret number " + str(mid) +"?")
        var = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
