print("1.idli\n2.dosa\n3.pongal\n4.poori\n5.parrota")
menu=int(input("enter your menu no:"))
match menu:
    case 1:
        print("your order is idle")
    case 2:
        print("your order is dosa")
    case 3:
        print("your order is pongal")
    case 4:
        print("your order is poori")
    case 5:
        print("your order is parrota")
    case _:
        print("not available you ask menu")
