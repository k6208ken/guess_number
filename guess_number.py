import random

r = random.randint(1,100)
while True:
	
	num = int(input('請隨便輸入一個數字'))
	if num == r:
		print('終於猜對了！')
		break
	elif num > r:
		print('猜小一點')
	elif num < r:
		print('猜大一點')
