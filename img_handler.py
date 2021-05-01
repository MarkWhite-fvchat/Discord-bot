import requests
import os
import glob
from PIL import Image, ImageDraw, ImageFont

imgs ={
    "vs_bg":"./img/vs_bg.jpg",
    "vs_bg_animated":"./img/vs_bg_animated/frame_*.jpg"
}

async def vs_create(url1:str, url2:str):
    vs_bg = Image.open(os.path.join(imgs["vs_bg"]))
    size = (100, 100)

    f1 = Image.open(requests.get(url1, stream=True).raw).resize(size)
    f2 = Image.open(requests.get(url2, stream=True).raw).resize(size)

    pos1 = (vs_bg.width//2-f1.width*2, vs_bg.height//2-f1.height)
    pos2 = (vs_bg.width//2+f2.width, vs_bg.height//2-f2.height)

    vs_bg.paste(f1, pos1)
    vs_bg.paste(f2, pos2)


    vs_bg.save(os.path.join("./img", "result.png"))
    return vs_bg


async def vs_create_animated(url1:str, url2:str, r1:str, r2:str):
    vs_bg, *img = [Image.open(path) for path in glob.glob(imgs["vs_bg_animated"])]
#   vs_bg.resize(bg_size)
    size = (100, 100)

    f1 = Image.open(requests.get(url1, stream=True).raw).resize(size)
    f2 = Image.open(requests.get(url2, stream=True).raw).resize(size)
    pos1 = (vs_bg.width//2-f1.width*2, vs_bg.height//2-f1.height)
    pos2 = (vs_bg.width//2+f2.width, vs_bg.height//2-f2.height)
    vs_bg.paste(f1, pos1)
    vs_bg.paste(f2, pos2)

    fontsize = 28
    font = ImageFont.truetype("arial.ttf", fontsize)
    draw_text = ImageDraw.Draw(vs_bg)

    for im in img:
        im.paste(f1, pos1)
        im.paste(f2, pos2)
        draw_text = ImageDraw.Draw(im)
        draw_text.text(
            (im.width//2 - f1.width*2, im.height//2 - f1.height//2 + f1.height),
            r1,
            font=font,
            fill=('#696969')
        )
        draw_text.text(
            (im.width//2 + f2.width, im.height//2 - f2.height//2 + f2.height),
            r2,
            font=font,
            fill=('#696969')
        )        
    vs_bg.save(fp=os.path.join("./img/result.gif"), append_images=img, save_all=True, duration=20, loop=0)