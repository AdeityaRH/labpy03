#Menampilkan bilangan acak yang < 0.5 
import random
n=str(input("Masukkan nilai N: "))

for x in range (1,6):
 print("data ke:",x,"=>",random.uniform(0.0,0.5))

print("Selesai")
