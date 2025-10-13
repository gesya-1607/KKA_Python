
umur = 12
harga =  12.5
nama = "Gesya"
absen = [1,2,3,4,5,6]

print(f'umur ={umur} ({type(umur)})')
print(f'harga ={harga} ({type(harga)})')
print(f'nama ={nama} ({type(nama)})')
print(f'absen ={absen} ({type(absen)})')

belanja = ["beras", "minyak", "telur"]
belanja.append("gula")
belanja.append("kopi")
for item in belanja:
    print(item)

hargabelanja = {
    "beras":12000,
    "minyak":17000,
    "telur":24000,
    "gula":15000,
    "kopi":20000
}
total = sum(hargabelanja.values())
print("Total harga belanja:", total)

def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

panjang = 10
lebar = 5
luas, keliling = hitung_persegi_panjang(panjang, lebar)
print(f"laus persegi panjang ={luas}")
print(f"Luas: {luas}, Keliling: {keliling}")

print("\n=== 5. Percabangan ===")
usia = int(input("Masukkan usia: "))

if 0 <= usia <= 13:
    print("Anak")
elif 14 <= usia <= 24:
    print("Remaja")
elif 25 <= usia <= 49:
    print("Dewasa")
elif usia > 50:
    print("Lansia")
else:
    print("Usia tidak valid")