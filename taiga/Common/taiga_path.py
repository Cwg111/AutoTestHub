import os

# ------基础路径配置------------
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cases_dir = os.path.join(base_dir, "TestCases")
datas_dir = os.path.join(base_dir, "TestDatas")
reports_dir = os.path.join(base_dir, r"Outputs\allure")
logs_dir = os.path.join(base_dir, r"Outputs\logs")
screenshot_dir = os.path.join(base_dir, "Outputs", "screenshots")
verify_code_dir = os.path.join(base_dir, "Outputs", "verify_code")
test_data_dir = os.path.join(base_dir, "TestDatas")  # 测试数据目录
login_data_dir = os.path.join(test_data_dir, "login_datas.json")  # 登录数据文件

# 如果输出目录不存在，则创建
list_dir = [reports_dir, logs_dir, screenshot_dir, verify_code_dir]
for dir_path in list_dir:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# --------环境URL配置----------
# 初始接口地址
base_url = "http://192.168.146.128:9000/"

# 发现页面
discover_url = os.path.join(base_url, 'discover')

# 登录页面
login_url = os.path.join(base_url, 'login?next=%252Fdiscover')

# 登录成功页面
home_url = os.path.join(base_url, '')

if __name__ == '__main__':
    print(base_dir)
    print(logs_dir)
    print(screenshot_dir)
    print(discover_url)
    print(login_url)
    from Common.data import read_json_data

    login_data = read_json_data(login_data_dir)
    print(login_data)
    print(login_data["login_success"])
    print(login_data["login_fail"])

