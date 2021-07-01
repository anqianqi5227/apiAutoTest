
import json
import urllib2

cookies = 'COID=eyJ2ZXIiOiIxLjAifQ.eyJiY0lkIjoyLCJlbnZJZCI6NCwiZXhwIjoxNjExMTQ3ODQzLCJpYXQiOjE2MDU5NjM4NDMsInJtYiI6MSwidWlkIjoyODE3NDN9.586FECD478CFB4CBF3689E65BAFB77D234377AAFAE44BFCF12376397A3AD5EB8; NICKNAME4=13711112223; UID4=281743; device=F3E90EE1-637C-456B-91E9-E41F2AD98171; CNZZDATA1278204453=108176307-1605935044-%7C1605935044; UM_distinctid=175e93018b7481-0cadc1f718db4-1a670c51-3d10d-175e93018b8b4; _xmLog=xm_khr89f6x6yk020'
url = 'https://www.test.qingxuetang.com/h5/api/page/v1?pageId=48&pageSource=1'


headers = {
        "cookie": cookies
     }

res = urllib2.Request(url, headers=headers)
res1 = urllib2.urlopen(res)
res2 = res1.read()
print (res2)
print(str(res2))

res3 = json.loads(res2)
l = res3['data']['moduleList']
l1 = []
# l1 = l[0]['moduleType']
# print (l1)


for i in range(0, len(l)):
    if l[i]['moduleType'] == 3:
        module_id = l[i]['moduleId']
        l1.append(str(module_id))

print (l1)
s1 = ','.join(l1)


print(s1)
