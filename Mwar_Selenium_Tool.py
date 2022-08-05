from selenium import webdriver
import time
from tkinter import *
from PIL import Image, ImageTk
from win10toast import ToastNotifier
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os

# Set interface
root = Tk()
root.title("Moon Warrior Tool")
root.geometry("600x400")
root.iconbitmap("warrior.ico")

# Set the background
input_file = Image.open("background.jpg")
bgr = ImageTk.PhotoImage(input_file)
img = Label(root, image=bgr)
img.place(x=0, y=0)

# Title
user = Label(root, text="User File", fg="#FFFFFF", bg="#011226", bd=0)
user.config(font=("Transformers Movie", 20))
user.place(x=240, y=20)
pass_wallet = Label(root, text="Password", fg="#FFFFFF", bg="#011226", bd=0)
pass_wallet.config(font=("Transformers Movie", 20))
pass_wallet.place(x=230, y=110)

# Box text
box_1 = Text(root, width=55, height=1, font=("ROBOTO", 10), borderwidth=5)
box_1.place(x=98, y=60)
box_2 = Text(root, width=55, height=1, font=("ROBOTO", 10), borderwidth=5)
box_2.place(x=98, y=150)


# Load File Button

def load_file():
    user_data_dir = box_1.get(1.0, END)
    password = box_2.get(1.0, END)
    print(user_data_dir)
    print(password)
    return user_data_dir, password

def start_tool():
    # Create profile
    user_data_dir, password_wl = load_file()
    path_driver = "chromedriver.exe"
    ch_options = webdriver.ChromeOptions()
    ch_options.add_argument(f"--user-data-dir={user_data_dir}")
    driver = webdriver.Chrome(executable_path=path_driver, chrome_options=ch_options)
    time.sleep(1)
    driver.refresh()
    driver.refresh()
    driver.refresh()
    driver.get("https://app.moonwarriors.io/pve")
    time.sleep(2)
    # Enter password metamask
    window_before = driver.window_handles[0]
    handles = driver.window_handles
    wait = WebDriverWait(driver, 10)
    for handle in handles:
        driver.switch_to.window(handle)
    time.sleep(2)
    password = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/form/div/div/input")))
    password.clear()
    password.send_keys(password_wl)
    unlock_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiButton-label")))
    unlock_button.click()
    time.sleep(2)
    driver.switch_to.window(window_before)
    # Fight
    while True:
        fight = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/img")))
        fight.click()
        new_handles = driver.window_handles
        for new_handle in new_handles:
            driver.switch_to.window(new_handle)
        choose_card = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[8]/div/div[2]/div[1]")))
        choose_card.click()
        time.sleep(2)
        fight_next = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[8]/div/div[2]/div[3]/img")))
        fight_next.click()
        time.sleep(2)
        skip_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "done-btn")))
        skip_button.click()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
# Buttons
button_frame = Frame(root).pack(side=BOTTOM)
load_button = Button(button_frame, text="Load Data", font=("Arial", 10, "bold"), fg="#FFFFFF", bg="#000000",
                     borderwidth=7, command=load_file)
load_button.place(x=180, y=200)
start_button = Button(button_frame, text="Start Tool", font=("Arial", 10, "bold"), fg="#FFFFFF", bg="#000000",
                      borderwidth=7, command=start_tool)
start_button.place(x=330, y=200)

def remind():
    t = ToastNotifier()
    while True:
        note = "Nhớ hẹn báo thức sau 4 tiếng nữa nhé\nHẹn luôn đi không quên!"
        t.show_toast("Moon Warrior", note, icon_path="warrior.ico", duration=14400)
        time.sleep(60)
root.mainloop()
remind()
