# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list into a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#for key in travel_log:
#    print(key)
#    print(travel_log[key])

# Nesting a dictionary into a dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits":12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#for key in travel_log:
#    print(key)
#    print(travel_log[key])


# Nesting a dictionary in a list

travel_log = [

    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]

for dict in travel_log:
    #print(dict["country"])
    #print(dict["cities_visited"])
    #print(dict["total_visits"])
    for city in dict["cities_visited"]:
        print(city)