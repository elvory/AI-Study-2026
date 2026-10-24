from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

# 1. 加载数据
iris_data = load_iris()
X = iris_data.data
y = iris_data.target

# 2. 划分数据集
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 3. 训练模型
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

# 4. 预测
predictions = knn_model.predict(X_test)

# 5. 生成混淆矩阵
cm = confusion_matrix(y_test, predictions)

print("混淆矩阵：")
print(cm)



from sklearn.metrics import classification_report

report = classification_report(
    y_test,
    predictions,
    target_names=iris_data.target_names
)

print(report)
