import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

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

# 3. 训练决策树
tree_model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)
tree_model.fit(X_train, y_train)

# 4. 绘制决策树
plt.figure(figsize=(16, 8))

plot_tree(
    tree_model,
    feature_names=iris_data.feature_names,
    class_names=iris_data.target_names,
    filled=True,    # 表示给树节点填充颜色
    rounded=True
)

plt.show()
# 默认情况下会等待窗口关闭。才执行后面的代码


# 但实际开发中，有时候我们希望直接查看模型学到了哪些判断规则。
# export_text() 会将决策树转换成文本形式，方便我们分析模型的判断过程。
from sklearn.tree import export_text

tree_rules = export_text(
    tree_model,
    feature_names=list(iris_data.feature_names)
)

print(tree_rules)
