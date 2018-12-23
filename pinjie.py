from moviepy.editor import *
import os


def get_sub_file_names(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files


def pie_jie_file(file_path, out_file_name):
    video_final = []
    parts_name = []
    for file in get_sub_file_names(file_path):
        if file.endswith(".flv"):
            parts_name.append(os.path.join(file_path, file))
    parts_name.sort()
    print(parts_name)
    for part in parts_name:
        print(part)
        # 载入视频
        video = VideoFileClip(part)
        # 添加到数组
        video_final.append(video)
    # 拼接视频
    final_clip = concatenate_videoclips(video_final)
    # 生成目标视频文件
    final_clip.to_videofile(out_file_name, fps=24, remove_temp=True)
    final_clip.close()
    video_final.clear()






