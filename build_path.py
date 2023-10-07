build_path_final = [("Spellthief's Edge", 450, None),
                    ("Shurelya's Battlesong", 2300, build_path_mythic),
                    ("Staff of Flowing Water", 2100, build_path_staff_ardent)
                    ("Ardent Censer", 2100, build_path_staff_ardent),
                    ("Redemption", 2300, build_path_redemption_mikael),
                    ("Mikael's Blessing", 2300, build_path_redemption_mikael)
                    ]

build_path_mythic = [("Bandleglass Mirror", 950),
                    ("Kindlegem", 800)]

build_path_staff_ardent = [("Forbidden Idol", 800),
                            ("Aether Wisp", 850)]

build_path_redemption_mikael = [("Forbidden Idol", 800), 
                                ("Chalice of Blessing", 950)]

def purchase_item(item):
    print(f'Processing {item}')

def buy_items(items, current_gold):
    if not items:
        return
    for item in items.copy():
        if item[0] < current_gold:
            purchase_item(item)
            items.remove(item)
        elif isinstance(item, list):
            buy_items(item, current_gold)

    if len(items) == len(new_items):
        new_items = [(str(i), i) for i in range(x, x+5)]
        buy_items(new_items, x)
        