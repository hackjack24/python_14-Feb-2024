# operasi aritmatika
a = 20
b = 8

# operasi +
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi -
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi *
hasil = a * b
print(a,'*',b,'=',hasil)

# operasi /
hasil = a / b
print(a,'/',b,'=',hasil)

# operasi pangkat A pangkat B** (eksponen)
hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi pangkat % (modulus)-sisa dr hasil pembagian
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floor division //(pembgian dibulatkan kebawah)
hasil = a // b
print(a,'//',b,'=',hasil)


# operational precedence/prioritas operasi
# urutan prioritas

# ()
# pangkat 2/eksponen
# perkalian/pembagian/modulus/floor operation
# tambah/ kurang


x = 3
y = 2
z = 4

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

hasil = (x + y) * z
print('(',x,'+',y,') *',z,'=',hasil)