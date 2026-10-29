from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. 加载数据
iris_data = load_iris()
X = iris_data.data
y = iris_data.target

# 2. 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 3. 创建决策树模型
tree_model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

# 4. 训练模型
tree_model.fit(X_train, y_train)

# 5. 预测
predictions = tree_model.predict(X_test)

# 6. 计算准确率
accuracy = accuracy_score(y_test, predictions)
print("决策树准确率：", accuracy)





# 比较不同决策树深度
depth_values = [1, 2, 3, 5, None]

for depth in depth_values:
    depth_model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    depth_model.fit(X_train, y_train)

    train_predictions = depth_model.predict(X_train)
    test_predictions = depth_model.predict(X_test)

    train_accuracy = accuracy_score(y_train, train_predictions)
    test_accuracy = accuracy_score(y_test, test_predictions)

    print(
        f"深度={depth}, "
        f"训练准确率={train_accuracy:.4f}, "
        f"测试准确率={test_accuracy:.4f}"
    )
