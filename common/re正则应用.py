# -- encoding: utf-8 --
# @time:    	2022/4/8 22:14
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import re
import json
res = {'code': 0, 'success': True, 'data': {
    'result': {'isSucceed': True, 'message': '44704', 'mdmId': 0, 'setMessage': True, 'setIsSucceed': True,
               'setMdmId': False}}, 'msg': None}
res= json.dumps(res)
info = re.compile(r'"message": ".*?",')
# message_new = r'"message": ' + '"123456",'
# body1 = info.sub(message_new,res)
# print(body1)

# info = re.compile(r'"message": ".*?"')
# print(info.search(res).group().split(":")[1].strip(' ,"'))
code = re.search(r'"message": ".*?"',res)[0].split(":")[1].strip(' "')
print(code)