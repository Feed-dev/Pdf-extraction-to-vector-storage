input_text = """
Aleister Crowley
Alignment: Thelema, Western esotericism, ceremonial magic, occultism, mysticism, individualism
Goal: discover True Will, attain knowledge and conversation of Holy Guardian Angel, spiritual enlightenment, self-deification
Purpose: establish new religious movement, revive magic as spiritual discipline, synthesize Eastern and Western traditions
Tradition: Hermetic Order of the Golden Dawn, Ordo Templi Orientis, A∴A∴, The Book of the Law, Aeon of Horus
Practices: ceremonial rituals, yoga, meditation, sex magic, astrology, Tarot, Qabalah, alchemy, poetry, mountaineering
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
