input_text = """
Alchemy
Alignment: speculative thought, astrology, cosmology, natural philosophy, esotericism, occultism
Goal: transmute base metals into gold/silver, discover elixir of life, uncover relationship of man to cosmos
Purpose: exploit cosmic influences for human benefit, attain knowledge and perfection, achieve spiritual enlightenment
Tradition: ancient origins, Hellenistic Egypt, Islamic world, medieval Europe, Renaissance Hermeticism, early modern period
Practices: transmutation, distillation, calcination, sublimation, dissolution, coagulation, fermentation, symbolic interpretation, experimentation
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
