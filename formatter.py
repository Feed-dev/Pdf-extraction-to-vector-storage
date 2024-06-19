input_text = """
biblical
alignment: non-canonical, suppressed, apocryphal, rejected by Nicene Council
goal: provide additional gospels and epistles attributed to Jesus's apostles and disciples
purpose: offer diverse range of early Christian beliefs and perspectives that challenge traditional teachings
tradition: venerated by some early Christian churches in first 4 centuries, later forbidden by Nicene Council in 4th century under Emperor Constantine
practices: translation of original texts from ancient languages, historical authentication of writings, compilation and publication of suppressed works to make them accessible
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
