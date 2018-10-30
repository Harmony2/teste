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

zipp = ''

for i in both:
	if (i[0] == now) & (i[1] != 'compress.py'):
		zipp += "\'%s\',"%i[1]

zipp = zipp[:-1]
print(zipp)
name = os.popen('hostname').read()
name = name[:-1]
name = 'backup_%s_db_%s%s%s.zip'%(name,form.year,form.month,form.day)
print(name)

os.system('powershell Compress-Archive %s \'%s\''%(zipp,name))

os.system('rclone copy %s remoto:pontocertodb02.prod.sfl.cloud1.local/%s%s%s'%(name,form.year,form.month,form.day))

#rclone.exe mkdir remoto:pontocertdb02.prod.sfl.cloud1.local/#date
#rclone.exe copy /arquivo remoto:pontocertdb02.prod.sfl.cloud1.local/#date/
#backup_hostname_db_20181030.zip