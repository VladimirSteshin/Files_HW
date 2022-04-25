import os

file_path_merge = os.path.join(os.getcwd())

with os.scandir(file_path_merge) as objects:
    file_list = []
    for file in objects:
        if 'txt' in file.name and 'Result' not in file.name and 'recipes' not in file.name:
            file_list.append(file.name)


def file_sort(package):
    file_dict = {}
    for doc in package:
        with open(doc, encoding='UTF-8') as content:
            file_dict[doc] = content.read().strip()
    return file_dict


with open("Result.txt", "a", encoding='UTF-8') as container:
    library = file_sort(file_list)
    lengths = []
    for i in library.values():
        lengths.append(i.count('\n'))
    lengths = sorted(lengths)
    for count in lengths:
        for key, value in library.items():
            if count == value.count('\n'):
                container.write(key + '\n')
                container.write(str(count + 1) + '\n')
                container.write(value + '\n')