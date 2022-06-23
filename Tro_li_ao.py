#truy cập, xử lí file hệ thống
import os
import threading
from tkinter import Frame, Label
import tkinter as tk
#Chuyển âm thanh thành văn bản
import speech_recognition as sr
#Xử lí thởi gian
from time import strftime
import time
import sys
import ctypes
import wikipedia
import datetime
#Chọn ngẫu nhiên
import random
#Truy cập web, trình duyệt
import re
import webbrowser
#Lấy thông tin từ webS
import requests
import json
#Truy cập web, trình duyệt, hỗ trợ tìm kiếm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from youtube_search import YoutubeSearch
#Chuyển văn bản thành âm thanh
import pyttsx3

language = 'vi'
path = ChromeDriverManager().install()
wikipedia.set_lang('vi-VN')
with open('intents.json',encoding='utf-8') as file:
    data1 = json.load(file)
# def Assist_giaodien(manh,text):
#     frame = Frame(manh)
#     Scroll = tk.Scrollbar(frame)
#     assistant_text = tk.Text(frame, height=8,width=30,bd=0,bg='white',font=("Courier",13,"bold"))
#     Scroll.config(command=assistant_text.yview,bd=0)
#     assistant_text.config(yscrollcommand=Scroll.set)
#     assistant_text.insert(tk.END, text)
#     frame.place(x=150,y=250)
# Chuyển văn bản sang giọng nói
def speak(text):
    print("Trợ lí ảo: {}".format(text))
    troliao = pyttsx3.init()
    vi_voice_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
    troliao.setProperty('voice',vi_voice_id)
    voice = troliao.getProperty('rate')
    troliao.setProperty('rate',130)
    volume = troliao.getProperty('volume')
    troliao.setProperty('volume',1.0)
    troliao.say(text)
    troliao.runAndWait()

# chuyển giọng nói thành văn bản
def get_voice():
     m = sr.Recognizer()
     with sr.Microphone() as source:
        time.sleep(2)
        print("Tôi: ", end = '')
        audio = m.listen(source, phrase_time_limit=5)
        try:
            text = m.recognize_google(audio, language="vi-VN")
            # user_text = Text(height =2, width=40,bd=0,font=("Courier",13,"bold"))
            # user_text.insert(Tk.END,text)
            # user_text.place(x=160,y=200)
            print(text)
            return text
        except:
            # print("...")
            return 0

def stop():
    list5=["Vâng chào bạn","Hẹn gặp lại bạn nhé!","Hẹn gặp lại sau nhé","Chào tạm biệt bạn"]
    more5= random.choice(list5)
    speak(more5)
    listen_label2()
def get_text():
    for i in range(4):
        text = get_voice()
        if text:
            return text.lower()
        elif i < 3:
            speak(" Không nghe rõ, bạn có thể nói lại không ?")
    time.sleep(5)
    stop()
    return 0

def talk(name):
    day_and_time = int(strftime('%H'))
    if day_and_time >= 6 and day_and_time < 12:
        speak("Chào buổi sáng {}. Chúc bạn ngày mới tốt lành!".format(name))
    elif day_and_time >= 12 and day_and_time < 18:
        speak("Chào buổi chiều {}!".format(name))
    else:
        speak("Chào buổi tối {}!".format(name))
    time.sleep(2)
    speak("Bạn có khỏe không ?")
    time.sleep(2)
    ans = get_voice()
    if ans:
        if "có" in ans or "khỏe" in ans:
            list2 = ["Thật là tốt!","Bạn hãy thường xuyên chơi thể thao nhé , cho cơ thể được khỏe "]
            more2 = random.choice(list2)
            speak(more2)
        else:
            list3=["Bạn hãy tự thưởng cho mình bằng ly nước cam nhé","Vậy à, bạn nên nghỉ ngơi đi!"]
            more3=random.choice(list3)
            speak(more3)
    time.sleep(1)

    speak("Bạn đã ăn cơm chưa ?")
    time.sleep(1)
    ans = get_voice()
    if ans:
        if "rồi" in ans or "mới ăn xong" in ans:
            list = ["Thật là tốt. Bạn nên tráng miệng với một ít trái cây nhé!",
            "Bạn ăn thật nhiều để có sức khỏe nhé","Ăn xong thì bạn giúp mẹ rửa bát đi nhé!  hahaha"]
            more=random.choice(list)
            speak(more)
        else:
            speak("Bạn mau đi ăn thôi. Chúc bạn ăn ngon miệng nhé!")
    time.sleep(1)

    speak("Bạn đã làm xong bài tập chưa ?")
    time.sleep(1)
    ans = get_voice()
    if ans:
        if "rồi" in ans:
            list1 = ["Thật là tốt!. Chúc bạn một kỳ nghỉ tốt lành","Bạn hãy nghỉ ngơi sau khi làm bài tập thật khó và nhiều nhé!","Bạn hãy ra ngoài chơi long nhong nhé. Chúc bạn chơi vui vẻ"]
            more1 = random.choice(list1)
            speak(more1)
        else:
            speak("Vậy à, bạn nên có gắng hoàn thành thật tốt nhé!")   

