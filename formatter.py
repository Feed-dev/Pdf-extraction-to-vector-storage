input_text = """
Order of the Cubic Stone
Alignment: Hermetic Order Golden Dawn tradition, Enochian magic, ceremonial magic, occultism
Goal: train students ceremonial magic, attain spiritual unity, amplify virtues associated Tarot
Purpose: provide magical training, guide spiritual attainment, indicate the Path of Attainment
Tradition: founded 1930s Britain, Theodore Howard, David Edwards, Robert Turner, The Monolith magazine
Practices: Enochian magic system, ceremonial magic training, meditation Tarot images, practical occult work
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
