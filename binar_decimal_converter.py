def binary_to_decimal(binary_str):
    #how can I convert a number from binary to decimaal
    #binary are 1s and 0s 
    #example 1111
    #from the right 2 ** 0 + 2 ** 1 + 2** 2 + 2 ** 3 = 15
    #from decimal to binary no % 2 == taking account of the remainder 
    #return the remainder 
    decimal_num = 0
    power = 0 
    for num in reversed(binary_str):
        if num == '1':
            decimal_num += 2 ** power
        power += 1

    return decimal_num

def decimal_to_binary(decimal_num):
    if decimal_num == 0 :
        return "0"
    binary_str = ""

    while decimal_num > 0 :
        remainder = decimal_num % 2 
        binary_str = str(remainder) + binary_str
        decimal_num //= 2
    return binary_str

binary_input = '1100'
converter = binary_to_decimal(binary_input)
print(converter)

decimal_input = 15
b_converter = decimal_to_binary(decimal_input)
print(b_converter)




