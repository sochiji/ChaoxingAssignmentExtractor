import sys
import os

try:
    import zipfile
except ImportError:
    import pip

    pip.main(["install", "zipfile"])
    import zipfile

file_list = [file_name for file_name in os.listdir() if file_name.endswith('.zip')]
if len(file_list) == 0:
    print("当前目录下", os.getcwd(), "未发现zip文件")
    sys.exit()
else:
    for index, file_name in enumerate(file_list, 1):
        print(index, file_name)
    index = int(input("请输入要处理的压缩包编号："))
    file_name = file_list[index - 1]

# 打开原始压缩文件
zip_file = zipfile.ZipFile(file_name, 'r')
# 创建一个新的压缩文件
new_zip_file = zipfile.ZipFile("已处理-" + file_name, 'w')

# 遍历原始压缩文件中的所有文件
for file_name in zip_file.namelist():
    # 打开每个学生的压缩文件
    inner_zip_file = zipfile.ZipFile(zip_file.open(file_name), 'r')
    decoded_name = '.'.join(file_name.encode('cp437').decode('utf8').split('.')[:-1])
    # 遍历学生压缩包中的每个文件
    for inner_file_name in inner_zip_file.namelist():
        inner_decoded_name = inner_file_name.encode('cp437').decode('utf8')
        # 如果文件名不是需要删除的文件，则将其写入新的压缩文件中
        if '学院' not in inner_decoded_name or '.doc' not in inner_decoded_name:
            file_content: bytes = inner_zip_file.read(inner_file_name)
            new_zip_file.writestr(r"{}/{}".format(decoded_name, inner_decoded_name), file_content)

# 关闭压缩文件
zip_file.close()
new_zip_file.close()

# 删除原始压缩文件
# os.remove('作业测试班-作业上传入口(word).zip')

# 将新的压缩文件重命名为原始压缩文件的名称
# os.rename('new.zip', '作业测试班-作业上传入口(word).zip')
