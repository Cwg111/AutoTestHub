import os
import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, logger, screenshot_dir, driver: WebDriver):
        """
        :param logger: 日志
        :param screenshot_dir: 截图保存地址
        :param driver:
        """
        self.driver = driver
        self.screenshot_dir = screenshot_dir
        self.logger = logger

    def get_page_img(self, page_action):
        """
        当前页面截图
        :param page_action: 元素操作描述
        :return:
        """
        cur_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        file_path = os.path.join(self.screenshot_dir, f"{cur_time}_{page_action}.png")
        self.driver.save_screenshot(file_path)
        self.logger.info(f"截图保存在：{file_path}")

    def wait_ele_visible(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        显性等待元素可见
        :param locator:元素定位
        :param page_action:操作
        :param timeout:
        :param poll_frequency:
        :return:
        """
        self.logger.info(f"在 {page_action} 操作，等待元素：{locator} 可见。")
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator)
            )
        except:
            self.logger.exception("等待元素可见失败！")
            # 失败截取当前页面
            self.get_page_img(page_action + "可见失败")
            raise
        else:
            end = time.time()
            self.logger.info(f"等待耗时为：{end-start}")

    def wait_ele_not_visible(
        self, locator, page_action, timeout=20, poll_frequency=0.5
    ):
        """
        显性等待元素不可见
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :return:
        """
        self.logger.info(f"在 {page_action} 操作，等待元素：{locator} 不可见。")
        try:
            # time.sleep(5)
            WebDriverWait(self.driver, timeout, poll_frequency).until_not(
                EC.visibility_of_element_located(locator)
            )
        except:
            self.logger.exception("等待元素不可见失败！")
            self.get_page_img(page_action + "不可见失败")
            raise

    def wait_page_contains_element(
        self, locator, page_action, timeout=20, poll_frequency=0.5
    ):
        """
        显性等待元素存在
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :return:
        """
        self.logger.info(f"在 {page_action} 操作，等待元素：{locator} 存在。")
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(locator)
            )
        except:
            self.logger.exception("等待元素存在失败！")
            self.get_page_img(page_action)
            raise
        else:
            end = time.time()
            self.logger.info(f"等待耗时为：{end - start}")

    def wait_page_clickable(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        等待元素可点击
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :return:
        """
        self.logger.info(f"在 {page_action} 操作，等待元素：{locator} 存在。")
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.element_to_be_clickable(locator)
            )
        except:
            self.logger.exception("等待元素可点击失败！")
            self.get_page_img(page_action)
            raise
        else:
            end = time.time()
            self.logger.info(f"等待耗时为：{end - start}")

    def get_element(
        self, locator, page_action, timeout=20, poll_frequency=0.5, wait="visibility"
    ):
        """
        先等待元素可见、存在、可点击
        查找单个元素
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :param wait: 默认元素可见
        :return: ele，返回查找到的单个元素
        """
        if wait == "presence":
            # 元素存在
            self.wait_page_contains_element(
                locator, page_action, timeout, poll_frequency
            )
        elif wait == "visibility":
            # 元素可见
            self.wait_ele_visible(locator, page_action, timeout, poll_frequency)
        elif wait == "clickable":
            # 元素可点击
            self.wait_page_clickable(locator, page_action, timeout, poll_frequency)
        self.logger.info(f"在 {page_action} 操作，查找元素：{locator}")
        try:
            ele = self.driver.find_element(*locator)
        except:
            self.logger.exception("查找元素失败！")
            self.get_page_img(page_action)
            raise
        else:
            return ele

    def click_element(
        self, locator, page_action, timeout=20, poll_frequency=0.5, wait="visibility"
    ):
        """
        点击元素操作
        默认元素可见
        :param wait: 默认元素可见
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :return:
        """
        # 先获取到元素
        ele = self.get_element(locator, page_action, timeout, poll_frequency, wait)
        # 点击
        self.logger.info(f"在 {page_action} 操作，点击元素：{locator}")
        try:
            ele.click()
        except:
            self.logger.exception("点击元素失败！")
            self.get_page_img(page_action)
            raise

    def click_elements(
        self, locator, page_action, timeout=20, poll_frequency=0.5, wait="visibility"
    ):
        """
        同一个定位能定位到多个元素
        勾选多个元素
        :param wait: 默认元素可见
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :return:
        """
        eles = self.get_elements(locator, page_action, timeout, poll_frequency, wait)
        for value in eles:
            self.logger.info(f"在 {page_action} 操作，点击多个 {value} 元素")
            try:
                value.click()
            except:
                self.logger.info(f"元素{value}，点击失败")
                raise

    def click_element_selected(
        self, locator, page_action, timeout=20, poll_frequency=0.5, wait="visibility"
    ):
        """
        点击元素后，判断元素是否被选中
        复选框或单选按钮
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :param wait: 默认元素可见
        :return:
        """
        self.click_element(locator, page_action, timeout, poll_frequency, wait)
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.element_to_be_selected(locator)
            )
        except:
            self.logger.info("元素未被勾选成功")
            self.get_page_img(page_action)
            raise

    def input_text(
        self,
        locator,
        page_action,
        value,
        timeout=20,
        poll_frequency=0.5,
        wait="visibility",
    ):
        """
        输入元素操作
        :param wait: 默认元素可见
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param value: 要输入的内容
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :return:
        """
        ele = self.get_element(locator, page_action, timeout, poll_frequency, wait)
        self.logger.info(f"在 {page_action} 操作，给元素：{locator} 输入文本值：{value}")
        try:
            ele.clear()
            ele.send_keys(value)
        except:
            self.logger.exception("元素输入文本失败！")
            self.get_page_img(page_action)
            raise

    def get_text(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        获取元素文本
        默认等待方式为可见
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :return: txt 返回元素的文本值
        """
        ele = self.get_element(
            locator, page_action, timeout, poll_frequency, wait="visibility"
        )
        self.logger.info(f"在 {page_action} 操作，获取元素：{locator}的文本")
        try:
            txt = ele.text
            self.logger.info(f"元素：{locator}的文本值：{txt}")
            return txt
        except:
            self.logger.info("获取元素文本失败")
            self.get_page_img(page_action)
            raise

    def get_attribute(
        self, locator, page_action, attr_name, timeout=20, poll_frequency=0.5
    ):
        """
        获取元素属性
        等待方式为存在
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param attr_name: 需要获取的属性名称
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :return:
        """
        ele = self.get_element(
            locator, page_action, timeout, poll_frequency, wait="visibility"
        )
        self.logger.info(f"在 {page_action} 操作，获取元素 {locator} 的属性")
        try:
            value = ele.get_attribute(attr_name)
            self.logger.info(f"元素：{locator} 的{attr_name}属性值：【{value}】 ")
            return value
        except:
            self.logger.info("获取元素属性失败")
            raise

    def get_attributes(
        self, locator, page_action, attr_name, timeout=20, poll_frequency=0.5
    ):
        """
        获取多个元素属性值
        等待方式为可见
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param attr_name: 需要获取的属性名称
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :return: values 返回多个元素的属性值
        """
        values = []
        eles = self.get_elements(
            locator, page_action, timeout, poll_frequency, wait="visibility"
        )
        for value in eles:
            self.logger.info(f"在 {page_action} 操作，获取多个 {value} 元素的属性")
            try:
                value = value.get_attribute(attr_name)
            except:
                self.logger.info(f"元素{value}，获取文本值失败")
            else:
                values.append(value)
        self.logger.info(f"多个元素属性值为：{values}")
        return values

    def wait_eles_visible(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        等待一个定位再一页中多个元素可见
        返回找到后的元素值列表
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :return: list_eles 返回查找到的多个元素列表
        """
        self.logger.info(f"在 {page_action} 操作，等待多个元素：{locator} 可见。")
        try:
            start = time.time()
            list_eles = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except:
            self.logger.exception("等待多个元素可见失败！")
            self.get_page_img(page_action + "可见失败")
            raise
        else:
            end = time.time()
            self.logger.info(f"等待耗时为：{end-start}")
            return list_eles

    def wait_eles_presence(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        等待一个元素定位再页面中多个存在
        返回找到后的元素值列表
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :return: 返回查找到的多个元素列表
        """
        self.logger.info(f"在 {page_action} 操作，等待多个元素：{locator} 存在。")
        try:
            start = time.time()
            list_eles = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_all_elements_located(locator)
            )
        except:
            self.logger.exception("等待多个元素存在失败！")
            self.get_page_img(page_action + "存在失败")
            raise
        else:
            end = time.time()
            self.logger.info(f"等待耗时为：{end-start}")
            return list_eles

    def get_elements(
        self, locator, page_action, timeout=20, poll_frequency=0.5, wait="visibility"
    ):
        """
        查找获得多个元素
        一个定位获得多个元素
        :param wait: 默认元素可见
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :return: eles 返回查找到的元素列表
        """
        if wait == "presence":
            self.wait_eles_presence(locator, page_action, timeout, poll_frequency)
        if wait == "visibility":
            self.wait_eles_visible(locator, page_action, timeout, poll_frequency)
        self.logger.info(f"在 {page_action} 操作，查找多个元素：{locator}可见")
        try:
            eles = self.driver.find_elements(*locator)
        except:
            self.logger.exception("查找多个元素失败！")
            self.get_page_img(page_action)
            raise
        else:
            return eles

    def get_texts(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        一个定位获得多个元素
        获取多个文本值
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :return: values 返回多个元素的文本值列表
        """
        values = []
        eles = self.get_elements(locator, page_action, timeout, poll_frequency)
        for value in eles:
            self.logger.info(f"在 {page_action} 操作，获取多个 {value} 元素的文本值")
            try:
                txt = value.text
            except:
                self.logger.info(f"元素{value}，获取文本值失败")
            else:
                values.append(txt)
        self.logger.info(f"多个元素文本值为：{values}")
        return values

    def keyboard(self, locator, page_action, cmd, value=None):
        """
        键盘操作
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param cmd: 键盘命令
        :param value: 文本框中输入的值
        :return:
        """
        ele = self.get_element(
            locator, page_action, timeout=20, poll_frequency=0.5, wait="visibility"
        )
        if value:
            # 键盘清除选择框中所有的数据
            ele.send_keys(Keys.CONTROL, "a")
            ele.send_keys(Keys.DELETE)
            time.sleep(1)
            ele.send_keys(value, cmd)
            self.logger.info(
                f"实际文本框的值：{self.get_attribute(locator, page_action, 'value')}"
            )
        else:
            ele.send_keys(cmd)

    def action_chains_click(
        self, locator, page_action, timeout=20, poll_frequency=0.5, click="click"
    ):
        """
        鼠标点击操作（单击、双击、右键点击）
        默认为单击
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :param click: 默认点击行为（单击）
        :return:
        """
        ele = self.get_element(
            locator, page_action, timeout, poll_frequency, wait="visibility"
        )
        ta = ActionChains(self.driver)
        if click == "click":
            # 鼠标单击操作
            try:
                ta.move_to_element(ele).click(ele)
            except:
                self.get_page_img("鼠标左键单击失败")
                raise
        elif click == "double":
            # 鼠标左键双击操作
            try:
                ta.move_to_element(ele).double_click(ele)
            except:
                self.get_page_img("鼠标左键双击失败")
                raise
        else:
            # 鼠标右键单击操作
            try:
                ta.move_to_element(ele).context_click(ele)
            except:
                self.get_page_img("鼠标右键单击失败")
                raise
        ta.perform()

    def action_move_element(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        鼠标移动到某元素上，才会显示数据（与点击显示不同）
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param timeout: 超时时间
        :param poll_frequency: 轮询频率
        :return:
        """
        ele = self.get_element(
            locator, page_action, timeout, poll_frequency, wait="visibility"
        )
        ta = ActionChains(self.driver)
        ta.move_to_element(ele).perform()

    def select_element(self, locator, page_action):
        """
        下拉列表中，随机选择其中一个元素，增加测试的随机性和覆盖面
        :param locator: 多个元素的同一定位
        :param page_action: 元素操作描述
        :return:
        """
        if len(self.get_elements(locator, page_action)) > 1:
            # 随机选择一个元素，排除最后一个元素，因为最后一个元素可能是“更多”按钮，不排除会出问题
            random.choice(self.get_elements(locator, page_action)[0:-1]).click()
        else:
            self.get_elements(locator, page_action)[0].click()

    def wait_page_url_change(self, old_url, timeout=20, poll_frequency=0.5):
        """
        获取当前页面的URL
        :param old_url: 页面跳转前的网址
        :param timeout: 超时时间
        :param poll_frequency: 轮询间隔
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                lambda driver: driver.current_url != old_url
            )
        except:
            self.logger.error("页面跳转失败")
            self.get_page_img("页面跳转失败")
            raise
        else:
            self.logger.info(f"页面跳转成功,新的页面url为{self.driver.current_url}")

    def refresh_page(self):
        """
        刷新页面
        :return:
        """
        self.driver.refresh()

    def get_page_url(self):
        """
        获取当前页面的URL
        :return: 返回当前页面的url
        """
        return self.driver.current_url

    def upload_file_by_input(self, locator, page_action, file_path):
        """
        使用//input[@type="file"]上传文件
        :param locator: 元素定位
        :param page_action: 元素操作描述
        :param file_path: 文件路径
        :return:
        """
        ele = self.get_element(locator, page_action)
        ele.send_keys(file_path)
        self.logger.info(f"在 {page_action} 操作，上传文件：{file_path}")

    # shadow dom定位
    def get_shadow_element(self, shadow_host_locator, page_action):
        pass
