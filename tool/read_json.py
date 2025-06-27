# 导包
import json
from pathlib import Path

def read_json(filename):
    # 获取项目的根目录
    project_root = Path(__file__).parent.parent  # 从当前文件的父目录的父目录开始
    # 构建路径：项目根目录下的 data 文件夹中的文件
    filepath = project_root / "data" / filename
    # 打开文件并调用 load方法
    with open(filepath, "r", encoding="utf-8")as f:
        return json.load(f)

if __name__ == '__main__':
    print(read_json("login.json"))
    """
        需求格式：[(),(),(),(),(),()]
        实际格式为：{"login_001":{}}
    """
    print("--" * 50)

    # 定义空列表
    arrs = []
    for data in read_json("login.json").values():
        arrs.append((data.get("username"),
                     data.get("password"),
                     data.get("verify_code"),
                     data.get("expect_result"),
                     data.get("success")))
    print(arrs)

