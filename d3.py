import yaml
with open("d3input.yaml") as f:
    docs = yaml.load(f, Loader=yaml.FullLoader)
numbers = docs['numbers']
print(numbers)
posx = 0
posy = 0
trees = 0
for x in range(162):
    posx = (x*1) % 31
    posy = x*2
    # print(posx)
    # print(posy)
    point = numbers[posy][posx]
    print(point)
    if point == "#":
        trees = trees+1

print(trees)