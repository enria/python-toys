from PIL import Image, ImageDraw, ImageFont, ImageEnhance


def train():
    font_consola = ImageFont.truetype("C:\Windows\Fonts\consola.ttf", 60)
    pix_sum_arr = []
    max_pix = 0
    for i in range(33, 128):
        img = Image.new('L', (200, 100), '#000000')
        draw_object = ImageDraw.Draw(img)
        draw_object.text([20, 20], chr(i), font=font_consola, fill='#FFFFFF')
        pix = img.load()
        pix_sum = 0
        for y in range(img.height):
            for x in range(img.width):
                pix_sum += pix[x, y]
        if pix_sum > max_pix:
            max_pix = pix_sum
        pix_sum_arr.append({
            "char": i,
            "pix_sum": pix_sum
        })
    pix_sum_arr = [{"char": chr(
        x["char"]), "pix_sum":x["pix_sum"] / max_pix * 256} for x in pix_sum_arr]
    pix_sum_arr = sorted(pix_sum_arr, key=lambda x: x["pix_sum"])
    ai = 0
    char_arr = []
    for c in pix_sum_arr:
        for ti in range(ai, round(c["pix_sum"])):
            char_arr.append(c["char"])
        ai = round(c["pix_sum"])
    print(char_arr)


CHAR_ARR = ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '&', '&', '&', 'Q', 'Q', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '0', '0', '0', '0', '0', '%', 'N', 'N', 'B', 'B', 'B', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '#', '#', 'D', 'D', 'O', 'G', 'G', 'G', 'A', 'A', 'H', 'm', '\x7f', 'q', 'p', 'p', 'p', 'p', '9', '6', '6', 'U', 'U', 'K', 'K', 'w', 'Z', 'Z', 'Z', 'h', 'h', 'P', 'k', 'k', 'E', 'y', 'e', 'e', 'e', '2', '2', '2', 'C', 'j', '5', '5',
            '5', '5', '1', '1', '1', 'f', 'n', 'I', 'Y', 'x', 'x', '{', '{', '{', 'l', 'l', 'l', '7', 'J', 'i', 'i', 'i', '(', '(', 'v', 'T', '|', '|', '|', '|', '|', '|', '|', 'L', 'L', 'c', 'c', '?', '?', '?', '?', '?', '?', '?', '?', '+', '+', '/', '*', '*', '*', '*', '*', '*', '>', '>', '=', '=', ';', ';', ';', ';', ';', ';', ';', ';', ';', ';', ';', '^', '^', '~', '"', '"', '"', '"', '"', '"', '"', '"', ',', '_', '_', '_', ':', ':', ':', ':', ':', ':', ':', ':', ':', ':', ':', ':', ':', ':', ':', "'", "'", '.', '.', '-', '-', '-', '-', '-', '-', '-', '-', '-', '`', '`', '`', '`', '`', '`', '`', '`', '`', '`', '`', '`', '`', '`', '`', '`', ' ']

FONT_SIZE = 12
CHAR_PIX = 2


def rgb_to_hex(rgb):
    return ('#%02x%02x%02x' % (rgb[0],rgb[1],rgb[2])).upper()


def convert(ori_img):
    font_consola = ImageFont.truetype(
        "C:\Windows\Fonts\consola.ttf", FONT_SIZE)
    color_pix = ori_img.load()
    char_img = Image.new(
        'RGB', (ori_img.width * int(FONT_SIZE / CHAR_PIX-2), ori_img.height * int(FONT_SIZE / CHAR_PIX-2)), '#FFFFFF')
    img = ori_img.convert("L")
    draw_object = ImageDraw.Draw(char_img)
    pix = img.load()
    for y in range(0, img.height, CHAR_PIX):
        for x in range(0, img.width, CHAR_PIX):
            draw_object.text([x * int(FONT_SIZE / CHAR_PIX-2), y * int(FONT_SIZE / CHAR_PIX-2)],
                            CHAR_ARR[pix[x, y]], font=font_consola, fill=rgb_to_hex(color_pix[x,y]))
    char_img=ImageEnhance.Color(char_img).enhance(3.0)
    char_img.show()


convert(Image.open("dog.jpg"))
