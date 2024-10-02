import re


class Calculator:
    def __init__(self):
        self.value = "0"
        self.clear_at_next = False

    def act(self, e):
        value = "0" if self.clear_at_next else self.value
        self.clear_at_next = False
        match e.sender.text if hasattr(e, "sender") else e:
            case num if "0" <= num <= "9":
                terms = value.split()
                if terms[-1] in {"0", "-0"}:
                    value = value[:-1]
                elif terms[-1] in "/*-+=":
                    value += " "
                self.value = value + num
            case ".":
                if "." not in value:
                    self.value = value + "."
            case "AC":
                self.value = "0"
            case "+/-":
                terms = value.split()
                if float(terms[-1]):
                    if terms[-1].startswith("-"):
                        terms[-1] = terms[-1][1:]
                    else:
                        terms[-1] = "-" + terms[-1]
                    self.value = " ".join(terms)
            case "%":
                self.value = str(float(value) / 100)
            case operand if operand in "/*-+=":
                value = self.trim_operand(value)
                if operand == "=":
                    self.value = str(eval(value))
                    self.clear_at_next = True
                else:
                    self.value = value + " " + operand

    @classmethod
    def trim_operand(cls, value: str):
        return re.sub(r" [/*\-+]$", "", value)

    @classmethod
    def calc(cls, keys: list[str]) -> str:
        self = cls()
        for key in keys:
            self.act(key)
        return self.value
