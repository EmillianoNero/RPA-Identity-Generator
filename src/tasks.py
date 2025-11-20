from RPA.Browser.Selenium import Selenium
import time

browser = Selenium()

# take a screen of a research in duck duck go
def takeScreen():
    browser.open_browser("https://duckduckgo.com/", browser="firefox") # open duck duck go in firefox
    browser.wait_until_element_is_visible("name:q")
    browser.input_text("name:q", "apple")
    browser.press_keys("name:q", "ENTER")
    time.sleep(1) # wait the research
    browser.screenshot(filename="img/results.png")

# close all browser
def close():
    browser.close_all_browsers()
  
takeScreen()
close()