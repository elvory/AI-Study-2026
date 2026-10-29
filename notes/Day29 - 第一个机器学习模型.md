---
tags:
  - 主题/机器学习
  - 类型/每日笔记
aliases:
  - "Day29"
---

# Day29 - 第一个机器学习模型

## 一、今日学习目标

使用 scikit-learn 完成一个完整的机器学习分类流程。

## 二、鸢尾花数据集

```
from sklearn.datasets import load_iris

iris_data = load_iris()

X = iris_data.data
y = iris_data.target
```

- `X`：特征数据，形状为 `(150, 4)`。
    
- `y`：标签数据，形状为 `(150,)`。
    
- 数据集包含 3 种鸢尾花，每种有 50 个样本。
    
- 每个样本有 4 个特征。
    

## 三、划分训练集和测试集

```
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

- `test_size=0.2`：20% 的数据用于测试。
    
- `random_state=42`：固定随机划分，方便复现。
    
- `stratify=y`：尽量保持各类别的比例。
    

划分结果：120 条训练数据、30 条测试数据。

## 四、训练 KNN 分类模型

```
from sklearn.neighbors import KNeighborsClassifier

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)
```

KNN（K 近邻算法）的基本思想：根据新样本附近的 K 个邻居进行类别判断。

- `n_neighbors=3`：使用 3 个近邻进行预测。
    
- `fit()`：使用训练数据训练模型。
    

## 五、预测与评估

```
from sklearn.metrics import accuracy_score

predictions = knn_model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(predictions)
print(y_test)
print(accuracy)
```

- `predict()`：预测样本类别。
    
- `accuracy_score()`：计算预测正确的比例。
    

本次运行结果：测试集准确率为 `1.0`，即 100%。

注意：这是一次测试划分上的结果，不能据此认定模型在所有新数据上都能达到 100% 准确率。

## 六、预测一朵新花

```
new_flower = [[5.0, 3.4, 1.5, 0.2]]

predicted_label = knn_model.predict(new_flower)
predicted_name = iris_data.target_names[predicted_label[0]]

print(predicted_name)
```

预测结果：`setosa`。

四个输入值依次代表花萼长度、花萼宽度、花瓣长度、花瓣宽度。

## 七、今日核心知识

|方法|作用|
|---|---|
|`load_iris()`|加载鸢尾花数据|
|`train_test_split()`|划分训练集和测试集|
|`KNeighborsClassifier()`|创建 KNN 分类模型|
|`fit()`|训练模型|
|`predict()`|预测类别|
|`accuracy_score()`|计算准确率|

## 八、学习总结

今天完成了第一个机器学习实战，理解了从读取数据、划分数据、训练模型，到预测和评估的完整流程。

下一步：Day30 继续机器学习基础，学习如何通过混淆矩阵等方法分析分类模型的预测结果。

---

## 知识关联

- 主题入口：[[maps/机器学习|机器学习]]
- 相关知识：[[notes/Day27 - 机器学习基础概念|Day27]] · [[notes/Day26 - Pandas 数据处理|Day26]]
