colordic = {
    'red' : '#ff0000',
    'blue' : '#0000ff',
    'green' : '#008000',
    'yellow' : '#ffff00',
    'orange' : '#ffa500',
    'black' : '#000000',
    'white' : '#ffffff',
    'violet' : '#ee82ee',
    'pink' : '#ffc0cb',
    'lime' : '#00ff00',
}

color = input('Type a color : ')

if color in colordic:
    print(f"{color}'s RGB is {colordic[color]}.")
else:
    print(f"I can't find {color}'s RGB.")