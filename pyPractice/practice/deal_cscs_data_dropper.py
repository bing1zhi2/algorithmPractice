# -*- coding:utf-8 -*-
"""
复制2-29 和 30 的高铁4c数据 到 一个目录中，方便后面打标签
"""
import os


data_dir= 'H:\\高铁接触网data\\201902260255_郑机线_上行_新郑机场站_郑州东站'
data_dir= 'H:\\高铁接触网data\\201902260218_郑机线_下行_郑州东站_新郑机场站'
data_dir= 'H:\\高铁接触网data\\201902260110_郑开线_下行_宋城路站_郑州东站'
data_dir= 'H:\\高铁接触网data\\201902260011_郑开线_上行_郑州东站_宋城路站'
data_dir= 'H:\\高铁接触网data\\201901150006_郑徐线_上行_郑州东站徐兰场_商丘站'

dest_dir= 'H:\\高铁接触网data\\4c_dropper\\4'

def cp_dropper():
    print(os.listdir(data_dir))
    direction_files_path = os.listdir(data_dir)
    count = 0
    for file_path in direction_files_path:
        dir_one = os.path.join(data_dir,file_path)

        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir)

        if os.path.isdir(dir_one):
            print('dir_one ' , dir_one)
            print('file_path startswith K', file_path.startswith('K'))
            if not file_path.startswith('K'):



                km_file_paths = os.listdir(dir_one)
                for km_file_path in km_file_paths:
                    print(km_file_path)
                    pillar_file_path = os.path.join(dir_one, km_file_path)

                    cscs_files = os.listdir(pillar_file_path)
                    for cscs_file in cscs_files:
                        one_file = os.path.join(pillar_file_path,cscs_file)
                        targetFile = os.path.join(dest_dir,cscs_file)
                        print('target file', targetFile)
                        if os.path.isfile(one_file):
                            if cscs_file.endswith('2_29.jpg') or cscs_file.endswith('2_30.jpg'):
                                print(cscs_file)
                                count = count + 1
                                if count > 2000:
                                    return
                                if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (
                                        os.path.getsize(targetFile) != os.path.getsize(one_file))):
                                    open(targetFile, "wb").write(open(one_file, "rb").read())





cp_dropper()