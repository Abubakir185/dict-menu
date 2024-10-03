menu = {
    "osh": 30,
    "manti": 40,
    "mastava": 25
}

buyurtma = input("ovqat tanlang: ").lower()

if buyurtma in menu:
    print(f"{buyurtma} -> {menu[buyurtma]}mig som")
else:
    print(f"Uzur bizda {buyurtma} yoqi.")

