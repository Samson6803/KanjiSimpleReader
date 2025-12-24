import os, re, argparse

parser = argparse.ArgumentParser()

def clear_terminal():
    os.system('clear')

def get_kanjis_range_input():
    print('Pick the numer of first (including) kanji number...')
    first_kanji_number = int(input())

    clear_terminal()

    print(f'First kanji number: {first_kanji_number}\n')
    print('Pick the number of the last (including) kanji number...')
    last_kanji_number = int(input())

    clear_terminal()
    return first_kanji_number, last_kanji_number

def ask_user_for_kanjis_input():
    while True:
        first_kanji_number, last_kanji_number = get_kanjis_range_input()

        while True:
            print(f'First kanji number is {first_kanji_number} and the last one is {last_kanji_number}')
            print('Are these numbers correct? [y/n]')
            response = input()
            
            clear_terminal()
            if response == 'y':
                return first_kanji_number, last_kanji_number
            elif response == 'n':
                break

def parse_kanji_file(kanji_number: int, kanjis_path: str):
    kanji_number_text = str(kanji_number)
    number_of_digits = len(kanji_number_text)

    for x in range(number_of_digits, 4):
        kanji_number_text = '0' + kanji_number_text
    
    file_lines = open(f'{kanjis_path}/{kanji_number_text}.md', 'r').readlines()

    kanji_line = next((s for s in file_lines if 'kanji: ' in s), None)
    kanji = re.search(r"kanji:\s*(.+)", kanji_line).group(1)
    return kanji
    

if __name__ == '__main__':
    parser.add_argument('--kanjisPath', action="store", dest='kanjisPath', required=True)
    args = parser.parse_args()
    kanjisPath = args.kanjisPath 

    firstKanjiNumber, lastKanjiNumber = ask_user_for_kanjis_input()
    print(f'Chosen range is {firstKanjiNumber} and {lastKanjiNumber}... [press any key]')
    input()

    with open("cards.md", "w", encoding="utf-8") as file:
        clear_terminal()
        for x in range(firstKanjiNumber, lastKanjiNumber + 1):
            kanji = parse_kanji_file(x, kanjisPath)
            print(f'Kanji: {kanji}, number: {x}')
            print('Type translation...')
            word = input()
            print('Type notes...')
            notes = input()
            clear_terminal()
            markdown = f'word: {word}\nnotes: {notes}\n---\nkanji: {kanji}\n'

            file.write(markdown)

            if x != lastKanjiNumber:
                file.write('@@@\n')

    print('Done...[press any key]')
    input()

