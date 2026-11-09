# Periodic Table Information Finder (non-metals)
from pyscript import display, document

# Python dictionary of non-metal elements
non_metals = {
    'H':  {'name': 'Hydrogen', 'number': 1, 'mass': 1.008},
    'HE': {'name': 'Helium', 'number': 2, 'mass': 4.003},
    'C':  {'name': 'Carbon', 'number': 6, 'mass': 12.01},
    'N':  {'name': 'Nitrogen', 'number': 7, 'mass': 14.01},
    'O':  {'name': 'Oxygen', 'number': 8, 'mass': 16.00},
    'F':  {'name': 'Fluorine', 'number': 9, 'mass': 19.00},
    'NE': {'name': 'Neon', 'number': 10, 'mass': 20.18},
    'P':  {'name': 'Phosphorus', 'number': 15, 'mass': 30.97},
    'S':  {'name': 'Sulfur', 'number': 16, 'mass': 32.06},
    'CL': {'name': 'Chlorine', 'number': 17, 'mass': 35.45},
    'AR': {'name': 'Argon', 'number': 18, 'mass': 39.95},
    'SE': {'name': 'Selenium', 'number': 34, 'mass': 78.96},
    'BR': {'name': 'Bromine', 'number': 35, 'mass': 79.90},
    'KR': {'name': 'Krypton', 'number': 36, 'mass': 83.80},
    'I':  {'name': 'Iodine', 'number': 53, 'mass': 126.90},
    'XE': {'name': 'Xenon', 'number': 54, 'mass': 131.29},
    'RN': {'name': 'Radon', 'number': 86, 'mass': 222},
}

# Function triggered when the button is clicked
def search_element(e):
    # Clearing output box before displaying new result
    document.getElementById('result_display').innerHTML = ''

    # Collecting the input
    symbol_key = document.getElementById('symbol_input').value.strip().upper()

    # Member checking (returns true or false)
    is_in_list = symbol_key in non_metals

    # Retrieving dictionary information
    info = non_metals.get(symbol_key, {'name': 'N/A', 'number': 'N/A', 'mass': 'N/A'})
    formatted_symbol = symbol_key.capitalize()

    # Output of the message
    display_message = (
        f"The element symbol '{symbol_key}' does not exist in the non-metals list.",
        f"<b>Symbol:</b> {formatted_symbol}<br><b>Element:</b> {info['name']}<br><b>Atomic Number:</b> {info['number']}<br><b>Atomic Mass:</b> {info['mass']}"
    )

    # Displaying message
    document.getElementById('result_display').innerHTML = display_message[is_in_list]
