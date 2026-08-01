print("3. Rata - rata")
angka = int(input("Masukkan berapa angka yang ingin dirata-rata: "))
i = 0
total = 0
while i<angka:
    i += 1
    x = int(input(f'Masukkan angka {i}: '))
    total += i
print(total/angka)
