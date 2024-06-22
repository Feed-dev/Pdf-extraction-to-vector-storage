input_text = """
rune magic
alignment: Norse, Germanic, pagan, esoteric, practical
goal: divination, protection, healing, success, influencing fate, connecting with gods and mythic forces
purpose: harness runic energies, manifest intentions, gain wisdom and guidance, spiritual empowerment, preserve cultural heritage
tradition: Viking Age, medieval, Odinic mysticism, contemporary Paganism and Heathenry, revival of ancient practices
practices: carving and inscribing runes, rune casting, bindrunes, talismans and amulets, ritual magic, meditation, shamanic journeying
"""


# Function to format the input text and convert to lowercase
def format_text(input_text):
    lines = input_text.strip().split('\n')
    namespace = lines[0].lower()
    formatted_output = f'namespace = "{namespace}"\n'

    for line in lines[1:]:
        key, value = line.split(': ')
        key = key.strip().lower()
        value = ' '.join(value.lower().split(', ')).strip()
        formatted_output += f'{key} = "{value}"\n'

    return formatted_output


# Get the formatted text
formatted_text = format_text(input_text)
print(formatted_text)
