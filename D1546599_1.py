x = int(input())

if x < 0 or x > 15:
    print("輸入錯誤")
else:
    # 2
    a1 = x // 8
    a2 = x % 8 // 4
    a3 = x % 4 // 2
    a4 = x % 2

    # 8
    b1 = x // 8
    b2 = x % 8

    # 16
    if x < 10:
        c = x
    elif x == 10:
        c = "A"
    elif x == 11:
        c = "B"
    elif x == 12:
        c = "C"
    elif x == 13:
        c = "D"
    elif x == 14:
        c = "E"
    else:
        c = "F"

    print(f"二進制={a1}{a2}{a3}{a4}")
    print(f"八進制={b1}{b2}")
    print(f"十六進制={c}")