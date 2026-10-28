from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. 加载数据
iris_data = load_iris()
X = iris_data.data
y = iris_data.target

# 2. 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 3. 创建标准化 + KNN 流程
pipeline = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier()
)

# 4. 设置需要尝试的 K 值
param_grid = {
    "kneighborsclassifier__n_neighbors": [1, 3, 5, 7, 9, 11, 15]
}

# 5. 自动搜索最佳参数---重点
grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring="accuracy"
)

grid_search.fit(X_train, y_train)

# 6. 查看结果
print("最佳参数：", grid_search.best_params_)
print("最佳交叉验证准确率：", grid_search.best_score_)

# 7. 在测试集上评估最佳模型
predictions = grid_search.predict(X_test)
print("测试集准确率：", accuracy_score(y_test, predictions))
