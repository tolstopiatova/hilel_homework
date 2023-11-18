
# python args.py --file file_to_read.txt

import argparse


def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            print(f"Кількість слів у файлі {file_path}: {word_count}")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")


def main():
    parser = argparse.ArgumentParser(description="Програма для обробки файлів")
    parser.add_argument("--file", dest="file_path", required=True, help="Шлях до файлу")

    args = parser.parse_args()
    process_file(args.file_path)


if __name__ == "__main__":
    main()
