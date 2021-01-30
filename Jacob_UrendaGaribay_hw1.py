year = input("Enter in a year: ")
isleap = int(year)
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
            



