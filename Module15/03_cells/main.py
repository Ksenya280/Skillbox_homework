print('Количество клеток: 5','Эффективность 1 клетки: 3','Эффективность 2 клетки: 0','Эффективность 3 клетки: 6','Эффективность 4 клетки: 2','Эффективность 5 клетки: 10',sep = "\n")
cell_list = [3,0,6,2,10]
empty_list = []
for i in range(len(cell_list)):
     if i > cell_list[i]:
         empty_list.append(cell_list[i])
print('Неподходящие значения:', empty_list)
