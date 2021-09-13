from selenium import webdriver
from bs4 import BeautifulSoup
from typing import Dict
import chromedriver_binary
import json
import links as link
import time


def get_price(ville :str,hotel :str,inday :int, inmounth:int, inyear:int ,outday :int, outmounth:int, outyear:int)-> Dict:
    hotelname=hotel.replace("_"," ")
    hotelname=hotelname.lower()
    x = hotelname.split(",")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome()
    driver.set_window_position(-10000,0)
    my_dict = {}
    #my_dict['search']=x
    '''
    if(ville in 'Marrakech'):
        url = f"https://www.booking.com/searchresults.fr.html?sb=1&src=searchresults&src_elem=sb&is_ski_area=&ssne=Marrakech&ssne_untouched=Marrakech&checkin_year={inyear}&checkin_month={inmounth}&checkin_monthday={inday}&checkout_year={outyear}&checkout_month={outmounth}&checkout_monthday={outday}&group_adults=2&group_children=0&no_rooms=1&from_sf=1&ac_position=0&ac_langcode=fr&ac_click_type=b&dest_id=1606338&dest_type=hotel&place_id_lat=31.617789743201&place_id_lon=-8.00983944915163&search_pageview_id=e026505f0efc0161&search_selected=true&search_pageview_id=e026505f0efc0161&ac_suggestion_list_length=1&ac_suggestion_theme_list_length=0"
    elif (ville in 'Casablanca'):
        xville="https://www.booking.com/searchresults.fr.html?sb=1&src=searchresults&src_elem=sb&is_ski_area=&ssne=Marrakech&ssne_untouched=Marrakech&checkin_year={inyear}&checkin_month={inmounth}&checkin_monthday={inday}&checkout_year={outyear}&checkout_month={outmounth}&checkout_monthday={outday}&group_adults=2&group_children=0&no_rooms=1&from_sf=1&ac_position=0&ac_langcode=fr&ac_click_type=b&dest_id=-28159&dest_type=city&iata=CAS&place_id_lat=33.593102&place_id_lon=-7.61639&search_pageview_id=257b500a45190177&search_selected=true&dest_id=-28159&dest_type=city&iata=CAS&place_id_lat=33.593102&place_id_lon=-7.61639&search_pageview_id=257b500a45190177&search_selected=true&search_pageview_id=257b500a45190177&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0"
        url = f"{xville}"  
    '''
    
    driver.get(link.get_url(ville,inday , inmounth, inyear ,outday , outmounth, outyear))
    time.sleep(5) 
    content = driver.page_source
    
    soup = BeautifulSoup(content,'lxml')
    
    Ville=soup.find('input', attrs={'id':'ss'})
    value = Ville['value']
    
    for a in soup.findAll('div', attrs={'class':'sr_item_content'}):
        
        name=a.find('span', attrs={'class':'sr-hotel__name'})
        price=a.find('div', attrs={'class':'bui-price-display__value'})
        rating=a.find('div', attrs={'class':'bui-review-score__badge'})        
        oronge=a.find('label', attrs={'class':'tpi_price_label__orange'})
        nameof=name.text.replace("\n","")
        #my_dict["hotel__name"].append(nameof)
        #my_dict["hotel__price"].append(hotelname) 
        if nameof.lower() in x :

            #driver.quit()
            #print("Found!")
            if oronge is None:
                txt=price.text.replace("MAD","")
                txt=txt.replace(" ","")                
                my_dict[nameof.lower()]=int(txt.replace("\n",""))
                #return(txt.replace(" ",""))
            else :
                txt=oronge.text.replace("MAD","")
                txt=txt.replace(" ","")                
                my_dict[nameof.lower()]=int(txt.replace("\n",""))            
    #print(jsonStr)
    driver.quit()
    return my_dict

