#practice3, heap
import heapq
h = []

list1 = [4,6,8,1]
heapq.heapify(list1)
print list1

heapq.heappush(h, (1,"food"))
heapq.heappush(h, (2,"have fun"))
heapq.heappush(h, (3,"work"))
heapq.heappush(h, (4, "study"))

heapq.heappop(list1)

print list1
