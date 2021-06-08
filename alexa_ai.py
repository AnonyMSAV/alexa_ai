import speech_recognition as sr
import pyttsx3
import pyautogui
import os
import wolframalpha
import webbrowser
import pyjokes
import datetime
from bs4 import BeautifulSoup
import requests

r=sr.Recognizer()
mic=sr.Microphone()
speak = pyttsx3.init()
speak.setProperty("rate", 180)
voices = speak.getProperty('voices')
speak.setProperty('voice', voices[1].id)

def spk(sound):
	speak.say(sound)
	speak.runAndWait()


def cmd():
	with mic as s:
		print('Listening...')
		r.adjust_for_ambient_noise(s) 
		ad=r.listen(s) 
	try:
		print('Recognizing...')
		sts=r.recognize_google(ad,language='en=in')
		spk(f'You said : {sts}')
		print(f'You said : {sts}')
	except: 
		spk("I didn't get that")
		return "None"
	return sts 

def time(sts):
	t=datetime.datetime.now()
	if("what's the time now" in sts):
		spk(f'Now time is {t.hour}:{t.minute}')

	elif("today"in sts):
		spk(f'Today is {t.day}th of {t.month} {t.year}')

def screen(sts):
	if('screenshot please' in sts):
		ss=pyautogui.screenshot()
		ss.save('path to save screenshot')	
		spk('Ok sir, It saved')

def greet(sts):
	if('Alexa' in sts):
		spk('Yes sir?')
	if('hii'in sts):
		spk('Hii sir')

def quiz(sts):
	if('I need help' in sts):
		spk('Tell me sir')
		client = wolframalpha.Client('8KQTA2-G487L9YH39')
		res = client.query(cmd())
		answer = next(res.results).text
		spk(answer)

def search(sts):
	if('Google' in sts):
		spk('What you want to search sir?')
		webbrowser.open_new_tab(f'https://www.google.com/search?q={cmd()}')

	elif('YouTube'in sts):
		spk('What you want to search sir?')
		webbrowser.open_new_tab(f'https://www.youtube.com/results?search_query={cmd()}')

def app(sts):
	if('play music' in sts):
		spk('As you wish sir')
		songs = os.listdir('music path')
		os.startfile('music path'+songs[0])
		return oo
	elif('shutdown computer' in sts):
		spk('As you wish sir')
		os.system('shutdown /s ')
		quit()
	elif('restart computer' in sts):
		spk('As you wish sit')
		os.system('shutdown /r ')
		quit()
	elif('logout computer' in sts):
		spk('As you wish sir')
		os.system('shutdown -l')
		quit()

def slp(sts):
	import time
	if('stop listening' in sts):
		spk('set time sir')
		i=int(cmd())
		spk("Sleeping")
		time.sleep(i)

def alarm(sts):
	if('set alarm' in sts):
		h=int(input('Hour : '))
		m=int(input('Minutes : '))
		while True:
			set_alarm_time = f"{h}:{m}"
			c = datetime.datetime.now()
			c_time=c.strftime("%H:%M")
			if(c_time == set_alarm_time):
				while True:
					if('stop' in sts):
						break
					else:
						spk("Wake up Sir")
def weather(sts):
	if('weather report' in sts):
		spk('Place please sir')
		url = "https://www.google.com/search?q="+"weather"+cmd()
		html = requests.get(url).content
		soup = BeautifulSoup(html, 'html.parser')
		temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
		str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
		data = str.split('\n')
		sky = data[1]
		listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
		strd = listdiv[5].text
		pos = strd.find('Wind')
		other = strd[pos:]
		spk("Temperature is"+temp)
		spk("Sky Description: "+sky)
		spk(other)      

while True:
	if('Alexa' in cmd()):
		spk('Can I help you sir')
		while True:
			sts=cmd()
			if('offline' in sts):
				spk('Good Bye sir')
				exit()
			elif('tell me a joke' in sts):
				spk(pyjokes.get_joke())
				break
			quiz(sts)
			greet(sts)
			time(sts)
			screen(sts)
			search(sts)
			app(sts)
			slp(sts)
			alarm(sts)
			weather(sts)
