# -*- coding: utf-8 -*-

import pprint


import logging
logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Trie(object):
    def __init__(self):
        self.trie = {}
        self.depth = 0

    def add_node(self, entitys, entity_type):
        for word in entitys:
            word = word.lower()
            self.depth = max(len(word), self.depth)
            tree = self.trie
            for char in word:
                if char in tree:
                    tree = tree[char]
                else:
                    tree[char] = {}
                    tree = tree[char]
            if 'type' in tree:
                logging.info("entity: {} is '{}' and '{}', save {} (*_*) ...".format(word, tree['type'], entity_type, tree['type']))
                continue
            tree['type'] = entity_type

    def search_word(self, word):
        tree = self.trie
        step = 0
        for char in word:
            if char in tree:
                tree = tree[char]
                step += 1
                if 'type' in tree:
                    return step, tree['type']
            else:
                break
        return 1, None


if __name__ == '__main__':
    trie = Trie()
    per = ["小明", "小红", "张三林", "欧阳李丹"]
    loc = ["河南", "洪洞县", "张家庄", "小明"]
    trie.add_node(per, "PER")
    trie.add_node(loc, "LOC")
    pprint.pprint(trie.trie)

    step, type = trie.search_word("小明")
    print(step, type)


