# 概述
> 采用自定义词典识别文本中实体


# 使用示例

```python

from ner import NER

# 自定义实体词典
ner_dict = {"LOC": ["河南", "洪洞县", "张家庄", "西门"],
            "PER": ["小明", "小红", "张三林", "欧阳李丹", "西门", "JACk"]}
                
                          
ner = NER(ner_dict)
res = ner.tag("小明和jack在张家庄工作")



"""
result:

[{'offsets': [0, 2], 'text': '小明', 'type': 'PER'},
 {'offsets': [3, 7], 'text': 'jack', 'type': 'PER'},
 {'offsets': [8, 11], 'text': '张家庄', 'type': 'LOC'}]

"""

```