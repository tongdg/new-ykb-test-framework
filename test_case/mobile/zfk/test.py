import random

Random=int(random.uniform(10, 20))
print(Random)
for i in range(0,10000000):
    Random_input=input("请输入一个数字")
    if Random_input>int(Random):
        print()
