def power_set_iterative(s):
    result = [[]]
    for elem in s:
        new_subsets = [subset + [elem] for subset in result]
        result += new_subsets
    return result

print(power_set_iterative([1,2]))