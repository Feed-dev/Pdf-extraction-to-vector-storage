input_text = """
Ordo Templi Orientis
Alignment: Thelema, Ordo Templi Orientis, ceremonial magick, Western esotericism, Qabalah, Tarot
Goal: spiritual enlightenment, self-discovery, understanding True Will, sharing esoteric knowledge
Purpose: educate others on magick and mysticism, demystify complex concepts, encourage personal exploration
Tradition: Aleister Crowley's teachings, Hermetic Order of the Golden Dawn, Rosicrucianism, Freemasonry
Practices: ritual magick, Gnostic Mass, meditation, divination, writing, lecturing, teaching
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
