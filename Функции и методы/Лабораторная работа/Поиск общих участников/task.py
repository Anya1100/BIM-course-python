# TODO Напишите функцию find_common_participants
def find_common_participants(first,second,arg=","):
  firstnew = set(first.split(arg))
  secondnew = set(second.split(arg))
  fs = sorted(firstnew.intersection(secondnew))
  return fs

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

a = find_common_participants(participants_first_group,participants_second_group,"-")
print(a)
# TODO Провеьте работу функции с разделителем отличным от запятой
