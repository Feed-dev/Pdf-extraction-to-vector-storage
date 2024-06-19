input_text = """
chaos magic
alignment: individualistic, eclectic, postmodern, rejects absolute truth and fixed beliefs
goal: achieve practical magical results, alter reality through changing beliefs and paradigms
purpose: strip away dogma and ornamental aspects of occult traditions, focus on core techniques that work
tradition: emerged in 1970s England, influenced by Austin Osman Spare, related to discordianism, key groups include Illuminates of Thanateros and Thee Temple ov Psychick Youth
practices: belief as a tool, shifting paradigms, sigil magic, servitors, gnosis/altered states of consciousness through inhibitory, ecstatic, or indifferent means, borrowing from various traditions
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
