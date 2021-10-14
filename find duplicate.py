# find duplicate number in integer list

def find_duplicates(elements):
    duplicates, seen = set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return list(duplicates)

l = [1, 1, 1, 1, 2, 2, 7, 8, 10, 11]
print(find_duplicates(l))