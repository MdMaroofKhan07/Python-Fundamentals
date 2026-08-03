# WAF to print the elements of a list in a single line.( list is the parameter )
cities = [ "Delhi","Mumbai","Ghazipur","Aligarh" ]
heroes = [ "Thor","Iron Man","Superhero" ]

def print_list(list):
    for item in list:
        print( item,end=" ")

print_list(cities)
print_list(heroes)