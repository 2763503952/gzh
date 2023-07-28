# from playwright.sync_api import sync_playwright
import requests
import time
import json
from Sprider.set_imag import get_image
from Sprider.setting import IMAGE_PATH1,IMAGE_PATH2
from Sprider.opencv import calculate_distance
from Crypto.Cipher import AES
import base64
from playwright.sync_api import sync_playwright
BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

class YunduoKeep:

    def __init__(self):
        self.JSESSIONID = None
        self.USERNAME='18263954077'
        self.PASSWORD='Mm14768326851..'
        self.headers={
            "authority": "www.iyunduo.com",
            "accept": "application/json, text/plain, */*",
            "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7",
            "content-type": "application/json; charset=UTF-8",
            "origin": "https://www.iyunduo.com",
            "referer": "https://www.iyunduo.com/login",
            "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
        self.cookies = {
            "username": "18263954077",
            "rememberMe": "true",
            "password": "lgR4GAyrO0NAIeMNFypZwPluXSlwLMRTOjIX53kzQO20scUoRgZsljmKkzJ3D78T0UqHfxiHZbgWFStniVuZRQ==",
            "JSESSIONID": "6F0358731B09CF78806D397DF81EB7D2"
        }

    def browers_add(self,Admin_Token,JSESSIONID,data):
        """
        :param Admin_Token:
        :param JSESSIONID:
        :param data: 填充的数据
        :return:
        """
        headers={
            "authority": "www.iyunduo.com",
            "accept": "application/json, text/plain, */*",
            "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7",
            "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjJjZDkxZjk2LWU0YjctNDkzZi1hOTVhLWQwMGM5NDVkYmNmZiJ9.ZoSiBIFcWSNNvNxLcfYJVyQ59CPNbPu-mvDNsjM8jtQUyMEl57zg973Zp6eMx2qiKUciruyJypsfl_oChzNuow",
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://www.iyunduo.com",
            "referer": "https://www.iyunduo.com/oa/calendar",
            "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        cookies={
            "username": "18263954077",
            "rememberMe": "true",
            "password": "dyuAtevSY+FREzhjMRJ/DM4nPl8piZFxW7iKdixSnVFYRf8i2oZnPucZY1imU+Fn/U/e3K9c6Muyc08JKsHQTQ==",
            "Admin-Token": Admin_Token,
            "JSESSIONID": JSESSIONID
        }
        url="https://www.iyunduo.com/prod-api/task/info/add"
        data={
            "taskName": "【代码研发】修改花盘中心线bug",
            "businessType": "1",
            "businessId": "2c4fc7f6-69ce-48bc-9056-f0d7d179435a",
            "excuteUserId": "4cb1c696-0358-4075-a6bc-ca44f1e55f99",
            "isAllDay": 2,
            "startTime": "2023-07-27 00:00:00",
            "deadLine": "2023-07-27 00:00:00",
            "workload": "2.0",
            "taskType": "1",
            "taskCycle": 1,
            "taskPriority": 2,
            "taskDesc": "",
            "remindUserIds": ""
        }
        data=json.dumps(data, separators=(',', ':'))
        response=requests.post(url, headers=headers, cookies=cookies, data=data)

        print(response.text)
        print(response)
    def brower_mian(self):
        """
        自动化
        :return:
        """
        with sync_playwright() as p:
            browser_type=p.chromium
            browser=browser_type.launch(headless=False)
            context=browser.new_context()
            page=context.new_page()
            while(True):
                page.goto('https://www.iyunduo.com/login?redirect=%2Foa%2Findex')
                page.fill('xpath=//*[@id="app"]/div/div[2]/form/div[1]/div/div/input',self.__USERNAME)
                page.fill('xpath=//*[@id="app"]/div/div[2]/form/div[2]/div/div/input',self.__PASSWORD)
                page.click('//*[@id="app"]/div/div[2]/form/div[4]/div/button')

                image_url1 = page.get_attribute('xpath=//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/img','src')
                image_url2 = page.get_attribute('xpath=//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/img','src')

                offset_x = self._code(image_url1,image_url2)
                slider=page.locator('xpath=//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/i').bounding_box()
                page.mouse.move(x=slider['x'], y=slider['y']+slider['height']/2)
                page.mouse.down()
                page.mouse.move(x=slider['x']+offset_x, y=slider['y']+slider['height']/2)
                page.mouse.up()

                time.sleep(3)
                flag = page.locator('xpath=//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/i')
                if flag.count()==0:
                    cookies = context.cookies()




    """
    js逆向方法暂时搁置，不会了，用自动化处理。
    """


    def main(self):
        get_json,get_cookie = self.get_requests()
        img_1 = 'data:image/png;base64,'+get_json['repData']['originalImageBase64'] #背景
        img_2 = 'data:image/png;base64,'+get_json['repData']['jigsawImageBase64'] #滑块
        offsetx = self._code(img_1,img_2) #偏移距离
        ojson = {"x":offsetx,"y":5} #构建json字符串

        secretKey = get_json['repData']['secretKey'] #获取加密密钥secretKey

        pointJson = self.AES_encode(json.dumps(ojson).replace(' ',''),secretKey)
        token = get_json['repData']['token']
        self.get_repData(token,pointJson)

        pointJson2 = self.AES_encode(token+'---'+json.dumps(ojson).replace(' ',''),secretKey)
        print(json.dumps(ojson).replace(' ','')+'---'+token)
        self.loign(token,pointJson2)


    def get_requests(self):
        """
        对get文件进行请求,返回里面的Json
        :return:Json
        """


        url="https://www.iyunduo.com/prod-api/captcha/get"
        data={
            "captchaType": "blockPuzzle",
            "clientUid": "slider-f2b7d5b2-2360-440d-aaf6-d5d582cc8763",
            "ts": int(time.time()*1000)
        }
        # data=json.dumps(data, separators=(',', ':'))
        response=requests.post(url, headers=self.headers,cookies=self.cookies,json=data)
        return response.json(),response.cookies

    def get_repData(self,token,pointJson):
        re_url="https://www.iyunduo.com/prod-api/captcha/check"
        data={
            "captchaType": "blockPuzzle",
            "pointJson": pointJson,
            "token": token
        }
        # data=json.dumps(data, separators=(',', ':'))
        response=requests.post(url=re_url, headers=self.headers, cookies=self.cookies, json=data)
        print(response.text)


    def loign(self,token,pointJson):
        url = 'https://www.iyunduo.com/prod-api/login'
        data = {
          'captchaVerification':pointJson,
          'password':self.PASSWORD,
          'username':self.USERNAME
        }
        response=requests.post(url=url, headers=self.headers, cookies=self.cookies, json=data)
        print(response.text)


    def _code(self,url1,url2):
        """
        识别验证码,获得偏移距离
        url1:base64编码
        url2:base64编码
        :return:偏移距离
        """
        get_image(url1,url2) #获取图片保存到imag文件夹内
        offsetx,offsety = calculate_distance(IMAGE_PATH2,IMAGE_PATH1)

        return offsetx

    def AES_encode(self,json,key):
        '''
        AES的ECB模式加密方法
        :param key: 密钥
        :param data:被加密字符串（明文）
        :return:密文
        '''
        key=key.encode('utf8')
        # 字符串补位
        data=pad(json)

        cipher=AES.new(key, mode=AES.MODE_ECB)
        # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
        result=cipher.encrypt(data.encode('utf-8'))
        encodestrs=base64.b64encode(result)
        enctext=encodestrs.decode('utf-8')
        return enctext








if __name__=='__main__':
    # YunduoKeep.get_requests()

    YunduoKeep().main()
