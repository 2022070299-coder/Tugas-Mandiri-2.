print("5. Fibonacci (1)")
angka = int(input("Masukkan fibonacci angka ke berapa: "))
i = 0
a, b = 0, 1
deret = [0] * angka

# Pakek for
# for i in range(angka):
#     deret[i] = a
#     a, b = b, a+b
# print(deret)

# Pakek while
while i<angka:
    deret[i] = a
    a, b = b, a+b
    i += 1
print(deret)
