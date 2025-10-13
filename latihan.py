#no 1
umur = 12
harga =  12.5
nama = "Gesya"
absen = [1,2,3,4,5,6]

print(f'umur ={umur} ({type(umur)})')
print(f'harga ={harga} ({type(harga)})')
print(f'nama ={nama} ({type(nama)})')
print(f'absen ={absen} ({type(absen)})')

#no 2
belanja = ["beras", "minyak", "telur"]
belanja.append("gula")
belanja.append("kopi")
for item in belanja:
    print(item)

#no 3
hargabelanja = {
    "beras":12000,
    "minyak":17000,
    "telur":24000,
    "gula":15000,
    "kopi":20000
}
total = sum(hargabelanja.values())
print("Total harga belanja:", total)

#no 4
def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

panjang = 10
lebar = 5
luas, keliling = hitung_persegi_panjang(panjang, lebar)
print(f"laus persegi panjang ={luas}")
print(f"Luas: {luas}, Keliling: {keliling}")

#no 5
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


# cast from str to int
str_numbers = "456"
str_numbers_to_int = int(str_numbers)
print("Before casting :", str_numbers, ", the data type is",
type(str_numbers))
print("After casting :", str_numbers_to_int, ", the data type is",
type(str_numbers_to_int))


# casting from int to str
integer = 12345
integer_to_str = str(integer)
print("Before casting :", integer, ", the data type is", type(integer))
print("After casting :", integer_to_str, ", the data type is",
type(integer_to_str))

# casting from int to bool
num_int = 1
num_bool = bool(num_int)
print(num_bool, type(num_bool))
num_int = 0
num_bool = bool(num_int)
print(num_bool, type(num_bool))

#Koding comparison operators
# Equal to
print(8 == 8)
# Not equal to
print(8 != 9)
# Greater than
print(8 > 9)
# Less than
print(8 < 9)
# Less than or equal
print(8 <= 9)
# Greater than or equal
print(9 >= 9)

#Koding logical operators
a = True
b = True
print(a and b)
print(a or b)
print(not b)

# logic
print(5 > 6 and 6 < 7)

#Koding arithmetic operators
e = 8
f = 2
# Summation
sum = e + f
print(f"The sum of e with f is : {sum}\n")
# Reduction
red = e - f
print(f"The reduction of e with f is : {red}\n")

# Multiplication
multi = e * f
print(f"The multipication of e with f is : {multi}\n")
# Division
divi = e / f
print(f"The quotient of e with f is : {divi}\n")
# Modulo
mod = e % f
print(f"The remainder of e with f is : {mod}\n")
# Power
pow = e ** f
print(f"The power of e of f is : {pow}\n")

#Koding Input Output
#Input
name = str(input("What is your name : "))
age = int(input("What's your age : "))

print("Name: ", name)
print("Age: ", age)

# Output
name = "Parman"
age = 24
# normal print
print('Hi all! I am', name, 'age', age, 'years old')

# format print (f-string)
print(f'Hi all! I am {name} age {age} years old')

# format print (% formatting)
print("Hi all! I am %s age %d years old" % (name, age))

# format output
print(30*"=")
print("Temperature Calculator Program")
print(30*"=")