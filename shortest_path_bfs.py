graph = {
    'GHY': [['KOL',2000], ['BANG',10000], ['HYD',4000]],
    'KOL': [['BANG',7000], ['HYD',3000]],
    'HYD': [['BANG',2000]],
    'BANG': []
}

visited = []
queue = []
mindist = float('inf')
#INT_MAX  float(-inf)

def shortest_path(first, last, mindist, midRoute):
    #visited.append(first)
    # neighbours 
    queue.append([[first],0])
    while queue:
        s=queue.pop(0)
        #[ [[GHY,HYD],6000] ,
        #whatever is popped is it the dest
        if(s[0][len(s[0])-1]==last):
            if s[1]<mindist:
                mindist=s[1]
                midRoute = s[0]
        for i in graph[s[0][len(s[0])-1]]:
            c = []
            c.extend(s[0])
            c.append(i[0])
            queue.append([ c , s[1]+i[1] ])
            # [[HYD,BANG], 6000][[GHY,KOL,HYD, BANG], 7000]
            
    return [mindist,midRoute]

print(shortest_path('GHY', 'BANG', mindist,[]))
