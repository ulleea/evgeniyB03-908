import os
import zipfile
a = os.getcwd()
print(a)
zip_file = None
for current_dir, dir, files in os.walk('.'):
    for i in files:
        s = i[-3::1]
        if s == 'zip':
            zip_file = i
            break
    if zip_file:
        break
z = zipfile.ZipFile(a + "\\" + zip_file)
z.extractall(a + '\\' + 'archive')
os.chdir(a + '\\' + 'archive')
tree = os.walk(a + '\\' + 'archive')
array = []
for folder, subfolders, files in os.walk(a + '\\' + 'archive'):
    for file in files:
        if file.endswith('.py'):
            array.append(folder)
            break
array.sort()
with open(a + '\\' + 'archive' + '\\' + 'answer', 'w') as file:
    for i in array:
        file.write(i + '\n')