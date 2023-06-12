def get_input_parameters():
    shift = int(input('Сдвиг: '))
    original_list = [1, 2, 3, 4, 5]
    print('Изночальный список:', original_list)
    return shift, original_list

def display_result(shifted_list):
    print('Сдвинутый список:', shifted_list)

def shift_list(shift, original_list):
    original_list = original_list[- shift :] + original_list[: - shift]
    return original_list

shift, original_list = get_input_parameters() 
shifted_list = shift_list(shift, original_list) 
display_result(shifted_list)