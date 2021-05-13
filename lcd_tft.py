import display

tft = display.TFT()

def init():
    tft.init(tft.ST7735R, width=128, height=160, miso=2, mosi=15, clk=14, cs=17, dc=16, rst_pin=5, spihost=tft.HSPI, rot=3, splash=False)


def dispimg(file):
    tft.image(0, 0, file)
