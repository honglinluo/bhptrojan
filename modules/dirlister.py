import os


def run(*args, **kwargs):
    print("[*] In dirlister module.")
    files = os.listdir('.')
    return '/'.join(files)
