input_text = """
alchemy
Alignment: spagyrics, laboratory alchemy, chemistry, herbalism, spiritual transformation
Goal: create alchemical medicines, understand nature's intelligence, balance science and spirit
Purpose: heal body and soul, reveal esoteric virtues of plants, educate others in the Art
Tradition: classical alchemy, Paracelsian spagyrics, 3 Essentials (Mercury, Sulfur, Salt), 7 planetary archetypes
Practices: calcination, dissolution, separation, conjunction, fermentation, distillation, cohobation, plant work, mineral work
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
