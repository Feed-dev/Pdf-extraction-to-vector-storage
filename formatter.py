input_text = """
Discordian
Alignment: chaos, disorder, strife, individualism, anti-dogmatism, absurdism, surrealism
Goal: embrace chaos, question reality, challenge authority, promote creativity, seek personal liberation
Purpose: venerate Eris (goddess of discord), balance order/disorder, satirize organized religion, encourage free thought
Tradition: founded 1963, Principia Discordia holy book, Malaclypse the Younger and Omar Khayyam Ravenhurst, counterculture
Practices: irreverent rituals, pope cards, chaos magic, initiation rites, Discordian calendar, joke religion/parody religion
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
