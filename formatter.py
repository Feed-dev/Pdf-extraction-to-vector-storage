input_text = """
Psychedelics
Alignment: consciousness expansion, mystical experiences, spiritual growth, psychological healing, mind-body connection
Goal: self-discovery, personal transformation, overcoming mental health issues, enhancing well-being, fostering connection
Purpose: catalyze profound insights, treat depression and addiction, provide new perspectives, support psychotherapy
Tradition: indigenous rituals, shamanic healing, countercultural exploration, underground therapy, clinical research
Practices: ceremonial use, self-care, integration practices, therapeutic sessions, recreational use
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
