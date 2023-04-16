```python
"""
在python中，使用 bin()、oct()、int()、hex() 这四个函数可以对进制进行转换
在python编程中，二进制是0b开头表示，八进制0o开头表示，十进制直接是数字表示，16进制是0x表示
"""

# 十六进制转换
print(bin(0x110))  # 16 转 2 = 100010000
print(oct(0x110))  # 16 转 8 = 420
print(int(0x110))  # 16 转 10 = 272

# 十进制转换
print(bin(110))  # 10 转 2 = 1101110
print(oct(110))  # 10 转 8 = 156
print(hex(110))  # 10 转 16 = 6e

# 八进制转换
print(bin(0o77))  # 8 转 2 = 111111
print(int(0o77))  # 8 转 10 = 63
print(hex(0o77))  # 8 转 16 = 3f


# 二进制转换
print(oct(0b110110))  # 2 转 8 = 66
print(int(0b110110))  # 2 转 10 = 54
print(hex(0b110110))  # 2 转 16 = 36
```