Rdata = int(input("masukkan range data :"))

Dikti = {}
for i in range(Rdata):
    if i%2 == 0:
        if i != 0:
            faktor = 1
            for y in range(2,i+1):
                faktor = faktor * y
            Dikti[i] = faktor
        else:
            Dikti[i] = 1

        
print(Dikti)
data = int(input("data ditampilkan :"))
if data not in Dikti:
    print("data tidak ditemukan")
else:
    print(Dikti[data])
