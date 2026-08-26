import pyautogui
import pyperclip
import time
from datetime import datetime

# Get today's date and time
now = datetime.now()

date = now.strftime("%Y-%m-%d")
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

# File names
excel_file = "daily_report_" + date + ".xlsx"
screenshot_file = "daily_report_" + date + ".png"


# -----------------------------------
# Step 1: Open Chrome
# -----------------------------------

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(5)


# -----------------------------------
# Step 2: Open a weather website
# -----------------------------------

pyautogui.hotkey("ctrl", "l")

pyautogui.write("https://wttr.in/Chennai?format=3")

pyautogui.press("enter")

time.sleep(5)


# -----------------------------------
# Step 3: Copy weather information
# -----------------------------------

pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")

time.sleep(1)

weather = pyperclip.paste()

print("Weather information:")
print(weather)


# -----------------------------------
# Step 4: Open Microsoft Excel
# -----------------------------------

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("excel")
pyautogui.press("enter")

time.sleep(5)


# -----------------------------------
# Step 5: Create a new Excel workbook
# -----------------------------------

pyautogui.hotkey("ctrl", "n")

time.sleep(2)


# -----------------------------------
# Step 6: Enter report data
# -----------------------------------

# Headers
pyautogui.write("Date & Time")
pyautogui.press("tab")

pyautogui.write("Weather")
pyautogui.press("tab")

pyautogui.write("Comment")

pyautogui.press("enter")


# Data
pyautogui.write(date_time)
pyautogui.press("tab")

# Paste weather information
pyperclip.copy(weather)
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")

pyautogui.write("Good for outdoor activities")


# -----------------------------------
# Step 7: Save the Excel file
# -----------------------------------

pyautogui.hotkey("ctrl", "shift", "s")

time.sleep(3)

# Type the filename in the Save As dialog
pyautogui.write(excel_file)

time.sleep(1)

pyautogui.press("enter")

time.sleep(5)

# -----------------------------------
# Step 8: Take screenshot
# -----------------------------------

screenshot = pyautogui.screenshot()

screenshot.save(screenshot_file)


# -----------------------------------
# Finished
# -----------------------------------

print()
print("Daily report created successfully!")
print("Excel file:", excel_file)
print("Screenshot:", screenshot_file)