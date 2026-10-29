---
tags:
  - 主题/机器学习
  - 类型/每日笔记
aliases:
  - "Day30"
---

# Day30 - 机器学习模型评估

## 一、今日学习目标

掌握分类模型常用的评估指标：

- 混淆矩阵（Confusion Matrix）
    
- 准确率（Accuracy）
    
- 精确率（Precision）
    
- 召回率（Recall）
    
- F1-score
    
- classification_report()
    

## 二、混淆矩阵

混淆矩阵用于分析分类模型的预测结果。

```
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, predictions)
print(cm)
```

本次鸢尾花模型运行结果：

```
[[10  0  0]
 [ 0 10  0]
 [ 0  0 10]]
```

含义：

- 行表示真实类别。
    
- 列表示预测类别。
    
- 主对角线表示预测正确的数量。
    
- 非对角线表示预测错误的数量。
    

本次 30 条测试数据全部预测正确。

## 三、准确率 Accuracy

准确率表示所有预测中，预测正确的比例。

公式：

Accuracy = 正确预测数量 / 总预测数量

例如：

30 条测试数据全部预测正确：

Accuracy = 30 / 30 = 100%

## 四、精确率 Precision

精确率表示：

模型预测为某一类别的样本中，有多少真正属于该类别。

公式：

Precision = TP / (TP + FP)

其中：

- TP：真正例
    
- FP：假正例
    

例如：

模型预测了 10 封垃圾邮件，其中 8 封确实是垃圾邮件。

Precision = 8 / 10 = 80%

## 五、召回率 Recall

召回率表示：

实际属于某一类别的样本中，有多少被模型成功识别出来。

公式：

Recall = TP / (TP + FN)

其中：

- TP：真正例
    
- FN：假负例
    

例如：

实际存在 20 封垃圾邮件，模型成功找到 15 封。

Recall = 15 / 20 = 75%

## 六、F1-score

F1-score 是 Precision 和 Recall 的调和平均数。

公式：

F1 = 2 × Precision × Recall / (Precision + Recall)

当 Precision 和 Recall 都很高时，F1-score 通常也较高。

## 七、classification_report()

scikit-learn 可以直接生成分类评估报告。

```
from sklearn.metrics import classification_report

report = classification_report(
    y_test,
    predictions,
    target_names=iris_data.target_names
)

print(report)
```

报告包含：

|指标|作用|
|---|---|
|precision|精确率|
|recall|召回率|
|f1-score|综合衡量精确率和召回率|
|support|每个类别的真实样本数量|
|accuracy|整体准确率|
|macro avg|各类别指标的简单平均|
|weighted avg|按类别样本数量加权的平均|

## 八、今日实验结果

使用 Iris 数据集与 KNN 分类模型：

- 训练集：120 条
    
- 测试集：30 条
    
- KNN：n_neighbors=3
    
- Accuracy：100%
    
- Precision：1.00
    
- Recall：1.00
    
- F1-score：1.00
    

注意：100% 仅代表本次测试集的表现，不代表模型面对所有新数据时都不会出错。

## 九、今日总结

1. 混淆矩阵可以分析模型具体错在哪里。
    
2. Accuracy 衡量整体预测正确的比例。
    
3. Precision 关注预测结果的可靠程度。
    
4. Recall 关注实际正类被找出的程度。
    
5. F1-score 综合衡量 Precision 和 Recall。
    
6. classification_report() 可以快速生成分类评估报告。
    

## 十、学习进度

- Day30：分类模型评估已完成。
    
- 下一步：Day31，继续 Week5 机器学习实战。

---

## 知识关联

- 主题入口：[[maps/机器学习|机器学习]]
- 相关知识：[[notes/Day29 - 第一个机器学习模型|Day29]]
