def ackermann(x,y):

    if x == 0:
        print(y+1)
        return y + 1
    
    elif x > 0 and y == 0:
        print("Ackermann(", x-1,",",1,")")
        return ackermann(x - 1, 1)

    elif x > 0 and y > 0:
        print("Ackermann(",x-1,",","Ackermann(",x,",",y - 1,")",")")
        return ackermann(x - 1, ackermann(x, y -1))

point1 = int(input("Lütfen birinci sayıyı giriniz..."))        
point2 = int(input("Lütfen ikinci sayıyı giriniz..."))

ackermann(point1, point2)