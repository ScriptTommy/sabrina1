import glob
import json
import os
import random
import time
import shutil
from pathlib import Path
import csv
import pandas as pd
from playwright.sync_api import sync_playwright
from datetime import datetime
# pip install playwright
# playwright install
# pip install pandas, requests
import time
import random



emails_csv = pd.read_csv('emails.csv')  # Replace with your dataset file
emails_data_list = emails_csv['Emails'].tolist()
print(emails_data_list)



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    count = 1
    for all_emails in emails_data_list:
        print(f"Submitting email {count} of {len(emails_data_list)}")
        page.goto("https://laylo.com/teamsabrina/m/frtxe", timeout=0)

        Hallenstadion_btn = page.click("//button[@id='laylo-rsvp-button-Zürich, Switzerland-']", timeout=0)

        Email_icon_btn = page.click('//button[@value="EMAIL"]', timeout=0)

        Email_Input = page.fill('//input[@name="email"]', all_emails, timeout=0)

        RSVP_btn = page.click("//form[@class='MuiGrid-root MuiGrid-container css-sow6z2']//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-auto css-5y77kd']", timeout=0)

        header = ['Done-process-emails']
        with open('done_emails.csv', 'a+', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:  # Check if file is empty
                writer.writerow(header)
            writer.writerow([all_emails])
        count += 1
        time.sleep(5)

    print("All emails submitted")
    browser.close()

