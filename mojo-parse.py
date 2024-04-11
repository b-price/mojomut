import os
import random
import re
import subprocess
import argparse

BINARY_OPERATORS = ('+', '-', '*', '/', '%')


def find_op_position(line):
    numbers = re.findall(r'\d+', line)
    op_position = [int(num) for num in numbers][-2:]
    op_position[1] = op_position[1] - 3
    return op_position


parser = argparse.ArgumentParser(description='mojo-parse')
parser.add_argument('filepath', help='mojo file to parse')
filepath = parser.parse_args().filepath
os.makedirs('mutants', exist_ok=True)

result = subprocess.run(["npx", "tree-sitter", "parse", filepath], stdout=subprocess.PIPE)
string_out = result.stdout.decode("utf-8")

mutant = "binary_operator"

arithmetic_operators = [line for line in string_out.splitlines() if mutant in line]

op_positions = [find_op_position(line) for line in arithmetic_operators]
mutant_ops = []

for op_position in op_positions:
    mutant_ops.append(random.choice(BINARY_OPERATORS))

print(op_positions)

with open(filepath, 'r') as file:
    original = file.readlines()

mutated = original
print(mutated)

for idx, pos in enumerate(op_positions):
    mutated_line = mutated[pos[0]]
    while mutated_line[pos[1]] not in BINARY_OPERATORS:
        pos[1] -= 1
        if pos[1] < 0:
            break

    mutated_line = mutated_line[:pos[1]] + mutant_ops[idx] + mutated_line[pos[1] + 1:]
    mutated[pos[0]] = mutated_line
    with open('mutants/mutant_' + str(idx) + '.mojo', 'w') as file:
        file.writelines(mutated)
    mutated[pos[0]] = original[pos[0]]

print(mutated)
