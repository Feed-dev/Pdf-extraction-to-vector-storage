input_text = """
shamanism
alignment: spiritual, nature-based, animistic, eclectic, individualistic yet community-oriented
goal: restore harmony and balance, facilitate healing, gain wisdom and guidance from spirit world, empower individuals
purpose: maintain health and wellbeing of community, bridge material and spiritual realms, preserve ancient wisdom, promote personal growth and transformation
tradition: ancient, cross-cultural, tied to indigenous worldviews, passed through lineages and apprenticeships, adaptable
practices: journeying/trancing to spirit realms, rituals, power animal retrieval, soul retrieval, energy clearing, divination, use of drums and other sacred objects, herbalism, healing ceremonies
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
