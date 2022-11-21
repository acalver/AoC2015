f = open('data/Day7.txt', 'r')
wires = f.read()
f.close()

#wires = '123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> h\nNOT y -> i'


import pandas  as pd

wires = pd.DataFrame(wires.split('\n'), columns=['aoc'])
wires['op'] = wires.aoc.str.extract(r'([A-Z]+)')
wires = wires.fillna(value='ASSIGN')

wires['input1'] = wires.aoc.str.extract(r'^([a-z0-9]+) ')
wires['input2'] = wires.aoc.str.extract(r'[A-Z]+ ([a-z]+) ->')
wires['shift_value'] = wires.aoc.str.extract(r'([0-9]+)')
wires['output'] = wires.aoc.str.extract(r'-> (.*)')


wires['assign_only'] = wires.aoc.str.extract(r'(.*) ->')

def operation(ins):
    
    op = ins['op']
    
    if str(ins['input1']).isnumeric():
        ins['input1'] = int(ins['input1'])
        
    if str(ins['input2']).isnumeric():
        ins['input2'] = int(ins['input2'])
    
    if op == 'ASSIGN':
        
        d[ins['output']] = ins['input1']
        
    elif op == 'AND':
        
        d[ins['output']] = d[ins['input1']] & d[ins['input2']]
    
    elif op == 'OR':
        
        d[ins['output']] = d[ins['input1']] | d[ins['input2']]
        
    elif op == 'LSHIFT':
        
        d[ins['output']] = d[ins['input1']] << int(ins['shift_value'])
    
    elif op == 'RSHIFT':
        
        d[ins['output']] = d[ins['input1']] >> int(ins['shift_value'])
    
    elif op == 'NOT':
        
        d[ins['output']] = ~d[ins['input2']] + 65536

d = dict()

for i in range(len(wires)):

    instruction = wires.iloc[i]
    task = instruction['op']
    
    line_inputs = [str(instruction['input1']), str(instruction['input2'])]
    
    if str(instruction['input1']).isnumeric():
        line_inputs.remove(str(instruction['input1']))
    if str(instruction['input2']).isnumeric():
        line_inputs.remove(str(instruction['input2']))
    if  'nan'  in line_inputs:
        line_inputs.remove('nan')
    
    if all(x in d.keys() for x in line_inputs):
    
        operation(instruction)

    elif task == 'ASSIGN':
        
        if instruction['input1'].isnumeric():
            d[instruction['output']] = int(instruction['input1'])
            
        elif instruction['input1'] in d.keys():
            d[instruction['output']] = d[instruction['input1']]
