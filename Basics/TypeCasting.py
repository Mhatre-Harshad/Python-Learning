"""
Type Casting: Converting one data type into another data type.
"""
# data type in python- integer ,float,string,boolean
# Integer to Float

num_int = 100
num_float = float(num_int)
print("Integer to Float:", num_float)

# Float to Integer
num_float2 = 13.67
num_int2 = int(num_float2)
print("Float to Integer:", num_int2)

# String to Integer
num_str = "2544"
num_int3 = int(num_str)
print("String to Integer:", num_int3)

# Integer to String
num_int4 = 100
num_str2 = str(num_int4)
print("Integer to String:", num_str2)

# String to Float
num_str3 = "45.78"
num_float3 = float(num_str3)
print("String to Float:", num_float3)

# Boolean to Integer
bool_val = True
bool_to_int = int(bool_val)
print("Boolean to Integer:", bool_to_int)

# Integer to Boolean
num_int5 = 0
to_bool = bool(num_int5)
print("Integer to Boolean:", to_bool)


