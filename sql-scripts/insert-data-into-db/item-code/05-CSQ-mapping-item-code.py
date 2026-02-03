import pandas as pd

sec_08_mapping = {
    96:  "other fuel (charcoal, biogas, gobar gas, coal, dung cake, petrol [excl. conveyance], diesel [excl. conveyance], other natural gas [CNG, etc.], matches, candle, others)",

    331: "firewood and chips",
    332: "electricity (std. unit)",

    334: "kerosene – PDS (litre)",
    335: "kerosene – other sources (litre)",

    338: "LPG [excl. conveyance]",
    349: "fuel and light: sub-total",

    # Added detailed DDM items (“&” category)
    341: "charcoal",
    343: "biogas / gobar gas",
    337: "coal",
    333: "dung cake",
    344: "petrol (litre) [excl. conveyance]",
    345: "diesel (litre) [excl. conveyance]",
    340: "other natural gas (CNG, etc.)",
    336: "matches (box)",
    342: "candle (number)",
    346: "other fuel – miscellaneous"
}

category_mapping = {
    349: "fuel and light",
    459: "toilet articles",
    479: "other household consumables",
    409: "education",
    419: "medical (hospitalization)",
    429: "medical (non-hospitalization)",
    519: "conveyance",
    499: "consumer services excl. conveyance",
    439: "entertainment",
    529: "rent",
    539: "house rent, garage rent (imputed)",
    899: "other consumer taxes & cesses",
    309: "pan",
    319: "tobacco",
    329: "intoxicants",
}

fuel_and_light_mapping = {
    332: "electricity (std. unit)",
    338: "LPG [excl. conveyance]",
    331: "firewood and chips",
    334: "kerosene – PDS (litre)",
    335: "kerosene – other sources (litre)",
    96:  "other fuel (charcoal, biogas, gobar gas, coal, dung cake, petrol [excl. conveyance], diesel [excl. conveyance], other natural gas [CNG, etc.], matches, candle, etc.)",
    349: "fuel and light: sub-total",
}

toilet_articles_mapping = {
    450: "toilet soap, body-wash, hand-wash, shower gel, face-wash",
    16:  "sanitizer",
    451: "toothpaste, mouthwash, toothbrush, etc.",
    453: "shampoo, conditioner, hair serum/gel, hair cream",
    17:  "hair oil, hair colour",
    18:  "other hair products, accessories, comb, etc.",
    452: "powder, cream, body lotion, moisturizers",
    20:  "other beauty products (lipstick, nail polish, compact, foundation, eye makeup kit, etc.)",
    21:  "perfume, body spray, deodorant, roll-ons, etc.",
    456: "sanitary napkins",
    22:  "baby products (diapers, lotion, powder, etc.)",
    454: "shaving blades, shaving stick, razor",
    455: "shaving cream, shaving foam, aftershave lotion, aftershave balm",
    457: "other toilet articles (body oil, make-up brushes, etc.)",
    459: "toilet articles: sub-total",
}

other_household_consumables_mapping = {
    466: "washing soap/soda/powder/liquid detergent",
    467: "other washing requisites",
    465: "floor cleaner, acid, toilet cleaner",
    471: "mosquito repellent, insecticide, anti-rodent, etc.",
    464: "bucket & other plastic goods",
    468: "incense (agarbatti), room freshener",
    470: "flower (fresh): all purposes",
    23:  "LED bulb, CFL bulbs",
    460: "other electric bulb, tubelight, decorative lights",
    462: "earthenware, paperware, thermocol plates, etc.",
    461: "electric batteries",
    463: "glassware",
    472: "other petty articles like coir, rope, door mat, non-durable electric goods, etc.",
    479: "other household consumables: sub-total",
}

medical_non_hospitalisation_mapping = {
    420: "medicine",
    422: "doctor's/surgeon's fee",
    421: "X-ray, ECG, pathological test, etc.",
    423: "family planning devices",
    424: "other medical expenses",
    429: "medical – non-hospitalisation: sub-total",
}

medical_hospitalisation_mapping = {
    410: "medicine",
    412: "doctor's/surgeon's fee",
    411: "X-ray, ECG, pathological test, etc.",
    413: "hospital & nursing home charges",
    414: "other medical expenses",
    419: "medical – hospitalisation: sub-total",
}

