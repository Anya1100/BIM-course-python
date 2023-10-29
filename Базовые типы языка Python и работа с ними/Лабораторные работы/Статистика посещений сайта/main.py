users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
unique_users = len(set(users))
total_count = len(users)
res = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
res['Общее количество'] = total_count
res['Уникальные посещения'] = unique_users

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
print(res)