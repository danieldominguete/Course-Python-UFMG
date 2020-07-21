# -*- coding: utf8


import threading
import requests
import urllib.request

class Get(object):
    pass


def get(url):
    response = urllib.request.urlopen(url)
    g = Get()
    g.status = response.status
    g.text = response.read().decode("utf-8")
    return g

class Worker(threading.Thread):
    def __init__(self, book_id, **kwargs):
        super(Worker, self).__init__(**kwargs)
        self.__book_id = book_id
        self.__result = None

    def run(self):
        self.__result = 0
        book = requests.get(
            "http://www.gutenberg.org/files/{}/{}-0.txt".format(
                self.__book_id, self.__book_id
            )
        )

        self.__result = len(book.text.splitlines())

    def get_result(self):
        return self.__result

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]

def crawler(num_threads):
    book_ids = [
        1342,
        11,
        1661,
        2701,
        25525,
        1952,
        1727,
        1080,
        98,
        84,
        2600,
        74,
        2591,
        28054,
        62610,
        1184,
    ]
    total_lines = 0

    if num_threads >= len(book_ids):
        threads = []

        for id_ in book_ids:
            threads.append(Worker(id_))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
            total_lines += thread.get_result()

        return total_lines

    else:
        size = int(len(book_ids) / num_threads)
        split_ids = list(chunks(book_ids, size))

        for chunck in split_ids:
            threads = []
            for id_ in chunck:
                threads.append(Worker(id_))

            for thread in threads:
                thread.start()

            for thread in threads:
                thread.join()
                total_lines += thread.get_result()

        return total_lines