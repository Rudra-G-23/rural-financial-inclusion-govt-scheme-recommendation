import pandas as pd

category_mapping = {
    129: "cereals",
    139: "cereal substitute",
    159: "pulses & products",
    179: "salt & sugar",
    169: "milk & milk products",
    219: "vegetables",
    239: "fruits (fresh)",
    249: "fruits (dry)",
    199: "egg, fish & meat",
    189: "edible oil",
    269: "spices",
    279: "beverages",
    289: "served processed food",
    299: "packaged processed food"
}

cereal_mapping = {
    61: "rice-free",
    62: "wheat/atta-free",
    70: "coarse grains-free",
    101: "rice – PDS",
    102: "rice – other sources",
    103: "chira",
    105: "muri",
    106: "other rice products (khoi/lawa, etc.)",
    107: "wheat/atta – PDS",
    108: "wheat/atta – other sources",
    110: "maida",
    111: "suji/rawa",
    112: "vermicelli (sewai)",
    114: "other wheat products",
    1: "coarse grains – PDS",
    2: "coarse grains – other sources",
    122: "other cereals & products",
    129: "cereals: sub-total"
}

cereal_substitute_mapping = {
    139: "cereal substitutes (tapioca, etc.)"
}

pulses_mapping = {
    140: "arhar/tur",
    141: "gram: split",
    142: "gram: whole",
    143: "moong",
    144: "masur",
    145: "urd",
    146: "peas/chickpeas",
    148: "other pulses (khesari, etc.)",
    150: "besan/gram products",
    152: "other pulse products (soya chunks, etc.)",
    158: "pulses – PDS",
    71: "pulses – free",
    72: "gram – free",
    159: "pulses & pulse products: sub-total"
}

salt_sugar_mapping = {
    73: "salt – free",
    74: "sugar – free",
    178: "salt – PDS",
    170: "salt – other sources",
    171: "sugar – PDS",
    172: "sugar – other sources",
    173: "jaggery (gur)",
    174: "candy/misri",
    175: "honey",
    179: "salt & sugar: sub-total"
}

milk_mapping = {
    160: "milk: liquid",
    162: "milk: condensed/powder",
    163: "curd/yogurt",
    164: "ghee",
    165: "butter",
    166: "ice-cream",
    3: "paneer",
    4: "prepared sweets",
    5: "cheese",
    92: "other milk products (lassi, buttermilk, etc.)",
    169: "milk & milk products: sub-total"
}

vegetables_mapping = {
    200: "potato",
    201: "onion",
    202: "tomato",
    203: "brinjal",
    204: "radish",
    205: "carrot",
    206: "leafy vegetables",
    207: "green chillies",
    208: "lady’s finger",
    210: "parwal/patal/kundru",
    211: "cauliflower",
    212: "cabbage",
    213: "gourd/pumpkin",
    214: "peas",
    215: "beans/barbati",
    216: "lemon",
    217: "other vegetables",
    219: "vegetables: sub-total"
}

fruits_fresh_mapping = {
    220: "banana",
    224: "coconut",
    225: "green coconut",
    226: "guava",
    228: "orange/sweet lime (mausami)",
    230: "papaya",
    231: "mango",
    232: "kharbooza",
    236: "apple",
    237: "grapes",
    222: "watermelon",
    93: "other fresh fruits (litchi, pineapple, etc.)",
    239: "fruits (fresh): sub-total"
}

fruits_dry_mapping = {
    240: "coconut: copra",
    241: "groundnut",
    242: "dates",
    243: "cashew nut",
    245: "other nuts (almond, pistachio, walnut, etc.)",
    246: "raisin/kishmish",
    94: "other dry fruits (apricot, fig, etc.)",
    249: "fruits (dry): sub-total"
}

nonveg_mapping = {
    190: "eggs",
    191: "fish/prawn",
    192: "goat meat/mutton",
    193: "beef/buffalo meat",
    194: "pork",
    195: "chicken",
    196: "other meat (crab, oyster, etc.)",
    199: "egg, fish & meat: sub-total"
}

edible_oil_mapping = {
    181: "mustard oil",
    182: "groundnut oil",
    183: "coconut oil",
    184: "refined oil",
    188: "edible oil – PDS",
    95: "other oils (vanaspati, margarine, etc.)",
    75: "edible oil – free",
    189: "edible oil: sub-total"
}

spices_mapping = {
    250: "ginger",
    251: "garlic",
    252: "cumin",
    253: "coriander",
    254: "turmeric",
    255: "black pepper",
    256: "dry chillies",
    257: "tamarind",
    258: "curry powder",
    260: "oilseeds",
    261: "other spices",
    263: "poppy seeds",
    269: "spices: sub-total"
}

beverages_mapping = {
    11: "soda drinks",
    270: "tea: cups",
    271: "tea: leaf",
    272: "coffee: cups",
    273: "coffee: powder",
    274: "mineral water",
    275: "other cold beverages",
    276: "fruit juice/shake",
    278: "other beverages (cocoa, health drinks)",
    279: "beverages: sub-total"
}

served_processed_mapping = {
    76: "cooked meals purchased at subsidized rate",
    280: "cooked meals purchased",
    281: "cooked meals received free in workplace",
    282: "cooked meals received as assistance",
    283: "cooked snacks purchased",
    284: "other served processed food",
    289: "served processed food: sub-total"
}

packaged_processed_mapping = {
    12: "breakfast cereals",
    13: "biscuits",
    14: "health supplements",
    15: "noodles",
    113: "bread (bakery)",
    161: "baby food",
    290: "cake/pastry",
    291: "chocolates",
    292: "namkeen/papad/bhujia",
    293: "chips/wafers/nachos",
    294: "pickles",
    295: "sauce/jam/jelly/mayonnaise",
    296: "other packaged processed food",
    299: "packaged processed food: sub-total"
}

combine_dict = {
    **category_mapping,
    **cereal_mapping,
    **cereal_substitute_mapping,
    **pulses_mapping,
    **salt_sugar_mapping,
    **milk_mapping,
    **vegetables_mapping,
    **fruits_dry_mapping,
    **fruits_fresh_mapping,
    **nonveg_mapping,
    **edible_oil_mapping,
    **spices_mapping,
    **beverages_mapping,
    **served_processed_mapping,
    **packaged_processed_mapping
    
}

try:
    df = pd.DataFrame.from_dict(combine_dict, orient="index").reset_index()
    df.columns = ["item_code", "category"]
    df.to_csv("07-fdq-category-mapping.csv", index=False)
except Exception as e:
    print(e)