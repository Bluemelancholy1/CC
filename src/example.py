#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
这是一个示例Python文件，用于展示基本的编程结构。
你可以根据需要修改或删除此文件。
"""

def hello_world():
    """打印Hello World消息"""
    print("Hello, World!")
    print("欢迎来到CC项目！")

def add_numbers(a, b):
    """
    将两个数字相加并返回结果
    
    参数:
        a (int/float): 第一个数字
        b (int/float): 第二个数字
        
    返回:
        int/float: 两个数字的和
    """
    return a + b

def main():
    """主函数，程序的入口点"""
    hello_world()
    
    # 示例计算
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")

if __name__ == "__main__":
    main()