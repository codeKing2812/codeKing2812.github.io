

print('hello world')

data = [{'sted':'Bergen', 'år':2024},{'sted':'Oslo', 'år':1952},{'sted':'Trondheim', 'år':2007},{'sted':'Lillehammer', 'år':1994}]



with open('test.csv', 'w+') as fil:

    string = ''
    rad1 = ''
    
    for key in dict[0]:
        rad1 += (str(key) + ',')

    fil.write(rad1 + '\n')

    # for dict in data:
    #     for key in dict:
    #         print(dict[key])
    #         string += (str(dict[key]) + ',')
    #     fil.write(string + '\n ')
            
            