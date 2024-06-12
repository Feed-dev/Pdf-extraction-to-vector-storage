input_text = """
parapsychology
Alignment: anomalous experiences, psi phenomena, consciousness studies, scientific investigation, interdisciplinary approach
Goal: understand the nature of consciousness, explore the limits of human potential, investigate unexplained phenomena
Purpose: conduct research on psi abilities, challenge materialist paradigms, expand scientific understanding of the mind
Tradition: Society for Psychical Research, J.B. Rhine and experimental parapsychology, survival research, skeptic/proponent dialogue
Practices: controlled experiments, case studies, field investigations, statistical analysis, theoretical development, peer-reviewed publications
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
