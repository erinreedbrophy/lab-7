swag = 1
while(swag < 300):
    print swag
    swag = swag + 2
    
swagy = 0
List = [1,2,'this is the third', 4,5,6,7,8,9,10]
while(swagy < len(list)):
    print List[swagy]
    swagy = swagy + 1
    
    
import random
rand = random.randint (0,50)
keepgoing = -1
while(keepgoing != rand):
    print 'guess numbro uno'
    keepgoing = int(raw_input())
    if keepgoing > rand:
        print 'too high stupid'
    if keepgoing < rand:
        print 'too low loser'
    if keepgoing == rand:
        print 'yeah you win what ever'

    
