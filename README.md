# remote_config
Python scripts for getting configuration files for MMDVM hotspots and repeaters

You should place your non-empty configuration files and updater.py script from this project to publicly accessible(read no password required) servers or services. Then put links in the scripts.

Setup
1. sudo apt-get install python-pip
2. sudo pip install wget
3. Transfer your updater_updater.py script to your RPi and then run. It will download updater.py
4. Add them to startup type crontab -e and press enter. Put these lines at the end of file.
    @reboot python /home/pi-star/remote_config/updater_updater.py
    10 3 * * * python /home/pi-star/remote_config/updater_updater.py
    @reboot python /home/pi-star/remote_config/updater.py &
Note that updater_updater.py will run every day at 3:10 in the night. You may change this.
5. Now, you have to make your changes using these files. Web interface or other methods will be overwritten
