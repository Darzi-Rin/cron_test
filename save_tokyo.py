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

def login_save(id, userpw, area):
    #画像保存先指定
    iDir =os.path.abspath("C:/Users/student/Documents/cron_test/image_trim_tokyo")
    # iDir =os.path.abspath("C:/Users/ksout/Documents/中間発表_画像取得/image_copy")

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"download.default_directory": iDir })

    
    browser = webdriver.Chrome('C:/Users/student/Documents/chromedriver.exe',chrome_options=options)
    #検索にGoogleChrome指定
    url = "https://services.sentinel-hub.com/oauth/auth?client_id=1febe974-ca4f-44c1-9fc8-bafbd3bb4abd&redirect_uri=https%3A%2F%2Fapps.sentinel-hub.com%2Feo-browser%2FoauthCallback.html&response_type=token&state=&scope=EOBrowser%20SH"
    #ログインページのURL指定
    browser.maximize_window()

    browser.get(url)

    # ログインIdとパスワードの入力領域を取得します。 
    login_id = browser.find_element_by_xpath("//*[@id='loginForm']") 
    login_pw = browser.find_element_by_xpath("//*[@id='submitForm']/div[3]/div[1]/input")

    # ログインIDとパスワードを入力します。 
    userid = id
    userpw = userpw
    login_id.send_keys(userid) 
    # time.sleep(8)
    login_pw.send_keys(userpw)

    # ログインボタンをクリックします。 
    login_btn = browser.find_element_by_xpath("//*[@id='submitForm']/div[4]/button") 
    login_btn.click()

    browser.get("https://apps.sentinel-hub.com/eo-browser/?zoom=8&lat=35.84231&lng=138.58704&themeId=DEFAULT-THEME")

    #ポップアップの表示を閉じる
    browser.implicitly_wait(7)
    close_btn = browser.find_element_by_xpath("//*[@id='react-joyride-step-0']/div[@class='__floater __floater__open']/div[@class='__floater__body']/div[@class='tutorial-wrap']/div[@class='tutorial-body']/button[@class='close-cross']/span[@class='rodal-close']")
    #ポップアップの閉じるボタンのxpath取得
    close_btn.click()
    #閉じるボタンクリック


    # browser.implicitly_wait(20)
    login_btn2 = browser.find_element_by_xpath("//*[@id='logo-header']/div[2]/div/span/div") 
    login_btn2.click()
    #ログイン〇



    #↓画像保存↓

    #Pinsクリック
    pins_btn = browser.find_element_by_xpath("//*[@id='pins-tabButton']")
    pins_btn.click()

    #地域選択
    area=browser.find_element_by_xpath(area)
    area.click()

    #Discoverクリック
    discover_btn = browser.find_element_by_xpath("//*[@id='SearchTabButton']")
    discover_btn.click()

    #Searchクリック
    time.sleep(3)
    search = browser.find_element_by_xpath("//*[@id='SearchTab']/div/div/div[3]/a") 
    search.click()

    #場所選択
    area_choise = browser.find_element_by_xpath("//*[@id='SearchTab']/div/div[1]/div[2]/div/div[2]/div/div[1]/img") 
    area_choise.click()
    # area_choise = browser.find_element_by_xpath("//*[@id='SearchTab']/div/div[1]/div[2]/div[1]/div[19]/div/div[1]/a") 
    # area_choise.click()

    # ズーム
    zoom_btn = browser.find_element_by_xpath("//*[@id='root']/div[@id='app']/div[@id='map']/div[@class='leaflet-control-container']/div[@class='leaflet-bottom leaflet-right']/div[@class='leaflet-control-zoom leaflet-bar leaflet-control']/a[@class='leaflet-control-zoom-in']") 
    zoom_btn.click()
    time.sleep(3)
    zoom_btn.click()

    time.sleep(15)
    #dlクリック
    time.sleep(3)
    download_image = browser.find_element_by_xpath("//*[@id='root']/div[@id='app']/div[@id='map']/div[@class='controls-wrapper']/div[@class='img-download-btn-wrapper']") 
    download_image.click()

    #キャプションの削除
    time.sleep(3)
    cap_del = browser.find_element_by_xpath("//*[@id='app']/div[4]/div[2]/div/div[2]/div/div[1]/div/div/div[1]") 
    cap_del.click()

    #マップオーバーレイ削除
    mapov_del = browser.find_element_by_xpath("//*[@id='app']/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div[2]") 
    mapov_del.click()


    time.sleep(8)
    download = browser.find_element_by_xpath("//*[@id='app']/div[4]/div[2]/div/div[2]/a") 
    download.click()
    time.sleep(8)
    # 終了処理
    browser.close()

    # def image_name(dirname):
    #     target = os.path.join(dirname, '*')
    #     files = [(f, os.path.getmtime(f)) for f in glob(target)]
    #     latest_modified_file_path = sorted(files, key=lambda files: files[1])[-1]
    #     return latest_modified_file_path[0]
    # if __name__ == '__main__':
    #     dirname = "C:/Users/ksout/Documents/中間発表_画像取得/自動保存フォルダ/image"
    #     full_path=image_name(dirname)

    # #フルパスからファイル名だけ取得
    # im_name=os.path.basename(full_path)
    # print(im_name[1:3])
    # im = Image.open('{}'.format(full_path))




tokyo_bay ="//*[@id='0']/div[1]/div[3]/div[3]/span"
osaka_bay ="//*[@id='1']/div[1]/div[3]/div[3]/span"




login_save("ksw2070289@stu.o-hara.ac.jp","o-hara_kashiwa",tokyo_bay)


#↓　　定期実行　　↓
# スケジュール登録
#5秒毎
# schedule.every(4).seconds.do(login_save,id="ksw2070289@stu.o-hara.ac.jp", userpw="o-hara_kashiwa", area=tokyo_bay)


#三日毎
# schedule.every(3).days.do(login_save,id="ksw2070289@stu.o-hara.ac.jp", userpw="o-hara_kashiwa", area=tokyo_bay)

#ec2でdriverアップロード 
# https://prograshi.com/language/python/ec2-selenium-scraiping-summary/