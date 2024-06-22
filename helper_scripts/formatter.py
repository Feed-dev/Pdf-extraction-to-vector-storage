input_text = """
psychedelics
alignment: therapeutic, spiritual, indigenous, countercultural, consciousness-expanding
goal: healing trauma and mental health issues, personal growth, spiritual insight, enhanced well-being, cognitive flexibility
purpose: catalyze profound inner experiences, facilitate therapeutic breakthroughs, provide new perspectives, support spiritual development, challenge cultural paradigms
tradition: shamanic and indigenous use, 1960s countercultural movement, underground therapy, clinical research, harm reduction and community support
practices: ceremonial use in indigenous cultures, therapeutic administration with preparation and integration, microdosing, festival and recreational use, meditation and spiritual practices
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
