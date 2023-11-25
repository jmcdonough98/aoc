from collections import defaultdict

def parseFoods(foodList):
    allergens = defaultdict(set)
    ingredients = defaultdict(set)

    for i,food in enumerate(foodList):
        ings,allers = food.split(' (contains ')
        ings = ings.split(' ')
        allers = allers[:-1].split(', ')
        for ing in ings:
            ingredients[ing].add(i)
        for aller in allers:
            allergens[aller].add(i)
    return ingredients, allergens

def part1(ingredients, allergens):
    count = 0
    safe = set()
    for ing in ingredients:
        flag = True
        for aller in allergens:
            if allergens[aller].issubset(ingredients[ing]):
                flag = False
                break
        if flag:
            count += len(ingredients[ing])
            safe.add(ing)
    for s in safe:
        ingredients.pop(s)
    return count, ingredients,allergens
def part2(ingredients, allergens):
    pairs = []
    matrix = []
    a = list(sorted(ingredients.keys()))
    b = list(sorted(allergens.keys()))
    for i in range(len(a)):
        tmp2 = []
        for j in range(len(b)):
            tmp2.append(int(ingredients[a[i]].issuperset( allergens[b[j]])))
        matrix.append(tmp2)
    while sum(map(sum,matrix)) > 0:
        for i,row in enumerate(matrix):
            if sum(row) == 1:
                col = row.index(1)
                pairs.append((a[i],b[col]))
                for j in range(len(matrix)):
                    matrix[j][col] = 0

    return "".join([x[0] +',' for x in sorted(pairs,key = lambda x: x[1])])[:-1]

if __name__ == "__main__":
    foodList = open('input.txt','r').read().split('\n')
    ingredients, allergens = parseFoods(foodList)
    p1c, ingredients, allergens = part1(ingredients,allergens)
    p2 = part2(ingredients,allergens)
    print("Part1: {} Part 2: {} ".format(p1c,p2))