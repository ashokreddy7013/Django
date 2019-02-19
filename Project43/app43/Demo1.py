

from django.core.paginator import Paginator

names = ["Ravi","kumar","Krishna","Mohan","Rama","Prasad","Murali"]

p = Paginator(names,2)

print(p.count)
print(p.num_pages)
print("======================")
p1 = p.page(1)
print(p1)
print(p1.object_list)
print("======================")
p2 = p.page(2)
print(p2)
print(p2.object_list)
print("======================")
for x in range(p.num_pages):
    y = p.page(x+1)
    print(y)
    print(y.object_list)
print("============================")


