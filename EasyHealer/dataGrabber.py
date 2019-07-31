import cv2
import pytesseract
import imutils
import pyautogui
import numpy as np
from PIL import Image
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

def getData():
	try:
		pyautogui.screenshot("health_to_disk.png", region=(1867,140,50L,30L))
	except:
		print("Grab error...")
	life = 0
	mana = 0
	
	try:
		img = cv2.imread("health_to_disk.png")
		img = cv2.resize(img, dsize=(100, 60), interpolation=cv2.INTER_CUBIC)
		img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	except cv2.error:
		print ("Imread error...")
	
	try:
		lower_white = np.array([150,150,150], dtype = "uint16")
		upper_white = np.array([255,255,255], dtype = "uint16")
		white_mask = cv2.inRange(img, lower_white, upper_white)
		white_mask = ~white_mask
	except:
		print("Masking error...")
	
	try:
		cv2.imwrite("info.png", white_mask)
	except:
		print ("Imwrite error...")
	
	try:
		manaHealth = pytesseract.image_to_string(Image.open("info.png"), config='outputbase digits')

		manaHealth = manaHealth.replace('B', '8')
		manaHealth = manaHealth.replace('S', '5')
		manaHealth = manaHealth.replace('s', '5')
		manaHealth = manaHealth.replace('Z', '2')
		manaHealth = manaHealth.replace('v', '7')
		manaHealth = manaHealth.replace('V', '7')
		manaHealth = manaHealth.replace('i', '1')
		manaHealth = manaHealth.replace('I', '1')
		manaHealth = manaHealth.replace('l', '1')
		manaHealth = manaHealth.replace('$', '5')
		
		print manaHealth
		
	except:
		print("Tesser error...")
		
	try:
			
		manaHealth = manaHealth.replace(",", "")
		life, mana = manaHealth.split(chr(10))
		if (mana [0] == '0' or mana[0] == 'O'):
			mana[0] = '9'
		if(life[0] == '0' or life[0] == 'O'):
			life[0] = '9'

			
	except:
		print("No data...")
	
	try:
		life = float(life)
		mana = float(mana)
	except:
		print("Conversion error...")
	
	if(isinstance(life, float) and isinstance(mana, float)):
		return life, mana
	else:
		return 0, 0



