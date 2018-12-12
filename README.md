## AI-Challenger Baseline 细粒度用户评论情感分析

在线评论的细粒度情感分析对于深刻理解商家和用户、挖掘用户情感等方面有至关重要的价值，主要用于个性化推荐、智能搜索、产品反馈、业务安全等。

本次比赛我们提供了一个高质量的海量数据集，共包含6大类20个细粒度要素的情感倾向。

### 数据说明

数据集分为训练、验证、测试A与测试B四部分。

数据集中的评价对象按照粒度不同划分为两个层次，层次一为粗粒度的评价对象. 评价对象的具体划分如下表所示。

层次一(The first layer)	| 层次二(The second layer)
------ | ------
位置(location) | 交通是否便利(traffic convenience)
位置(location) | 距离商圈远近(distance from business district)
位置(location) | 是否容易寻找(easy to find)
.. | ..
服务(service) | 
 

数据标注示例如下：

> “味道不错的面馆，性价比也相当之高，分量很足～女生吃小份，胃口小的，可能吃不完呢。环境在面馆来说算是好的，至少看上去堂子很亮，也比较干净，一般苍蝇馆子还是比不上这个卫生状况的。中午饭点的时候，人很多，人行道上也是要坐满的，隔壁的冒菜馆子，据说是一家，有时候也会开放出来坐吃面的人。“

### 文件说明

    class_*.py 模型文件
    model_*_char.py 训练文件
    validation_*_char.py 生成验证结果，方便本地测试
    evaluate_char.py 评估本地验证集效果
    predict_*_char.py 生成提交结果文件

## Reference

- [keras lstm attention glove840b,lb 0.043][1]

[1]: https://www.kaggle.com/qqgeogor/keras-lstm-attention-glove840b-lb-0-043
