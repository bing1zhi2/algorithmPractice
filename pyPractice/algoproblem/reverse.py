def reverseString(s):
    s = list(s)

    end = len(s) - 1
    begin = 0

    while begin < end:
        temp = s[begin]
        s[begin] = s[end]
        s[end] = temp
        begin = begin + 1
        end = end - 1

    return "".join(s)


r = reverseString('abcd')
print(r)

'''
class SolutionClassic(object):
    def reverseString(self, s):
        r = list(s)
        i, j  = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)

# 使用切片进行反转 sequence[starting_index:ending_index:step]
class SolutionPythonic(object):
    def reverseString(self, s):
        return s[::-1]
'''