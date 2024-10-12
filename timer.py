import time 

myTime = int(input("please enter time ins seconds: "))

for x in range(myTime, 0, -1):
  seconds = x % 60
  minutes = (x // 60) % 60
  hours = (x // 3600) % 24
  days = x // 86400
  print(f'{days:02}:{hours:02}:{minutes:02}:{seconds:02}')

  time.sleep(1)

print("TIMES UPP!!!")
