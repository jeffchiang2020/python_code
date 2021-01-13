from sys import argv

script,input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline())

a = open(input_file)

print("首先让我们打印整个文件:\n")
print_all(a)

print("让我们回个文件开始位置：")
rewind(a)

print("让我们打印前三行：\n")

a_line = 1
print_a_line(a_line,a)

a_line += 1
print_a_line(a_line,a)

a_line += 1
print_a_line(a_line,a)

