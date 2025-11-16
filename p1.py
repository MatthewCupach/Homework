from nicegui import ui

def hashCode(hashString):
    h = 0x9E3779B1
    length_of_input = len(hashString)
    for c in hashString:
        h = h ^ ord(c)
        h = h * 0x517CC1C7
        h = h & 0xFFFFFFFF
        h = h ^ length_of_input
    return int(h)

def greet(mes):
    msg = f"Hello, stranger! " + mes
    ui.notify(msg) # Create a popup

ui.label("Welcome to Hash Help!").style("color: #00FFFF; font-size: 45px")
with ui.card():
    input_string
    ui.button('Find Hash', on_click=lambda: greet(input_string))

ui.run(title="Hash Help")