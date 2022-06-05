from urllib import request
import requests as rq
import xml.etree.ElementTree as ET
import os
import json
from collections import Counter
import time
import tkinter as tk
import random
from PIL import Image, ImageTk
from io import BytesIO


class Relic:
    name = ""
    drops = []
    vaulted = False
    average_price = 0
    best_drop = []

    def __init__(self, name):
        self.name = name
        self.drops = []


visitedDrops = {}

all_relics = []
searching = False


def get_best_relic(relics, vaultedCheck, unvaultedCheck):
    global searching, best_relic_text, top_ten
    best_relic = Relic("")
    top_ten = {}
    for relic in relics:
        if len(top_ten) < 10:
            top_ten[relic.best_drop[1]] = relic.best_drop[0]
        print(relic.name, relic.average_price)
        if relic.average_price > best_relic.average_price:
            best_relic = relic
    print(best_relic.name)
    searching = False
    # list top ten best drops from the list of relics

    for relic in relics:
        if relic.vaulted == True and vaultedCheck == False:
            continue
        elif relic.vaulted == False and unvaultedCheck == False:
            continue
        for key, value in top_ten.items():
            if relic.best_drop[1] in top_ten:

                continue
            if relic.best_drop[0] > value:
                top_ten[relic.best_drop[1]] = relic.best_drop[0]
                top_ten.pop(key)
                break
    for key, value in top_ten.items():
        print(key, value)

    return best_relic.name


def get_items_id(relics, vaultedCheck, unvaultedCheck):
    global all_relics, visitedDrops, searching
    print("searching")
    for relic in relics:

        relic.best_drop = [0, ""]
        if relic.vaulted == True and vaultedCheck == False:
            continue
        elif relic.vaulted == False and unvaultedCheck == False:
            continue
        response = rq.get(
            'https://api.warframe.market/v1/items/' + relic.name + '/orders')
        rarity_counter = 0
        rarity_bias = .25
        avg_plat = 0
        for drop in relic.drops:
            if rarity_counter > 3 and rarity_counter < 5:
                rarity_bias = .11
            elif rarity_counter >= 5:
                rarity_bias = .2
            if drop == "forma_blueprint" or drop == "n/a":
                rarity_counter += 1
                continue
            if drop in visitedDrops:
                avg_plat += visitedDrops[drop]
                rarity_counter += 1
                relic.average_price += avg_plat
                continue
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', }
            response = rq.get(
                'https://api.warframe.market/v1/items/' + drop + '/orders', headers=headers)
            while response.status_code == 503:
                time.sleep(1)
                response = rq.get(
                    'https://api.warframe.market/v1/items/' + drop + '/orders', headers=headers)

            response.raise_for_status()
            if response.text == "":
                rarity_counter += 1
                continue
            tojson = json.loads(response.text)

            if tojson.get('payload') != None:
                payload = tojson.get('payload')
                if payload.get('orders') != None:
                    orders = payload.get('orders')

                    plat_values = []

                    for order in orders:
                        if order.get('order_type') == 'sell':

                            plat_values.append(
                                float(order.get('platinum')) * rarity_bias)

                    # Get average of 10 lowest prices
                    if len(plat_values) != 0:
                        plat_values.sort()
                        plat_values = plat_values[:10]
                        plat = sum(plat_values) / len(plat_values)

                        if plat > relic.best_drop[0]:
                            relic.best_drop = [plat, drop]
                        avg_plat += plat
                        visitedDrops[drop] = avg_plat

                        relic.average_price = avg_plat
            rarity_counter += 1
    all_relics = relics
    return relics


def parseResponse(response, desiredID):
    tree = ET.parse(response)
    root = tree.getroot()


def random_relic_icon():
    global all_relics, searching
    get_best_relic(get_items_id(parseXML('D:\GIT\plat_bot\items.xml')))
    print("length of all_relics: ", len(all_relics))
    random_relic_index = random.randint(0, len(all_relics) - 1)
    response = rq.get("https://api.warframe.market/v1/items/" +
                      all_relics[random_relic_index].name)
    print(all_relics[random_relic_index].name)
    while response.status_code == 503:
        time.sleep(1)
        print("sleeping")
        response = rq.get(
            'https://api.warframe.market/v1/items/' + all_relics[random_relic_index].name)

    response.raise_for_status()
    print("wow")
    tojson = json.loads(response.text)
    if tojson.get('payload') != None:
        print("payload exists")
        payload = tojson.get('payload')
        if payload.get('item') != None:
            print("item exists")
            item = payload.get('item')
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', }
            if item.get('items_in_set') != None:
                item_in_set = item.get('items_in_set')
                if item_in_set != None:
                    print(item_in_set[0]['icon'])
                    imageurl = rq.get(
                        'https://warframe.market/static/assets/' + item_in_set[0]['icon'], headers=headers)
                    if imageurl == None:
                        print("imageurl is none")
                        return None
                    img = Image.open(BytesIO(imageurl.content))
                    print(img)
                    # save in folder
                    img.save(r"D:\\GIT\plat_bot\images\relics\{}.png".format(
                        item.get('id'), 'r'))
                    return "D:\\GIT\plat_bot\images\\relics\{}.png".format(
                        item.get('id'))


def parseXML(xmlfile):
    searching = True
    # parse the xml file, sorting each relic drop into a dictionary with the drops stored as the values

    tree = ET.parse(xmlfile)
    root = tree.getroot()
    relics = []
    for child in root.findall('Relic'):
        relic = Relic(child.find('Type').text)
        if(child.find('Vaulted').text == "vaulted"):
            relic.vaulted = True
        drops = list(child.iter())
        for grandchild in drops:
            if grandchild.tag == 'Drop':
                relic.drops.append(grandchild.attrib['name'])
        relics.append(relic)

    return relics
