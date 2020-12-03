import yaml
with open("d2input.yaml") as f:
    docs = yaml.load(f, Loader=yaml.FullLoader)

numbers = docs['passwords']
print(numbers)
valid = 0
invalid = 0
for item in numbers:
    rule = list(item.keys())[0]
    ruleno = rule.split(" ")
    letter = ruleno[1]
    ruleno1 = ruleno[0]
    ruleno1 = ruleno1.split("-")
    rulemin = int(ruleno1[0])
    rulemax = int(ruleno1[1])
    password = list(item.values())[0]
    counting = password.count(letter)
    print(counting)
    print(rulemin)
    print(rulemax)
    if bool(password[rulemin-1] == letter) ^ bool(password[rulemax-1] == letter):
        valid = valid+1
    else:
        invalid = invalid+1
    # if password[rulemin] == letter or password[rulemin] == letter:
    #     if counting <=rulemax:
    #         valid = valid+1
    #     else:
    #         invalid = invalid+1
    # else:
    #     invalid = invalid+1


print(valid)
print(invalid)

