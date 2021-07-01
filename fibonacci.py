def fibonacci(n):
    point1 = 0
    point2 = 1

    print(point1)
    print(point2)

    for i in range(n - 2):
        point3 = point2 + point1
        
        print(point3)

        point1 = point2
        point2 = point3

n = int(input("Bir n değeri giriniz..."))

print("Girdiğiniz n değerine kadar Fibonacci dizisinin sonucu : ")

fibonacci(n)