def open_website(text):
    timkiem = re.search ('mở (.+)', text)
    if timkiem:
        mo_web = timkiem.group(1)
        url = 'https://www.' + mo_web
        webbrowser.open(url)
        speak("Trang web của bạn đã được mở lên!")
        return True
    else:
        return False
       
def google_search(text):
    search_for = text.split("kiếm", 1)[1]
    speak("Google đã được mở")
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    query = driver.find_element_by_xpath("//input[@name='q']")
    query.send_keys(str(search_for))
    query.send_keys(Keys.RETURN)
    time.sleep(15)
def youtube():
    speak("Xin mời bạn chọn bài hát")
    time.sleep(2)
    my_song = get_text()
    while True:
        result = YoutubeSearch(my_song, max_results = 10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Bài hát của bạn đã được mở, hãy thưởng thức nó!")
    time.sleep(10)

def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak("Bây giờ là %d giờ %d phút" % (now.hour, now.minute))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d " % (now.day, now.month, now.year))
    else:
        speak("Tôi không hiểu")
    
def weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ")
    time.sleep(3)
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_text()
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temp = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        sun_time  = data["sys"]
        sun_rise = datetime.datetime.fromtimestamp(sun_time["sunrise"])
        sun_set = datetime.datetime.fromtimestamp(sun_time["sunset"])
        wther = data["weather"]
        weather_des = wther[0]["description"]
        now = datetime.datetime.now()
        noi_dung = """
        - Hôm nay là ngày {day} tháng {month} năm {year}. Mặt trời mọc vào {hourrise} giờ {minrise} phút
        - Mặt trời lặn vào {hourset} giờ {minset} phút
        - Nhiệt độ trung bình là {temp} độ C
        - Áp suất không khí là {pressure} héc tơ Pascal
        - Độ ẩm là {humidity}%
        - Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day, month = now.month, year= now.year, hourrise = sun_rise.hour, minrise = sun_rise.minute,
                                                                           hourset = sun_set.hour, minset = sun_set.minute, 
                                                                           temp = current_temp, pressure = current_pressure, humidity = current_humidity)
        speak(noi_dung)
        time.sleep(3)
    else:
        speak(f"Không tìm thấy thành phố")
                
def open_application(text):
    if "google" in text:
        speak("Mở google chrome")
        os.startfile('https://www.google.com')
    elif "word" in text:
        speak("Mở Microsoft Word")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word")
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel")
    elif "powerpoint" in text:
        speak("Mở Microsoft PowerPoint")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint")
    elif "proteus" in text:
        speak("Mở Protues")
        os.startfile("C:\Program Files (x86)\Labcenter Electronics\Proteus 8 Professional\BIN\PDS.EXE")
    else:
        speak("Phần mềm của bạn chưa được cài đặt!")

def love():
    list4 = ["Hè đến nắng vàng. Lão Hạc nhớ chó anh thì nhớ em",
                "Trăng kia ai vẽ mà tròn, Lòng anh ai trộm mà hoài nhớ thương",
                "Thiếu 500 nghìn là anh tròn một củ. Thiếu em nữa là anh đủ một đôi.",
                "Suốt bao năm lòng anh luôn yên tĩnh. Gặp em rồi, tĩnh lặng hóa phong ba.",
                "Nắng kia là của ông trời, còn em đã của ai rồi hay chưa? ",
                "Mây kia là của hạt mưa, em xem đã thích anh chưa hay rồi?",
                "Cánh đồng xanh xanh, làn mây trăng trắng. Tưởng là say nắng ai ngờ say em.",
                "Đố ai quét sạch được lá rừng. Đố ai khuyên được anh ngừng yêu em!",
                "Trời không xanh, mây cũng không trắng, anh không say nắng, nhưng lại say em",
                "Cho anh một cốc trà đào, tiện cho anh hỏi lối vào tim em",
                "Anh đây rất thích đồng hồ, thích luôn cả việc làm bồ của em",
                "Vertor chỉ có một chiều, anh dân chuyên toán chỉ yêu 1 người.",
                "Hoa vô tình bỏ rơi cành lá, người vô tình bỏ lỡ tơ duyên",
                "Ngoài kia bão táp mưa sa, bôn ba mệt quá về nhà với anh",
                "Nhân gian vốn lắm bộn bề, sao không bỏ hết mà về với anh",
                "Thức khuya anh tỉnh bằng trà, yêu em anh trả bằng tình được không?"]
    more4 = random.choice(list4)
    speak(more4)

def temperature(text):
    temp="mát mẻ"
    if text<15:
        temp="lạnh buốt giá"
    elif text<20:
        temp="khá lạnh"
    elif text<30:
        temp="mát mẻ"
    elif text<33:
        temp="khá nóng"
    else:
        temp="nóng bức"

    return temp

def menu():
    speak("""Tôi có thể làm những việc sau:
    1. Chào hỏi
    2. Thông báo ngày giờ
    3. Mở website và các ứng dụng
    4. Tìm kiếm trên Google
    5. Dự báo thời tiết
    6. Mở video nhạc
    7. Đọc báo hôm nay 
    8. Thả thính crush""")
    time.sleep(5)

def listen_label1():
    time.sleep(1)
    listen_label1 = Label(text="Trợ lí ảo đang lắng nghe...",border=0,bg='light blue',font=("Counter",13,"bold"))
    listen_label1.place(x=130,y=445)
def listen_label2():
    time.sleep(1)
    listen_label2 = Label(text=" Ngưng hoạt động!!!         ",border=0,bg='light blue',font=("Counter",13,"bold"))
    listen_label2.place(x=130,y=445)

def main_one():
    speak("Xin chào, bạn tên là gì nhỉ?")
    # print("Xin chào, bạn tên là gì nhỉ?")
    # time.sleep(1)
    name = get_text()
    if name:
        speak("Chào bạn {}".format(name))
        time.sleep(1)
        speak("Bạn cần tôi giúp gì không ạ!")
        time.sleep(1)
        while True:
            text = get_text()
            if not text:
                listen_label2()
                break
            elif "trò chuyện" in text or "nói chuyện" in text:
                talk(name)
            elif "hẹn gặp lại" in text or "tạm biệt" in text:
                stop()
                listen_label2()
                break
            elif "mở" in text:
                if "mở google và tìm kiếm" in text:
                    google_search(text) 
                    
                elif "." in text:
                    open_website(text)               
                else:
                    open_application(text)              
            elif "ngày" in text  or "giờ" in text:
                get_time(text)
               
            elif "chơi nhạc" in text or "phát nhạc" in text:
                youtube()
            elif "nói câu sến" in text or "cách để crush đỗ" in text:
                love()            
            elif "thời tiết" in text:
                weather()             
            elif "có thể làm gì" in text or " làm được những gì" in text:
                menu()
        
def thread_mutiii():
    t1 = threading.Thread(target=listen_label1,args=())
    t2 = threading.Thread(target=main_one,args=())
    t1.start()
    t2.start()