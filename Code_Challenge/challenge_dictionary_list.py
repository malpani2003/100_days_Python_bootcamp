travel_log=[]



def add_new_country(country_name,visits,cities):
    dic={}
    dic["country"]=country_name
    dic["visits"]=visits
    dic["cities"]=cities
    travel_log.append(dic)

add_new_country("Russia",2,["Moscow","Saint Petersburg"])
add_new_country("Germany",5,["berlin","Hamburg"])

print(travel_log)

print(f"You have been visted {travel_log[0]['country']} {travel_log[0]['visits']} times")