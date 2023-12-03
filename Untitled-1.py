def count_lines(file_path):
    with open(file_path, encoding="utf-8") as file:
        return len(file.readlines())
    

sorted_files = sorted([("1.txt", 1, count_lines(r"C:\Users\Зевс\Downloads\1.txt")),
                       ("2.txt", 2, count_lines(r"C:\Users\Зевс\Downloads\2.txt")),
                       ("3.txt", 3, count_lines(r"C:\Users\Зевс\Downloads\3.txt"))], key=lambda x: x[-1])


with open("lesson.txt", "w", encoding="utf-8") as f:
    for elem in sorted_files:
        f.write(f"{elem[0]}\n") 
        f.write(f"{elem[1]}\n") 
        for line in range(1, elem[-1] + 1):
            f.write(f"строка номер {line} файл номер {elem[1]}\n")