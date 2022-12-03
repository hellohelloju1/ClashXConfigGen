# Imports
import os
import os.path
import tkinter as tk
from tkinter import ttk
import requests
from datetime import date

# get file function
def genfile():
    text2.config(text="Error! Try again later or look for errors within the code")
    page = requests.get(finalURL)
    dnldfile = open(os.path.expanduser(filepath), "w")
    dnldfile.write(page.text)
    text2.config(text="done! Check your desktop")

# tkinter main
window = tk.Tk()
window.title("ClashX Config Gen")
style = ttk.Style(window)
style.theme_use("aqua")
window.geometry("400x150+100+100")
text = tk.Label(window, text="Generate most recent ClashX config", font=("AppleGothic", "17"))
text2 = tk.Label(window, text=" ", font=("AppleGothic", "17"))
button = tk.Button(window, text="Generate", font=("AppleGothic", "17"), command=genfile)

# Variables
# https://v2rayshare.com/wp-content/uploads/2022/11/20221130.yaml
BaseURL = "https://v2rayshare.com/wp-content/uploads/year/month/yearmonthday.yaml"
today = date.today()
yr = today.strftime("20%y")

mnth = today.strftime("%m") 

dy = today.strftime("%d")

# main
if dy != "01":
    dy = str(int(today.strftime("%d")) - 1)

if dy == "01":
    if mnth == "01":
        dy = "30"
        mnth = "12"
        yr = str(int(today.strftime("20%y")) - 1)


if len(dy) == 1:
    dy = "0" + dy

finalURL = BaseURL.replace("year", yr)
finalURL = finalURL.replace("month", mnth)
finalURL = finalURL.replace("day", dy)
filepath = ("~/Desktop/Gen{}-{}-{}.yaml".format(yr, mnth, dy))

#tkinter pack
text.pack(pady=6)
text2.pack()
button.pack(pady=4)
window.mainloop()