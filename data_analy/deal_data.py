import json
import numpy as np
import pandas as pd

#json数据
obj = """
{"data": {
        "bar": 1,
        "logo": 1,
        "entr": 1,
        "act": [{
            "name": "Major",
            "en_type": 1,
            "en_word": "Major",
            "en_pic": "",
            "start_time": 1636287660,
            "end_time": 1636324200,
            "course_open": 0}]
        }
}
"""
res = json.loads(obj) #将json字符串转换成python
res1 = json.dumps(res) #将python转换成json
sib = pd.DataFrame(res['data'],index=['a'],columns=['logo','entr']) #转换其中的一部分为dataframe
print(sib)