# 这里导入 utils.root_path 是为了确保项目根目录被添加到 sys.path，不用显示调用root_path
import utils.root_path # noqa: F401
import pytest
import os
import shutil
from taiga.Common.taiga_path import taiga_base_dir, report_dir,allure_results_dir

def is_jenkins():
    """
    检测是否在 Jenkins 环境中运行
    """
    return os.getenv('JENKINS_URL') is not None or os.getenv('BUILD_NUMBER') is not None

def view_last_report():
    """
    查看上一次的测试报告
    """
    if os.path.exists(report_dir) and os.listdir(report_dir):
        os.system(f"allure open {report_dir}")
    else:
        print("没有找到上一次的报告，请先运行测试")


def run_tests_and_generate_report(test_dir):
    """
    运行测试用例并生成 Allure 报告
    :param test_dir: 需要运行的测试用例目录
    :return:
    """

    # 清理旧目录
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)
    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)

    # 运行测试
    pytest.main([test_dir, "-v", f"--alluredir={allure_results_dir}"])

    # 只在非 Jenkins 环境下生成和打开报告
    if not is_jenkins():
        # 生成报告
        os.system(f"allure generate {allure_results_dir} -o {report_dir}")
        os.system(f"allure open {report_dir}")
    else:
        print("Jenkins 环境：报告已生成，请使用 Jenkins Allure 插件查看")

if __name__ == "__main__":
    # 运行并查看报告
    run_tests_and_generate_report(taiga_base_dir)
