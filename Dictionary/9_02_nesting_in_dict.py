# Nesting list in dictionary
travel_log={
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"],
    "Like_travelling":True
}

# Nesting dictionary and list  in dictionary
cities_visted_number={
    "France":{"Paris":2,"Lille":3,"Dijon":1},
    "Germany":{"cities_visted":["Berlin","Hamburg","Stuttgart"]}
}

# nesting a dictionary in list
  
travel_log_2=[
    {
       "Paris":0,
        "Lille":1,
        "Dijon":2

    },
    {
        "Berlin":2,
        "Hamburg":0,
        "Stuttgart":1
    }
    ]

print(travel_log)
print(travel_log_2)
print(cities_visted_number)

# how access member in nesting
print(travel_log_2[0]["Paris"])

print(travel_log["France"])

print(cities_visted_number["Germany"]["cities_visted"])

print(travel_log["France"][0])