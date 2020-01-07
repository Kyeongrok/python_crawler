users = [
    {"name": "kyeongrok", "age": 33, "salary": 80000000},
    {"name": "yeonghwan", "age": 30, "salary": 50000000}
]

for user in users:
    print(user["age"], user["salary"])

#
def plus(val1, val2):
    return val1 + val2

def multiple(val1, val2):
    return val1 * val2

result = multiple(plus(10, 20), plus(20, 30))
print(result)