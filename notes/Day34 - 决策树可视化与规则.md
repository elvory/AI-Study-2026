
## 一、今日学习目标

1. 使用 `plot_tree()` 可视化决策树。
    
2. 理解 Gini、Samples、Value。
    
3. 使用 `export_text()` 提取决策树规则。
    
4. 根据决策树规则进行手动预测。
    

## 二、决策树可视化

```
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(16, 8))

plot_tree(
    tree_model,
    feature_names=iris_data.feature_names,
    class_names=iris_data.target_names,
    filled=True,
    rounded=True
)

plt.show()
```

主要参数：

- `feature_names`：显示特征名称。
    
- `class_names`：显示类别名称。
    
- `filled=True`：填充节点颜色。
    
- `rounded=True`：使用圆角节点。
    

## 三、理解决策树节点

例如：

```
petal length (cm) <= 2.45
gini = 0.667
samples = 120
value = [40, 40, 40]
class = setosa
```

### 1. Gini（基尼不纯度）

衡量节点中不同类别的混杂程度。

- Gini 越小，节点越纯净。
    
- Gini = 0，表示节点中所有训练样本属于同一类别。
    
- Gini 越大，类别越混杂。
    

### 2. Samples

表示到达当前节点的训练样本数量。

例如：

`samples = 120`

说明当前节点包含 120 个训练样本。

### 3. Value

表示当前节点中各类别的样本数量。

例如：

```
value = [40, 40, 40]
```

分别表示：

- setosa：40
    
- versicolor：40
    
- virginica：40
    

### 4. Class

表示当前节点预测的类别。

通常选择当前节点中样本数量最多的类别。

## 四、决策树分支

判断条件成立：

```
True → 左分支
```

判断条件不成立：

```
False → 右分支
```

不断判断，直到到达叶子节点。

## 五、提取决策树规则

```
from sklearn.tree import export_text

tree_rules = export_text(
    tree_model,
    feature_names=list(iris_data.feature_names)
)
```