input_text = """
tantra
alignment: spiritual, philosophical, esoteric, holistic, integrative
goal: spiritual enlightenment, self-realization, union with the divine, harmonizing body/mind/spirit, embracing fullness of life
purpose: transform consciousness, awaken divine potential, integrate spirituality and sensuality, cultivate presence and mindfulness, empower the individual
tradition: ancient Indian and Tibetan origins, influenced Hinduism and Buddhism, Shakta Tantra, Kaula Tantra, Vajrayana, Neotantra in the West
practices: meditation, breathwork, yoga, mantras, yantras, deity worship, ritual, energy work, sacred sexuality, guru-disciple relationship
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
