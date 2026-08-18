exam_points = {
  "Mariusz":30,
  "Mateusz":55,
  "Marta":76,
  "Roman":30,
  "Arleta":59,
  "Adrian":96,
  "Monika":91,
  "Andrzej":22,
  "Krzysztof":83,
  "Krystyna":93,
  "Piotr":44,
  "Dawid":10,
  "Agnieszka":15
}

failed_students = [x for x in exam_points if exam_points[x] <= 45]
top_students = [x for x in exam_points if exam_points[x] > 90]
best_student = ("",0)

best_score = 0
for x,y in exam_points.items():
    if y > best_score:
        best_score = y
        best_student = (x,y)

print(f'''Osoby z oceną niedostateczną:
{'\n'.join(failed_students)}''')
print()
print(f'''Osoby z oceną bardzo dobrą:
{'\n'.join(top_students)}''')
print()
print(f'''Osoba z najlepszym wynikiem:
{best_student[0]}, {best_score} pkt''')

