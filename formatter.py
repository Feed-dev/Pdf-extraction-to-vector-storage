input_text = """
Ordo Templi Orientis
Alignment: occultism, Western esotericism, Thelema, Freemasonry, Rosicrucianism, Illuminism
Goal: spiritual enlightenment, self-realization, liberty of the individual, advancement in light/life/love
Purpose: preserve occult knowledge, confer initiations, promulgate Thelema, facilitate personal transformation
Tradition: founded early 20th century, Theodor Reuss, Aleister Crowley, ceremonial magic, fraternal order
Practices: graded initiations, ritual drama, Gnostic Mass, study of Hermetic sciences, yoga, sexual magic
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
