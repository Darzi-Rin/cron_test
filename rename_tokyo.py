from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import schedule
import sys
from PIL import Image
from glob import glob
import shutil

def image_name(dirname):
        target = os.path.join(dirname, '*')
        files = [(f, os.path.getmtime(f)) for f in glob(target)]
        latest_modified_file_path = sorted(
        files, key=lambda files: files[1])[-1]
        return latest_modified_file_path[0]
if __name__ == '__main__':
    dirname = "C:/Users/student/Documents/cron_test/image_trim_tokyo"
    full_path=image_name(dirname)

    # フルパスからファイル名だけ取得
    im_name = os.path.basename(full_path)
    im_name2 = os.path.basename(full_path)
    change = im_name[:10]
    renames = change + ".png"
    im_name_change = "C:/Users/student/Documents/cron_test/image_trim_tokyo/" + im_name2
    im_name_change2 = "C:/Users/student/Documents/cron_test/" + renames
    os.rename(im_name_change, renames)