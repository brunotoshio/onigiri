# -*- coding: utf-8 -*-
# Copyright 2019 Bruno Toshio Sugano <brunotoshio@gmail.com>
from collections import Counter

from .dict_handler import DictHandler


class DictCounter(object):
    def __init__(self, dict_path):
        self._dict = DictHandler(dict_path)
        self.reset()

    def count(self, list_of_words):
        for word in list_of_words:
            self.number_of_words += 1
            self._category_counter.update(self._dict.search(word))

    def reset(self):
        self.number_of_words = 0
        self._category_counter = Counter()
        self._category_counter.update({category: 0 for category in self._dict.categories()})

    def top(self, n):
        return self._category_counter.most_common(n)

    def top_normalized(self, n):
        normalized = Counter()
        for key in self._category_counter:
            normalized[key] = self._category_counter[key] / self.number_of_words
        return normalized.most_common(n)
