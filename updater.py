import wget
import filecmp
import time
import os

period = 60		#minutes

filesdict = {
"/etc/pistar-remote":"LINKLINKLINKLINK",
"/etc/dmrgateway":"LINKLINKLINKLINK",
"/etc/mmdvmhost":"LINKLINKLINKLINK"}

#time.sleep(600) #delay to prevent reboot loops

while True:
	changed = False
	for x in filesdict:
	  try:
		os.remove('TempFile')
	  except:
		pass
	
	  exists = os.path.isfile(x)
	  if not exists:
		wget.download(filesdict[x], x)
		print "\n file created: " +x
	  else:
		try:
			wget.download(filesdict[x], 'TempFile')
			if not filecmp.cmp(x,'TempFile'):
				print "\n Change detected in" +x
				changed = True
				os.system('sudo cp TempFile %s' %x)
			else:
				print "\n nothing changed in " +x
			os.remove('TempFile')
		except:
			print "\n could not download or process file: " +x

	if changed:
#		os.system("sudo shutdown -r now")
#		print "rebooting"
		os.system("sudo systemctl restart mmdvmhost.service")
		print "restarting mmdvmhost.service"
	else:
		print "waiting for " + str(period) + " minutes"
		
	time.sleep(period*60)
