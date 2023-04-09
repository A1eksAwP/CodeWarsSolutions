"""
This is my simple parser for automatic made KATA.py files to solution a new kata from codewars URL.
"""
import requests
import sys
import json
import re
import os


class Kata:
    def __init__(self):
        self.kata_url = self.set_new_kata
        self.kata_id = re.search(r'/kata/?(?P<id>[^/]+)', self.kata_url).group('id')
        self.response_url = f'https://www.codewars.com/api/v1/code-challenges/{self.kata_id}'
        self.response = None
        self.response_json = None
        self.kata_dict = None
        self.new_file = None

    @property
    def set_new_kata(self):
        if len(sys.argv) <= 1:
            return self.validate_url(input('Введите url вашей новой "kata": '))
        else:
            return self.validate_url(sys.argv[1])

    @staticmethod
    def validate_url(url):
        while not re.fullmatch(r'(https://)?www\.codewars\.com/kata/[^/]+(/train/python)?', url):
            url = input('Введите КОРРЕКТНОЕ url вашей новой "kata": ')
        return url

    def start_parser(self):
        self.response = requests.get(self.response_url, timeout=1000)
        self.set_kata_dict()
        self.set_new_file()
        self.create_new_file()

    def set_kata_dict(self):
        if self.response.status_code == 200:
            self.response_json = json.loads(self.response.content)
            self.kata_dict = {
                'id': self.response_json['id'],
                'title': self.response_json['slug'],
                'kyu': self.response_json['rank']['name'],
                'description': self.response_json['description'],
                'tags': self.response_json['tags']
            }
        else:
            print('Ошибка извлечения данных.')

    def set_new_file(self):
        file_name = f"{self.kata_dict['kyu'].replace(' ', '_')}_{self.kata_dict['title'].replace('-', '_')}.py"
        file_url = f"https://www.codewars.com/kata/{self.kata_dict['id']}/train/python"
        file_description = self.kata_dict['description']
        self.new_file = {
            'name': file_name,
            'url': file_url,
            'description': file_description
        }

    @staticmethod
    def create_sep(sep='"', cnt=3):
        return f'{sep * cnt}'

    def create_new_file(self):
        if not os.path.isfile(self.new_file['name']):
            with open(f"{self.new_file['name']}", 'w', encoding='utf-8') as f:
                f.write(f"# {self.new_file['url']}\n\n")
                f.write(f"{self.create_sep()}\n")
                f.writelines(f"{self.new_file['description']}\n")
                f.write(f"{self.create_sep()}\n\n\n")
                f.write("def my_solution(): \n\t...\n")
            print(f"Файл: {self.new_file['name']} успешно создан!")
        else:
            print(f"Файл: '{self.new_file['name']}' уже существует!")


if __name__ == '__main__':
    new_kata = Kata()
    new_kata.start_parser()
