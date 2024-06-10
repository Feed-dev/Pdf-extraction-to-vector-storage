input_text = """
Aleister Crowley
Alignment: postmodern, individualistic, pragmatic, eclectic, anti-dogmatic, fluid belief systems
Goal: achieve practical results, manifest desires, personal empowerment, reality manipulation
Purpose: utilize belief as a tool, bypass limitations, explore consciousness, challenge paradigms
Tradition: emerged late 20th century, influenced by Austin Osman Spare, Aleister Crowley, discordianism, postmodernism
Practices: sigil magic, servitors, gnosis, reality shifting, paradigm shifting, personal rituals, psychonautics
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
