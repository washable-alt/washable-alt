import colorgram


rgb_colors = []

#extract to 30 colors
colors = colorgram.extract(r'file path', 30)

print(colors)

# learn how to extract from a tuple and put r, g, b colors to a list
for color in colors:
    print(color.rgb)
    
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)
