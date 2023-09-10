from selenium import webdriver
import random
import undetected_chromedriver as uc
import time
import requests
from bs4 import BeautifulSoup
import os

from selenium.webdriver.common.by import By
from urllib.request import urlopen
print("Tiktok profile video downloader without watermark")
print("--------------------------------------------------")
print("For Follower Criteria Press Y or for all user data download press any key and enter")
print("--------------------------------------------------")
key=input("Enter Key > ")
print(key)



if key=='y':
        print("Enter The Number Of Follower Program Will Focus On Profile Which Have Follower Equal Or Above To Your Value ")
        f = input("")

        usernames = []  # List to store the lines

        # Open the file
        with open('username.txt', 'r') as file:
                # Read each line and store it in the list
                for line in file:
                        usernames.append(line.strip())

        for username in usernames:
                options = webdriver.ChromeOptions()

                driver = uc.Chrome(use_subprocess=True)

                def downloadVideo(link, id):

                        cookies = {
                                '_gid': 'GA1.2.288225543.1685551250',
                                '__cflb': '0H28v8EEysMCvTTqtuFFMWyYEmbm6aBgGxDdvjbv2zR',
                                '_gat_UA-3524196-6': '1',
                                '__gads': 'ID=11120b4e8ed54f99-226eba6e9fb40017:T=1685551251:RT=1685631040:S=ALNI_MaznYdotNXMiugodF4OpQZaNrDZ_Q',
                                '__gpi': 'UID=00000c3a61a416b4:T=1685551251:RT=1685631040:S=ALNI_Mbu9_9gEUmn6mwKcaJ1__lRlcThjQ',
                                '_ga': 'GA1.2.1643096165.1685551250',
                                '_ga_ZSF3D6YSLC': 'GS1.1.1685629610.2.1.1685631044.0.0.0',
                        }

                        headers = {
                                'authority': 'ssstik.io',
                                'accept': '*/*',
                                'accept-language': 'en-US,en;q=0.9',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                # 'cookie': '_gid=GA1.2.288225543.1685551250; __cflb=0H28v8EEysMCvTTqtuFFMWyYEmbm6aBgGxDdvjbv2zR; _gat_UA-3524196-6=1; __gads=ID=11120b4e8ed54f99-226eba6e9fb40017:T=1685551251:RT=1685631040:S=ALNI_MaznYdotNXMiugodF4OpQZaNrDZ_Q; __gpi=UID=00000c3a61a416b4:T=1685551251:RT=1685631040:S=ALNI_Mbu9_9gEUmn6mwKcaJ1__lRlcThjQ; _ga=GA1.2.1643096165.1685551250; _ga_ZSF3D6YSLC=GS1.1.1685629610.2.1.1685631044.0.0.0',
                                'hx-current-url': 'https://ssstik.io/en',
                                'hx-request': 'true',
                                'hx-target': 'target',
                                'hx-trigger': '_gcaptcha_pt',
                                'origin': 'https://ssstik.io',
                                'referer': 'https://ssstik.io/en',
                                'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                        }

                        params = {
                                'url': 'dl',
                        }

                        data = {
                                'id': link,
                                'locale': 'en',
                                'tt': 'MndBRXc3',
                        }

                        response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies,
                                                 headers=headers,
                                                 data=data)
                        downloadSoup = BeautifulSoup(response.text, "html.parser")
                        downloadLink = downloadSoup.find('a',
                                                         class_='pure-button pure-button-primary is-center u-bl dl-button download_link without_watermark vignette_active notranslate')
                        try:
                                global temp
                                temp = (downloadLink.get('href'))
                        except:
                                print("")


                        mp4File = urlopen(temp)
                        folder_name = username

                        # Check if the folder already exists
                        if not os.path.exists(folder_name):
                                # Create the folder
                                os.makedirs(folder_name)
                                print("Folder created successfully")
                                print("Saving Video To Folder")


                        # Feel free to change the download directory



                        with open(f"{folder_name}/{id}.mp4", "wb") as output:
                                while True:
                                        data = mp4File.read(4096)
                                        if data:
                                                output.write(data)
                                        else:
                                                break


                print(username)

                driver.get('https://www.tiktok.com/@' + username)

                driver.implicitly_wait(50)
                followers = driver.find_element(By.XPATH,
                                                '//*[@id="main-content-others_homepage"]/div/div[1]/h3/div[2]/strong').text
                value_str = followers
                if value_str[-1] == 'K':
                        result_int = int(float(value_str[:-1]) * 1000)
                else:
                        result_int = int(value_str)

                print(result_int)
                if int(f) <= result_int:
                        print("Profile meet your criteria")
                        time.sleep(2)
                        try:
                                new = driver.find_element(By.XPATH,
                                                          '//*[@id="main-content-others_homepage"]/div/div[2]/div[2]/div/div[1]')
                                new.click()
                                counter = 1
                                while True:
                                        time.sleep(2)

                                        time.sleep(5)

                                        button = driver.find_element(By.XPATH,
                                                                     '//*[@id="app"]/div[2]/div[4]/div/div[1]/button[3]')
                                        count = 1
                                        time.sleep(3)
                                        q = driver.current_url
                                        downloadVideo(q, counter)
                                        counter += 1

                                        if button.is_enabled():
                                                button.click()
                                        else:
                                                driver.quit()
                        except:
                                print("")
                                continue
                else:
                        print("Profile Don't meet your criteria")







