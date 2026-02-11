set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

union_set = set1.union(set2)
print("\nUnion:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

difference_set = set1.difference(set2)
print("Difference (Set1 - Set2):", difference_set)

symmetric_diff = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_diff)

