## 🧩 1. Define Separate Mapping Dictionaries

> Item_Code → Description
---

### 🍚 **Cereals**

```python
cereal_mapping = {
    061: "rice-free",
    062: "wheat/atta-free",
    070: "coarse grains-free",
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
    001: "coarse grains – PDS",
    002: "coarse grains – other sources",
    122: "other cereals & products",
    129: "cereals: sub-total"
}
```

---

### 🌿 **Cereal Substitutes**

```python
cereal_substitute_mapping = {
    139: "cereal substitutes (tapioca, etc.)"
}
```

---

### 🫘 **Pulses & Products**

```python
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
    071: "pulses – free",
    072: "gram – free",
    159: "pulses & pulse products: sub-total"
}
```

---

### 🧂 **Salt & Sugar**

```python
salt_sugar_mapping = {
    073: "salt – free",
    074: "sugar – free",
    178: "salt – PDS",
    170: "salt – other sources",
    171: "sugar – PDS",
    172: "sugar – other sources",
    173: "jaggery (gur)",
    174: "candy/misri",
    175: "honey",
    179: "salt & sugar: sub-total"
}
```

---

### 🥛 **Milk & Milk Products**

```python
milk_mapping = {
    160: "milk: liquid",
    162: "milk: condensed/powder",
    163: "curd/yogurt",
    164: "ghee",
    165: "butter",
    166: "ice-cream",
    003: "paneer",
    004: "prepared sweets",
    005: "cheese",
    092: "other milk products (lassi, buttermilk, etc.)",
    169: "milk & milk products: sub-total"
}
```

---

### 🥦 **Vegetables**

```python
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
```

---

### 🍌 **Fruits (Fresh)**

```python
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
    093: "other fresh fruits (litchi, pineapple, etc.)",
    239: "fruits (fresh): sub-total"
}
```

---

### 🥜 **Fruits (Dry)**

```python
fruits_dry_mapping = {
    240: "coconut: copra",
    241: "groundnut",
    242: "dates",
    243: "cashew nut",
    245: "other nuts (almond, pistachio, walnut, etc.)",
    246: "raisin/kishmish",
    094: "other dry fruits (apricot, fig, etc.)",
    249: "fruits (dry): sub-total"
}
```

---

### 🍗 **Egg, Fish & Meat**

```python
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
```

---

### 🛢️ **Edible Oil**

```python
edible_oil_mapping = {
    181: "mustard oil",
    182: "groundnut oil",
    183: "coconut oil",
    184: "refined oil",
    188: "edible oil – PDS",
    095: "other oils (vanaspati, margarine, etc.)",
    075: "edible oil – free",
    189: "edible oil: sub-total"
}
```

---

### 🌶️ **Spices**

```python
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
```

---

### ☕ **Beverages**

```python
beverages_mapping = {
    011: "soda drinks",
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
```

---

### 🍱 **Served Processed Food**

```python
served_processed_mapping = {
    076: "cooked meals purchased at subsidized rate",
    280: "cooked meals purchased",
    281: "cooked meals received free in workplace",
    282: "cooked meals received as assistance",
    283: "cooked snacks purchased",
    284: "other served processed food",
    289: "served processed food: sub-total"
}
```

---

### 🥪 **Packaged Processed Food**

```python
packaged_processed_mapping = {
    012: "breakfast cereals",
    013: "biscuits",
    014: "health supplements",
    015: "noodles",
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
```

---
