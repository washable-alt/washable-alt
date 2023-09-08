###################### Scope ###################################

#enemies = 1

#def increase_enemies():
#    enemies = 2
#    print(f"enemies inside function: {enemies}")

#increase_enemies()
#print(f"enemies outside function: {enemies}")


########## Local Scope #######################

#def drink_potion():
#    potion_strength = 2
#    print(potion_strength)

#drink_potion()
#print(potion_strength)


#global scope 
#player_health = 10

#def game():
#    def drink_potion():
#        potion_strength = 2
#        print(player_health)
#    drink_potion()

#game()
#print(player_health)

# Global Constants
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

def calc():
    return TWITTER_HANDLE

twitter_handle=calc()
print(twitter_handle)