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
from pathlib import Path


class Relic:
    name = ""
    drops = []
    vaulted = False
    average_price = 0
    best_drop = []

    def __init__(self, name):
        self.name = name
        self.drops = []

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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



def parseXML(xmlfile):
    global all_relics

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
        all_relics.append(relic)

    return relics

def get_relic_names(xmlfile):
    relics = parseXML(xmlfile)
    names = []
    for relic in relics:
        names.append(relic.name)
    return names

def search_specific_relic(relic_name):
    global all_relics
    # find relic in all_relics
    req_relic = None
    print(relic_name)
    for relic in all_relics:
        print(relic.name)
        if relic.name == relic_name:
            req_relic = relic
            break
    rarity_counter = 0
    rarity_bias = .25
    avg_plat = 0   
    for drop in req_relic.drops:
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
                req_relic.average_price += avg_plat
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

                        avg_plat += plat
                        visitedDrops[drop] = avg_plat

                        req_relic.average_price = avg_plat
            rarity_counter += 1
    return req_relic
        
    
