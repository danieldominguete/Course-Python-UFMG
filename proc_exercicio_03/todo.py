# -*- coding: utf8
from collections import Counter
from bs4 import BeautifulSoup
from functools import reduce

import multiprocessing as mp
import tarfile


def extract_and_process(member):
    # observe como cada processo abre o tar novamente
    # a extração é feita por processo
    # veja exemplos do HTML na pasta exemplo
    # Para pegar o nome de um artist use texto.strip().split('-')[-1].
    # O formato do texto no html é Música - Artista

    tar = tarfile.open("dados.tar.gz", "r:gz")
    f = tar.extractfile(member)
    soup = BeautifulSoup(f, 'html.parser')

    cnt = Counter()

    for i in range(len(list(soup.find_all(class_="listEntry trackCompactEntry")))):
        cnt[soup.find_all(class_="trackName")[i].string.strip().split("- ")[-1]] += int(
            "".join(filter(str.isdigit, soup.find_all(class_="counts")[i].string))
        )

    return cnt


def merge_function(dict_1, dict_2):
    return Counter(dict_1) + Counter(dict_2)


def mapreduce(num_cpus=2):
    tar = tarfile.open('dados.tar.gz', 'r:gz')
    if num_cpus > 1:
        with mp.Pool(num_cpus) as pool:
            intermed = pool.imap_unordered(extract_and_process,
                                           tar.getmembers())
    else:
        intermed = map(extract_and_process, tar.getmembers())
    final = reduce(merge_function, intermed)
    return final