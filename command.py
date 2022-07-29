import os
import sys

def clear():
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')

def scrapeWork(name, id):
    os.system(f'python lib/ao3_get_fanfics.py {id}')
    
    if os.name in ('nt', 'dos'):
        os.system('del errors_fanfics.csv')
    else:
        os.system('rm errors_fanfics.csv')
    
    print(os.getcwd())
    os.system(f'python lib/extras/csv_to_txts.py fanfics.csv')

    if os.name in ('nt', 'dos'):
        os.system('del fanfics.csv')
        os.system(f'del "books/{name}.txt"')
        os.system(f'move fanfics.csv_text_files/{id}.txt "books/{name}.txt"')
        os.system('rmdir /s fanfics.csv_text_files')
    else:
        os.system('rm fanfics.csv')
        os.system(f'rm "books/{name}.txt"')
        os.system(f'cp fanfics.csv_text_files/{id}.txt "books/{name}.txt"')
        os.system('rm -r fanfics.csv_text_files')