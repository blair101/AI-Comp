AI Challenger 2018 Sentiment Analysis 细粒度评论情感分析
=========================================

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

功能描述
---

AI Challenger

处理流程，如数据读取、分词、特征提取、模型定义以及封装、模型训练、模型验证、模型存储以及模型预测等

开发环境
---

* 主要依赖工具包以及版本，详情见requirements.txt

项目结构
---

* src/config.py 项目配置信息模块，主要包括文件读取或存储路径信息
* src/util.py 数据处理模块，主要包括数据的读取以及处理等功能
* src/main_train.py 模型训练模块，模型训练流程包括 数据读取、分词、特征提取、模型训练、模型验证、模型存储等步骤
* src/main_predict.py 模型预测模块，模型预测流程包括 数据和模型的读取、分词、模型预测、预测结果存储等步骤


使用方法
---

* pip install -r requirement.txt
* 配置 在config.py中配置好文件存储路径
* 训练 运行 python main_train.py -mn your_model_name 训练模型并保存，同时通过日志可以得到验证集的F1_score指标
* 预测 运行 python main_predict.py -mn your_model_name 通过加载上一步的模型，在测试集上做预测

运行方法
---

```py
python main_train.py -mn fasttext_wn2_model.pkl -wn 2
```
