point = int(input("İstediğiniz Sayıyı Giriniz... : "))
factorial = 1

if point < 0:
    print("Negatif sayılarda faktoriyel hesaplanma yapılmaz!!!")

elif point == 0:
    print("0! = 1'dir." )    

else:
    for i in range(1, point + 1):
        factorial = factorial * i

    print(point, "Sayısının Faktoriyel Hesaplanması : ", factorial)       