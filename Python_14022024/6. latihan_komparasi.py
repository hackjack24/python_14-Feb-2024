

# --------0+++++++5-------8++++++11---------

inputUser = float(input("input angka:" ))

isLebihDari0 = (inputUser > 0)
isKurangDari5 = (inputUser < 5)
isLebihDari8 = (inputUser > 8)
isKurangDari11 = (inputUser <11)

isBenar = isLebihDari0 and isKurangDari5 or isLebihDari8 and isKurangDari11
print(isBenar) 


# ++++0--------5+++++++8--------11+++++++

inputUser_2 = float(input("input angka kedua:"))

isKurangDari0 = (inputUser_2 < 0)
isLebihDari5 = (inputUser_2 > 5)
isKurangDari8 = (inputUser_2 < 8)
isLebihDari11 = (inputUser_2 > 11)

isBenar2 = isKurangDari0 or isLebihDari5 and isKurangDari8 or isLebihDari11
print(isBenar2)