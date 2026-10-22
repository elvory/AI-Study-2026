# scikit-learn 是 Python 常用的机器学习库
from sklearn.datasets import load_iris

iris_data = load_iris()

X = iris_data.data
y = iris_data.target

print("特征数据形状：", X.shape)
print("标签数据形状：", y.shape)
print("花的类别：", iris_data.target_names)
print("第一朵花的特征：", X[0])
print("第一朵花的标签：", y[0])



# 划分 训练集 和 测试集
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("训练集特征：", X_train.shape)
print("测试集特征：", X_test.shape)
print("训练集标签：", y_train.shape)
print("测试集标签：", y_test.shape)


# 训练第一个机器学习模型
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. 创建模型
knn_model = KNeighborsClassifier(n_neighbors=3)

# 2. 使用训练集训练模型
knn_model.fit(X_train, y_train)

# 3. 使用测试集进行预测
predictions = knn_model.predict(X_test)

# 4. 计算准确率
accuracy = accuracy_score(y_test, predictions)

print("预测结果：", predictions)
print("真实标签：", y_test)
print("模型准确率：", accuracy)



# 预测一朵新花
new_flower = [[5.0, 3.4, 1.5, 0.2]]

predicted_label = knn_model.predict(new_flower)

predicted_name = iris_data.target_names[predicted_label[0]]

print("预测的花朵类别：", predicted_name)
