import json


INPUT_FILE = "radio.txt"
OUTPUT_FILE = "radio.json"

lines = []

with open(INPUT_FILE, "r") as infile:
    lines = [line.strip() for line in infile.readlines() if line.strip()]

data = []

for i in range(0, len(lines), 2):
    if lines[i].startswith("#EXTINF"):
        logo_url = lines[i].split('tvg-logo="')[1].split('"')[0]
        radio_name = lines[i].split(",")[-1].removeprefix("Radio_")
        stream_url = lines[i + 1]

        data.append(
            {
                "name": radio_name, 
                "logo": logo_url, 
                "stream": stream_url
            }
        )

for radio in data:
    print(f"Name: {radio['name']}")
    print(f"Logo: {radio['logo']}")
    print(f"Stream: {radio['stream']}")
    print("\n")

with open(OUTPUT_FILE, "w") as outfile:
    json.dump(data, outfile)

print(f"Imported {len(data)} links into '{OUTPUT_FILE}'.")