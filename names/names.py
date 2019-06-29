import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# solution using set operator:
# duplicates = set(names_1) & set(names_2)

# provided solution:
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# MVP Solution
duplicates = []
names_dict = {}

for name_1 in names_1:
    names_dict[name_1] = True
for name_2 in names_2:
    if name_2 in names_dict:
        duplicates.append(name_2)

# Stretch
# Less efficient on runtime than MVP solution, but still more efficient than the provided solution
# for name_1 in names_1:
#     duplicates.append(name_1)
# duplicates = [i for i in names_2 if i in duplicates ]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

