import base64
from Sprider.setting import IMAGE_PATH1,IMAGE_PATH2,IMAGE_PATH3
from PIL import Image


"""
图片处理方法
"""


def get_image(url1,url2):
    """
    url1:Base64编码
    url2:Base64编码
    获取图片,把base64解码后的图片加载到本地
    :return:None
    """
    for byte_data,path in zip(base_to_byte(url1,url2),[IMAGE_PATH1,IMAGE_PATH2]):
        with open(path,'wb') as f:
            f.write(byte_data)
    add_image(IMAGE_PATH1,IMAGE_PATH2)


def base_to_byte(url1:str,url2:str):
    """
    base64解码
    :return:List:byte
    """
    head1,context1 = url1.split(",")
    img_data1 = base64.b64decode(context1)
    head2, context2=url2.split(",")
    img_data2=base64.b64decode(context2)
    return [img_data1,img_data2]


def add_image(path1,path2):
    """
    合并图片
    :param path1: str
    :param path2: str
    :return:
    """
    img1 = Image.open(path1).convert('RGB')# 背景图片，需要读取为RGB，3通道的格式
    img2 = Image.open(path2).convert('RGBA')# 叠加的透明PNG图片，需要读取为RGBA，4通
    img1.paste(img2, (0,0), img2)
    img1.save(IMAGE_PATH3)





if __name__ == '__main__':
    pass


