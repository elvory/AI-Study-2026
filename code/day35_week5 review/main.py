### 1.使用 load_iris() 加载鸢尾花数据集
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


### 加载数据
iris_data = load_iris()


# 将特征保存到 X，标签保存到 y
X = iris_data.data
y = iris_data.target


# 使用 train_test_split() 划分数据集
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,   # 20% 用作测试集
    random_state=42,    # 固定随机种子
    stratify=y      # 按类别比例分层抽样
)

print("训练集特征：", X_train.shape)
print("测试集特征：", X_test.shape)
print("训练集标签：", y_train.shape)
print("测试集标签：", y_test.shape)




### 2.创建并训练 KNN 模型

# 导入工具
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
## KNeighborsClassifier：创建 KNN 分类模型
## accuracy_score：计算模型预测准确率


# 创建 KNN 模型
review_knn_model = KNeighborsClassifier(n_neighbors=3)
# n_neighbors=3：预测时参考最近的 3 个邻居


# 使用训练集训练模型
review_knn_model.fit(X_train, y_train)
# .fit()：让模型学习训练集中的特征和标签




### 3.使用模型进行预测

# 使用测试集进行预测
review_predictions = review_knn_model.predict(X_test)

# 打印预测结果
print("预测结果：", review_predictions)




### 4.计算模型准确率

# 计算模型准确率
review_accuracy = accuracy_score(y_test, review_predictions)

print("模型准确率：", review_accuracy)
