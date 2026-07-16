names = ["alice", "bob", "charlie"]
#expected: ["ALICE", "BOB", "CHARLIE"]
capital = [name.upper() for name in names]
print(capital)

lambda_map = list(map(lambda name: name.upper(), names))
print(lambda_map)