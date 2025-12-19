import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cases_dir = os.path.join(base_dir, "TestCases")
datas_dir = os.path.join(base_dir, "TestDatas")
reports_dir = os.path.join(base_dir, r"Outputs\allure")
logs_dir = os.path.join(base_dir, r"Outputs\logs")
screenshot_dir = os.path.join(base_dir, "Outputs", "screenshots")
verify_code_dir = os.path.join(base_dir, "Outputs", "verify_code")

# 如果输出目录不存在，则创建
list_dir = [reports_dir, logs_dir, screenshot_dir, verify_code_dir]
for dir_path in list_dir:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


if __name__ == '__main__':
    print(base_dir)
    print(logs_dir)
    print(screenshot_dir)
