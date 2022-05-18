import requests as rq
import xml.etree.ElementTree as ET
import os
import json
from collections import Counter
import time
# 1. List of all vaulted relics drops
# 2. Need to get average price of every relic drop with drop chance considered
# 3. Compare with average price of all relics drops


class Relic:
    name = ""
    drops = []
    vaulted = False
    average_price = 0

    def __init__(self, name):
        self.name = name
        self.drops = []


visitedDrops = {}


def get_best_relic(relics):
    best_relic = Relic("")
    for relic in relics:
        print(relic.name, relic.average_price)
        if relic.average_price > best_relic.average_price:
            best_relic = relic
    return best_relic.name


def get_items_id(relics):
    for relic in relics:
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
                    plat_values.sort()
                    plat_values = plat_values[:10]

                    avg_plat += sum(plat_values) / len(plat_values)
                    visitedDrops[drop] = avg_plat

                    relic.average_price = avg_plat
            rarity_counter += 1

    return relics
    #orders = payload.get('orders', [])


def parseResponse(response, desiredID):
    tree = ET.parse(response)
    root = tree.getroot()
   # for child in root.findall('Item'):


def parseXML(xmlfile):

    # parse the xml file, sorting each relic drop into a dictionary with the drops stored as the values

    tree = ET.parse(xmlfile)
    root = tree.getroot()
    relics = []
    for child in root.findall('Relic'):
        relic = Relic(child.find('Type').text)
        drops = list(child.iter())
        for grandchild in drops:
            if grandchild.tag == 'Drop':
                relic.drops.append(grandchild.attrib['name'])
        relics.append(relic)

    return relics


def main():
    print(get_best_relic(get_items_id(parseXML('D:\GIT\plat_bot\items.xml'))))


if __name__ == "__main__":
    main()
