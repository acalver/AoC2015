import pandas as pd
import re
import numpy as np


light_config = pd.read_csv('data/day6.csv', header =  None, names=['x'])

light_config['op'] = light_config.x.str.extract('(?P<op>.+?(?=[0-9]))')
light_config['op'] = light_config['op'].str.strip()
light_config['startPoint'] = [re.findall('\d{1,3},\d{1,3}', s)[0] for s in light_config['x']]
light_config['endPoint'] = [re.findall('\d{1,3},\d{1,3}', s)[1] for s in light_config['x']]

start_coords = light_config['startPoint'].str.split(pat=',', expand=True)
light_config['startPoint.x'] = start_coords[0]
light_config['startPoint.y'] = start_coords[1]

end_coords = light_config['endPoint'].str.split(pat=',', expand=True)
light_config['endPoint.x'] = end_coords[0]
light_config['endPoint.y'] = end_coords[1]


light_config[['startPoint.x', 'startPoint.y', "endPoint.x", "endPoint.y"]] = \
    light_config[['startPoint.x', 'startPoint.y', "endPoint.x", "endPoint.y"]].apply(pd.to_numeric)


light_grid = np.zeros((1000,1000))

def light_task(task, x_coord, y_coord):
    
    if task == 'turn on':
        light_grid[x_coord][y_coord] = 1
        
    elif task == 'turn off':
        light_grid[x_coord][y_coord] = 0
        
    else:
        light_grid[x_coord][y_coord] = (light_grid[x_coord][y_coord] + 1) % 2

x_coord = 0
y_coord = 0
task = 'toggle'

def light_box(x_start, x_stop,y_start,y_stop, to_do):
    
    for x in range(x_start, x_stop + 1):
        
        for y in range (y_start, y_stop+1):
            
            light_task(to_do, x, y)


for n in range(300):
    
    x_start = light_config.iloc[n]['startPoint.x']
    y_start = light_config.iloc[n]['startPoint.y']

    x_stop = light_config.iloc[n]['endPoint.x']
    y_stop = light_config.iloc[n]['endPoint.y']
    
    to_do = light_config.iloc[n]['op']
    
    light_box(x_start, x_stop, y_start, y_stop, to_do)


sum(sum(light_grid))


#%%
def light_task_pt2(task, x_coord, y_coord):
    
    if task == 'turn on':
        light_grid2[x_coord][y_coord] += 1
        
    elif task == 'turn off':
        if light_grid2[x_coord][y_coord] > 0:
            light_grid2[x_coord][y_coord] -= 1
        
    else:
        light_grid2[x_coord][y_coord] += 2
        
def light_box2(x_start, x_stop,y_start,y_stop, to_do):
    
    for x in range(x_start, x_stop + 1):
        
        for y in range (y_start, y_stop+1):
            
            light_task_pt2(to_do, x, y)
        

light_grid2 = np.zeros((1000,1000))

for n in range(300):
    
    x_start = light_config.iloc[n]['startPoint.x']
    y_start = light_config.iloc[n]['startPoint.y']

    x_stop = light_config.iloc[n]['endPoint.x']
    y_stop = light_config.iloc[n]['endPoint.y']
    
    to_do = light_config.iloc[n]['op']
    
    light_box2(x_start, x_stop, y_start, y_stop, to_do)


sum(sum(light_grid2))
