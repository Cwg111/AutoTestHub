# @Create Date: 2025/6/3
# @Author: ganlu
import base64
import ddddocr
import datetime
import os

from urllib.parse import unquote


def __save_data_url_image(data_url: str, picture_dir):
    """
    将 Data URL 格式的图片保存到本地
    :param data_url: 页面上图片url地址
    :param picture_dir: 图片保存地址
    :return: 保存的文件路径
    """
    try:
        header, data = data_url.split(",", 1)
        # 提取MIME类型和编码
        parts = header.split(";")
        mime_type = parts[0].replace("data:", "")
        encoding = parts[1] if len(parts) > 1 else ""
        if "base64" not in encoding:
            raise ValueError("仅支持Base64编码的URL")
        # 解码数据
        binary_data = base64.b64decode(unquote(data))
        file_extension = mime_type.split("/")[-1]
        filename = "{}.{}".format(datetime.datetime.now().strftime('%Y-%m-%d%H%M%S'), file_extension)
        save_path = os.path.join(picture_dir, filename)
        with open(save_path, "wb") as f:
            f.write(binary_data)
        return save_path

    except Exception as e:
        raise RuntimeError("保存图片失败: {}".format(e))


def get_data_url_code(img_url, picture_dir):
    """
    data_url类型验证码
    读取验证码图片,返回验证码字母数字
    :param img_url: 页面上图片url地址
    :param picture_dir: 图片保存地址
    :return:
    """

    ocr = ddddocr.DdddOcr(show_ad=False)
    with open(__save_data_url_image(img_url, picture_dir), "rb") as f:
        image_bytes = f.read()
        return ocr.classification(image_bytes)
