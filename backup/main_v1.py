import re

class MiniJS:
    def __init__(self):
        self.variables = {}

    def execute(self, code):
        lines = code.split("\n")

        for line in lines:
            line = line.strip()

            if not line:
                continue

            if line.startswith("let "):
                self.handle_let(line)

            elif line.startswith("console.log("):
                self.handle_log(line)

    def handle_let(self, line):
        line = line.replace("let ", "")
        line = line.rstrip(";")

        name, value = line.split("=")

        name = name.strip()
        value = value.strip()

        if value.isdigit():
            value = int(value)

        self.variables[name] = value

    def handle_log(self, line):
        content = re.findall(r"console\.log\((.*)\)", line)[0]

        content = content.strip()

        if "+" in content:
            parts = content.split("+")

            result = ""

            for part in parts:
                part = part.strip()

                if part in self.variables:
                    result += str(self.variables[part])
                else:
                    result += part.strip('"').strip("'")

            print(result)

        elif content in self.variables:
            print(self.variables[content])

        else:
            print(content.strip('"').strip("'"))

code = """
let num = 7;

console.log(num);
console.log("Hello");
console.log(num + " is Odd");
"""

MiniJS().execute(code)