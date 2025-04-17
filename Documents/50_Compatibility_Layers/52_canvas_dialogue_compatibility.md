# ACP Canvas 对话兼容层规范补充
## 设计背景  

继承于 [[51_diactue_compatibility]]。

当 Commonspace 是 Canvas 时，从逻辑上维持整个 Canvas 根节点内容的连续性。

确保：
1. **行为一致性** - 强制Agent遵守Commonspace状态机逻辑
2. **错误预防** - 解决传统对话模式导致的三大问题： 
   - 格式违规（如缺失关键属性）  
   - 响应不完整（如忽略多轮交互需求）  
   - 单单元谬误（违反Canvas的Node链式处理原则）  

## 语法规范  

格式：

``````xml
<CommonspaceSection>
<!-- 当前产生的ct，完整Node链等，及其内部内容 -->
</CommonspaceSection>
``````

采用多个`CommonspaceSection`替代完整的`Canvas`上下文：
如 ：
User：

``````xml
<CommonspaceSection>
<!-- User 创建的 ct，完整Node链等，及其内部内容 -->
</CommonspaceSection>
``````
 
Agent: 

``````xml
<CommonspaceSection>
<!-- Agent 创建的 ct，完整Node链等，及其内部内容 -->
</CommonspaceSection>
``````

等价于：

```xml
<Canvas>
     <!-- User 创建的 ct，完整Node链等，及其内部内容 -->
     <!-- Agent 创建的 ct，完整Node链等，及其内部内容 -->
</Canvas>
```
