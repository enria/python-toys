from PIL import Image, ImageGrab,ImageDraw
import time

def some_color(c1,c2):
    if abs(c1[0]-c2[0])>15:
        return False
    if abs(c1[1]-c2[1])>18:
        return False
    if abs(c1[2]-c2[2])>10:
        return False
    return True

def some_color_2(c1,c2):
    if c1[0]-c2[0]>80 or c1[0]-c2[0]<60:
        return False
    if c1[1]-c2[1]>80 or c1[1]-c2[1]<60:
        return False
    if c1[2]-c2[2]>80 or c1[2]-c2[2]<40:
        return False
    return True

def get_target(im):
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    lastC=pix[0, 0]
    for y in range(10,height):
        for x in range(10,width):
            curC = pix[x, y]
            if not some_color(lastC,curC):
                print("not some",x,y)
                lastC=pix[x,y-3]
                lastx2r,repeatTime=0,0
                for y2 in range(y+2,height):
                    curC=pix[x, y2]
                    x2l,x2r =x-1, x + 1
                    while x2l > 0:
                        if not some_color(pix[x2l, y2], lastC) and not some_color_2(lastC,pix[x2l, y2]):
                            x2l -= 1
                        else:
                            break
                    while x2r < width:
                        if not some_color(pix[x2r, y2], lastC):
                            x2r += 1
                        else:
                            break
                    if x2r-x2l<=lastx2r and x2r-x>10:
                        if repeatTime>2:
                            return round((x2l+x2r)/2), y2-5
                        else:
                            repeatTime+=1
                    else:
                        repeatTime=0
                    lastx2r=x2r-x2l
            lastC=pix[x,y]
            
def get_player(im):
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    for y in range(height):
        for x in range(width):
            if some_color(pix[x,y],(78,73,110))\
                and some_color(pix[x+4,y],(99,96,135))\
                and some_color(pix[x,y+62],(55,60,100))\
                and some_color(pix[x+4,y+24],(95,96,131)):
                drawObeject = ImageDraw.Draw(im)
                drawObeject.rectangle((x-12,y-12,x+15,y+67),pix[0,y])
                im.save("screenshot.png")
                return x,y+63

def draw_se_line():
    img = Image.open('screenshot.png')
    xp,yp=get_player(img)
    img = Image.open('screenshot.png')
    xt,yt=get_target(img)
    drawObeject = ImageDraw.Draw(img)
    drawObeject.line([xt,yt,xp,yp],fill = 10)
    img.save('screenshot-2.png')
    return pow(
                pow((xt-xp),2)+
                pow((yt-yp),2)
            ,0.5)

def snapshot():
    im=ImageGrab.grab()
    im=im.crop((9, 169, 375, 660))
    im.save("screenshot.png")
    pix = im.load()
    if some_color(pix[192,471],(254, 255, 254)) and some_color(pix[138,445],(0,200,118)):
        raise Exception("over")
    return draw_se_line()

if __name__=="__main__":
    img = Image.open('screenshot-2.png')
    xt,yt=get_target(img)
    print(xt,yt)