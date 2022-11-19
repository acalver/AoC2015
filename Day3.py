f = open('data/Day3.txt', 'r')
route = f.read()
f.close()

#route = '^v^v^v^v^v'

x_coord = 0
y_coord = 0

previous_houses = {(0,0)}

for d in route:
    if d == '<':
        x_coord -= 1
        
    if d == '>':
        x_coord += 1
    
    if d == '^':
        y_coord += 1
        
    if d == 'v':
        y_coord -= 1
        
    position = (x_coord, y_coord)
    
    previous_houses.add(position)

print(len(previous_houses))
        
#%% Part 2

x_coord_Santa = 0
y_coord_Santa = 0

x_coord_robo = 0
y_coord_robo = 0

previous_houses = {(0,0)}
instruction = 1
for d in route:
    
    #Santa
    if  instruction % 2 == 1:
        
        if d == '<':
            x_coord_Santa -= 1
            
        if d == '>':
            x_coord_Santa += 1
        
        if d == '^':
            y_coord_Santa += 1
            
        if d == 'v':
            y_coord_Santa -= 1
            
        position = (x_coord_Santa, y_coord_Santa)
        
        previous_houses.add(position)
        
    #robo santa
    else:
         
         if d == '<':
             x_coord_robo -= 1
             
         if d == '>':
             x_coord_robo += 1
         
         if d == '^':
             y_coord_robo += 1
             
         if d == 'v':
             y_coord_robo -= 1
             
         position = (x_coord_robo, y_coord_robo)
        
         previous_houses.add(position)
        
    instruction += 1

print(len(previous_houses))