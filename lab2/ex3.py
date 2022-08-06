import os

path = 'D:/PyProjects/lab2'
for dirs, folder, files in os.walk(path):
    for file in files:
        if os.path.getsize(os.path.join(dirs, file)) < 1024 * 1024:
            print(os.path.join(dirs, file))
