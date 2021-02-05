from bs4 import BeautifulSoup
import requests
import re
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(string):
   html_text = requests.get('https://www.newegg.com/p/pl?d=graphic+card&N=100007709%20601359415%20601357250&isdeptsrh=1')
   soup = BeautifulSoup(html_text.text, 'lxml')
   all_item_containers = soup.find_all('div', class_ = "item-container")
   all_item_button_areas = soup.find_all('div', class_ = "item-button-area")
   #print(button_text)
   for single_item_container, single_item_button in zip(all_item_containers, all_item_button_areas):
       item_links = re.findall('href="([^"]*)"', str(single_item_container))
       item_stock = re.findall('>(.*)<', str(single_item_button))
       print(str(single_item_button))
       print((item_links[0]).replace(" ", ""))
       print(item_stock[0].find("Sold Out"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
