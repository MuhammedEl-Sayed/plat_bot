
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Label, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage

import threading
import plat_bot as pb
import random
from time import sleep

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def get_relic():
    text.config(text=pb.get_best_relic(pb.get_items_id(
        pb.parseXML('D:\GIT\plat_bot\items.xml'))))


def thread_relic():
    global relic_thread, photo_thread
    relic_thread = threading.Thread(target=get_relic)
    photo_thread = threading.Thread(target=test_random())
    photo_thread.daemon = True

    relic_thread.daemon = True
    relic_thread.start()
    window.after(50, check_thread_relic)


def check_thread_relic():
    if relic_thread.is_alive():
        if photo_thread.is_alive() == False:
            test_random()
        window.after(50, check_thread_relic)


def test_random():

    temp_photo = PhotoImage(file=str(random_icon()))
    temp_photo = temp_photo.subsample(2, 2)
    relic_image_label.config(image=temp_photo)
    relic_image_label.image = temp_photo
    sleep(0.05)
    window.update()


window = Tk()

window.geometry("535x336")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=336,
    width=535,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)


canvas.place(x=0, y=0)
# get an updated random image using random_relic_icon() that constantly updates
# the image on the screen


def random_icon():
    # pick random icon from E:\Git\plat_bot\images\relics
    global img
    img = random.choice(
        list(Path("D:\GIT\plat_bot\images\\relics").glob("*.png")))
    return img


relic_image = PhotoImage(file=str(random_icon()))
relic_image = relic_image.subsample(2, 2)
relic_image_label = Label(window, image=relic_image, anchor="center")
relic_image_label.place(x=150, y=50)


text = Label(window, text="The Best Relic is: ", font=("Arial", 12))
text.place(x=10, y=10)
# update the text on the screen to show the best drop

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: thread_relic(),
    relief="flat"
)
button_1.place(
    x=182.0,
    y=302.0,
    width=104.0,
    height=22.0
)


window.resizable(False, False)

window.mainloop()
