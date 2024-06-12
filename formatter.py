input_text = """
Shamanism
Alignment: animism, spirit world, altered states of consciousness, indigenous cultures, nature-based spirituality
Goal: communicate with spirits, heal the sick, restore balance and harmony, guide souls to the afterlife
Purpose: mediate between physical and spiritual realms, maintain well-being of individuals and community
Tradition: ancient practices, passed down through generations, culture-specific, often involving initiation and mentorship
Practices: trance states, drumming, chanting, spirit communication, healing rituals, soul retrieval, divination, use of sacred objects
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
