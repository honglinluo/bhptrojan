import os


def run(*args, **kwargs):
    print('[*] In environment module.')
    return os.environ
