

a = 3
b = 5
# 011 ^ 101  = 110
c = a ^ b

print(bin(c))
print(bin(-c))

d = c & (-c)
print(d,bin(d))
