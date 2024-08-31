import itertools
from copy import deepcopy

nested_data = {"env": ["prd", "dev"], "os": ["win", "unx"], "msg": "ok"}

base_data = {}
non_base_data = []

for k, v in nested_data.items():
    if isinstance(v, list):
        non_base_data.append([{k: single_v} for single_v in v])
    else:
        base_data.update({k: v})

print("base_data:", base_data)
print("non_base_data:", non_base_data)

flatted_list = list(itertools.product(*tuple(non_base_data)))

for l in flatted_list:
    print(l)
print(len(flatted_list))


flatted_data = []
for one_combinaition in flatted_list:
    line = deepcopy(base_data)
    for column in one_combinaition:
        line.update(column)
    flatted_data.append(line)

for l in flatted_data:
    print(l)
print(len(flatted_data))


# base_data: {'msg': 'ok'}
# non_base_data: [[{'env': 'prd'}, {'env': 'dev'}], [{'os': 'win'}, {'os': 'unx'}]]
# ({'env': 'prd'}, {'os': 'win'})
# ({'env': 'prd'}, {'os': 'unx'})
# ({'env': 'dev'}, {'os': 'win'})
# ({'env': 'dev'}, {'os': 'unx'})
# 4
# {'msg': 'ok', 'env': 'prd', 'os': 'win'}
# {'msg': 'ok', 'env': 'prd', 'os': 'unx'}
# {'msg': 'ok', 'env': 'dev', 'os': 'win'}
# {'msg': 'ok', 'env': 'dev', 'os': 'unx'}
# 4