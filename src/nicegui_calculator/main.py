from nicegui import ui

from .calculator import Calculator


def main():
    calculator = Calculator()
    ui.button.default_classes("rounded-full w-14 text-white")
    c_main, c_top, c_right = "bg-grey-8", "bg-blue-2 text-black", "bg-orange-5"
    rows = [
        [("AC", c_top), ("+/-", c_top), ("%", c_top), ("/", c_right)],
        [("7", c_main), ("8", c_main), ("9", c_main), ("*", c_right)],
        [("4", c_main), ("5", c_main), ("6", c_main), ("-", c_right)],
        [("1", c_main), ("2", c_main), ("3", c_main), ("+", c_right)],
        [("0", c_main + " w-32"), (".", c_main), ("=", c_right)],
    ]
    with ui.card().classes("rounded-2xl bg-black"):
        label = ui.label().classes("text-xl w-full text-right text-white")
        label.bind_text(calculator, "value")
        for row in rows:
            with ui.row():
                for text, class_ in row:
                    ui.button(text, on_click=calculator.act).classes(class_)
    ui.run(title="Calculator", reload=False, native=True, window_size=(360, 380), show_welcome_message=False)
