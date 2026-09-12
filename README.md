plaintext
# 软件工程个人作业：基于SimHash文本查重工具
## 项目介绍
本程序使用SimHash算法+海明距离，计算两篇文本的相似度，输出文本重复率。

## 环境依赖
Python3.7及以上
```bash
pip install -r requirements.txt
使用方法
bash
python main.py test1.txt test2.txt result.txt
参数说明：
test1.txt：原文文件路径
test2.txt：待比对文件路径
result.txt：输出相似度结果的文件
单元测试运行
bash
python -m unittest test.py
文件结构
plaintext
3224004232/
├─ main.py        # 主程序，simhash核心算法
├─ requirements.txt # 依赖库
├─ test.py        # 单元测试
└─ PSP.md         # PSP预估表
