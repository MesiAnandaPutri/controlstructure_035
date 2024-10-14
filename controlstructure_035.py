#consolstructure_035
#  1 mencetak decision persentase
persentase = int(input('Masukan nilai persentase : '))

if persentase >= 90:
    print('Excellent performance')
elif persentase >= 80:
    print('Very Good performance')
elif persentase >= 70:
    print('Good performance')
elif persentase >= 60:
    print('Average performance')
else:
    print('Below average performance')

 
    
# 2 mencetak angka terbesar

def largest(num1, num2, num3):
    return max(num1, num2, num3)

num1 = int (input('Masukan bilangan pertama : '))
num2 = int (input('Masukan bilangan kedua : '))
num3 = int (input('Masukan bilangan ketiga : '))
print('Bilangan terbesar dari tiga bilangan adalah: ', largest(num1, num2, num3))

# 3 Mencetak deret fibonacci sampai n

nilai_fibonacci = int(input('Masukan nilai fibonacci : '))
def fibonacci(n):
    a, b = 0,1
    hasil = []
    while a <= n:
        hasil.append(a)
        a, b = b, a + b
    return hasil

deret_fibonacci = fibonacci(nilai_fibonacci)
print("Deret Fibonacci hingga", nilai_fibonacci, "adalah:", deret_fibonacci)

# 4 Mencetak odd number

nilai_odd = int(input('Masukan nilai batas bilangan ganjil : '))
def odd_number(n):
    for i in range(1, n + 1, 2):
        print(i, end=" ")
odd_number(nilai_odd)
print()

# 5 mencetak design

n = int(input("Masukkan nilai untuk tinggi pola: "))
def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")  
        print()  
print_pattern(n)