

"""import csv
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException,ElementClickInterceptedException,TimeoutException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import simpledialog
import xlsxwriter"""
import pathlib
import datetime
import pandas as pd
from time import sleep
from selenium import webdriver
from tkinter import filedialog
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("profile-directory=Profile 1")
options.add_argument("--user-data-dir=D:/insta-screenshot-bot/instachrome data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

idurl = []
Idl = []
bio = []
followers = []
posts = []
following = []
names = []
#excel = r"book11.xlsx"
excel = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("Excel File", "*.xlsx"), ("all files", "*.*")))
df = pd.read_excel(excel)



class elem :
    def element_presence(self ):

        global df
        for i in range(len(df)):
            Id = (df.loc[i, "Insta Id"])
            urltogo = f"http://www.instagram.com/{Id}".format(Id=Id)

            driver.get(urltogo)

            #idurl.append(urltogo)
            try:

                sleep(3)
                getid = driver.find_element(By.XPATH,
                                            '/html/body/div[1]/section/main/div/header/section/div[1]/h2').text


                datenow = datetime.datetime.now()
                pdate = datenow.strftime("%d-%m-%y")
                path = pathlib.Path.cwd()/'output'/f'{pdate}'
                path.mkdir(parents=True,exist_ok=True)

                driver.get_screenshot_as_file(r"output\\{pdate}\\{id}.png".format(id=getid,pdate = pdate))

                print("shot {}...".format(getid))

            except Exception as e:
                print(e)

out = elem()
out.element_presence()

