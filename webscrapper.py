from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import xml.etree.ElementTree as ET

banned_list = ["Lith", "Meso", "Axi", "Ducats", "Requiem", "Neo"]




def add_to_xml(relic_name, a_container):
    tree = ET.parse('E:\Git\plat_bot\items - Copy.xml')
    root = tree.getroot()
    item = ET.SubElement(root, "Relic")
    typeR = ET.SubElement(item, "Type")
    relic_name = relic_name.lower()
    relic_name = relic_name.replace(" ", "_")
    relic_name = relic_name + "_relic"
    typeR.text = relic_name
    vaulted = ET.SubElement(item, "Vaulted")
    vaulted.text = "vaulted"
    drops = ET.SubElement(item, "Drops")
    for a in a_container:
        if a == "":
            continue
        a = a.lower()
        # replace space with underscore
        a = a.replace(" ", "_")
        drop = ET.SubElement(drops, "Drop")
        drop.set("name", a)
        

    tree = ET.ElementTree(root)
    tree.write("items - Copy.xml")
    

def parse(url):
    response = webdriver.Firefox()
    response.get(url)
    sleep(3)
    sourceCode=response.page_source
    return  sourceCode

def scrape():
    url =  "https://warframe.fandom.com/wiki/Category:Vaulted_Relics"
    html_soup = BeautifulSoup(get("https://warframe.fandom.com/wiki/Category:Vaulted_Relics").text, "html.parser")
   
    relic_containers = html_soup.find_all('li', class_='category-page__member')
    
    for relic in relic_containers:
        newUrl = "https://warframe.fandom.com" + relic.a['href']
        relic_name = relic.a['title']
        html_soup = BeautifulSoup(get(newUrl).text, "html.parser")
        items_container = html_soup.find_all("table")
        drops = []
        for item in items_container:
            tbody_container = item.find_all("tbody")
            for tbody in tbody_container:
                tr_container = tbody.find_all("tr")
                for tr in tr_container:
                    td_container = tr.find_all("td")
                    for td in td_container:
                        a_container = td.find_all("a")
                        for a in a_container:
                            if any(word in a.text for word in banned_list):
                                # remove from a_container
                                a_container.remove(a)
                                break
                            else:
                                drops.append(a.text)
                                continue
        print(drops)
        add_to_xml(relic_name, drops)
                                


def main():
    scrape()

if __name__ == "__main__":
    main()