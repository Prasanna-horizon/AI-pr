g = {
'A':[('B',6),('F',13)],
'B':[('C',3),('D',2)],
'C':[('D',1)],
'D':[('E',8)],
'E':[('J',5),('I',5)],
'F':[('G',1),('H',7)],
'G':[('I',3)],
'H':[('I',2)],
'I':[('J',3),('E',5)],
'J':[]
}

h = {'A':10,'B':8,'C':5,'D':7,'E':3,'F':6,'G':5,'H':3,'I':1,'J':0}
start = 'A'
goal = 'J'

open = [start]
g_cost = {start:0}
parent = {start:start}

while open:

    n = open[0]
    for v in open:
        if g_cost[v] + h[v] < g_cost[n] + h[n]:
            n = v

    if n == goal:
        path = []
        while parent[n] != n:
            path.append(n)
            n = parent[n]
        path.append(start)
        path.reverse()

        print("->".join(path), "=", g_cost[goal])
        break
    open.remove(n)

    for (m,cost) in g[n]:
        new_cost = g_cost[n] + cost

        if m not in g_cost or new_cost < g_cost[m]:
            g_cost[m] = new_cost
            parent[m] = n
            open.append(m)
