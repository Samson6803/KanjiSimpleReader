import os, re

def clearTerminal():
    os.system('clear')

def getKanjisRangeInput():
    print('Pick the numer of first (including) kanji number...')
    firstKanjiNumber = int(input())

    clearTerminal()

    print(f'First kanji number: {firstKanjiNumber}\n')
    print('Pick the number of the last (including) kanji number...')
    lastKanjiNumber = int(input())

    clearTerminal()
    return firstKanjiNumber, lastKanjiNumber

def askUserForKanjisInput():
    while True:
        firstKanjiNumber, lastKanjiNumber = getKanjisRangeInput()

        while True:
            print(f'First kanji number is {firstKanjiNumber} and the last one is {lastKanjiNumber}')
            print('Are these numbers correct? [y/n]')
            response = input()
            
            clearTerminal()
            if response == 'y':
                return firstKanjiNumber, lastKanjiNumber
            elif response == 'n':
                break

def parseKanjiFile(kanjiNumber: int):
    kanjiNumberText = str(kanjiNumber)
    numberOfDigits = len(kanjiNumberText)

    for x in range(numberOfDigits, 4):
        kanjiNumberText = '0' + kanjiNumberText
    
    fileLines = open(f'./kanjis/{kanjiNumberText}.md', 'r').readlines()

    kanjiLine = next((s for s in fileLines if 'kanji: ' in s), None)
    kanji = re.search(r"kanji:\s*(.+)", kanjiLine).group(1)
    return kanji
    

if __name__ == '__main__':
    firstKanjiNumber, lastKanjiNumber = askUserForKanjisInput()
    print(f'Chosen range is {firstKanjiNumber} and {lastKanjiNumber}... [press any key]')
    input()

    with open("cards.md", "w", encoding="utf-8") as file:
        clearTerminal()
        for x in range(firstKanjiNumber, lastKanjiNumber + 1):
            kanji = parseKanjiFile(x)
            print(f'Kanji: {kanji}, number: {x}')
            print('Type translation...')
            word = input()
            print('Type notes...')
            notes = input()
            clearTerminal()
            markdown = f'word: {word}\nnotes: {notes}\n---\nkanji: {kanji}\n'

            file.write(markdown)

            if x != lastKanjiNumber:
                file.write('@@@\n')


    print('Done...[press any key]')
    input()

