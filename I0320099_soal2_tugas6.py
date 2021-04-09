print("===MENGHITUNG NILAI RATA-RATA===")

n = int(input("\nMasukkan banyaknya nilai yang akan diinput: "))

nilai = []
jumlah = 0

for i in range (0,n):
    value = int(input("\nMasukkan nilai ke- %d: " %(i+1)))
    nilai.append(value)
    jumlah += nilai[i]
    avg = jumlah/n

print("---------------------------------")
print("\nNilai Rata-rata Anda adalah", avg)
