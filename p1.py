from nicegui import ui

#the hashing code

def hashCode(hashString):
    h = 0x9E3779B1
    length_of_input = len(hashString)
    for c in hashString:
        h = h ^ ord(c)
        h = h * 0x517CC1C7
        h = h & 0xFFFFFFFF
        h = h ^ length_of_input
    return int(h)

#the method I used spawned the hashes in a list on the webside
#so this is to improve said list.

currentHash = 0
def hashRun(enterStringHere):
    global currentHash
    currentHash = currentHash + 1
    return f"Hash {currentHash}: {hashCode(enterStringHere)}"

# the ui setup

ui.label("Welcome to Hash Help!").style("color: #00FFFF; font-size: 45px")
with ui.card():
    input_string = ui.input(label="Hash", placeholder="Enter string to hash here").style("min-width: 200px")
    ui.button('Find Hash', on_click=lambda: ui.label(hashRun(input_string.value.strip())))

ui.run(title="Hash Help")