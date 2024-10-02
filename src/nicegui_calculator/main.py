from nicegui import ui

from nicegui_calculator import Calculator

calculator = Calculator()
button_styles = [
    "rounded-full w-14 bg-blue-2 text-black",
    "rounded-full w-14 bg-orange-5 text-white",
    "rounded-full w-14 bg-grey-8",
    "rounded-full w-32 bg-grey-8",
]
rows = [
    [("AC", 0), ("+/-", 0), ("%", 0), ("/", 1)],
    [("7", 2), ("8", 2), ("9", 2), ("*", 1)],
    [("4", 2), ("5", 2), ("6", 2), ("-", 1)],
    [("1", 2), ("2", 2), ("3", 2), ("+", 1)],
    [("0", 3), (".", 2), ("=", 1)],
]
with ui.card().classes("rounded-2xl bg-black"):
    label = ui.label().classes("text-xl w-full text-right text-white")
    label.bind_text(calculator, "value")
    for row in rows:
        with ui.row():
            for text, i in row:
                ui.button(text, on_click=calculator.act).classes(button_styles[i])

ui.run(native=True, window_size=(360, 380))
