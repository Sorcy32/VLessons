"""
Домашнее задание №2
Работа с файлами
* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    file = open("referat.txt", "r", encoding='utf8')
    cont = file.read()
    file.close
    print("Длина строки: " + str(len(cont)))
    print("Количество слов в тексте: " + str(len(cont.split())))
    changed=""
    for word in cont:
        if word == ".":
             word = "!"
             changed+=word
        elif word!=".":
             changed+=word
    print(changed)
    f = open("referat2.txt", "w",encoding='utf8')
    f.write(changed)
    f.close
     


if __name__ == "__main__":
    main()
