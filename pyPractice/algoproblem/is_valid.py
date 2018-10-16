"""leetcode problem 20 """
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#  An input string is valid if:
#
#  Open brackets must be closed by the same type of brackets.
#  Open brackets must be closed in the correct order.
#  Note that an empty string is also considered valid.

def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    d = {")": "(", "]": "[", "}": "{"}
    for i in s:
        if i in d.values():
            stack.append(i)
        elif i in d.keys():
            if stack == [] or stack.pop() != d[i]:
                return False
        else:
            return False

    return stack == []


result = is_valid("()")
print(result)