education_mapping = {
    405: "tuition and other fees (school, college, etc.)",
    406: "private tutor/coaching centre",
    400: "books, journals (incl. e-books, audio books): first hand",
    401: "books, journals, etc.: second hand",
    404: "stationery, photocopying charges",
    408: "other educational expenses (incl. fees for enrolment in web-based training, library charges, educational CD, etc.)",
    409: "education: sub-total",
}

pan_mapping = {
    300: "pan: leaf (no.)",
    301: "pan: finished (no.)",
    302: "ingredients for pan (gm)",
    309: "pan: sub-total",
}

rent_mapping = {
    520: "house rent, garage rent (actual)",
    521: "hotel lodging charges",
    522: "residential land rent",
    523: "other consumer rent",
    529: "rent: sub-total",
    539: "house rent, garage rent (imputed)",
    899: "other consumer taxes & cesses",
}

entertainment_mapping = {
    437: "cable TV/DTH/set top box (incl. broadband charges if not separable)",
    430: "cinema, theatre",
    402: "newspapers, periodicals",
    435: "photography",
    433: "club, gym, swimming fees & other subscriptions",
    28:  "online media service provider/streaming services",
    438: "other entertainment (mela, fair, picnic, VCD/DVD hire, etc.)",
    439: "entertainment: sub-total",
}

consumer_services_mapping = {
    488: "telephone charges: mobile (incl. data charges if not separable)",
    487: "telephone charges: landline (incl. broadband charges if not separable)",
    496: "internet expenses (cable broadband, mobile data charges, etc. if separable)",
    540: "water charges",
    483: "barber, beautician, spas, etc.",
    480: "domestic helper/cook",
    484: "washerman, laundry, ironing, dry cleaning, dyeing of clothes",
    482: "sweeper",
    481: "attendant, babysitter",
    27:  "watchmen/security guard, driver",
    485: "tailor",
    486: "grinding/husking charges, etc.",
    492: "priest",
    495: "pet animals (incl. birds, fish)",
    494: "repair charges for non-durables (electrician’s charges, plumbing charges, etc.)",
    493: "legal expenses",
    490: "postage, couriers, fax & money order",
    497: "other consumer services excluding conveyance (car parking charges, coolie/porter charges, toll charges, miscellaneous expenses, etc.)",
    499: "consumer services excluding conveyance: sub-total",
}

conveyance_mapping = {
    24:  "railway fare",
    504: "bus fare for school, college, etc.: periodic (lumpsum) payment",
    25:  "bus fare for commuting to work: periodic (lumpsum) payment",
    506: "bus/tram fare for school, college: daily (miscellaneous) payments",
    505: "bus/tram fare for commuting to work: daily (miscellaneous) payments",
    500: "bus/tram fare: occasional",
    508: "taxi fare",
    501: "auto-rickshaw/e-rickshaw fare",
    510: "car/bus hired for ceremonial occasion, picnic, etc.",
    26:  "steamer, boat fare",
    511: "rickshaw (hand-drawn & cycle) fare",
    503: "air fare",
    512: "petrol for vehicle",
    513: "diesel for vehicle",
    514: "other conveyance expenses",
    519: "conveyance: sub-total",
}

intoxicants_mapping = {
    322: "country liquor (litre)",
    324: "foreign/refined liquor or wine (litre)",
    323: "beer (litre)",
    321: "toddy (litre)",
    320: "ganja (gm)",
    325: "other intoxicants",
    329: "intoxicants: sub-total",
}

tobacco_mapping = {
    310: "bidi (no.)",
    311: "cigarettes (no.)",
    316: "gutka, zarda, kimam, surti (gm)",
    312: "leaf tobacco (gm)",
    314: "hookah tobacco (gm)",
    315: "cheroot (no.)",
    313: "snuff (gm)",
    317: "other tobacco products",
    319: "tobacco: sub-total",
}

combine_dict = {
    **sec_08_mapping,
    **category_mapping,
    **fuel_and_light_mapping,
    **toilet_articles_mapping,
    **other_household_consumables_mapping,
    **medical_hospitalisation_mapping,
    **medical_non_hospitalisation_mapping,
    **education_mapping,
    **pan_mapping,
    **rent_mapping,
    **entertainment_mapping,
    **consumer_services_mapping,
    **conveyance_mapping,
    **intoxicants_mapping,
    **tobacco_mapping
}

try:
    df = pd.DataFrame.from_dict(combine_dict, orient="index").reset_index()
    df.columns = ["item_code", "category"]
    df.to_csv("05-csq-category-mapping.csv", index=False)
except Exception as e:
    print(e)