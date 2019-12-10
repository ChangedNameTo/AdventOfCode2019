from program import string

n = 25 * 6
layers = [string[i:i+n] for i in range(0, len(string), n)]


# zero_count = 999999999
# lowest = None
# for layer in layers:
#     layer_count = 0
#     for char in layer:
#         if char == '0':
#             layer_count += 1

#     if layer_count < zero_count:
#         zero_count = layer_count
#         lowest = layer

# # print(lowest)
# count1 = 0
# count2 = 0
# for char in lowest:
#     if char == '1':
#         count1 += 1
#     if char == '2':
#         count2 += 1

# print(count1 * count2)
master = [2] * 25 * 6
for layer in layers:
    for x in range(0, len(layer)):
        if master[x] == 2 and int(layer[x]) != 2:
            master[x] = int(layer[x])

for x in range(0,6):
    layer_str = ""
    for y in range(0,25):
        if str(master[(x*25) + y]) == '0':
            layer_str += ' '
        else:
            layer_str += str(master[(x*25) + y])
    print(layer_str)
