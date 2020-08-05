# -*- coding: utf-8 -*-

import pprint
from trie import Trie


class NER(object):
    def __init__(self, ner_dict):
        """
        采用自定义词典进行NER
        :param ner_dict:

        ner_dict = {"LOC": ["河南", "洪洞县", "张家庄", "西门"],
                    "PER": ["小明", "小红", "张三林", "欧阳李丹", "西门", "JACk"]}

        """
        self.trie = Trie()
        self.add_nodes(ner_dict)

    def add_nodes(self, ner_dict):
        for entity_type, entitys in ner_dict.items():
            self.trie.add_node(entitys, entity_type)

    def tag(self, text):
        ner_results = []
        idx = 0
        while idx < len(text):
            words = text[idx: idx+self.trie.depth].lower()
            step, ner_type = self.trie.search_word(words)
            if ner_type:
                ner_results.append({"text": text[idx:idx+step], "offsets": [idx, idx+step], "type": ner_type})
            idx += step

        pprint.pprint(ner_results)

        return ner_results


if __name__ == '__main__':
    ner_dict = {"LOC": ["河南", "洪洞县", "张家庄", "西门"],
                "PER": ["小明", "小红", "张三林", "欧阳李丹", "西门", "JACk"]}
    ner = NER(ner_dict)
    ner.tag("小明和jack在张家庄工作")



