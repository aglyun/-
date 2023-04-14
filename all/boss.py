# _*_coding. utf-8_*_
# 开发时间：2021/3/8 16:21
# 加油！
import time
import requests
from lxml import etree
from selenium.webdriver import Chrome,ChromeOptions
# # 配置
setting = ChromeOptions()
# # 添加代理ip
i = {'http': 'http://220.165.42.30:4250'}
setting.add_argument('--proxy-server=%s' % i.get('http'))


def ip():
    """ 这是个ip代理池"""
    ips = '114.96.218.185:4262 223.215.170.63:4210 114.101.248.248:4203 114.99.1.200:4224 114.99.222.33:4217 60.166.167.66:4248 183.166.150.17:4226 183.166.139.10:4238 114.99.10.227:4226 114.106.170.205:4245 36.57.70.242:4220 223.243.69.245:4265 114.104.140.100:4278 223.242.222.170:4264 114.104.180.50:4263 117.70.46.9:4245 114.99.254.104:4234 114.104.138.30:4214 220.179.210.62:4278 117.69.176.241:4220 60.172.85.74:4226 114.99.220.108:4217 60.173.35.186:4278 183.166.150.5:4270 60.166.180.23:4263 223.243.62.73:4278 223.243.177.41:4278 117.66.167.108:4278 60.172.85.35:4227 117.57.63.81:4278 114.101.251.185:4286 114.99.13.60:4278 114.96.166.206:4225 223.214.196.71:4278 114.99.23.236:4278 223.214.30.25:4235 114.106.171.204:4245 114.99.196.57:4278 36.6.146.200:4280 117.69.51.114:4231 36.62.211.54:4217 220.179.214.85:4278 36.35.5.4:4226 114.103.60.81:4237 117.57.90.174:4264 36.7.248.31:4235 183.166.179.80:4286 223.244.193.83:4217 114.104.141.111:4231 183.166.144.113:4220 223.242.221.145:4281 114.104.182.199:4216 183.166.160.38:4226 36.7.27.143:4272 114.106.157.104:4245 124.112.213.156:4234 60.166.94.66:4228 223.215.119.100:4278 36.6.134.35:4281 223.243.171.240:4278 117.69.177.61:4278 36.57.91.26:4226 36.6.148.148:4281 223.214.196.77:4216 60.173.47.129:4232 117.69.170.205:4273 183.166.161.166:4270 117.57.91.115:4282 223.215.177.161:4247 223.215.118.137:4285 114.103.21.251:4265 114.99.11.180:4224 114.99.3.201:4232 58.243.28.159:4270 223.214.221.88:4216 114.96.168.96:4281 223.214.223.243:4216 36.57.76.41:4214 114.103.62.203:4220 114.99.15.27:4232 114.99.221.101:4245 114.99.252.140:4258 220.179.214.137:4278 183.166.135.175:4286 114.99.221.80:4226 114.99.21.114:4276 220.179.102.85:4214 36.7.27.133:4216 58.243.28.221:4270 223.214.201.89:4234 36.62.210.39:4245 117.68.244.85:4251 117.64.255.95:4251 114.104.128.123:4214 60.166.182.61:4278 60.173.34.183:4278 58.243.28.14:4270 183.166.135.197:4248 60.167.116.134:4278 223.214.216.197:4216 61.132.171.128:4278 114.104.183.135:4220 183.166.164.182:4227 114.99.252.191:4234 114.99.13.114:4278 114.103.156.96:4203 60.166.183.40:4216 114.99.255.148:4258 61.190.161.192:4227 61.132.170.108:4224 114.99.196.182:4245 60.175.39.68:4234 36.57.85.121:4270 223.214.123.158:4235 114.106.171.113:4247 36.62.241.123:4215 112.123.40.32:4270 117.69.183.143:4227 36.6.135.42:4252 114.106.131.33:4210 223.215.170.156:4220 114.103.177.243:4216 183.164.239.29:4264 36.33.20.188:4226 114.104.141.226:4263 114.99.1.53:4224 117.69.24.19:4251 112.132.50.219:4226 223.242.247.73:4231 112.123.40.76:4254 114.99.196.202:4245 183.162.146.90:4235 36.57.95.92:4227 183.165.33.191:4235 117.69.25.86:4251 117.69.151.207:4238 36.57.68.189:4286 114.101.241.136:4234 114.99.222.28:4278 114.96.218.73:4282 223.243.52.90:4278 117.70.47.161:4210 223.242.221.37:4281 36.33.19.166:4226 183.165.232.227:4264 114.103.156.12:4235 124.112.222.94:4203 114.103.88.120:4247 183.166.139.196:4238 60.175.9.173:4258 223.215.117.156:4234 223.214.31.43:4265 114.103.60.78:4210 36.34.14.138:4226 60.173.47.246:4226 223.214.197.119:4278 116.149.193.208:4226 117.69.171.236:4238 36.62.211.55:4278 117.69.129.151:4248 223.215.75.143:4278 223.242.20.111:4265 36.6.147.160:4282 36.32.5.68:4226 58.243.28.224:4254 60.167.52.187:4278 61.191.85.93:4232 114.99.5.24:4225 114.99.131.172:4278 223.215.170.206:4210 36.62.241.29:4245 112.132.49.6:4226 117.67.131.186:4228 36.6.146.143:4262 183.165.26.62:4278 114.99.130.172:4278 60.173.34.18:4224 114.103.156.201:4235 223.214.71.234:4235 60.166.172.230:4247 112.132.51.198:4226 114.99.252.48:4235 223.243.182.172:4272 36.57.71.98:4247 114.104.141.61:4216 36.57.87.141:4238 223.243.177.142:4286 124.113.193.89:4251 117.69.201.218:4280 117.70.35.58:4237'
    i = ips.split(' ')
    return i

