
from django.core.paginator import Paginator

names = ["Ravi","kumar","Krishna","Mohan","Rama","Prasad","Murali"]

p = Paginator(names,3)
print(p.num_pages)

p1 = p.page(1)
print(p1)
print(p1.object_list)
print("======================")
print(p1.has_next())
print(p1.has_previous())
print(p1.has_other_pages())
print("======================")
p3 = p.page(3)
print(p3.has_other_pages())
print(p3.has_next())