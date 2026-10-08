x = int(input())

if x < 0 or x > 15:
    print("輸入錯誤")
else:
    # 二進位
    b1 = x // 8
    b2 = x % 8 // 4
    b3 = x % 4 // 2
    b4 = x % 2

    # 八進位
    o1 = x // 8
    o2 = x % 8

    # 十六進位
    if x < 10:
        h = x
    else:
        h = chr(x - 10 + ord('A'))

    print(f"二進制={b1}{b2}{b3}{b4}")
    print(f"八進制={o1}{o2}")
    print(f"十六進制={h}")