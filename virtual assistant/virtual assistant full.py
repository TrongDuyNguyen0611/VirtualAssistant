import speech_recognition as sr
import pyttsx3
from datetime import date,datetime
from gtts import gTTS
import pyaudio
import playsound
import os
import datetime
import time
import wikipedia
import webbrowser
Duynt_mouth = pyttsx3.init()
Duynt_brain =""

x = datetime.datetime.now()
thoigian = int(x.strftime("%H"))
if 5 < thoigian < 12 :
	loichao = "Chào buổi sáng tốt lành  "
elif 12 <= thoigian < 13:
	loichao = "Nghỉ trưa thôi "
elif 13 <= thoigian < 17:
	loichao = "Chào buổi chiều "
elif 18 <= thoigian < 23:
	loichao = "Chào buổi trưa "
elif thoigian >= 23:
	loichao = "Đêm rồi đi ngủ thôi "

# def playmusic():
#     global run
#     music_dir = 'C:\\music'          # thư mục để nhạc
#     songs = os.listdir(music_dir)
#     os.startfile(os.path.join(music_dir,songs[0]))
#     run = False

def wiki(keyword):
    try:
        print('**đang tim kiem tren wiki**')
        print(wikipedia.summary(keyword))       # search wiki
    except:
        print('Không mở được.')
        print('')
    run = False

# playmusic()
i=0
while i<3:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Duynt: Mời bạn nói: ")
		audio = r.listen(source,timeout=5, phrase_time_limit=5)
		print("Duynt:...")
		try: 
			you = r.recognize_google(audio,language="vi-VI")
			print("You -->: {}".format(you))
		except:
			i=i+1
			print("Duynt: Xin lỗi! tôi không nhận được voice!")
			Duynt_brain = "Mình không nghe được bạn nói, bạn nói lại nhé"
			output = gTTS(Duynt_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			os.remove('output.mp3')
			continue
		if "chào" in you:
			Duynt_brain = loichao + "Tôi là Duynt, trợ lý ảo của bạn. Bạn cần giúp gì không"
			print("Duynt: ",Duynt_brain)
		elif "ngày" in you:
			today = date.today()
			Duynt_brain = today.strftime("Hôm nay là ngày: %d tháng %m năm %Y")
			print ("Duynt: ", Duynt_brain)
		elif "giờ" in you:
			giờ = time.localtime()
			Duynt_brain= time.strftime ("Lúc này là: %H gi{y} %M phút %S giây").format(y='ờ')
			print ("Duynt: ",Duynt_brain)
		

		elif 'nhạc trên máy' in you:
			Duynt_brain = "Đang mở nhạc trên offline"
			print("Duynt: ",Duynt_brain)
			playmusic()
		
		elif "YouTube" in you:
			webbrowser.open('https://www.youtube.com/',new=1)
			Duynt_brain="Ok! youtube đang được mở"
			print('you:',you)
			print('Duynt:',Duynt_brain)
			output = gTTS(Duynt_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break

		elif "Chrome" in you:
			webbrowser.open('https://www.google.com.vn/',new=1)
			Duynt_brain="Ok!Google đang được mở"
			print('you:',you)
			print('Duynt:',Duynt_brain)
			output = gTTS(Duynt_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break
		elif "Facebook" in you:
			webbrowser.open('https://www.facebook.com/',new=1)
			Duynt_brain="Ok!facebook đang được mở"
			print('you:',you)
			print('Duynt:',Duynt_brain)
			output = gTTS(Duynt_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break

		elif "Gmail" in you:
			webbrowser.open('https://mail.google.com/mail/u/0/#inbox',new=1)
			Duynt_brain="Ok!Gmail đang được mở"
			print('you:',you)
			print('Duynt:',Duynt_brain)
			output = gTTS(Duynt_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break
		elif "music" in you:
			webbrowser.open('https://www.youtube.com/results?search_query=music',new=1)
			Duynt_brain="Ok!Nhạc đang được mở"
			print('you:',you)
			print('Duynt:',Duynt_brain)
			output = gTTS(Duynt_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break

		elif "edm" in you:
			webbrowser.open('https://www.youtube.com/watch?v=KjvM4WJcedA',new=1)
			Duynt_brain="Ok!EDM đang được mở"
			print('you:',you)
			print('Duynt:',Duynt_brain)
			output = gTTS(Duynt_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break
		elif "Wikipedia" in you:
			r = sr.Recognizer()
			with sr.Microphone() as source:
				print("Wikipedia: ...")
				audio = r.listen(source,timeout=5, phrase_time_limit=5)
			try:
				wiki = r.recognize_google(audio,language="vi-VI")
			except:
				wiki='Sorry'
			wikipedia.set_lang("vi")
			wiki=wikipedia.summary(wiki)
			print(wiki)
			Duynt_brain=wiki
			
			output = gTTS(Duynt_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			os.remove('output.mp3')
			Duynt_brain='Đến đây là hết thông tin'
			time.sleep(3)
			continue
		elif "bật đèn" in you:
			webbrowser.open('http://172.20.10.3/LED=OFF',new=1)
			Duynt_brain="Ok!Đèn hành lang đang được mở"
			print('you:',you)
			print('Duynt:',Duynt_brain)
			output = gTTS(Duynt_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break
		elif "Tắt Đèn" in you:
			webbrowser.open('http://172.20.10.3/LED=ON',new=1)
			Duynt_brain="Ok!Đèn hành lang đang được tắt"
			print('you:',you)
			print('Duynt:',Duynt_brain)
			output = gTTS(Duynt_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break
		elif "Flappy Bird" in you:
			os.system('python flappybird.py')
			Duynt_brain='Đang mở game'	
		elif 'nghỉ 10 giây' in you:
			Duynt_brain='Finish'
			time.sleep(10)

		elif 'nghỉ 1 phút' in you:
			Duynt_brain='Finish'
			time.sleep(60)

		elif 'tắt máy' in you:
			os.system('shutdown -s')

		elif 'khởi động lại' in you:
			os.system('shutdown -r')
		
		elif "tạm biệt" in you:
			Duynt_brain = "Tạm biệt bạn, hẹn gặp lại"
			output = gTTS(Duynt_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break
		else:
	 		Duynt_brain = "Xin lỗi phần này tôi chưa được học"

		output = gTTS(Duynt_brain,lang="vi", slow=False)
		output.save("output.mp3")
		playsound.playsound('output.mp3')
		os.remove('output.mp3')