else:
        usernames = []  # List to store the lines

        # Open the file
        with open('username.txt', 'r') as file:
                # Read each line and store it in the list
                for line in file:
                        usernames.append(line.strip())

        for username in usernames:
                options = webdriver.ChromeOptions()

                driver = uc.Chrome(use_subprocess=True)




                def downloadVideo(link, id):

                        cookies = {
                                '_gid': 'GA1.2.288225543.1685551250',
                                '__cflb': '0H28v8EEysMCvTTqtuFFMWyYEmbm6aBgGxDdvjbv2zR',
                                '_gat_UA-3524196-6': '1',
                                '__gads': 'ID=11120b4e8ed54f99-226eba6e9fb40017:T=1685551251:RT=1685631040:S=ALNI_MaznYdotNXMiugodF4OpQZaNrDZ_Q',
                                '__gpi': 'UID=00000c3a61a416b4:T=1685551251:RT=1685631040:S=ALNI_Mbu9_9gEUmn6mwKcaJ1__lRlcThjQ',
                                '_ga': 'GA1.2.1643096165.1685551250',
                                '_ga_ZSF3D6YSLC': 'GS1.1.1685629610.2.1.1685631044.0.0.0',
                        }

                        headers = {
                                'authority': 'ssstik.io',
                                'accept': '*/*',
                                'accept-language': 'en-US,en;q=0.9',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                # 'cookie': '_gid=GA1.2.288225543.1685551250; __cflb=0H28v8EEysMCvTTqtuFFMWyYEmbm6aBgGxDdvjbv2zR; _gat_UA-3524196-6=1; __gads=ID=11120b4e8ed54f99-226eba6e9fb40017:T=1685551251:RT=1685631040:S=ALNI_MaznYdotNXMiugodF4OpQZaNrDZ_Q; __gpi=UID=00000c3a61a416b4:T=1685551251:RT=1685631040:S=ALNI_Mbu9_9gEUmn6mwKcaJ1__lRlcThjQ; _ga=GA1.2.1643096165.1685551250; _ga_ZSF3D6YSLC=GS1.1.1685629610.2.1.1685631044.0.0.0',
                                'hx-current-url': 'https://ssstik.io/en',
                                'hx-request': 'true',
                                'hx-target': 'target',
                                'hx-trigger': '_gcaptcha_pt',
                                'origin': 'https://ssstik.io',
                                'referer': 'https://ssstik.io/en',
                                'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                        }

                        params = {
                                'url': 'dl',
                        }

                        data = {
                                'id': link,
                                'locale': 'en',
                                'tt': 'MndBRXc3',
                        }

                        response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies,
                                                 headers=headers,
                                                 data=data)
                        downloadSoup = BeautifulSoup(response.text, "html.parser")
                        downloadLink = downloadSoup.find('a',
                                                         class_='pure-button pure-button-primary is-center u-bl dl-button download_link without_watermark vignette_active notranslate')
                        try:
                                global temp
                                temp = (downloadLink.get('href'))
                        except:
                                print("")

                        mp4File = urlopen(temp)
                        folder_name = username

                        # Check if the folder already exists
                        if not os.path.exists(folder_name):
                                # Create the folder
                                os.makedirs(folder_name)
                                print("Folder created successfully.")
                                print("Saving Video To Folder")

                        # Feel free to change the download directory

                        with open(f"{folder_name}/{id}.mp4", "wb") as output:
                                while True:
                                        data = mp4File.read(4096)
                                        if data:
                                                output.write(data)
                                        else:
                                                break


                print(username)

                driver.get('https://www.tiktok.com/@' + username)

                driver.implicitly_wait(50)
                followers = driver.find_element(By.XPATH,
                                                '//*[@id="main-content-others_homepage"]/div/div[1]/h3/div[2]/strong').text
                print(followers)
                time.sleep(2)
                try:
                        new = driver.find_element(By.XPATH,
                                                  '//*[@id="main-content-others_homepage"]/div/div[2]/div[2]/div/div[1]')
                        new.click()
                        counter = 1
                        while True:
                                time.sleep(2)

                                time.sleep(5)

                                button = driver.find_element(By.XPATH,
                                                             '//*[@id="app"]/div[2]/div[4]/div/div[1]/button[3]')
                                count = 1
                                time.sleep(3)
                                q = driver.current_url
                                downloadVideo(q, counter)
                                counter += 1

                                if button.is_enabled():
                                        button.click()
                                else:
                                        driver.quit()
                except:
                        print("THis user has no video")
                        continue


