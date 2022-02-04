#東京湾のみ　トリミング
import sys
from PIL import Image
import time

import os
from glob import glob
import schedule

import shutil

def trim(left,top,right,bottom):
    #最新のファイルのフルパスを取得
    def image_name(dirname):
        target = os.path.join(dirname, '*')
        files = [(f, os.path.getmtime(f)) for f in glob(target)]
        latest_modified_file_path = sorted(files, key=lambda files: files[1])[-1]
        return latest_modified_file_path[0]
    if __name__ == '__main__':
        dirname = "C:/student/Documents/cron_test/image"
        full_path=image_name(dirname)

    #フルパスからファイル名だけ取得
    im_name=os.path.basename(full_path)


    im = Image.open('{}'.format(full_path))
    #トリミングする座標の指定
    im_crop = im.crop((left,top,right,bottom))
    im_crop.save("C:/Users/student/Documents/cron_test/image/"+im_name,quality=95)
    
    # schedule.every(3).seconds.do(trim,left,top,right,bottom)
trim(496, 208, 646, 358)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
    #フォルダの中身ごと削除
    # shutil.rmtree('C:/Users/student/Documents/sotuken/auto_save_trim/image')

    # #フォルダの作り直し
    # os.mkdir('C:/Users/student/Documents/sotuken/auto_save_trim/image')







