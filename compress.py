import os
import datetime
import shutil

now = datetime.datetime.now()
form = now

date = os.popen('dir').read()
date = date.split('\n')

for i in range(0,7):
	date.pop(0)

date.pop()
date.pop()
date.pop()

for i in range(0,len(date)):
	date[i] = date[i].split(' ')

files = os.listdir(os.getcwd())
both = []

for i in range(0,len(date)):
	both.append([date[i][0],files[i]])


if now.day == 1:
	day = '01'
else:
	day = str(now.day)

if now.month < 10:
	month = "0%s"%now.month
else:
	month = str(now.month)

year = str(now.year)

now = "%s/%s/%s"%(day,month,year)

name = os.popen('hostname').read()
name = name[:-1]
name = 'backup_%s_db_%s%s%s'%(name,year,month,day)
os.mkdir(name)

for i in both:
	if (i[0] == now) & (i[1] != 'compress.py'):
		print('[+]',i[1],i[0])
		os.system('powershell mv \'%s\' %s'%(i[1],name))

os.system('rar a %s.zip %s'%(name,name))

if "%s.zip"%name in os.popen('rclone ls remote:pontocertdb02.prod.sfl.cloud1.local/%s%s%s'%(year,month,day)).read():
	shutil.rmtree(name)
	os.system('powershell rm %s.zip'%name)
else:
	print("[-] Upload failed")
	quit()

print('[+] Done!')

#rclone.exe copy /arquivo remoto:pontocertdb02.prod.sfl.cloud1.local/#date/
#backup_hostname_db_20181030.zip