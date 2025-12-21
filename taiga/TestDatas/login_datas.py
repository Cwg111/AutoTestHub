import os

# 初始接口地址
base_url = "http://192.168.88.130:9000/"

# 发现页面
discover_url = os.path.join(base_url, 'discover')

# 登录页面
login_url = os.path.join(base_url, 'login?next=%252Fdiscover')

# 登录成功页面
home_url = os.path.join(base_url, '')

# 成功登录的账号密码
login_admin_success = {
    "username": "admin",
    "password": "Admin@123456"
}

login_error_input = [
    {
        "username": "admin",
        "password": "Admin@1234567",
        "message": "username/email or password are incorrect"
    },
    {
        "username": "admin1",
        "password": "Admin@123456",
        "message": "username/email or password are incorrect"
    }
]

if __name__ == '__main__':
    print(login_url)
    print(home_url)


