import yaml
with open("d1input.yaml") as f:
    docs = yaml.load(f, Loader=yaml.FullLoader)

numbers = docs['numbers']
print(numbers)
for no1 in numbers:
    for no2 in numbers:
        for no3 in numbers:

            if no1 == no2:
                continue
            if no1 == no3:
                continue
            if no2 == no3:
                continue
            # print(f" testing no1 is {no1} no2 is {no2}")
            product = no1+no2+no3
            if product == 2020:
                factor = no1*no2*no3
                print(f" no1 is {no1} no2 is {no2} and factor is {factor}")