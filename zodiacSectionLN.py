def zodiac():
    year = int(input("Enter your birth year: "))

    if year < 1900:
        print("Year should not be earlier than 1900!")
    elif year >= 1900:
        animals = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox",
                   "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"]
        sign = animals[year % 12]
        print("Your zodiac sign is " + sign + ".")
    else:
        print("Invalid input. Please enter a valid year.")
        

zodiac()