AutoTestHub

Web 自动化测试项目，用于实现 Web 端的自动化测试流程（如页面操作、结果输出、报告生成等）

一、环境准备
确保本地已安装：

Python 3.8 及以上版本

Git（用于克隆代码）

二、项目部署步骤

克隆代码到本地：git clone https://github.com/Cwg11/AutoTestHub.git

cd AutoTestHub

安装项目依赖包使用requirements.txt一键安装第三方依赖：
pip install -r requirements.txt

初始化项目文件夹结构执行以下两个文件，自动生成项目所需的输出 / 配置文件夹（如Outputs、Conf下的子文件夹）：

python common/path.py

python taiga/Common/taiga_path.py

三、快速开始
完成上述部署后，即可运行自动化测试脚本（以项目主入口为例）：

python project_board_main.py

注意事项：

项目的输出文件（测试报告、日志、截图等）会自动保存在Outputs下的对应子文件夹中；

若运行脚本时提示 “文件夹不存在”，重新执行步骤 2 中的两个路径文件即可自动创建。
