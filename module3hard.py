# #Задание "Раз, два, три, четыре, пять .... Это не всё?"
def calculate_structure_sum(*args):
    summ = 0
    for i in args:
        if isinstance(i, int):
            summ += i
        elif isinstance(i, str):
            summ += len(i)
        elif isinstance(i, dict):
            summ += calculate_structure_sum(*i.items())
        elif isinstance(i, (list, tuple, set)):
            summ += calculate_structure_sum(*i)
    return summ




data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)

