import os
import datetime

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

now = '%s/%s/%s'%(now.day,now.month,now.year)

name = os.popen('hostname').read()
name = name[:-1]
name = 'backup_%s_db_%s%s%s'%(name,form.year,form.month,form.day)
os.mkdir(name)

for i in both:
	if (i[0] == now) & (i[1] != 'compress.py'):
		print(i[1],i[0])
		os.system('powershell mv %s %s'%(i[1],name))

os.system('rar a %s.zip %s'%(name,name))

#os.system('rclone copy %s remoto:pontocertodb02.prod.sfl.cloud1.local/%s%s%s'%(name,form.year,form.month,form.day))

#rclone.exe mkdir remoto:pontocertdb02.prod.sfl.cloud1.local/#date
#rclone.exe copy /arquivo remoto:pontocertdb02.prod.sfl.cloud1.local/#date/
#backup_hostname_db_20181030.zip