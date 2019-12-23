print('number has int float and complex')
# int
number_int_value = 100
# float
number_float_value = 99.99
# 复数
number_complex_value = complex(number_int_value, number_float_value)
number_int_const_age = 99
# 全部大写代表常量
NUMBER_INT_AGE = 10

print(number_int_value, number_float_value, number_complex_value, number_int_const_age, NUMBER_INT_AGE)
number_int_sum = number_int_value + number_float_value
number_int_difference = number_int_value - number_float_value
number_int_ji = number_int_value * number_int_value
number_int_shang = number_int_const_age / NUMBER_INT_AGE
number_int_mi = NUMBER_INT_AGE ** NUMBER_INT_AGE
number_int_yu = number_int_value % number_int_const_age
print(number_int_sum, number_int_difference, number_int_ji, number_int_shang)
print(number_int_mi, number_int_yu)