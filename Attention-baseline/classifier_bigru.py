import keras
from keras import Model
from keras.layers import *
# from JoinAttLayer import Attention


class TextClassifier():

    def model(self, embeddings_matrix, maxlen, word_index, num_class):

        inp = Input(shape=(maxlen,)) # 当输入序列的长度固定时，该值为其长度， 1200 （一个文档doc的最大长度）
        # Input 一个网络层次，输入层 在 keras

        # SpatialDropout1D ，那么常规的 dropout 将无法使激活正则化，且导致有效的学习速率降低。
        # SpatialDropout1D ，在这种情况下，SpatialDropout1D 将有助于提高特征图之间的独立性，应该使用它来代替 Dropout。

        # CuDNNGRU 是 基于CuDNN的快速GRU实现，只能在GPU上运行，只能使用 tensoflow 为后端
        # CuDNNLSTM 是 基于CuDNN的快速LSTM实现，只能在GPU上运行，只能使用 tensoflow 为后端

        encode = Bidirectional(CuDNNGRU(128, return_sequences=True))
        encode2 = Bidirectional(CuDNNGRU(128, return_sequences=True))

        # attention = Attention(maxlen)

        # Embedding嵌入层将正整数（下标）转换为具有固定大小的向量，如[[4], [20]]->[[0.25, 0.1], [0.6, -0.2]]
        #keras.layers.embeddings.Embedding(input_dim, output_dim, embeddings_initializer='uniform',
                                         # embeddings_regularizer=None, activity_regularizer=None,
                                         # embeddings_constraint=None, mask_zero=False, input_length=None)
        # Embedding层只能作为模型的第一层
        '''
        input_dim: int > 0。词汇表大小， 即，最大整数 index + 1。
        output_dim: int >= 0。词向量的维度。
        embeddings_initializer: 嵌入矩阵的初始化方法，为预定义初始化方法名的字符串，或用于初始化权重的初始化器。参考initializers
        input_length：当输入序列的长度固定时，该值为其长度。如果要在该层后接Flatten层，然后接Dense层，则必须指定该参数，否则Dense层的输出维度无法自动推断。
        '''

        x_4 = Embedding(len(word_index) + 1,#7983+1 # 词汇表大小， 即，最大整数 index + 1
                        embeddings_matrix.shape[1],
                        weights=[embeddings_matrix],# 7983 * 100
                        input_length=maxlen,
                        trainable=True)(inp)

        x_3 = SpatialDropout1D(0.2)(x_4)
        x_3 = encode(x_3)
        x_3 = Dropout(0.2)(x_3)
        x_3 = encode2(x_3)
        x_3 = Dropout(0.2)(x_3)

        # 输入shape， 形如（samples，steps，features）的3D张量
        # 输出shape， 形如(samples, features)的2D张量
        avg_pool_3 = GlobalAveragePooling1D()(x_3) # GlobalAveragePooling1D 为时域信号施加全局平均值池化
        max_pool_3 = GlobalMaxPooling1D()(x_3) # 对于时间信号的全局最大池化

        # attention_3 = attention(x_3)

        # x = keras.layers.concatenate([avg_pool_3, max_pool_3, attention_3], name="fc")
        x = Dense(num_class, activation="sigmoid")(x_3)

        adam = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, amsgrad=True)
        rmsprop = keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-06)
        model = Model(inputs=inp, outputs=x)

        model.compile(
            loss='categorical_crossentropy',
            optimizer=adam)

        # categorical_crossentropy 用来做多分类问题
        # binary_crossentropy 用来做多标签分类问题

        return model
