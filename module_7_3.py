import re
from itertools import chain

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        list_name = []
        lines = []
        for file_name in self.file_names:

            with open(file_name, encoding='utf-8') as file:
                name = file.name
                list_name.append(name)

                line_read = file.readlines()
                for line in line_read:

                    line = re.sub('[,.!?=;:]','',line)
                    line = line.replace(' - ', '')
                    ll = line.lower().split()
                    #rez = chain.from_iterable(ll)
                    #list_rez = rez

                lines.append(ll)

        all_words = dict(zip(list_name, lines))
        return all_words

    def find(self, word):
        new_dict = {}
        for keys, values in self.get_all_words().items():
             if word.lower() in values:
                new_dict[keys] = values.index(word.lower()) + 1
                new_dict.update()
             else:
                continue
        return new_dict


    def count(self, word):
        new_dict2 = {}

        for key, value in self.get_all_words().items():
            if word.lower() in value:
                new_dict2[key] = value.count(word.lower())
                new_dict2.update()
            else:
                continue
        return new_dict2


ff = WordsFinder('file1.txt', 'file2.txt','file3.txt' )
#ff2 = WordsFinder('file2.txt')
print(ff.get_all_words())
print(ff.find('как'))
print(ff.count('списки'))
