while True:
    word = input('Type word : ')
    wordlength = len(word)
    if wordlength == 0:
        break
    elif 5 <= wordlength <= 8:
        continue
    elif wordlength < 5:
        result = '*' + word + '*'
    elif wordlength > 8:
        result = '$' + word + '$'
    print(f"result : {result}")