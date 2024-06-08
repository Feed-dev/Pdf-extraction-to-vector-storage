input_text = """
Hermes Trismegistus
Alignment: Hellenistic philosophy, Neoplatonism, Gnosticism, Egyptian mysticism, esotericism, occultism
Goal: spiritual enlightenment, self-knowledge, unity with the divine, transmutation, immortality, cosmic understanding
Purpose: attain gnosis, uncover hidden wisdom, harmonize man and cosmos, perfect the soul, achieve salvation
Tradition: Corpus Hermeticum, Asclepius, Emerald Tablet, prisca theologia, perennial philosophy, Renaissance revival
Practices: alchemy, astrology, theurgy, magic, meditation, initiation rites, symbolic interpretation, correspondences
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
