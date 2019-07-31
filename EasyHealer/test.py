import time
import dataGrabber as dG
import setproctitle
from pynput.keyboard import Key, Controller
import random
from multiprocessing import Process

setproctitle.setproctitle("kupa.exe")
keyboard = Controller()

def manaPot():
	time.sleep(random.uniform(0.2, 0.4))
	keyboard.press(Key.f12)
	time.sleep(random.uniform(0.1,0.2))
	keyboard.release(Key.f12)

def healGran():
	time.sleep(random.uniform(0.3, 0.5))
	keyboard.press(Key.f10)
	time.sleep(random.uniform(0.1,0.2))
	keyboard.release(Key.f10)

def healSan():
	time.sleep(random.uniform(0.3,0.4))
	keyboard.press(Key.f11)
	time.sleep(random.uniform(0.1,0.2))
	keyboard.release(Key.f11)
	
def healGranSan():
	time.sleep(random.uniform(0.2, 0.3))
	keyboard.press(Key.f9)
	time.sleep(random.uniform(0.1,0.2))
	keyboard.release(Key.f9)
	
if __name__ == '__main__':
	while True:
	
		health, mana = dG.getData()
		health = float(health)
		mana = float(mana)
		manaPotion = 1700
		healthSan = 1300
		healthGran = 1400
		healthGranSan = 1100
		
		print 'HP: ' + str(health)
		print 'MANA: ' + str(mana)
		
		try:
			if(0 < health <= healthGranSan):
				if(mana > 210):
					healGranSan()
				else:
					keyboard.press(Key.f12)
					healGranSan()
					time.sleep(random.uniform(0.15,0.22))
					keyboard.release(Key.f12)
			elif(healthGranSan < health <= healthSan):
				if(mana > 160):
					healSan()
				else:
					keyboard.press(Key.f12)
					healGran()
					time.sleep(random.uniform(0.15,0.22))
					keyboard.release(Key.f12)
			elif(healthSan < health <= healthGran):
				healGran()
		except:
			print("Heal error")
		try:
			if(1 <= mana < manaPotion):
				manaPot()
		except:
			print("ManaPotion Errors")
		time.sleep(0.1)
		last = health

	
