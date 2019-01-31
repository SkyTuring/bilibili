import os
import json
from natsort import natsorted


def get_sub_dir_names(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return dirs


def get_sub_file_names(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files


if __name__ == "__main__":
    srcFile = "E:\\BiliBili\\25609975"  # 文件所在目录
    dir_names = get_sub_dir_names(srcFile)
    dir_names = natsorted(dir_names)
    for path in dir_names:
        file_path = os.path.join(srcFile, path)
        file_names = get_sub_file_names(file_path)
        for info_file_name in file_names:
            info_file_path = os.path.join(file_path, info_file_name)
            if info_file_path.endswith("info"):
                info_file = open(info_file_path, encoding='UTF-8')
                part = json.loads(info_file.read())["TotalParts"]
                if str(part) != "1":
                    print(info_file_path, end="")
                    print("\t\t", end="")
                    print(part)
                info_file.close()
