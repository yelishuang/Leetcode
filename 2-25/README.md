LC_!独立完成
复习其它，异或方法，还有python的列表拼接操作

### tip
在Python中，nums = nums[k+1:] + nums[0:k+1] 和 nums[:] = nums[k+1:] + nums[0:k+1] 这两种操作看起来很相似，但实际上它们有重要的区别，主要涉及到是否修改原对象以及对列表的影响。

nums = nums[k+1:] + nums[0:k+1]
创建新对象：这个语句首先计算右侧的表达式，生成一个新的列表对象，然后将 nums 变量指向这个新的列表。这意味着原来的 nums 列表对象没有被修改，而是让 nums 变量指向了一个全新的列表。
影响：如果 nums 是某个函数外定义的全局变量，并且你在函数内部使用了这条语句，那么仅局部改变了 nums 的引用，不会影响到外部的 nums 列表本身。
nums[:] = nums[k+1:] + nums[0:k+1]
就地修改：这里的 nums[:] 表示对 nums 列表的所有元素进行就地替换（in-place replacement）。右侧的表达式计算出的结果会直接替换掉 nums 中原有的元素，而不会改变 nums 所指向的对象。
影响：这种方式会修改原始列表的内容而不改变其引用。因此，任何对该列表的引用都会看到更新后的结果。这在需要确保所有引用同步更新的情况下非常有用。
示例