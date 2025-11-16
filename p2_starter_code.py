from nicegui import ui
from random import shuffle

# TODO 1: Create list of 8 unique emojis, duplicate, and shuffle
IDKCARD = "❓"
EMOJIS = ["💃", "🍕", "🛺", "🎈", "🧧", "🎫", "📺", "🍌"]  # ← Your task
buttons = []
opened = []    # indices of currently flipped cards
matched = []   # indices of solved cards
currentSet = []

#the setup (duplication and shuffling)
def startGame():
    global buttons
    global opened
    global matched
    buttons.clear()
    opened.clear()
    matched.clear()
    for x in EMOJIS:
        buttons.append(x)
        buttons.append(x)
    #shuffle go here
    shuffle(buttons)
    print(buttons)
    startbutton.set_text("Restart!") #used as the end of the function

# TODO 2: Write function to flip non-matching cards back
def reset_pair():
    global opened
    for x in opened:
        gamebtns[opened[x]].set_text(IDKCARD)

# TODO 3: Write click handler
def handle_click(idx):
    global opened
    if not(idx in (matched or opened)):
        opened.append(idx)
        numIndex = idx[2:]
        gamebtns[idx].set_text(buttons[int(numIndex)])
        currentSet.append(buttons[int(numIndex)])
    if len(opened) == 2:
        if currentSet[0] == currentSet[1]:
            for x in opened:
                matched.append(opened[x])
        else:
            ui.timer(0.5, lambda: reset_pair(), once=True)
        opened.clear()

#set up the ui
ui.label("Press the button below to start the game!")
startbutton = ui.button("Start!", on_click=lambda: startGame())
# Build 4x4 grid
with ui.grid(columns=4):
    # TODO 4: Create 16 buttons
    gamebtns = {
        'id1': ui.button(IDKCARD, on_click=lambda: handle_click('id1')),
        'id2': ui.button(IDKCARD, on_click=lambda: handle_click('id2')),
        'id3': ui.button(IDKCARD, on_click=lambda: handle_click('id3')),
        'id4': ui.button(IDKCARD, on_click=lambda: handle_click('id4')),
        'id5': ui.button(IDKCARD, on_click=lambda: handle_click('id5')),
        'id6': ui.button(IDKCARD, on_click=lambda: handle_click('id6')),
        'id7': ui.button(IDKCARD, on_click=lambda: handle_click('id7')),
        'id8': ui.button(IDKCARD, on_click=lambda: handle_click('id8')),
        'id9': ui.button(IDKCARD, on_click=lambda: handle_click('id9')),
        'id10': ui.button(IDKCARD, on_click=lambda: handle_click('id10')),
        'id11': ui.button(IDKCARD, on_click=lambda: handle_click('id11')),
        'id12': ui.button(IDKCARD, on_click=lambda: handle_click('id12')),
        'id13': ui.button(IDKCARD, on_click=lambda: handle_click('id13')),
        'id14': ui.button(IDKCARD, on_click=lambda: handle_click('id14')),
        'id15': ui.button(IDKCARD, on_click=lambda: handle_click('id15')),
        'id16': ui.button(IDKCARD, on_click=lambda: handle_click('id16'))
    }
    pass

ui.run(title='Memory Game')