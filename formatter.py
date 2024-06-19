input_text = """
divination
alignment: intuitive, interpretive, metaphysical, spiritual, traditional, cross-cultural
goal: discern hidden information, foretell future events, gain insight into problems, discover divine will, remove troubles
purpose: self-reflection, guidance, clarification, connection to higher power, healing social rifts, worldmaking
tradition: ancient, widespread, diverse forms across cultures and religions, sometimes tied to cosmology and theology
practices: cartomancy (tarot, oracle cards), casting (runes, I Ching, bones), psychometry, automatic writing, bibliomancy, palmistry, pendulums, scrying, tea leaf reading
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
