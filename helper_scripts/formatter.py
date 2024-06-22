input_text = """
Voudon
alignment: African diaspora religion, syncretic, spiritual, cosmocentric worldview, interconnected realms
goal: connect with spirits (lwa), gain protection and guidance, maintain harmony and balance, heal maladies, manifest desires
purpose: preserve African spiritual heritage, provide framework for mental health and identity, empower individuals and communities, integrate diverse traditions
tradition: West African Vodun, Haitian Vodou, New Orleans Voodoo, influenced by Catholicism and Native American practices, evolving and adaptive
practices: rituals, possession (mounting) by lwa, offerings, divination, herbalism, magic (charms, dolls), ancestor veneration, drumming and dance
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
