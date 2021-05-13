import display, time, uos, network, machine
import lcd_tft
Pin = machine.Pin

#initialising lcd screen
lcd_tft.init()
tft = lcd_tft.tft
tft.font(tft.FONT_DefaultSmall,transparent=True,color=tft.WHITE)

tft.image(0, 0, 'boot_img.bmp') #use this bg for this img (0x583D72)

#mount sdcard
#tft.text(tft.CENTER,90,"Mounting SD card...")
#uos.sdconfig(uos.SDMODE_SPI, clk=14, mosi=15, miso=2, cs=13, maxspeed=16)
#err = False

#try:
#    uos.mountsd()
#except:
#    time.sleep_ms(200)
#    tft.rect(0,88,160,14,0x583D72,0x583D72)
#    tft.text(tft.CENTER,90,"Sd mounting failed")
#    err = True

#if(not err):
#    time.sleep_ms(200)
#    tft.rect(0,88,160,14,0x583D72,0x583D72)
#    tft.text(tft.CENTER,90,"Sd mount complete")
#else:
#    tft.text(tft.CENTER,90,"Mounted")

#connect to wifi

'''
Date calculator
calculates dates from list returned by rtc.now()
(year, month, day, hour, minute, second)
'''

def getDate():
    now = rtc.now()
    month_list = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    weak_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y = now[0] % 100
    y -= (now[1]<3)
    w = int((y + y/4 - y/100 + y/400 + t[now[1]-1] + now[2]) % 7)

    month = month_list[now[1]-1]
    weak  = weak_list[w-1]
    date = weak +" "+ str(now[2]) +" "+ month
    return(date)

'''****************************************'''


'''
get and format time to a neat string
example h=14, m=5 to "02:05 PM"
'''
def formatTime():
    timevar = rtc.now()
    h = timevar[3]
    m = timevar[4]
    
    if(h > 12):
        meridiem = "PM"
        hour = h - 12
    else:
        meridiem = "AM"
    if(hour < 10):
        h_txt = '0'+str(hour)
    else:
        h_txt = str(hour)
    if(m < 10):
        m_txt = '0'+str(m)
    else:
        m_txt = str(m)
    return(h_txt + ":" + m_txt + " " + meridiem)

'''*******************************'''

'''
This function is called when button is pressed
'''
def getbtn(btn):
    if(btn == b1):
        print("Button 1 pressed")
    elif(btn == b2):
        print("Button 2 pressed")
    elif(btn == b3):
        print("Button 3 pressed")
    return()

'''****************************************'''

'''**********************
to draw box for button
'''
def butbox():
    #drawing box for button
    #tft.rect(0  , 109, 160, 20,color=0x6a6a6a, fillcolor= 0x6a6a6a)
    tft.rect(0  , 111, 52, 17, color=0x6a6a6a, fillcolor= 0x000000)
    tft.rect(52 , 111, 56, 17, color=0x6a6a6a, fillcolor= 0x000000)
    tft.rect(108, 111, 52, 17, color=0x6a6a6a, fillcolor= 0x000000)
    tft.font("FreeSansBold12.fon")
    tft.text(20 , 114, "<", transparent = True, color=0xdedede)
    tft.text(70 , 114, "OK",transparent = True, color=0xdedede)
    tft.text(128, 114, ">", transparent = True, color=0xdedede)
    
'''********************'''

'''
Function which displays the homescreen
(The screen with time)
'''
def home():
    prvTime = ''
    tft.clear(0x4d91ff)
    tft.set_bg(0x4d91ff)
    tft.image(0, 0, 'wall1.bmp')
    tft.font(tft.FONT_Ubuntu)
    tft.text(60,16, "28*C", transparent = True, color=0xFFFFFF)
    tft.font("FreeSansBold24.fon")
    tft.text(2,80, getDate(), transparent = True, color=0xFFD82B)
    tft.font("FreeSansBold40.fon")
    butbox()
    
    while True:
        curTime = formatTime()
        if(curTime != prvTime):
            tft.image(0, 0, 'wall1.bmp')
            tft.font("FreeSansBold12.fon")
            tft.text(60,16, "28*C", transparent = True, color=0xFFFFFF)
            tft.font("FreeSansBold24.fon")
            tft.text(2,80, getDate(), transparent = True, color=0xffcb70)
            tft.font("FreeSansBold40.fon")
            tft.text(30,35, formatTime(), transparent = True, color=0xffff00)
            butbox()
            prvTime = curTime
        time.sleep_ms(1000)
        
'''******************************************'''


tft.text(tft.CENTER,90,"connecting to WiFi")
wifi_ssid = "Adharshk"
wifi_passwd = "flatapple123"
my_timezone = "IST-5:30"

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect(wifi_ssid, wifi_passwd)

time.sleep(6)
sta_if.ifconfig()

time.sleep_ms(1000)
tft.rect(0,88,160,15,0x583D72,0x583D72)
tft.text(tft.CENTER,90,"connected")
time.sleep_ms(1000)
tft.rect(0,88,160,15,0x583D72,0x583D72)
tft.text(tft.CENTER,90,("IP address : " + sta_if.ifconfig()[0]))
time.sleep_ms(1000)
tft.rect(0,88,160,15,0x583D72,0x583D72)

#sync rtc
tft.text(tft.CENTER,90,"Syncing from NTP Server")
rtc = machine.RTC()
rtc.ntp_sync(server= "in.pool.ntp.org", tz=my_timezone) # update_period=3600
timevar = rtc.now()
time.sleep_ms(1000)
tft.rect(0,88,160,15,0x583D72,0x583D72)
tft.text(tft.CENTER,90,"Time is: "+ str(timevar[3]) +":" + str(timevar[4]))
time.sleep_ms(1000)

b1 = Pin(21, Pin.IN, Pin.PULL_UP, trigger=Pin.IRQ_FALLING, handler=getbtn, debounce=6000)
b2 = Pin(22, Pin.IN, Pin.PULL_UP, trigger=Pin.IRQ_FALLING, handler=getbtn, debounce=6000)
b3 = Pin(23, Pin.IN, Pin.PULL_UP, trigger=Pin.IRQ_FALLING, handler=getbtn, debounce=6000)

home() #to display homepage

