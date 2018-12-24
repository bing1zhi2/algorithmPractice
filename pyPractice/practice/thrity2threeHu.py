
a =300
idx =[]
for i in range(1, a):
    j = i + 1
    while j <= a:
        j = j + 1

        if len(idx) < 300:
            idx.append( (i, j))
print('over', len(idx))
