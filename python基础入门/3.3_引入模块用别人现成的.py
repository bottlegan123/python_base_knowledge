# python的内置函数有限，有别人写好的现成的可以导入来自己用

# 求中位数不是python的内置函数，可以自己写（因为不是很麻烦），也可以用别人写好的

# 求一个列表的中位数
def median(num_list):
    sorted_list = sorted(num_list)
    n = len(num_list)
    # 如果是奇数个数则直接取中间的那个
    if n % 2 == 1:
        return sorted_list[int((n+1) / 2 - 1)]   # 索引括号中只能是整数不能是浮点数
        # 如果是偶数个数则取中间两个数的平均数
    else:
        # // 表示除的结果只保留整数部分，把小数点及小数点之后的全部去除
        return (sorted_list[n // 2]+sorted_list[n // 2 - 1]) / 2


print(median([2, 3, 5, 6, 8]))


# 上面是自己编写，也可以引入模块

import statistics
print(statistics.median([2, 3, 5, 6, 8]))
print(statistics.mean([2, 3, 5, 6, 8]))


from statistics import median, mean  # 使用这个比较好


from statistics import *  # 这样会把模块里面所以函数引入，当有多个模块引入时可能会出现命名冲突


# 用第三方库的模块
# 用第三方模块时要先在终端安装语法是： pip install 库的名称，然后再import之后就可以用了

