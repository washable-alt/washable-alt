Day 35 

# Objective: print "Bring an Umbrella" if any of the next 12 hourly weather condition codes is less than 700. 

# Hint: 
1. Practice printing out the weather ID for the weather in the 0th hour.
2. Try to create a slice from the weather data to get a list of the hourly forecasts for only the next 12 hours.
3. Using the above try to create a list of only the next 12 weather condition codes

Geocoding API is a simple tool that OpenWeatherMap has developed to ease the search for locations while working with geographic names and coordinates

Running `weather2.5.py script`
`weather2.5.py` - tells you the current weather data based on the lattitude and longitude provided
Afterwards sending of whatsapp message to tell you to bring an umbrella

`main.py` - hourly data for the next 12 hours retrieved; can include data such as current, daily, minutely and hourly
If the `id` is less than 700, it means weather is not sunny anymore, send a whatapp message
![bring_an_umbrella](https://github.com/washable-alt/washable-alt/assets/127829594/7318903a-5c7f-4a98-aec9-e1a60f95d375)
![openweathermap](https://github.com/washable-alt/washable-alt/assets/127829594/398c2185-8334-460f-804a-1dd2928fbdd8)
