input_text = """
hermeticism
alignment: philosophical, spiritual, esoteric, syncretic, individualistic
goal: attain gnosis (divine knowledge), live in harmony with universal laws, achieve spiritual enlightenment and liberation, transmute lower nature into higher self
purpose: understand and apply principles governing universe, discover inner divine nature, transform consciousness, contribute to collective awakening
tradition: ancient Egyptian and Greek roots, influenced by Platonism, Gnosticism, Neoplatonism, Kabbalah, alchemy, ritual magic
practices: study of Hermetic texts (e.g. Corpus Hermeticum, Emerald Tablet), meditation, contemplation, ritual, alchemy, astrology, theurgy, talismanic magic
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
