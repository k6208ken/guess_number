import random

r = random.randint(1,100)
count = 0
while True:
	count += 1
	num = int(input('請隨便輸入一個數字'))
	if num == r:
		print('終於猜對了！')
		print('這是你猜的第 {} 次'.format(count))
		break
	elif num > r:
		print('猜小一點')
	elif num < r:
		print('猜大一點')
	print('這是你猜的第 {} 次'.format(count))
