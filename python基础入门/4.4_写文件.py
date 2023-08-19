# with open("./data.txt", "r", encoding="utf-8") as f:
# 读文件时文件不存在会报错，而写文件时文件不存在会自动新建一个文件
# 如果是对已经存在的文件进行write会把原来的文件替换掉重新写、
# 怎么办啊原来的文件保留且在原来文件上面写呢？那得把读文件和写文件一起用蚕丝可以实现
with open("./data.txt", "w", encoding="utf-8") as f:  # utf-8保证写入的内容也是utf-8编码的
    f.write("hello")
# 写文件下不可以读文件，读文件下不可以写文件
# 但是有办法既可以读文件也可以写文件

with open("./data1.txt", "a", encoding="utf-8") as f:  # 文件不存在会自动新建一个文件
    f.write("\nyoo")  # 没有换行符就会紧跟在后面写
    f.write("\nbey")

# a w 是只包涵write的方式，所以会自动创建文件
# r w+ r+ 是包含了write和read的方式如果文件不存在会报错

# r+可以实现同时读和写
# r+ 形式下是对在文件中的位置后面的内容的改写，只有 a 形式才是直接在后面追加
with open("./data.txt", "r+", encoding="utf-8") as f:
    f.read()  # 这里读取之后就位于文件的最末尾了，write自然就会在后面写
    f.write("\nhello")  # 并不是直接在后面追加，而是在所在位置后面改写
# 如果前面不在前面一行加f.read()就会是对文件的前面部分的改写

# 写文件练习
# 任务1：在一个新的名字为"poem.txt"的文件里，写入以下内容：
# 我欲乘风归去，
# 又恐琼楼玉宇，
# 高处不胜寒。
with open("./poem.txt", "w", encoding="utf-8") as f:
    f.write("我欲乘风归去，\n又恐琼楼玉宇，\n高处不胜寒。\n")

# 任务2：在上面的"poem.txt"文件结尾处，添加以下两句：
# 起舞弄清影，
# 何似在人间。
with open("./poem.txt", "a", encoding="utf-8") as f:
    f.write("起舞弄清影，\n")
    f.write("何似在人间。")

