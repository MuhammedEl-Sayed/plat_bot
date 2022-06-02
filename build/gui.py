
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *

import threading
import plat_bot as pb
import random
import os
from time import sleep
from PIL import ImageTk, Image
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


## GLOBAL DECLARATIONS ##



def get_relic():
    final_relic = pb.get_best_relic(pb.get_items_id(
        pb.parseXML('E:\GIT\plat_bot\items - Copy.xml'), vaulted_var.get()), vaulted_var.get())
    i = 0
    curr_top_ten = dict(sorted(pb.top_ten.items(), key=lambda item: item[1]))
    print(curr_top_ten)
    for key, value in curr_top_ten.items():
        i += 1
        tempText = Label(window, text="Drop #" + str(i) +
                         ": " + key + " - " + str(value), font=("Arial", 10))
        tempText.grid(row=i, column=0)
    text.config(text=final_relic)
    text.grid(row=i+1, column=0)
    relic_image_label.place_forget()


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
    image = Image.open(str(str(random_icon())))
    image = image.resize((220, 250), Image.ANTIALIAS)
    temp_photo = ImageTk.PhotoImage(image)
    
    relic_image_label.config(image=temp_photo)
    relic_image_label.image = temp_photo
    sleep(0.05)
    window.update()




def random_icon():
    global img
    img = random.choice(
        list(Path("E:\GIT\plat_bot\images\\relics").glob("*.png")))
    return img

window = Tk()

window.geometry("800x800")
window.configure(bg="#000000")
window.iconbitmap(str(relative_to_assets("PlatinumLarge.ico")))
window.title("Platinum Bot")
canvas = Canvas(
    window,
    bg="#000015",
    height=800,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)


canvas.place(x=0, y=
0)
## GUI SETUP HERE ##

relic_image = PhotoImage(file=str(random_icon()))
relic_image = relic_image.subsample(2, 2)
relic_image_label = Label(window, image=relic_image, anchor="center")
relic_image_label.place(x=300, y=300)


text = Label(window, text="The Best Relic is: ", font=("Arial", 12))
text.place(x=10, y=10)




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
    relx=0.5,
    rely=0.9,
    anchor="center",
    width=104.0,
    height=22.0
)
vaulted_var = IntVar()
normal_drops_var = IntVar()

def read_settings():
    global vaulted_var, normal_drops_var
    if os.path.isfile('settings.txt'):  
        with open('settings.txt', 'r') as f:
            settings = f.readlines()
        if(len(settings) < 2):
            vaulted_var = 0
            normal_drops_var = 0
        else:
            vaulted_temp = int(settings[0])
            normal_drops_temp = int(settings[1])
            print(vaulted_temp)
            print(normal_drops_temp)
        vaulted_var.set(vaulted_temp)
        normal_drops_var.set(normal_drops_temp)
    else:
        with open('settings.txt', 'w') as f:
            f.write("0\n0")
        vaulted_temp = 0
        normal_drops_temp = 0
        print("no file")
    





def settings_window():
    global vaulted_var, normal_drops_var
    settings = Toplevel(window)
    settings.geometry("400x100")
    settings.title("Settings")
    read_settings()
    print("reading settings")
    print(vaulted_var.get())
    print(normal_drops_var.get())
    vaulted = Checkbutton(settings, text="Vaulted", variable=vaulted_var, onvalue=1, offvalue = 0)
    vaulted.grid(row=0, column=0)
    normal_drops = Checkbutton(settings, text="Normal Drops (non relic)", variable=normal_drops_var, onvalue=1, offvalue = 0)
    normal_drops.grid(row=1, column=0)
    settings.mainloop()
    with open('settings.txt', 'w') as f:
        f.write(str(vaulted_var.get()) + "\n")
        f.write(str(normal_drops_var.get()))




menubar = Menu(window)
menu_settings = Menu(menubar, tearoff=0)
menu_settings.add_command(label="Settings", command=settings_window)
menu_settings.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=menu_settings)
window.config(menu=menubar)



window.resizable(False, False)

window.mainloop()


