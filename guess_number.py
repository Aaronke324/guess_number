import random
start = input('請決定隨機整數範圍開始值:')
end = input('請決定隨機整數範圍結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0 
while True:
	count += 1 # count += 1 = (count = count +1)
	answer = input('猜範圍中的一個數字:')
	answer = int(answer)
	if answer == r:
		print('恭喜你猜對了')
		print('這是你猜的第', count, '次')
		break
	elif answer > r:
		print('你猜錯了，答案比你猜的數字更小。')
	elif answer < r:
		print('你猜錯了，答案比你猜的數字更大。')
	print('這是你猜的第', count, '次')
