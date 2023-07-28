import cv2
from Sprider.setting import IMAGE_PATH1,IMAGE_PATH2,IMAGE_PATH3


"""
用于处理滑块图片的opencv的各种方法
"""

GAUSSIAN_BLUR_KERNEL_SIZE = (5, 5)
GAUSSIAN_BLUR_SIGMA_X = 0
CANNY_THRESHOLD1 = 200
CANNY_THRESHOLD2 = 350


RENDERING_IMAGE_X = 360 #浏览器渲染时的图片长度
RENDERING_IMAGE_Y = 180 #浏览器渲染时的图片宽度




def get_gaussian_blur_image(image):
    return cv2.GaussianBlur(image, GAUSSIAN_BLUR_KERNEL_SIZE, GAUSSIAN_BLUR_SIGMA_X)


def get_canny_image(image):
    return cv2.Canny(image, CANNY_THRESHOLD1, CANNY_THRESHOLD2)


def get_contours(image):
    contours, _ = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def get_contour_area_threshold(image_width, image_height):
    contour_area_min = (image_width * 0.15) * (image_height * 0.2) * 0.6
    contour_area_max = (image_width * 0.15) * (image_height * 0.25) * 1.3
    return contour_area_min, contour_area_max


def get_arc_length_threshold(image_width, image_height):
    arc_length_min = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 0.6
    arc_length_max = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 1.3
    return arc_length_min, arc_length_max


def get_offset_threshold(image_width):
    offset_min = 0.15 * image_width
    offset_max = 0.85 * image_width
    return offset_min, offset_max


def main():
    image_raw = cv2.imread(IMAGE_PATH1)
    image_height, image_width, _ = image_raw.shape
    image_gaussian_blur = get_gaussian_blur_image(image_raw)
    image_canny = get_canny_image(image_gaussian_blur)
    contours = get_contours(image_canny)
    cv2.imwrite('imag\image_canny.png', image_canny) #计算出边缘
    cv2.imwrite('imag\image_gaussian_blur.png', image_gaussian_blur)#高斯模糊
    contour_area_min, contour_area_max = get_contour_area_threshold(image_width, image_height)
    arc_length_min, arc_length_max = get_arc_length_threshold(image_width, image_height)
    offset_min, offset_max = get_offset_threshold(image_width)
    offset = None

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if contour_area_min < cv2.contourArea(contour) < contour_area_max and \
                arc_length_min < cv2.arcLength(contour, True) < arc_length_max and \
                offset_min < x < offset_max:
            cv2.rectangle(image_raw, (x, y), (x + w, y + h), (0, 0, 255), 2)
            offset = x

    cv2.imwrite('imag\image_label.png',image_raw)


def clear_white(img):
    """清除图片的空白区域，这里主要清除滑块的空白"""
    img = cv2.imread(img)
    rows, cols, channel = img.shape
    min_x = 255
    min_y = 255
    max_x = 0
    max_y = 0
    for x in range(1, rows):
        for y in range(1, cols):
            t = set(img[x, y])
            if len(t) >= 2:
                if x <= min_x:
                    min_x = x
                elif x >= max_x:
                    max_x = x

                if y <= min_y:
                    min_y = y
                elif y >= max_y:
                    max_y = y
    img1 = img[min_x:max_x, min_y: max_y]
    return img1

def template_match(tpl, target):
    """
    :param tpl: 滑块
    :param target: 背景
    :return:
    """
    th, tw = tpl.shape[:2] #滑块长宽
    result = cv2.matchTemplate(target, tpl, cv2.TM_CCOEFF_NORMED)
    """
    MatchTemplate函数，是在一幅图像中寻找与另一幅模板图像最匹配(相似)部分。
    :param 参数名称
    image：输入一个待匹配的图像，支持8U或者32F。
    templ：输入一个模板图像，与image相同类型。
    result：输出保存结果的矩阵，32F类型。
    method：要使用的数据比较方法。
    :return 矩阵
    """
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    """
    传入一个矩阵，返回这个矩阵的最小值，最大值，并得到最大值，最小值的索引
    """
    tl = max_loc #tl最大值索引
    br = (tl[0] + tw, tl[1] + th)
    cv2.rectangle(target, tl, br, (0, 0, 255), 2)
    return tl[0], tl[1]

def calculate_distance(pic1_path, pic2_path):
    """
    计算滑块到缺口的距离
    pic1_path:滑块图片
    pic2_path:背景图片
    """
    img1 = clear_white(pic1_path)
    cv2.imwrite('imag\image_clear.png', img1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    img1_canny = cv2.Canny(img1, 100, 200)
    cv2.imwrite('imag\image1_canny.png', img1_canny)  # 计算出边缘

    img2 = cv2.imread(pic2_path, 0)
    width,length= img2.shape
    img2_canny = cv2.Canny(img2, 100, 200)
    cv2.imwrite('imag\image2_canny.png', img2_canny) # 计算边缘

    slide_pic = cv2.cvtColor(img1_canny, cv2.COLOR_GRAY2RGB)
    cv2.imwrite('imag/cvt_image1.png',slide_pic)
    """
    cvtColor()：颜色空间转换函数
    :param 参数名称
    frame: 图片
    cv2.COLOR_BGR2RGB: 要进行的色彩转换方式
    """
    back_pic = cv2.cvtColor(img2_canny, cv2.COLOR_GRAY2RGB)
    cv2.imwrite('imag/cvt_image2.png', back_pic)
    # 滑块在图片上的位置
    x, y = template_match(slide_pic, back_pic)
    print(x,y)
    # 滑块到缺口的距离
    dis_x = ((x) * (RENDERING_IMAGE_X / length))
    dis_y = (y * (RENDERING_IMAGE_Y/ width))

    cv2.rectangle(img2, (x, y), (x+40, y+40), (0, 0, 255), 2)
    cv2.rectangle(img2, (0, 0), (x, y), (0, 255, 0), 2)
    """
    function:rectangle 在图片中绘制方框
    :param 参数名称 
    img: 图片
    pt1: 绘制方框左上角坐标 Type:Tuple
    pt2: 绘制方框右下角坐标 Type:Tuple
    color: 字体颜色
    thinckness: 字体粗细
    lineType: 线型
    shift:
    
    """
    cv2.imwrite('imag\e_image.png',img2)
    return x, dis_y


def identify_gap(bg, cut):
    '''
    bg: 背景图片
    cut: 缺口图片
    '''
    # 读取背景图片和缺口图片
    bg_img=cv2.imread(bg)  # 背景图片
    cut_img=cv2.imread(cut)  # 缺口图片

    # 识别图片边缘
    bg_edge=cv2.Canny(bg_img, 100, 200)
    cut_edge=cv2.Canny(cut_img, 100, 200)

    # 转换图片格式
    bg_pic=cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
    cut_pic=cv2.cvtColor(cut_edge, cv2.COLOR_GRAY2RGB)

    # 缺口匹配
    res=cv2.matchTemplate(bg_pic, cut_pic, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc=cv2.minMaxLoc(res)  # 寻找最优匹配

    # 返回缺口坐标
    return max_loc



if __name__ == '__main__':
    a,b=calculate_distance(IMAGE_PATH2,IMAGE_PATH1)
    print(a,b)