from PIL import Image, ImageDraw, ImageFont
import json
import os

font_check = ImageDraw.Draw(Image.new('RGB', (1, 1)))

# Initialize empty arrays for streamer names, links (only their unique id and not the full link) and their platforms
streamer_names = []
streamer_links = []
streamer_platforms = []

platform_names = []
platform_links = []
platform_colors = []
platform_logos = []

# Set the path for the background box and the Tarkov font
box_path = 'assets/Box.png'
font_path = 'assets/Bender.otf'

# Open the background box
box = Image.open(box_path)

# Get the path to the JSON file with all streamers and their info
while True:
    json_path = input('Data Path: ')
    if json_path[len(json_path) - 5: len(json_path)] != '.json':
        print('File is not JSON.')
    else:
        break

# Open the file
json_file = open(json_path, 'r')

# Convert plain text from the file to JSON and close the file
streamers_json = json.loads(json_file.read())
json_file.close()

# Loop though each JSON object and append values to their respective lists
for line in streamers_json:
    streamer_names.append(str(line['name']))
    streamer_links.append(str(line['link']))
    streamer_platforms.append(str(line['platform']))

# Open the platform data, convert it into JSON and close it
data_file = open('assets/data.json', 'r')
data_json = json.loads(data_file.read())
data_file.close()

# Extract individual platform values from JSON object
for line in data_json:
    platform_names.append(str(line['platform']))
    platform_links.append(str(line['link']))
    platform_colors.append(str(line['color']))
    platform_logos.append(str(line['pathLogo']))


# Check if an output folder already exists, if not, make one
output_path = os.path.abspath(os.curdir)
output_path = os.path.join(output_path, 'out')
if not os.path.exists(output_path):
    os.mkdir(output_path)

# Loop though all streamer data and generate banners with unique file names
for i in range(len(streamer_names)):
    # Generate transparent background (1920x1080 px)
    img = Image.new('RGBA', (1920, 1080))

    # Make image editable
    draw = ImageDraw.Draw(img)

    platform_index = platform_names.index(streamer_platforms[i])

    logo_path = os.path.join(os.path.abspath(os.curdir), platform_logos[platform_index])
    logo = Image.open(logo_path)

    # Scale logo to 100x100 px
    logo = logo.resize((100, 100))

    # Add the logo and background box to the main image
    img.paste(logo, (150, 50))
    img.paste(box, (250, 50))

    streamer_name = streamer_names[i]

    # Set the font size to 40 and put the streamer's name onto the main image
    draw.font = ImageFont.truetype(font_path, 40)
    draw.text((280, 55), streamer_name)

    streamer_link = platform_links[platform_index] + streamer_links[i]
    platform_color = platform_colors[platform_index]

    # Set the font size to 20 and combine the
    draw.font = ImageFont.truetype(font_path, 20)
    draw.text((280, 110), streamer_link.upper(), platform_color)

    # Save the overlay with the streamer's name as a unique file
    img.save(output_path + f'/{streamer_name}.png')