# 把代理配置配置到chrome对象中

chrome = Chrome(chrome_options=setting)
url = 'https://www.zhipin.com/job_detail/?query=python&city=100010000&industry=&position='
cookie = {
    'Cookie': 'https%3A%2F%2Fopen.weixin.qq.com%2Fconnect%2Fqrconnect%3Fappid%3Dwxf68ac2d384a75d96%26scope%3Dsnsapi_login%26redirect_uri%3Dhttps%3A%2F%2Fwww.zhipin.com%2Fwechat%2Faccount%2Flogin.html%26state%3D554GF2gylo7Qw81eQtxHhMM7it8qlIcB%26login_type%3Djssdk%26self_redirect%3Ddefault%26styletype%3D%26sizetype%3D%26bgcolor%3D%26rst%3D%26style%3Dwhite%26href%3Dhttps%3A%2F%2Flogin.zhipin.com%2Fv2%2Fweb%2Fgeek%2Fcss%2Fwechat-scan.css&l=%2Fjob_detail%2F%3Fquery%3Dpython%26city%3D100010000%26industry%3D%26position%3D&s=1'
}
# chrome.get(url)


# 使用ip代理循环发送请求
for i in ip():
    proxies = {
        "http": 'http://{}'.format(i),
        "https": 'https://{}'.format(i)
    }
