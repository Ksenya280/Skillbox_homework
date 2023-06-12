
import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

site_dict = {}


def site_structure_func(count):
    if count == 0:
        return
    else:
        name = input('Введите название продукта для нового сайта: ')
        key = {'title': f'Куплю/продам {name} недорого', 'h2': f'У нас самая низкая цена на {name}'}
        new_site = copy.deepcopy(site)
        change_value_by_key(new_site, key)
        site_dict[name] = new_site
        print_site(site_dict)
        site_structure_func(count - 1)


def print_site(dict):
    for name in dict.keys():
        print('Сайт для {}:'.format(name))
        print('site = ', dict.get(name), '\n')


def change_value_by_key(struct, key):
    for i_key in struct:
        if i_key in key.keys():
            struct[i_key] = key[i_key]
        else:
            for sub_dict in struct.values():
                if isinstance(sub_dict, dict):
                    change_value_by_key(sub_dict, key)


count = int(input('Сколько сайтов: '))
site_structure_func(count)
