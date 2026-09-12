import random

def generate_palette():
    colors = []

    for _ in range(5):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)

        color = f"#{red:02X}{green:02X}{blue:02X}"
        colors.append(color)

    return colors
        