testing = False

import shared
import re

def parse_text(text):
    if testing:
        print(f"-- Parsing Input --")
    all_allergens = dict()
    for line in text.splitlines():
        matches = re.findall(r'([a-z ]+)( \(contains )([a-z, ]+)(\))', line)
        ingredients = set(matches[0][0].split())
        if testing:
            print(f"match ingredients: {ingredients}")
        allergens = matches[0][2].split(', ')
        if testing:
            print(f"match allergens: {allergens}")
        for allergen in allergens:
            if allergen not in all_allergens:
                if testing:
                    print(f"new allergen found: {allergen}")
                all_allergens[allergen] = ingredients
                if testing:
                    print(f"added {ingredients} to new {allergen}")
            else:
                if testing:
                    print(f"processing existing allergen {allergen} that has ingredients {all_allergens[allergen]}")
                all_allergens[allergen] = all_allergens[allergen].intersection(ingredients)
                if testing:
                    print(f"intersected {ingredients} with existing {allergen} that now has ingredients {all_allergens[allergen]}")
    return all_allergens

def translate_allergens(allergens):
    processed_allergens = dict()
    todo = allergens.copy()
    while todo:
        if testing:
            print(f"-- Processing Allergens --")
        for allergen in todo:
            if testing:
                print(f"{allergen} has {len(allergens[allergen])} possible ingredients: {allergens[allergen]}")
            if len(allergens[allergen]) == 1:
                mask = allergens[allergen].pop()
                if testing:
                    print(f"{allergen} has only 1 ingredient: {mask}")
                processed_allergens[allergen] = mask
                del allergens[allergen]
                if testing:
                    print(f"moved {allergen} to processing. allergens is now {allergens}. processed is now {processed_allergens}")
                for a in allergens:
                    allergens[a].discard(mask)
                    if testing:
                        print(f"removed {mask} from {a}")
                        print(f"{a} now has the ingredients: {allergens[a]}")
        todo = allergens.copy()
    if testing:
        print(f"translated allergens: {processed_allergens}")
    return processed_allergens

def count_safe_ingredients(text, allergens):
    count = 0
    if testing:
        print(f"-- Counting Safe Ingredients --")
    for line in text.splitlines():
        matches = re.findall(r'([a-z ]+)( \(contains )([a-z, ]+)(\))', line)
        ingredients = matches[0][0].split()
        if testing:
            print(f"match ingredients: {ingredients}")
        for ingredient in ingredients:
            if ingredient not in allergens.values():
                if testing:
                    print(f"{ingredient} is a safe ingredient")
                count += 1
    return count

def canonical_ingredients(allergens):
    if testing:
        print(f"-- Compiling caonical dangerous ingredient list --")
    dangerous = list(allergens.keys())
    dangerous.sort()
    for a in dangerous:
        if testing:
            print(f"appending dangerous ingredient {a} -> {allergens[a]}")
    canonical_dangerous = [allergens[a] for a in dangerous]
    return ','.join(canonical_dangerous)

# import text from file
if testing:
    text = shared.read_input("input_test")
    #text = shared.read_input("input")
    print(text)
else:
    text = shared.read_input("input")

# Part 1
allergens = translate_allergens(parse_text(text))
part1 = count_safe_ingredients(text, allergens)
print(f"[Part 1] {part1}")

# Part 2
part2 = canonical_ingredients(allergens)
print(f"[Part 2] {part2}")

# Display the time this took to run
shared.printTimeElapsed()
