from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from pytz import timezone


def get_current_time():
    return datetime.now(timezone('Europe/Moscow')).strftime('%H:%M')


def generate_image(text):
    image = Image.new('RGB', (500, 500), color = 'black')
    W, H = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='resources/ds-digit.ttf', size = 212)
    wt, ht = draw.textsize(text, font=font)
    draw.text(((W - wt) / 2, (H - ht) / 2 ), text, font = font, fill = '#ff3814')
    text1 = '  Ты прочтёшь это в'
    font1 = ImageFont.truetype(font='resources/17372.otf', size = 50)
    wt1, ht1 = draw.textsize(text1, font=font1)
    draw.text(((W - wt) / 2 + 10, 100 ), text1, font = font1, fill = '#42aaff')
	
    image.save('time_image.jpg')
