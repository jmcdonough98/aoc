import string
import networkx as nx

def getAvailableTasks():
    tmp = ""
    for n in G.nodes():
        if len(G.pred[n]) == 0:
            tmp += str(n)
    tmp = ''.join(sorted(tmp))
    return tmp
def taskTime(c):
    return string.ascii_uppercase.index(c) + timeOffest + 1
text = open('input.txt','r').read().splitlines()

deps = []
orders = ""

numWorkers = 5
timeOffest = 60
workers = [('',-1)]*numWorkers
G = nx.DiGraph()
for o in text:
    a = o.split('tep ')
    deps.append((a[1][0],a[2][0]))
G.add_edges_from(deps)

nodeOrder = ""
t=0
takenTasks = []

while G.order() > 0:
    for j,w in enumerate(workers):
        if w[1] == t:
            nodeOrder += w[0] #concat finished task
            G.remove_node(w[0]) #free up new tasks
            workers[j] =('',-1) #reset worker
    tasks = getAvailableTasks()
    for k in tasks:
        if k in takenTasks:
            tasks = tasks.replace(k,"")
    for j,w in enumerate(workers):
        if w[0] == '' and len(tasks) > 0 and tasks[0] not in takenTasks: 
            workers[j] = (tasks[0],t + taskTime(tasks[0]))
            takenTasks.append(tasks[0])
            tasks = tasks[1:]  
    t+= 1
print nodeOrder,t - 1