
b = b"example"
#字符串对象s
s = "example"
print(b)
print("example")


#字符串encode将获得一个bytes对象
b3 = str.encode(s)
b4 = s.encode()
print(b3)
print(type(b3))
print(b4)

s2 = bytes.decode(b)
s3 = b.decode()
print(s2)
print(s3)