import wget
import filecmp
import time
import os

#download link for main update script
link = "www.EDITthisLINK.com"

#clear remainings
try:
   os.remove('updaterTemp')
except:
   pass

exists = os.path.isfile('updater.py')
if not exists:
	wget.download(link, 'updater.py')
	print "\n updater.py downloaded"
else:
	try:
	  wget.download(link, 'updaterTemp')
	  if not filecmp.cmp('updater.py','updaterTemp'):		#check for updates
		print "\n Change detected"
		os.system('cp updaterTemp updater.py')		#replace old script
		os.system("sudo shutdown -r now")
	  else:
		print "\n Nothing changed"
	os.remove('updaterTemp')

	except:
	  print "\n could not download or process file"
