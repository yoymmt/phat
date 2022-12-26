from datetime import date
from socket import TCP_NODELAY
from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw

inky_display = auto()
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)
from font_fredoka_one import FredokaOne

font = ImageFont.truetype("/usr/share/fonts/truetype/fonts-japanese-gothic.ttf", 15, encoding='unic')

  message = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd  =  'date "+%y/%m/%d(%a) %H:%M"'
w, h = font.getsize(message)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((x, y), message, inky_display.RED, font)
inky_display.set_image(img)
inky_display.show()