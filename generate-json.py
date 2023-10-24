"""
Generar autograding.json para ejercicio de verificar contraseña.
"""

import json
import random

FILENAME = ".github/classroom/autograding.json"
PROG_FILE = "contrasena.py"

cases = [
    ["2021", False],
    ["AnsiEdad99", True],
    ["abcdefghijk", False],
    ["abcdEfghiJk", True],
    ["0abcdEEfghijk", False],
    ["1AbcAefghijk", False],
    ["3abcdefghijk", False],
    ["5abcdefGijK", False],
    ["9abcdEFhijk", False],
    ["7abCDefghijk", False],
    ["A1$Ea_aaA", False],
    ["_$0=R/#&(W", True],
]

output = {}
tests = []

for i, case in enumerate(cases, start=1):
    inp, outp = case
    if outp:
        outp = "^(?=.*(sí|si) )(?!.*no ).*"
    else:
        outp = "^(?!.*(sí|si) )(?=.*no ).*"
    name = f"Test{i:02d}: {inp}"
    entry = {
        "name": name,
        "setup": "",
        "run": "LANG=en_US.utf8 timeout 1m python3 " + PROG_FILE,
        "input": inp,
        "output": outp,
        "comparison": "regex",
        "timeout": 1,
        "points": 1
        }
    tests.append(entry)
tests = {"tests": tests}

with open(FILENAME, "w") as f:
    json.dump(tests, f, indent=2)
