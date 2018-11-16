import os
l = []
def path_finder(path):
    for i in os.scandir(path):
        fullpath = os.path.join(path, i.name)
        if not i.is_file():
            path_finder(fullpath)
        else:
            l.append(fullpath)
path = '/home/vaibhav/test123' # Edit path here
path_finder(path)
print(l)