#Menentukan bilangan terbesar,dari buah bilangan yang diinputkan,dan menggunakan angka 0 untuk menghentikan programnya
max=0
while True:
	a=int(input("Masukkan bilangan:"))
	if a ==0:
		break
	if a>max:
		max=a
print("Bilangan terbesar:",max)
