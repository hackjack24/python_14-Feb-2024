# data integer
data_integer=1000
print("data :", data_integer)
print("-bertipe :", type(data_integer))

data_float=20.50
print("data :", data_float)
print("-bertipe", type(data_float))

data_string="HACKJACK"
print("data :", data_string)
print("-bertipe", type(data_string))

data_bool=True
print("data :", data_bool)
print("-bertipe", type(data_bool))








data_complex=complex(10,35)
print("data :", data_complex)
print("-bertipe :", type(data_complex))


from ctypes import c_double

data_c_double = c_double(20.89)
print("data :", data_c_double)
print("-bertipe :", type(data_c_double))
