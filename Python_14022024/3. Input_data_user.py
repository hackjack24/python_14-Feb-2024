# data dari input user hasilnya pasti STRING
data = input("input your name: ")
data2 = input("input your email: ")
# jika ingin merubah type data harus gunakan casting
data3 = int(input("input your mobilephone:"))


print("=====RETURN=====")

print("username = ", data, "type =", type(data))
print("email account = ", data2, "type =", type(data2))
# jika ingin merubah type data harus gunakan casting
print("mobilephone =", data3, ",type =", type(data3))

