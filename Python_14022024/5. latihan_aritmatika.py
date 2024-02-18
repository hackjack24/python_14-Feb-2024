# program konversi celcius ke satuan lain
# print("\nPROGRAM KONVERSI TEMPERATUR\n")

# celcius = float(input('masukkan suhu dalam celcius : '))
# print("suhu adalah",celcius, "celcius")

# # reamur
# reamur = (4/5)*celcius
# print("suhu dalam reamur adalah",reamur, "reamur")

# # fahrenheit
# fahrenheit = ((9/5)*celcius)+32
# print("suhu dalam fahrenheit adalah",fahrenheit, "fahrenheit")

# # kelvin
# kelvin = celcius+273
# print("suhu dalam kelvin adalah",kelvin, "kelvin")


# latihan
# 1. konversi dari fahrenheit ke kelvin "( F=5/9(f-32) ) ke celcius"
# 2. konversi dari kelvin ke fahrenheit "(K=k-273) ke celcius""

# jawaban
# 1. Konversi dari fahrenheit ke kelvin
# konversi dl ke celcius
fahrenheit = float(input('masukkan suhu dalam fahrenheit : '))
# print("suhu adalah",fahrenheit, "fahrenheit")

celcius = ((5/9)*fahrenheit)-32
# print("suhu dalam celcius adalah",celcius,"celcius")

kelvin = celcius+273
print("suhu dalam kelvin adalah",kelvin,"kelvin")

# 2. Konversi dari kelvin ke fahrenheit
# konversi dl ke celcius

kelvin = float(input('masukkan suhu dalam kelvin : '))
# print("suhu adalah",kelvin,"kelvin")

celcius = kelvin-273
# print("suhu dalam celcius adalah",celcius,"celcius")

fahrenheit = ((9/5)*celcius)+32
print("suhu dalam fahrenheit adalah",fahrenheit,"fahrenheit")
