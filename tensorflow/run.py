import tensorflow as tf;
# 加载数据集，mnist数据集是非常常用的数据集
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data() # load_data()函数返回两个元组，分别表示训练集和测试集
x_train, x_test = x_train / 255.0, x_test / 255.0

# 堆叠层 tf.keras.Sequential模型 是什么？
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
predictions

tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)


loss_fn(y_train[:1], predictions).numpy()

# 这里用到了最优化算法，adam 
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)