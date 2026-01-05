
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyfiglet
from time import sleep

def loop1():
    global i
    while True:
        sleep(10)
        try:
            driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/div[4]/div/button").click()
        except:
            print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
            driver.refresh()
            continue
        try:
            sleep(2)
            driver.find_element(By.XPATH, "//*[@id=\"sid4\"]/div/div/div/form/div/input").send_keys(vidUrl)
            sleep(1)
            driver.find_element(By.XPATH, "//*[@id=\"sid4\"]/div/div/div/form/div/div/button").click()
            sleep(2)
            driver.find_element(By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
            sleep(10)
            driver.refresh()
            i += 1
            total = i * 500
            print("Views success delivered! Total", total,"views")
            sleep(360)
            # Loop continues automatically
        except:
            print("A generic error occurred. Now will retry again")
            driver.refresh()
            sleep(20)
            # Loop continues automatically

def loop2():
    while True:
        sleep(10)
        try:
            driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
        except:
            print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
            driver.refresh()
            continue
        try:
            sleep(2)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div/form/div/input").send_keys(vidUrl)
            sleep(1)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div/form/div/div/button").click()
            sleep(10)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/form/button").click()
            sleep(10)
            hearts = driver.find_element(By.XPATH, '//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text
            sleep(55)
            print(hearts," Success delivered! Thank me with a $ 1 donation on GitHub")
            sleep(100)
            driver.refresh()
            sleep(200)
            # Loop continues automatically
        except:
            print("A generic error occurred. Now will retry again")
            driver.refresh()
            sleep(355)
            # Loop continues automatically

def loop3():
    while True:
        sleep(10)
        try:
            driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[3]/div/button").click()
        except:
            print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
            driver.refresh()
            continue
        try:
            sleep(2)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/form/div/input").send_keys(vidUrl)
            sleep(1)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/form/div/div/button").click()
            sleep(5)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/form/button").click()
            sleep(5)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div/form/ul/li/div/button").click()
            sleep(47)
            driver.refresh()
            print("Success delivered! Thank me with a $ 1 donation on GitHub")
            # Loop continues automatically
        except:
            print("A generic error occurred. Now will retry again")
            driver.refresh()
            sleep(50)
            # Loop continues automatically

def loop4():
    while True:
        sleep(20)
        wait_time = 660 #11 minutes
        try:
            driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click() #Followers
        except:
            print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
            driver.refresh()
            continue
        try:
            sleep(20)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div/form/div/input").send_keys(vidUrl) #Write
            sleep(2)
            driver.find_element(By.XPATH, "//*[@id=\"sid\"]/div/div/div/form/div/div/button").click() #Search
            sleep(20)
            driver.find_element(By.XPATH, "//*[@id=\"c2VuZF9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button").click() #AddFollowers
            sleep(wait_time/3)
            print("Success delivered! Thank me with a $ 1 donation on GitHub")
            sleep(wait_time/3)
            driver.refresh()
            sleep(wait_time/3)
            # Loop continues automatically
        except:
            print("A generic error occurred. Now will retry again")
            driver.refresh()
            sleep(wait_time)
            # Loop continues automatically

def loop5():
    while True:
        sleep(20)
        try:
            driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button").click()
        except:
            print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
            driver.refresh()
            continue
        try:
            sleep(20)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[6]/div/div/div/form/div/input").send_keys(vidUrl) # Write
            sleep(2)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[6]/div/div/div/form/div/div/button").click() # Search
            sleep(20)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[6]/div/div/div/div/div[1]/div/form/button").click() # AddShares
            sleep(60)
            print("Shares sent! Thank me with a $ 1 donation on GitHub")
            sleep(1700)
        except:
            print("A generic error occurred. Now will retry again")
            driver.refresh()
            sleep(300)
            # Loop continues automatically

def loop6():
    while True:
        sleep(1000)
        driver.refresh()
        print("Reload")
        loop5()

print("Author: https://github.com/NoNameoN-A")

vidUrl = input("Insert the video URL: ")

bot = int(input("What do you want to do?\n1 - Auto views(1000)\n2 - Auto hearts\n3 - Auto (FIRST) comments heart\n4 - Auto followers\n5 - [NEW]Auto Share\n6 - Simple reload\n"))
i = 0

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Use webdriver_manager to automatically install/locate chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://zefoy.com/")


if bot == 1:
    loop1()
elif bot == 2:
    loop2()
elif bot == 3:
    loop3()
elif bot == 4:
    loop4()
elif bot == 5:
    loop5()
elif bot == 6:
    loop5() # Note: loop6 calls loop5, so the loop6 function itself is just a wrapper now.
else:
    print("You can insert just 1, 2, 3, 4, 5 or 6")
