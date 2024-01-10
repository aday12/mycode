#! bin/usr/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# pull values from challenge list
print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[-1]}!")
# expected: My eyes! The goggles do nothing!

# pull values from trial list
print(f"My {trial[2].get('goggles')}! The {trial[2].get('eyes')} do {trial[3]}")
# expected output: My eyes! The goggles do nothing!

a= nightmare[0]["user"]["name"]["first"]
b= nightmare[0]["kumquat"]
c= nightmare[0]["d"]

print(f"My {a}! The {b} do {c}!")
