input_text = """
Sumerian
Alignment: city-states, theocratic government, priest-kings, anthropomorphic polytheistic religion
Goal: maintain order, please the gods, ensure prosperity, expand influence
Purpose: develop agriculture, trade, writing, technology for the betterment of their civilization
Tradition: invented cuneiform writing, math, astronomy, literature like Epic of Gilgamesh, built ziggurats
Practices: religion temples, city-states, kingship priests
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
