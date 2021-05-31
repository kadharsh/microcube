import lcd_tft, json, curl

tft = lcd_tft.tft

tft.clear(0xffffff)
tft.set_bg(0xffffff)

tft.text(tft.CENTER,10,"Weather", color=0xeb4634)
tft.line(5, 21, 155, 21, 0x101010)

print("collecting data")
res = curl.get('http://api.openweathermap.org/data/2.5/weather?id=1260728&appid=40b0fc55c3eef1e8b3f0bba8366d1eff&units=metric',"weather.json")
print(res[0])
print("/n/n")
print(res[1])
