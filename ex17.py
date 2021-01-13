from sys import argv
from os.path import exists

script, from_file,to_file = argv

print(f"复制文件{from_file}到{to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"需的复制的文件有{len(indata)} bytes ")

print(f"{to_file}这份文件存在吗？{exists(to_file)}")
print(f"准备完毕，点击回车后开始复制，CTRL-C退出。")
input()

out_file = open(to_file,'w')
out_file.write(indata)

print("复制完毕")

out_file.close()
in_file.close()