'''
1. Дана начальная точка (а, b), при которой вы должны дойти до финальной точки (x, y) используя правило: с
определенной точки можно делать шаги только таким образом
“(a, b) → (a, b+a) или (a+b, b) ”
Какое наименьшее количество шагов нужно сделать, чтобы дойти из точки (a, b) в (x, y)?
Если это сделать невозможно выведите “Impossible”.
Пример:
Start [1, 1] → Finish[4, 7]
Шаг 1: [1, 2]
Шаг 2: [1, 3]
Шаг 3: [4, 3]
Шаг 4: [4, 7]
'''
listok = []
def number_of_steps(start, stop, hod = 0):
    global listok
    if start[0] == stop[0] and start[1] == stop[1]: 
        return listok.append(hod)
    elif start[0] > stop[0] or start[1] > stop[1]: 
        return listok.append('impossible')
    
    else:
        left_step = [start[0], start[1] + start[0]]
        right_step = [start[0] + start[1], start[1]]
        return (number_of_steps(left_step, stop, hod+1) or number_of_steps(right_step, stop, hod+1))


 
number_of_steps([1, 1],[142, 142], hod=0)
listok = list(set(listok))

if len(listok) > 1:
  listok.remove('impossible')
  print(listok[0])
else:
  print('“Impossible”')