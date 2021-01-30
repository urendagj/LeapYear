#to run the program type in the following: python3 Jacob_UrendaGaribay_hw1.py
def isint(message):
  while True:
    try:
       isleap = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return isleap 
       break 

#year = input("Enter in a year: ")
isleap = isint("Enter in a year: ")
if isleap > 0:
    if (isleap % 4) == 0 and (isleap % 100) != 0:
        print(isleap, "is a leap year")
    elif (isleap % 400) == 0:
        print(isleap, "is a leapyear")
    elif (isleap % 100) == 0:
        print(isleap, "is not a leapyear")
    else:
        print(isleap, "is not a leapyear")
else:
    print(isleap, "is not a valid year")
            