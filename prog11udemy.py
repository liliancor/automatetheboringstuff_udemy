############# INPUT VALIDATION ##############
#print('How many cats do you have?')
numcats = input('How many cats do you have?')
try: 
    if int(numcats) >= 4:
        print("WOW! That's a lot and I have nothing to do with it.")
    else: 
        print("That's a not a lot and I have nothing to do with it.")
except ValueError:
    print('You did not enter a number.')            
