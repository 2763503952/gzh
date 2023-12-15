import requests


headers = {
    "authority": "48.push2.eastmoney.com",
    "accept": "*/*",
    "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7",
    "referer": "https://quote.eastmoney.com/center/gridlist.html",
    "sec-ch-ua": "^\\^Not_A",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
url = "https://36.push2.eastmoney.com/api/qt/clist/get"
params = {
    # "cb": "jQuery112409219904089331075_1702606675221",
    "pn": "2",
    "pz": "20",
    "po": "1",
    "np": "1",
    "ut": "bd1d9ddb04089700cf9c27f6f7426281",
    "fltt": "2",
    "invt": "2",
    "wbp2u": "^|0^|0^|0^|web",
    "fid": "f3",
    "fs": "m:0 t:6,m:0 t:80,m:1 t:2,m:1 t:23,m:0 t:81 s:2048",
    "fields": "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152",
    "_": "1702606675222"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)
