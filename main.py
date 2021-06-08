import random


def hangman_graphic(guesses):
    gallows = ["_______\n|     |\n|\n|\n|\n|\n|\n=======",
               "_______\n|     |\n|     O\n|\n|\n|\n|\n=======",
               "_______\n|     |\n|     O\n|     |\n|     |\n|\n|\n=======",
               "_______\n|     |\n|     O\n|    -|\n|     |\n|\n|\n=======",
               "_______\n|     |\n|     O\n|    -|-\n|     |\n|\n|\n=======",
               "_______\n|     |\n|     O\n|    -|-\n|     |\n|    /\n|\n=======",
               "_______\n|     |\n|     O\n|    -|-\n|     |\n|    / \\ \n|\n======="]
    print(gallows[guesses])


# סידור האותיות הנכונות בקווים
def emptyword(choice, succletter):
    word = ''
    for char in choice:
        if (char in succletter):
            word += str(char) + ' '
        else:
            word += '_ '
    return word


# המרת כל האותיות לאותיות קטנות
def lowerWord(word):
    return word.lower()


anotherGame = 'yes'
countOfWords = ["none"]
choice = "none"
countOfGames = {'hard': {'win': 0, 'lose': 0}, 'easy': {'win': 0, 'lose': 0}}

while (anotherGame == 'yes'):
    # בחירת רמת הקושי במשחק
    Difficulty_level = lowerWord(input("insert the level of the Difficulty that you want easy or hard: \n"))
    # זיהוי שגיאה (משתמש לא בחר easy/hard)
    if (not (Difficulty_level == "easy" or Difficulty_level == 'hard')):
        print('you need choose only easy or hard')
        continue
    # כל עוד המילה לא במחסן מילים כנס ללולאה
    while (choice in countOfWords):
        # בחירת מילה רנדומלית מקובץ המילים(או מהרמה הקשה או מהקלה )
        if Difficulty_level == "easy":
            my_file = open("shortwords")
            f = my_file.readlines()
            choice = random.choice(f)
            choice = choice.replace('\n', '')  # מוחק ירידה שורה מהמילה שהגיעה מהקובץ
            my_file.close()

        if Difficulty_level == "hard":
            my_file = open("longwords")
            f = my_file.readline()
            choice = random.choice(f)
            choice = choice.replace('\n', '')  # מוחק ירידה שורה מהמילה שהגיעה מהקובץ
            my_file.close()

    # הוספת המילה לרשימת המילים שכבר נבחרו
    countOfWords.append(choice)
    choice2 = choice
    counter = 0
    succLetter = []
    ignoreLetter = []
    while counter != 7:
        letter = lowerWord(input("please choose a letter \n"))
        # A-Z זיהוי שגיאה - אם לא הכניס אות אחת ובין
        if (not (letter >= 'a' and letter <= 'z' and len(letter) == 1)):
            print("you choose wrong letter")
            letter = input("please choose a letter \n")
            continue
            # זיהוי שגיאה - האות כבר נבחרה
        if (letter in ignoreLetter):
            print("this letter is chosen")
            continue
            # הוספת האות שנבחרה לרשימת האותיות בנבחרו
        ignoreLetter.append(letter)
        # הוספת האות לרשימת האותיות הנכונות לאותה מילה
        if letter in choice2:
            succLetter.append(letter)
            # מדפיס את המילה עם האותיות הנכונות
            print(emptyword(choice, succLetter))
            # את האותיות הנכונות שכבר נבחרו  choice2  מסיר מ
            choice2 = choice2.replace(letter, '')
        # אות שגויה - מוסיף פסילה ומדפיס איש תלוי
        else:
            hangman_graphic(counter)
            counter += 1
        #  אם ניחש הכל מוסיף ניצחון ללוח התוצאות לפי רמת הקושי
        if (choice2 == ''):
            if (Difficulty_level == "easy"):
                countOfGames['easy']['win'] += 1
            else:
                countOfGames['hard']['win'] += 1
            print("you win")
            break
    # אם הספירה הגיע ל 7 מוסיף הפסד ללוח התוצאות לפי רמת הקושי
    if (counter == 7):
        if (Difficulty_level == "easy"):
            countOfGames['easy']['lose'] += 1
        else:
            countOfGames['hard']['lose'] += 1
        print('you Lose!')
    # מחזיר את המילה לאיפוס התחלתי
    choice = 'none'
    # משחק חוזר? והדפס לוח התוצאות
    anotherGame = lowerWord(input("do you want another game? yes / no: "))
print("Hard Game: ", countOfGames['hard']['win'], ' wins', countOfGames['hard']['lose'], ' loses')
print("Easy Game: ", countOfGames['easy']['win'], ' wins', countOfGames['easy']['lose'], ' loses')
