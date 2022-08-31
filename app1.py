"""
Przygotuj dekoratory, które pozwolą:
a. Z napisu zwracanego przez dowolną funkcję pobrać tylko te znaki, które pasują do podanego regex-a.
b. Napis zwracany przez dowolną funkcję zapisac do pliku tekstowego o podanej przez Ciebie nazwie.
"""

import re

def filter(regex: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return ''.join(re.findall(regex, func(*args, **kwargs)))
        return wrapper
    return decorator

def save_to_file(filepath: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(filepath, 'w') as f:
                f.write(func(*args, **kwargs))
        return wrapper
    return decorator

@save_to_file(filepath="data1.txt")
@filter(regex=r'\d+')
def get_text() -> str:
    return 'KM Programs Kurs Python 2022'

@save_to_file(filepath="data2.txt")
@filter(regex=r'[A-Z]+')
def get_text_with_suffix(suffix: str) -> str:
    return f'KM Programs Kurs Python 2022 ... {suffix}'


def main() -> None:
    print(get_text())
    print(get_text_with_suffix('ABCD'))


if __name__ == '__main__':
    main()
