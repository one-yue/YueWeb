import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','YueWeb.settings')

import django
django.setup()
from rango.models import Category, Page
def populate():
    python_pages = [
        {"title":"CS-GO",
        "url":"https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/","views":32},
        {"title":"Dota 2",
        "url":"https://store.steampowered.com/app/570/Dota_2/","views":4},
        {"title":"World of Warships",
        "url":"https://store.steampowered.com/app/552990/World_of_Warships/","views":8}
    ]

    django_pages = [
        {"title":"Monster Hunter World: Iceborne",
        "url":"https://store.steampowered.com/app/1118010/Monster_Hunter_World_Iceborne/","views":32}, 
        {"title":"Red Dead Redemption 2",
        "url":"https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/","views":16}, 
        {"title":"GTA-5",
        "url":"https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/","views":8}
    ]

    other_pages = [
        {"title":"NBA-2k20",
        "url":"https://store.steampowered.com/app/1089350/NBA_2K20/","views":32},
         {"title":"Football Manager 2020",
        "url":"https://store.steampowered.com/app/1100600/Football_Manager_2020/","views":16}
    ]

    cats = {
        "FreeGame": {"pages": python_pages,"views":128,"likes": 64},
        "ActiveGame": {"pages": django_pages,"views": 64, "likes": 32},
        "SportGame": {"pages": other_pages,"views": 32, "likes": 16}
    }

    for cat,cat_data in cats.items():
        c = add_cat(cat,cat_data["views"],cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c,p["title"],p["url"],p["views"])
    
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print (" - {0} - {1}".format(str(c),str(p)))

def add_page(cat,title,url,views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name,viwes=0,likes=0):
    c=Category.objects.get_or_create(name=name)[0]
    c.views = viwes
    c.likes = likes
    c.save()
    return c

if __name__ == '__main__':
    print ("starting Rango population script...")
    populate()