
import requests, os, sys

try:

    from ItemUsage import *
    from _init_ import ___init___

except ImportError:

    print'failed importing...'
    sys.exit(1)


HEADERS = {

    'X-API-Key':    str('YOUR_KEY') #YOUR OWN API KEY
}


base_url = 'https://www.bungie.net/platform/Destiny/'
xur_url = 'https://www.bungie.net/Platform/Destiny/Advisors/Xur'
hashType = '6'


___init___()

if __name__ == '__main__':

    res = requests.get(xur_url, headers=HEADERS, verify=True)
    os.system('clear')


    for saleItem in res.json()['Response']['data']['saleItemCategories']:

        mysaleItems = saleItem['saleItems']

        for myItem in mysaleItems:

            hashID = str(myItem['item']['itemHash'])

            #https://www.bungie.net/platform/Destiny/Manifest/6/{THE HASH HERE}
            hashReqString = base_url + 'Manifest/' + hashType + '/' + hashID

            res = requests.get(hashReqString, headers=HEADERS)


            #To print the elements colored, the value must be in a string format


            item_name = res.json()['Response']['data']['inventoryItem']['itemName']
            _itemName = str(item_name)

            item_type = res.json()['Response']['data']['inventoryItem']['itemTypeName']
            _itemType = str(item_type)


            FUNCTIONS = {

                'pvp_weapon': is_PvP_Weapon(_itemName,_itemType),
                'hunter_armor': is_hunter_pvp_armor(_itemName,_itemType),
                'titan_armor': is_titan_pvp_armor(_itemName,_itemType),
                'warlock_armor': is_warlock_pvp_armor(_itemName,_itemType),
            }


            FUNCTIONS['pvp_weapon']()
            FUNCTIONS['hunter_armor']()
            FUNCTIONS['titan_armor']()
            FUNCTIONS['warlock_armor']()


            """
            Here on out should be for finding other values, maybe the item perks, tier, stats...etc
            tier  is listed below but commented out.

            """


            #item_tier = res.json()['Response']['data']['inventoryItem']['tierTypeName']



            """
            is_PvP_Weapon(_itemName,_itemType); is_hunter_pvp_armor(_itemName, _itemType)
            is_titan_pvp_armor(_itemName, _itemType); is_warlock_pvp_armor(_itemName, _itemType)

            """
