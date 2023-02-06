def uni_list(lt):
    unique = []
    for i in lt:
        if i not in unique:
            unique.append(i)
    return unique


print(uni_list([1, 2, 3, 1, 2, 3, 4]))