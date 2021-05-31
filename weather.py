import lcd_tft, json, curl

def getdata():
    tft = lcd_tft.tft
    tft.clear(0xffffff)
    tft.set_bg(0xffffff)

    tft.text(tft.CENTER,8,"Weather", color=0xeb4634)
    tft.line(5, 20, 155, 20, 0x101010)

    print("collecting data")
    res = curl.get('http://api.openweathermap.org/data/2.5/weather?id=1260728&appid=40b0fc55c3eef1e8b3f0bba8366d1eff&units=metric',"data.json")
    print(res[1])
    
    file = open("data.json", "r")
    data = file.read()
    parsed = json.loads(data)
    print( parsed["weather"][1])
    tft.text(tft.CENTER,30,parsed["weather"][1], color=0xeb4634)
    tft.text(tft.CENTER,38,parsed["main"][0], color=0xeb4634)

getdata()