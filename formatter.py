input_text = """
rosicrucian
Alignment: Rosicrucian Christianity, Western esotericism, occultism, mysticism, spiritual science
Goal: disseminate Rosicrucian teachings, spiritual enlightenment, self-knowledge, service to humanity
Purpose: establish Rosicrucian Fellowship, present esoteric wisdom in accessible form, promote spiritual healing
Tradition: Christian Rosenkreuz, Rosicrucian manifestos, Rudolf Steiner, Elder Brothers of Rose Cross
Practices: study of Rosicrucian Cosmo-Conception, astrology, spiritual healing, esoteric interpretation of Christianity
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
