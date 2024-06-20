input_text = """
hermes trismegistus
alignment: syncretistic, philosophical, initiatory, secretive, elite
goal: spiritual enlightenment, union with the divine, attainment of gnosis, immortality of the soul
purpose: preserve ancient wisdom, provide personal transformation and salvation, supplement state religion
tradition: Hermeticism, Gnosticism, Neoplatonism, Orphism, Pythagoreanism, mystery cults (Eleusinian, Dionysian, Mithraic, Isiac)
practices: astrology, magic, alchemy, theurgy, divination, initiation rituals, secrecy, allegorical interpretation of myths
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
