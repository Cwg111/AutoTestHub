"""
独立的根目录工具文件，无任何外部依赖，用于给所有入口脚本添加项目根路径
"""
import os
import sys

def get_project_root() -> str:
    """获取项目根目录的绝对路径（无需依赖任何其他包）"""
    # 此文件在 utils/root_path.py，所以回溯一级就是项目根目录
    current_file = os.path.abspath(__file__)
    project_root = os.path.dirname(os.path.dirname(current_file))
    return project_root

def add_project_root_to_path() -> None:
    """将项目根目录添加到 sys.path，确保所有模块可导入（仅添加一次）"""
    root = get_project_root()
    if root not in sys.path:
        sys.path.insert(0, root)

# 执行此文件时自动添加根路径（导入时也会执行）
add_project_root_to_path()