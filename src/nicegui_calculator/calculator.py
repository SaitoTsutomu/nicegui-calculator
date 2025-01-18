import re


class Calculator:
    """電卓"""

    def __init__(self):
        self.value = "0"

    def act(self, e):
        """ボタン押下"""
        match e.sender.text if hasattr(e, "sender") else e:
            case num if "0" <= num <= "9":
                value = self.value
                terms = value.split()
                if terms[-1] in {"0", "-0"}:
                    value = value[:-1]
                elif terms[-1] in "/*-+=":
                    value += " "
                self.value = value + num
            case ".":
                if "." not in self.value:
                    self.value += "."
            case "AC":
                self.value = "0"
            case "+/-":
                terms = self.value.split()
                if float(terms[-1]):
                    if terms[-1].startswith("-"):
                        terms[-1] = terms[-1][1:]
                    else:
                        terms[-1] = "-" + terms[-1]
                    self.value = " ".join(terms)
            case "%":
                self.value = str(float(self.value) / 100)
            case operand if operand in "/*-+=":
                value = self.trim_operand(self.value)
                value = str(eval(value)) if operand == "=" else value + " " + operand  # noqa: S307
                self.value = value.removesuffix(".0")

    @classmethod
    def trim_operand(cls, value: str):
        """末尾の演算子削除"""
        return re.sub(r" [/*\-+]$", "", value)

    @classmethod
    def calc(cls, keys: list[str]) -> str:
        """一連の計算"""
        self = cls()
        for key in keys:
            self.act(key)
        return self.value
