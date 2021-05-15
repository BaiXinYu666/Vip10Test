'''import requests

urla = 'https://s.weibo.com/Ajax_Search/suggest'
canshu = {'key': '啊啊'}

r = requests.get(url=urla, params=canshu)

print(r.text)
print(r.cookies)
print(r.raw)
print('-------')
print(r.headers)
print(r.url)
print(r.encoding)
print(r.content)
print(r.status_code)
print(r.json())
print(r.raise_for_status())
'''
'''import requests, json

urla = 'https://wanandroid.com/user/login'
canshu = {'username': '15535496803', 'password': 'BAIXINYU000'}
# header = {'User-Agent':'Mozilla/5.0'}
r = requests.post(url=urla, data=canshu)
zidian = r.json()

if r.status_code == 200 and zidian['data']['username']:
    print('成功了')
else:
    print('失败了')
'''

'''import requests

urla = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-773058962040428-shentong-KUAIDI1621064022560.html'

headers = {'User-Agent': 'Mozilla/5.0'}

s = requests.session()
r = s.get(url =  urla)
zhuanhuan = r.json()
print(zhuanhuan)
aa = zhuanhuan['data']
bb = aa[0]['context']
print(bb)'''
import requests

urla = 'https://wanandroid.com/user/login'
dataa = {'username': '15535496803', 'password': 'BAIXINYU000'}
r = requests.post(urla, data=dataa)
cookie = r.cookies
urlb = 'https://wanandroid.com/lg/todo/list/0'
rr = requests.get(urlb, cookies=cookie)
print(rr.text)
