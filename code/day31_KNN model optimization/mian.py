from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris_data = load_iris()
feature_data = iris_data.data
label_data = iris_data.target

X_train, X_test, y_train, y_test = train_test_split(
    feature_data,
    label_data,
    test_size=0.2,
    random_state=42,
    stratify=label_data
)

k_values = [1, 3, 5, 15]

for k in k_values:
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(X_train, y_train)

    predictions = knn_model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"K = {k}, 准确率 = {accuracy}")


# KNN 的 K 值是什么
# 预测新样本时，参考距离最近的 k 个训练样本，通常通过多数投票决定类别。




# 为什么 KNN 需要特征标准化
# KNN 通过计算样本之间的距离来寻找邻居

from sklearn.preprocessing import StandardScaler

# 1. 创建标准化工具
scaler = StandardScaler()

# 2. 标准化训练集和测试集
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)

# 3. 训练标准化后的 KNN 模型
scaled_knn_model = KNeighborsClassifier(n_neighbors=3)
scaled_knn_model.fit(scaled_X_train, y_train)

# 4. 预测并评估
scaled_predictions = scaled_knn_model.predict(scaled_X_test)
scaled_accuracy = accuracy_score(y_test, scaled_predictions)

print("标准化后的 KNN 准确率：", scaled_accuracy)



# 比较标准化后不同 K 值的表现
scaled_k_values = [1, 3, 5, 7, 15]

for k in scaled_k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(scaled_X_train, y_train)

    scaled_test_predictions = model.predict(scaled_X_test)
    score = accuracy_score(y_test, scaled_test_predictions)

    print(f"标准化后 K={k}, 准确率={score:.4f}")


# 今天最重要的结论：
# - K 值会影响模型的分类结果。
# - 标准化会改变样本之间的距离，因此不一定提高准确率。
# - 不能只看一次测试结果，就认定某个参数永远最好。

# 测试集主要用于最终评估，参数选择应优先使用交叉验证。



### 交叉验证（Cross-validation）
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline

# 比较不同 K 值的交叉验证表现
cv_k_values = [1, 3, 5, 7, 15]

for k in cv_k_values:
    cv_model = make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=k)
    )

    cv_scores = cross_val_score(
        cv_model,
        X_train,
        y_train,
        cv=5,
        scoring="accuracy"
    )

    print(f"K={k}, 平均交叉验证准确率={cv_scores.mean():.4f}")
