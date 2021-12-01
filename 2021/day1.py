
#%%
with open("data/input1.txt", 'r') as f:
    data_list = [int(line) for line in f.readlines()]

# %%
number_of_increases = 0
for i in range(len(data_list)-1):
    if data_list[i] < data_list[i+1]:
        number_of_increases += 1
print(number_of_increases)
# %%
result2 = 0
for i in range(len(data_list)-3):
    if sum(data_list[i:i+3]) < sum(data_list[i+1:i+4]):
        result2 += 1
print(result2)
