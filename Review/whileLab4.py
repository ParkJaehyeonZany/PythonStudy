while True:
    mon = int(input('Type Number between 1 and 12 : '))
    if mon == 12 or mon == 1 or mon == 2:
        print(f"{mon} is Winter.")
    elif 3 <= mon <= 5:
        print(f"{mon} is Spring.")
    elif 6 <= mon <= 8:
        print(f"{mon} is Summer.")
    elif 9 <= mon <= 11:
        print(f"{mon} is Fall.")
    else:
        print('Type Number between 1 and 12!')
        break