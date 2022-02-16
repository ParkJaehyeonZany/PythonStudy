weather = {
    'Mon' : (7,-6),
    'Tue' : (6,-7),
    'Wed' : (1,-8),
    'Thu' : (2,-9),
    'Fri' : (9,0),
    'Sat' : (8,-6),
    'Sun' : (3,-7),
}

day = input('Type the day : ')

if day in weather:
    print(f"{day}day's minimum temperature is {weather[day][1]} degrees and maximum temperature is {weather[day][0]} degrees Celsius. ")
else:
    print(f"I can't find on {day}day's temperature.")