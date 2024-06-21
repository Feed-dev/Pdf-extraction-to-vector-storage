input_text = """
gnostics
alignment: dualistic, spiritual over material, anti-cosmic, esoteric, individualistic
goal: attain gnosis (divine knowledge), awaken divine spark within, escape material realm, reunite with true God in Pleroma, achieve spiritual enlightenment and salvation
purpose: reveal hidden truth, provide path to transcend ignorance and suffering of material existence, preserve and transmit secret wisdom, enable spiritual transformation and liberation
tradition: syncretic, influenced by Platonism, Hermeticism, Neoplatonism, Orphism, Pythagoreanism, early Christianity, Jewish and Hellenistic mysticism, Persian and Babylonian religions
practices: initiation rituals, meditation, prayer, asceticism, theurgy, magic, channeling, study of esoteric texts (e.g. Nag Hammadi library), allegorical interpretation of myths and scriptures, cultivation of mystical experiences
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
