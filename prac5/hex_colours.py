"""
COLOUR_CODES = dictionary
get colour_name
while colour_name != ""
    display colour_name, COLOUR_CODES.get(colour_name)
    get colour_name
"""

COLOUR_CODES = {"Baker-Miller Pink": "#ff91af", "Banana Yellow": "#ffe135",
                "Bright Ube": "#d19fe8", "Cadmium Red": "#e30022", "CadetBlue1": "#98f5ff",
                "Cerise": "#de3163", "Chamoisee": "#a0785a", "Cherry Blossom Pink": "#ffb7c5",
                "Cool Grey": "#8c92ac", "Coral": "#ff7f50"}

colour_name = input("Enter the colour name: ")
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter the colour name: ")



