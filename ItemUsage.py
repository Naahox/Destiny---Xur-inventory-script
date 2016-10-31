from termcolor import colored

DICTIONARY = {

    'ARMOR_PRICE': int(13), #armor/armour
    'WEAPON_PRICE': int(23)
}

def is_PvP_Weapon(item_name, item_type):

    Exotic_pvp_weapons = [

        'Monte Carlo',
        'Bad Juju',
        'SUROS Regime',
        'Hawkmoon',
        'The Last Word',
        'Red Death',
        'MIDA Multi-Tool',
        'Universal Remote',
        'No Land Beyond'
    ]

    for exotic in Exotic_pvp_weapons:

        if exotic == item_name:

            usage = '%s   |  Type > %s  |  Usage > PvP   |   Price > %iSC'%(colored(item_name, 'green'),colored(item_type, 'grey'),DICTIONARY['WEAPON_PRICE'])
            print'===PVP Gun'+'='*66
            print usage
            print'='*76+'\n\n'

            break

        else:continue


def is_hunter_pvp_armor(item_name, item_type):

    hunter_exotic_armor = [

        'ATS/8 Tarantella',
        'Crest of Alpha Lupi',
        'Lucky Raspberry',
        "Shinobu's Vow",
        "Young Ahamkara's Spine",
        'Achlyophage Symbiote',
        'Knucklehead Radar',
        'Bones of Eao',
        'Fr0st-EE5',
        'Radiant Dance Machines',
        'Skyburners Annex'
    ]


    for exotic in hunter_exotic_armor:

        if exotic == item_name:

            usage = '%s   |  Type > %s  |  Usage > PvP   |   Price > %iSC'%(colored(item_name, 'green'),colored(item_type, 'grey'),DICTIONARY['ARMOR_PRICE'])
            print'===Hunter Armor'+'='*61
            print usage
            print'='*76 +'\n\n'

            break

        else:continue


def is_titan_pvp_armor(item_name, item_type):

    titan_exotic_armor = [

        'Crest of Alpha Lupi',
        'The Armamentarium',
        'Twilight Garrison',
        'ACD/0 Feedback Fence',
        'Immolation Fists',
        'No Backup Plans',
        'Thagomizers',
        'The Insurmountable Skullfort',
        'Eternal Warrior',
        'Helm of Inmost Light',
        'Dunemarchers,'
        'Mk. 44 Stand Asides',
        'Peregrine Greaves',
    ]


    for exotic in titan_exotic_armor:

        if exotic == item_name:

            usage = '%s   |  Type > %s  |  Usage > PvP   |   Price > %iSC'%(colored(item_name, 'green'),colored(item_type, 'grey'),DICTIONARY['ARMOR_PRICE'])
            print'===Titan Armor'+'='*62
            print usage
            print'='*76 +'\n\n'

            break

        else:continue


def is_warlock_pvp_armor(item_name, item_type):

    warlock_exotic_armor = [


        'Heart of the Praxic Fire',
        'Purifier Robers',
        'Starfire Protocol',
        'Voidfang Vestments',
        'Claws of Ahamkara',
        'Nothing Manacles',
        'Ophidian Aspect',
        'The Impossible Machines',
        'Apotheosis Veil',
        'Astrocyte Verse',
        'Loght Beyond Nemesis',
        'Obsidian mind',
        'Skull of Dire Ahamkara',
        'The Ram',
        'THE STAG'
    ]


    for exotic in warlock_exotic_armor:

        if exotic == item_name:

            usage = '%s   |  Type > %s  |  Usage > PvP   |   Price > %iSC'%(colored(item_name, 'green'),colored(item_type, 'grey'),DICTIONARY['ARMOR_PRICE'])
            print'===Warlock Armor'+'='*60
            print usage
            print'='*76 +'\n\n'

            break

        else:continue
