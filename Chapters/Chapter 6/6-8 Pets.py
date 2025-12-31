max = {"kind": "dog",
       "owner": "sherry"}
shawn = {"kind": "cat",
       "owner": "perry"}
terry = {"kind": "sheep",
       "owner": "harry"}
peter = {"kind": "bird",
       "owner": "berry"}

pets = [max, shawn, terry, peter]
for pet in pets:
    print(pet["kind"])
    print(pet["owner"])