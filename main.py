
import chardet


def open_file_txt(target_file):
    encode = None
    strings = None
    with open(target_file, "rb") as txt_file:
        raw_info = txt_file.read()
        encode = chardet.detect(raw_info)
        print(encode)
        strings = raw_info.decode(encode["encoding"])
    return strings


def count_frequency(target_file):
    data = open_file_txt(target_file)
    l_text = data.split()
    s_text = set(data.split())
    array = sorted(zip([l_text.count(w) for w in s_text], s_text), reverse=True)
    for i in array:
        if len(i[1])<7:
            continue
        else:
            print("Самое популярное слово длиной более 6 символов в этом файле {}. Оно встречается {} раз".format(i[1], i[0]))
            break


def main():
    answer = ""
    while True:
        print("\nПрограмма для работы с txt готова к работе.\nВыберите нужный файл и нажмите соответствующую цифру:\n",
            "Для 'newsafr.txt' нажмите 1\n",
            "Для 'newscy.txt' нажмите 2\n",
            "Для 'newsfr.txt' нажмите 3\n",
            "Для 'newsit.txt' нажмите 4\n",
            "Для выхода нажмите q\n")
        answer = input()
        if answer == "1":
            count_frequency("newsafr.txt")
        elif answer == "2":
            count_frequency("newscy.txt")
        elif answer == "3":
            count_frequency("newsfr.txt")
        elif answer == "4":
            count_frequency("newsit.txt")
        elif answer == "q":
            print("Программа для работы с txt завершена.")
            break
        else:
            print("команда неверна попробуйте ещё раз")

if  __name__ ==  "__main__" :    main()
