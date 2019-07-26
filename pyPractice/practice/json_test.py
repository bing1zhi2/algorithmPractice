import json

# str1 = '                                 '
#
# jobj= json.loads(str1)
# method =jobj.get('method','')
# print(method)
# ratio =jobj.get('ratio','')
# print(ratio)
#
# print(method == "wdsr" or method == "espcn")

json_dict = {}

data = {}
"""
epochs
dataset_format
dataset_path
max_label_length
img_height
img_weight
batch_size
learn_rate

"""
data['epochs']= 50
data['dataset_format']= 1
data['dataset_path']= '/home/test'
data['max_label_length']= 10
data['img_height']= 28
data['img_weight']= 300
data['batch_size']= 100
data['learn_rate']= None




json_dict['data']= data
json_dict['token']="sdfsdfwerwe213"


json_obj = json.dumps(json_dict, sort_keys=True, indent=4, separators=(',', ': '))

print(json_obj)


result ={}
result['code']=200
result['msg']=""
result['result']=None
result_obj = json.dumps(result)
print(result_obj)
