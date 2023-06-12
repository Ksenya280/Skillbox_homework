def function(num):
    if num <= 0:
        return
    function(num - 1)
    print(num)


number = int(input('Введите число: '))
function(number)