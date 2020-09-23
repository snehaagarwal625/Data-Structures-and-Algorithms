graph = {
    'GHY': [['KOL',2000], ['BANG',10000], ['HYD',4000]],
    'KOL': [['BANG',7000], ['HYD',3000]],
    'HYD': [['BANG',2000]],
    'BANG': []
}

# GHY-KOL-BANG
# GHY-KOL-HYD-BANG
# GHY-BANG
# GHY-HYD-BANG
queue=[]
all_path=[]
def all_paths(first, last):
    queue.append([[first],0]    )
    while queue:
        s=queue.pop(0)
        print('queue',s)
        # print('last',s[0][len(s[0])-1])
        if(s[0][len(s[0])-1]==last):
            all_path.append(s)
            #print('test',all_path)
        for i in graph[s[0][len(s[0])-1]]:
            c = []
            c.extend(s[0])
            c.append(i[0])
            queue.append([c, i[1]+s[1]])
    return all_path

print('result')
all_path=all_paths('GHY', 'BANG')
for i in all_path:
    print(i)
