# python读文件首先要找到文件的位置
# open("文件路径", "模式")：可以是相对路径也可以是绝对路径
# open("文件路径", "r")  open("文件路径", "r") r代表读取模式,w代表写入模式
# open("./data.txt", "r", encoding="utf-8")，UTF-8表示编码模式一般都是utf-8
# python喜欢纯文本格式，如果是word里面有字号、字体的python读出来就会很乱
f = open("./data.txt", "r", encoding="utf-8")
content = f.read()  # f.read()会把所有文件的内容进行返还
print(f.read())  # 这个会全部读完，程序会记录读到了那个位置，不会读取换行符
print(f.read())  # 再往下读会读出空的
f.close()

# 有时候文件太大你不想全部读完，这个时候就可以给read传入一个字节
f = open("./data.txt", "r", encoding="utf-8")
print(f.read(1))  # 这里面是字节数不是字数
print(f.readline())  # 还会读换行符，如果你写的行数多于文本本身的行数那么读到结尾时会返回空字符串表示后面没有内容了
# 前面已经读了第一个字节所以第二个print会从第二个字节开始读
f.close()

f = open("./data.txt", "r", encoding="utf-8")
line = f.readline()
while line != "":
    print(line)
    line = f.readline()
f.close()

f = open("./data.txt", "r", encoding="utf-8")
print(f.readlines())  # 会读取全部文件内容包括换行符，把每行内容储存到列表里，经常可以和for循环一起使用
f.close()

f = open("./data.txt", "r", encoding="utf-8")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

with open("./data.txt", "r", encoding="utf-8") as f:  # 缩进结束了文件就自动关闭了
    print(f.read())
