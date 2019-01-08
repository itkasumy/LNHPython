info = {
    "age": 18,
    "name": "ksm",
    "hobbys": ["girl", "money"],
    "subjects": ("english", "math"),
    "friends": [{
        "name": "yifei",
        "gender": "girl",
    },
        {
            "name": "dehua",
            "gender": "boy",
        }
    ],
    "gender": "boy"
}

print(info)
del info["gender"]
print(info)

for item in info:
    print(item, "=>", info[item])

for item in info.keys():
    print(item)

for item in info.values():
    print(item)

for k, v in info.items():
    print(k, "=>", v)

res01 = dict.fromkeys(["k1", 123, "ksm"])
print(res01)
res02 = dict.fromkeys(["k1", 123, "ksm"], 123)
print(res02)

dict01 = {
    "k1": "v1",
    "k2": "v2"
}

# val01 = dict01.get("k123")
# print(val01)
# val02 = dict01.get("k123", 123)
# print(val02)
# val03 = dict01.get("k1", 123)
# print(val03)
#
# val04 = dict01.pop("k1")
# print(dict01, val04)
# val05 = dict01.pop("k1", "abcdef")
# print(dict01, val05)

# val06 = dict01.popitem()
# print(dict01, val06)
# key1, value1 = dict01.popitem()
# print(dict01, key1, value1)
#
# val07 = dict01.setdefault("k1", "abcdef")
# print(dict01, val07)

# dict01.update({"k1": "fedcba", "key3": 123456})
# print(dict01)

dict01.update(k1="fedcba", k3=123456, k4=654321)
print(dict01)