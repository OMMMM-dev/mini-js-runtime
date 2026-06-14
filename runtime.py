import sys
import quickjs

ctx = quickjs.Context()

logs = []

def console_log(*args):
    logs.append(" ".join(str(arg) for arg in args))

ctx.add_callable("py_log", console_log)

js_prelude = """
const console = {
    log: (...args) => py_log(...args)
};
"""

if len(sys.argv) > 1:
    with open(sys.argv[1], "r") as f:
        js_code = f.read()
else:
    js_code = sys.stdin.read()

ctx.eval(js_prelude + js_code)

for line in logs:
    print(line)