input_text = """
egyptian
alignment: polytheistic religion, divine kingship, hierarchical society, cult-like priesthood, communal traditions
goal: maintain secular cosmological order, divine right pharaoh, gods favor
purpose: celebrate worship gods, honor king departed loved ones, ritual celebration
tradition: ancient festivals Opet Heb-Sed, visiting tombs, temples
practices: religious rituals, singing,  pyramid building architectural
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
