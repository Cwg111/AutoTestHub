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
        # 步骤1：分割Data URL的头部和数据部分
        # Data URL格式：data:[<媒体类型>];[<编码方式>],<Base64数据>
        # 用逗号分割1次，分离出header（如data:image/png;base64）和data（Base64编码的图片数据）
        header, data = data_url.split(",", 1)
        # 步骤2：提取MIME类型和编码
        parts = header.split(";")  # 分割header的分号，得到['data:image/png', 'base64']
        mime_type = parts[0].replace("data:", "")  # 去掉data:，得到媒体类型（如image/png）
        encoding = parts[1] if len(parts) > 1 else ""  # 提取编码方式（如base64）
        # 步骤3：校验编码方式，仅支持Base64
        if "base64" not in encoding:
            raise ValueError("仅支持Base64编码的URL")
        # 步骤4：解码数据
        # unquote：处理URL中的转义字符（比如%2F），避免解码失败
        # b64decode：将Base64字符串还原为二进制图片数据
        binary_data = base64.b64decode(unquote(data))
        # 步骤5：生成唯一的文件名
        # 媒体类型分割出扩展名（如image/png → png）
        file_extension = mime_type.split("/")[-1]
        # 用当前时间戳命名（精确到秒），避免文件名重复
        filename = f"{datetime.datetime.now().strftime('%Y-%m-%d%H%M%S')}.{file_extension}"
        # 步骤6：拼接保存路径，写入文件
        save_path = os.path.join(picture_dir, filename)
        with open(save_path, "wb") as f:  # 二进制写模式保存图片
            f.write(binary_data)
        # 返回保存的文件路径，供后续OCR识别使用
        return save_path

    except Exception as e:
        raise RuntimeError("保存图片失败: {}".format(e))


def get_data_url_code(img_url, picture_dir):
    """
    data_url类型验证码
    读取验证码图片,返回验证码字母数字
    :param img_url: 页面上图片url地址
    :param picture_dir: 图片保存地址
    :return: 识别后的验证码字符串
    """
    # 步骤1：初始化ddddocr实例，show_ad=False关闭广告输出（原版库可能有广告）
    ocr = ddddocr.DdddOcr(show_ad=False)
    # 步骤2：调用私有函数保存图片，得到本地文件路径；以二进制读模式打开图片
    with open(__save_data_url_image(img_url, picture_dir), "rb") as f:
        image_bytes = f.read()  # 读取图片字节数据
        # 步骤3：调用OCR的classification方法识别验证码，返回识别结果
        return ocr.classification(image_bytes)
