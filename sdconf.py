import uos
def spi8():
    uos.sdconfig(uos.SDMODE_SPI, clk=14, mosi=15, miso=2, cs=13, maxspeed=8)
    uos.mountsd()
def spi16():
    uos.sdconfig(uos.SDMODE_SPI, clk=14, mosi=15, miso=2, cs=13, maxspeed=16)
    uos.mountsd()
def spi40():
    uos.sdconfig(uos.SDMODE_SPI, clk=14, mosi=15, miso=2, cs=13, maxspeed=40)
    uos.mountsd()
def l4_8():
    uos.sdconfig(uos.SDMODE_4LINE, maxspeed=8)
    uos.mountsd()
def l4_16():
    uos.sdconfig(uos.SDMODE_4LINE, maxspeed=16)
    uos.mountsd()
def l4_40():
    uos.sdconfig(uos.SDMODE_4LINE, maxspeed=40)
    uos.mountsd()
def um():
    uos.umoutntsd()
