import inspect
import os


def img(name):
    folder = inspect.stack()[1][1]
    index = folder.find(".")
    if index >= 0:
        folder = folder[:folder.find(".")]
    print(folder)
    # folder = folder+"/"+name+".png"
    folder = os.path.join(folder, name)+".png"
    return folder


if __name__ == '__main__':
    name = "dada.fafa.afa.jpg"
    print(img(name))
