f = open('data/Day7.txt', 'r')
wires = f.read()
f.close()


import pandas  as pd
import re

wires = pd.DataFrame(wires.split('\n'), columns=['aoc'])
wires['op'] = wires.aoc.str.extract(r'([A-Z]+)')
wires = wires.fillna(value='ASSIGN')

wires['input1'] = wires.aoc.str.extract(r'^([a-z]+) ')
wires['input2'] = wires.aoc.str.extract(r'[A-Z]+ ([a-z]+) ->')
wires['shift_value'] = wires.aoc.str.extract(r'([0-9]+)')
wires['output'] = wires.aoc.str.extract(r'-> (.*)')


wires['assign_only'] = wires.aoc.str.extract(r'(.*) ->')

wires = '123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> h\nNOT y -> i'


d = dict()

op = 'ASSIGN'
if op == 'ASSIGN':
    