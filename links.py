from typing import Dict
def get_url(ville: str,inday :int, inmounth:int, inyear:int ,outday :int, outmounth:int, outyear:int) -> str:
    urls={}
    urls['Marrakech']=f"https://www.booking.com/searchresults.fr.html?sb=1&src=searchresults&src_elem=sb&is_ski_area=&ssne=Marrakech&ssne_untouched=Marrakech&checkin_year={inyear}&checkin_month={inmounth}&checkin_monthday={inday}&checkout_year={outyear}&checkout_month={outmounth}&checkout_monthday={outday}&group_adults=2&group_children=0&no_rooms=1&from_sf=1&ac_position=0&ac_langcode=fr&ac_click_type=b&dest_id=1606338&dest_type=hotel&place_id_lat=31.617789743201&place_id_lon=-8.00983944915163&search_pageview_id=e026505f0efc0161&search_selected=true&search_pageview_id=e026505f0efc0161&ac_suggestion_list_length=1&ac_suggestion_theme_list_length=0"
    urls['Casablanca']=f"https://www.booking.com/searchresults.fr.html?sb=1&src=searchresults&src_elem=sb&is_ski_area=&ssne=Marrakech&ssne_untouched=Marrakech&checkin_year={inyear}&checkin_month={inmounth}&checkin_monthday={inday}&checkout_year={outyear}&checkout_month={outmounth}&checkout_monthday={outday}&group_adults=2&group_children=0&no_rooms=1&from_sf=1&ac_position=0&ac_langcode=fr&ac_click_type=b&dest_id=-28159&dest_type=city&iata=CAS&place_id_lat=33.593102&place_id_lon=-7.61639&search_pageview_id=257b500a45190177&search_selected=true&dest_id=-28159&dest_type=city&iata=CAS&place_id_lat=33.593102&place_id_lon=-7.61639&search_pageview_id=257b500a45190177&search_selected=true&search_pageview_id=257b500a45190177&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0"
    return urls[ville]