# Задача №21.  Напишите программу для печати всех уникальных значений в словаре. 

# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
#          {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Примечание: Список словарей задан изначально. Пользователь его не вводит

list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

unique_values = set()

for cur_dict in list_dicts:
    for key in cur_dict:
        unique_values.add(cur_dict[key].strip())
        
print(unique_values)