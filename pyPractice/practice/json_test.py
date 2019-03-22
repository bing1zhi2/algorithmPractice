import json

str1 = '                                 '

jobj= json.loads(str1)
method =jobj.get('method','')
print(method)
ratio =jobj.get('ratio','')
print(ratio)

print(method == "wdsr" or method == "espcn")