str_data = "{ a1 : 20 }, { a2 : 30 }, { a3 : 15 }, { a4 : 50 }, { a5 : -15 }, { a6 : 80 }, { a7 : 0 }, { a8 : -110 }"

total = 0
split_str_data = str_data.split(",")
for i in range(0, len(split_str_data)):
    str_tmp = split_str_data[i].split(":")[1].split("}")[0]
    num_tmp = int(str_tmp)
    total += num_tmp

print(total)
