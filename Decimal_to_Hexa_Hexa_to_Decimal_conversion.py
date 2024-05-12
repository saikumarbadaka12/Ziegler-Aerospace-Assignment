# Decimal to Hexadecimal conversion
def decimal_to_hex(decimal):
    if not decimal.isdigit():
        print("Invalid input")
        return
    decimal = int(decimal)
    hex_chars = "0123456789ABCDEF"
    hex_value = ""
    while decimal > 0:
        remainder = decimal % 16
        hex_value = hex_chars[remainder] + hex_value
        decimal //= 16
    print(hex_value)

# Hexadecimal to Decimal conversion
def hex_to_decimal(hex_value):
    hex_chars = "0123456789ABCDEF"
    decimal = 0
    for digit in hex_value:
        if digit.upper() not in hex_chars:
            print("Invalid input")
            return
        decimal = decimal * 16 + hex_chars.index(digit.upper())
    print(decimal)

# Test
decimal_to_hex("255")  # Output: FF
hex_to_decimal("FF")   # Output: 255
