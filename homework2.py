number_of_completed_DZ = '12'
number_of_hours_spent = '1.5'
course_name = 'Python'
time_per_task = float(number_of_hours_spent) / int(number_of_completed_DZ)
print('Курс:', course_name, ',', 'всего задач:', number_of_completed_DZ, 'затрачено часов:', number_of_hours_spent, ',', 'среднее время выполнения', time_per_task)