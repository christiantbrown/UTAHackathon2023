build_path_final = [("Spellthief's Edge", 450, None),
                    ("Shurelya's Battlesong", 2300, build_path_mythic),
                    ("Staff of Flowing Water", 2100, build_path_staff)
                    ("Ardent Censer", 2100, build_path_ardent),
                    ("Redemption", 2300, build_path_redemption),
                    ("Mikael's Blessing", 2300, build_path_mikael)
                    ]

build_path_mythic = [("Bandleglass Mirror", 950),
                    ("Kindlegem", 800)]

build_path_staff = [("Forbidden Idol", 800),
                            ("Aether Wisp", 850)]

build_path_redemption = [("Forbidden Idol", 800), 
                                ("Chalice of Blessing", 950)]
                                
build_path_ardent = [("Forbidden Idol", 800),
                            ("Aether Wisp", 850)]

build_path_mikael = [("Forbidden Idol", 800), 
                                ("Chalice of Blessing", 950)]

def purchase_item(item):
    print(f'Processing {item}')

#recursively goes through list and invokes purchase_item if current gold is greather than item cost
def buy_items(items, current_gold):
    if not items:
        #if item list is empty, end the recursion
        return
    #iterates through item list
    for item in items.copy():
        #if current gold is greather than item cost, then buy it
        if item[0] < current_gold:
            purchase_item(item)
            items.remove(item)
        #if not, then if item has a sublist for components, then it goes through that list instead
        elif isinstance(item, list):
            buy_items(item, current_gold)
        