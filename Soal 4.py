print("4. Faktorial")
angka = int(input("Masukkan angka berapa yang ingin difaktorial: "))
i = 0
total = 1

# Pakek for
# for i in range(1, angka+1):
#     total *= i
#     print(i)
# print(total)

# Pakek while
while i<angka:
    i += 1
    total*= i
    print(i)
print(total)
