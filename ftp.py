# connect to a WIFI AP, sync time and start telnet and FTP server
# Paste it in the Python command line (REPL)
# Then you can connect to the IP of your ESP32 in FTP (passive mode) or in telnet !

wifi_ssid = "Adharshk"
wifi_passwd = "flatapple123"
my_timezone = "IST-5:30" # found in second field, text before the coma, in https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/blob/master/MicroPython_BUILD/components/micropython/docs/zones.csv

import network
import machine
import time

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect(wifi_ssid, wifi_passwd)

time.sleep(6)
sta_if.ifconfig()

rtc = machine.RTC()
rtc.ntp_sync(server= "in.pool.ntp.org", tz=my_timezone, update_period=3600)
network.ftp.start(user="micro", password="python", buffsize=1024, timeout=300)
network.telnet.start(user="micro", password="python", timeout=300)
print("IP of this ESP32 is : " + sta_if.ifconfig()[0])
