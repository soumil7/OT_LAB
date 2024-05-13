queue = [] 
queue.append('a')
queue.append('b') 
queue.append('c') 
print("Initial queue")
print(queue)
print("\nElements dequeued from queue")
queue.pop(0) 
queue.pop(0) 
print(queue)
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)

from queue import Queue 
q = Queue(maxsize=3) 
q.put('a')
q.put('b') 
q.put('c') 
print(q.qsize()) 
print(q) 
print(q.full()) 
print(q.get())
print(q.get())
print(q.get())
print(q.empty())
print(q.full()) 
print(q) 


from collections import deque 

q = deque() 

q.append('a')
q.append('b')
q.append('c') 

print(q.popleft()) 
print(q.pop())
print(q.popleft()) 

print(q)