headers = {
    'Referer': 'https://www.zhipin.com/job_detail/?query=python&city=101280100&industry=&position=&srcReferer=https://www.zhipin.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    # 'cookie': 'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1615256885; ___gtid=701088086; __fid=0fbe67f7b9966bf8c8fc899734402e6d; lastCity=100010000; __g=-; __c=1615256924; __a=48634732.1615256924..1615256924.3.1.3.3; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1615257035; __zp_stoken__=6ee4bKUQhcCNVaAwpbAo8JG9QZWYnX2InPDF2KT9pF2kNSlU8c05iYTRzGjURCxc7Jl1SbiFFJWdcd3tmC0EDaEoubTptP0wuPSQodkMRSTccBmgJXXxXfzVIODNJJ2QPIAxYV2RDIAZdXEsFeg%3D%3D'
     'Cookie': 'https%3A%2F%2Fopen.weixin.qq.com%2Fconnect%2Fqrconnect%3Fappid%3Dwxf68ac2d384a75d96%26scope%3Dsnsapi_login%26redirect_uri%3Dhttps%3A%2F%2Fwww.zhipin.com%2Fwechat%2Faccount%2Flogin.html%26state%3D554GF2gylo7Qw81eQtxHhMM7it8qlIcB%26login_type%3Djssdk%26self_redirect%3Ddefault%26styletype%3D%26sizetype%3D%26bgcolor%3D%26rst%3D%26style%3Dwhite%26href%3Dhttps%3A%2F%2Flogin.zhipin.com%2Fv2%2Fweb%2Fgeek%2Fcss%2Fwechat-scan.css&l=%2Fjob_detail%2F%3Fquery%3Dpython%26city%3D100010000%26industry%3D%26position%3D&s=1'

}
i = {'http': 'http://114.239.222.176:4236'}
url = 'https://www.zhipin.com/job_detail/?query=python&city=100010000&industry=&position='
# session = requests.session()
r = requests.get(url, headers=headers)
print(r.text)

html = etree.HTML(r.text)
title = html.xpath('//div[@class="job-list"]//div[@class="job-title"]/span/a/text()')
area = html.xpath('//div[@class="job-list"]//div[@class="job-title"]//span[@class="job-area"]/text()')
pub_time = html.xpath('//div[@class="job-list"]//div[@class="job-title"]//span[@class="job-pub-time"]/text()')
money = html.xpath('//div[@class="job-list"]//div[@class="job-limit clearfix"]/span/text()')
work = html.xpath('//div[@class="job-list"]//div[@class="job-limit clearfix"]/p/text()')
print('职位：', title)
print('薪资：', money)
print('要求：', work)
print('工作地址：', area)
print('职位发布日期：', pub_time)
    # if r.status_code == 200:
        # 判断是否能使用，如果能使用就跳出循环
        # break
    # else:
    #     print(False)

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
#     'Cookie': '_bl_uid=wgkLylk2xm7fFb7Opzkz0m1bdd3p; lastCity=101280100; __zp_seo_uuid__=2c0ac5b6-a6c4-48f5-9ae5-36ea0975aa89; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1615016626,1615191686,1615193011,1615205247; __l=r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DIvYczyS1TQtoi9SmrGVLiplT3FPTKf7h-VF261s6tIBS7xDKmcX85Ic4wWH1gaqw%26wd%3D%26eqid%3Dccc1b20d0003edca000000066046137a&l=%2Fwww.zhipin.com%2Fguangzhou%2F&s=3&g=&friend_source=0&s=3&friend_source=0; ___gtid=1843515921; __fid=e7c0c2d868a696bb83ec83b350a2db31; __c=1615205247; __a=50319361.1615016626.1615191686.1615205247.39.3.5.33; __zp_stoken__=37d4bWxBNBQ0cVnh8GG1lV28sPksSLnwMbQYoYjBwKnRQZ1MQDXMMZCMXLTF%2FUVRJAmNfHBlQfXB9NnkCYAFJBG9zOTcFIVAELzpcESt8AQ9fImV7LmIhFwVnRBBKZQRwBDJVJVxWDA4NPzBhdA%3D%3D; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1615205810'
#
# }
# api_url = 'https://www.zhipin.com/wapi/zpgeek/recommend/job/list.json?expectId=206478640&sortType=1&page=1&salary=&payType=&degree=&experience=&stage=&scale=&districtCode=0&businessCode='
# r = requests.get(api_url, headers=headers)
# print(r.text)