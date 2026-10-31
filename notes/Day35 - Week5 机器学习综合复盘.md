

## 一、今日学习目标

通过独立编程，复习 Week5 学习的机器学习知识，掌握完整的机器学习基本流程。

## 二、独立编程：鸢尾花分类实验

### 1. 导入工具

```
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
```

### 2. 加载数据集

```
iris_data = load_iris()

X = iris_data.data
y = iris_data.target
```

- X：特征数据。
    
- y：标签数据。
    
- 数据集包含 150 个样本，每个样本有 4 个特征。
    

### 3. 划分训练集和测试集

```
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

划分结果：

|数据|形状|
|---|---|
|X_train|(120, 4)|
|X_test|(30, 4)|
|y_train|(120,)|
|y_test|(30,)|

### 4. 创建并训练 KNN 模型

```
review_knn_model = KNeighborsClassifier(n_neighbors=3)

review_knn_model.fit(X_train, y_train)
```

- `KNeighborsClassifier()`：创建 KNN 分类模型。
    
- `n_neighbors=3`：使用最近的 3 个邻居进行多数投票。
    
- `fit()`：使用训练集训练模型。
    

### 5. 预测测试集

```
review_predictions = review_knn_model.predict(X_test)

print("预测结果：", review_predictions)
```

`predict()`：使用训练好的模型预测新数据。

### 6. 计算准确率

```
review_accuracy = accuracy_score(y_test, review_predictions)

print("模型准确率：", review_accuracy)
```

本次实验结果：

```
模型准确率：1.0
```

即测试集准确率为 100%。

注意：这仅代表本次 30 条测试数据的预测表现，不代表模型对所有新数据都能达到 100%。

---

## 三、Week5 知识体系复习

### Day29：第一个机器学习模型

- scikit-learn 基础使用
    
- Iris 鸢尾花数据集
    
- 特征 X 与标签 y
    
- 训练集与测试集
    
- KNN 分类算法
    
- `fit()`、`predict()`
    

### Day30：机器学习模型评估

- 混淆矩阵 `confusion_matrix()`
    
- 准确率 Accuracy
    
- 精确率 Precision
    
- 召回率 Recall
    
- F1-score
    
- `classification_report()`
    

### Day31：KNN 模型优化

- K 值对模型表现的影响
    
- 特征标准化 `StandardScaler`
    
- 交叉验证 `cross_val_score()`
    
- 训练集与测试集的正确使用
    

### Day32：自动参数搜索

- `GridSearchCV`
    
- `best_params_`
    
- `best_score_`
    
- 5 折交叉验证
    
- 参数选择与最终测试的区别
    

### Day33：决策树与过拟合

- `DecisionTreeClassifier`
    
- `max_depth`
    
- 训练准确率与测试准确率
    
- 欠拟合（Underfitting）
    
- 过拟合（Overfitting）
    
- 模型泛化能力
    

### Day34：决策树可视化与规则

- `plot_tree()`
    
- Gini 基尼不纯度
    
- Samples、Value、Class
    
- `export_text()`
    
- 根据判断条件进行手动预测
    

### Day35：机器学习综合复盘

- 独立加载数据
    
- 独立划分数据集
    
- 创建并训练 KNN
    
- 使用测试集预测
    
- 计算模型准确率
    

---

## 四、Week5 核心函数速查

|函数或属性|作用|
|---|---|
|`load_iris()`|加载鸢尾花数据|
|`train_test_split()`|划分训练集和测试集|
|`KNeighborsClassifier()`|创建 KNN 模型|
|`DecisionTreeClassifier()`|创建决策树模型|
|`fit()`|训练模型|
|`predict()`|预测结果|
|`accuracy_score()`|计算准确率|
|`confusion_matrix()`|生成混淆矩阵|
|`StandardScaler()`|特征标准化|
|`cross_val_score()`|交叉验证|
|`GridSearchCV()`|自动搜索参数|
|`plot_tree()`|绘制决策树|
|`export_text()`|提取决策树规则|

## 五、Week5 学习总结

本周完成了从机器学习基础概念到实际模型训练的初步过渡。

已经能够在指导下完成：

1. 加载和处理机器学习数据集。
    
2. 划分训练集和测试集。
    
3. 使用 KNN 和决策树进行分类。
    
4. 使用准确率、混淆矩阵等指标评估模型。
    
5. 使用交叉验证和 GridSearchCV 优化参数。
    
6. 理解决策树、过拟合与欠拟合。
    

### 需要继续加强的地方

- 提高独立编写机器学习代码的能力。
    
- 加强对模型原理的理解。
    
- 熟练掌握模型评估和参数优化。
    
- 增加真实数据集上的实践。
    

## 六、下一阶段学习计划

Week6 开始逐步进入深度学习阶段。

计划学习：

- PyTorch 基础
    
- Tensor 与张量运算
    
- 自动求导
    
- 神经网络基础
    
- 模型训练与损失函数
    

为后续 Transformer、LLM、Embedding、RAG 和 Agent 学习做准备。

---

**Week5 状态：已完成（Day29–Day35）**

**下一阶段：Week6 · Day36**