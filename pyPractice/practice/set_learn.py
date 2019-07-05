# import cv2

set1 = set()
set2 = set()

set1.add(1)
set1.add(1)
set1.add(1)

print(set1)
set2.add(1)
set2.add(2)

# for i in set2:
#     set1.add(i)
# print(set1)

bbb = set1 & set2
print(bbb)
t = set()
print(len(t))

print(set2 & 2 )