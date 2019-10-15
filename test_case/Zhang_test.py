import os
from common.utils import Utils
base_dir = os.getcwd()
Utils = utils = Utils()
print(base_dir)
# 获取平台用例所在的文件夹
platform_case_dir = []
list = os.listdir(base_dir)
for l in list:
    if os.path.isdir(os.path.join(base_dir, l)) is True:
        platform_case_dir.append(l)
print(platform_case_dir)

#获取作者用例所在的文件夹
def get_author_dir(platform_dir):
    author_case_dir = []
    base_author_dir = os.path.join(base_dir, platform_dir)
    list = os.listdir(base_author_dir)
    for l in list:
        if os.path.isdir(os.path.join(base_author_dir, l)) is True:
            author_case_dir.append(l)
    return author_case_dir
# 创建测试套件
# 参数详解：
# platform 输入想测试的平台：pc mobile pc_mobile
# author   输入你写的测试用例的文件夹：lff tdg zfk
# 四种方式： 1.platform=None,author=None 跑全部测试用例
#          2.platform=None,author不=None 跑你写的全部测试用例
#          3.platform不=None,author=None 跑你想跑的平台的测试用例
#          4.platform不=None,author不=None 跑指定平台下的你写的测试用例
A=['zhangfukai','tongdingguo','lvfangfang']
print(A[:-1])