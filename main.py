# Imports
import os
from os.path import exists
import requests
from datetime import date

# https://v2rayshare.com/wp-content/uploads/2022/11/20221130.yaml
BaseURL = "https://v2rayshare.com/wp-content/uploads/year/month/yearmonthday.yaml"
yr = "2022"
mnth = "01"
dy = "01"


def genfileL():
    global yr, mnth, dy, BaseURL, page, filepath

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
    print("")
    print("Generating file...")
    todayURL = BaseURL.replace("year", yr)
    todayURL = todayURL.replace("month", mnth)
    todayURL = todayURL.replace("day", dy)

    filepath = ("~/Desktop/Gen{}-{}-{}.yaml".format(yr, mnth, dy))
    file_exists = exists(os.path.expanduser(filepath))
    if file_exists == True:
        print("""
        NOTICE: File already exists! Check your desktop
        """)

        exit()
    else:
        page = requests.get(todayURL)
        dnldfile = open(os.path.expanduser(filepath), "w")
        dnldfile.write(page.text)




def genfileS(udate):
    global yr, mnth, dy, BaseURL, page, filepath

    partedUdate = udate.split("/")
    print(partedUdate)
    yr = str(partedUdate[0])
    mnth = str(partedUdate[1])
    dy = str(partedUdate[2])
    print("")
    print("Generating file...")
    userURL = BaseURL.replace("year", yr)
    userURL = userURL.replace("month", mnth)
    userURL = userURL.replace("day", dy)

    filepath = ("~/Desktop/Gen{}-{}-{}.yaml".format(yr, mnth, dy))
    file_exists = exists(os.path.expanduser(filepath))
    if file_exists == True:
        print("""
        NOTICE: File already exists! Check your desktop
        """)

        exit()
    else:
        page = requests.get(userURL)
        dnldfile = open(os.path.expanduser(filepath), "w")
        dnldfile.write(page.text)




print("""
====================================================
  _          _ _       _          _ _       _       
 | |        | | |     | |        | | |     (_)      
 | |__   ___| | | ___ | |__   ___| | | ___  _ _   _ 
 | '_ \ / _ \ | |/ _ \| '_ \ / _ \ | |/ _ \| | | | |
 | | | |  __/ | | (_) | | | |  __/ | | (_) | | |_| |
 |_| |_|\___|_|_|\___/|_| |_|\___|_|_|\___/| |\__,_|
                                          _/ |      
                                         |__/       
====================================================  

                                         """)
modeselect = input("type \"l\" for latest config, \"s\" for config from a specific date: ")

if modeselect == "l":
    genfileL()

if modeselect == "s":
    userdate = input("Please input the date of config you would like to retrieve (format: 2022/12/31): ")
    genfileS(udate=userdate)

print("""
finished generating!

""")



# tkinter main
# window = tk.Tk()
# window.title("ClashX Config Gen")
# style = ttk.Style(window)
# style.theme_use("aqua")
# window.geometry("400x150+100+100")
# text = tk.Label(window, text="Generate most recent ClashX config", font=("AppleGothic", "17"))
# text2 = tk.Label(window, text=" ", font=("AppleGothic", "17"))
# button = tk.Button(window, text="Generate", font=("AppleGothic", "17"), command=genfile)

#tkinter pack
# text.pack(pady=6)
# text2.pack()
# button.pack(pady=4)
# window.mainloop()