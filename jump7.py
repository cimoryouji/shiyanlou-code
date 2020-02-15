for i in range(1,101):
    if i%7 == 0:
        continue

    elif (i-7)%10 == 0:
        continue

    elif 0 <= (i-70) <=9:
        continue

    print(i)
