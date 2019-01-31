import os
import json
import shutil
from natsort import natsorted


def get_sub_dir_names(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return dirs


def get_sub_file_names(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files


def makedir(dir_name):
    # 创建文件夹
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print("---------------------------")
        print("文件夹创建成功！")
        print(dir_path)
        print("---------------------------")


if __name__ == "__main__":
    file_format = '.flv'                    # 文件格式
    srcFile = "E:\\BiliBili"                # 文件所在目录
    title = ""                              # 文件标题
    dir_title = ""                          # 新目录名
    dir_path = "E:\\BiliBili"               # 新路径
    catalog = []                            # 最后目录
    total_part = ""
    global_index = 0
    dir_names = natsorted(get_sub_dir_names(srcFile))
    for path in dir_names:
        file_path = os.path.join(srcFile, path)
        file_names = natsorted(get_sub_file_names(file_path))
        for info_file_name in file_names:
            info_file_path = os.path.join(file_path, info_file_name)
            if info_file_path.endswith("info"):
                info_file = open(info_file_path, encoding='UTF-8')
                info = info_file.read()
                title = json.loads(info)["PartName"]
                total_part = json.loads(info)["TotalParts"]
                catalog.append(title)
                if not dir_title.strip():
                    # 创建文件夹
                    dir_title = json.loads(info)["Title"]
                    dir_path = os.path.join(dir_path, dir_title)
                    makedir(dir_path)
                    print(dir_path)
                info_file.close()
        if str(total_part) == "1":
            for file_name in file_names:
                old_file = os.path.join(file_path, file_name)
                if old_file.endswith(file_format):
                    global_index = global_index + 1
                    new_file = os.path.join(file_path, str(global_index).zfill(3)+"_"+title) + file_format
                    print(new_file)
                    # 改名
                    os.rename(old_file, new_file)
                    shutil.move(new_file, dir_path)
        else:
            index = 0
            file_names = natsorted(file_names)
            for file_name in file_names:
                old_file = os.path.join(file_path, file_name)
                if old_file.endswith(file_format):
                    index = index + 1
                    global_index = global_index + 1
                    new_file = os.path.join(file_path, str(global_index).zfill(3)+"_"+title+"_"+str(index)) + file_format
                    print(new_file)
                    # 改名
                    os.rename(old_file, new_file)
                    shutil.move(new_file, dir_path)

    # 生成目录
    write_catalog = open(dir_path + "\\catalog.txt", "w")
    catalog = natsorted(catalog)
    for title in catalog:
        write_catalog.write(title + "\n")
        print(title)
    write_catalog.close()
