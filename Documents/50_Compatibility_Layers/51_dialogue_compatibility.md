# ACP Textual Commonspace 对话兼容层规范  
## 设计背景  
当`User`与`LLM Agent`仅能通过某种对话界面以对话形式交互时，本规范确保：  
1. **上下文完整性** - 在非结构化对话中，从逻辑上维持整个 Textual Commonspace Context 完整性
2. **行为一致性** - 强制 Agent 遵守 Commonspace 逻辑
3. **渲染正确性** - 由于聊天界面通常采用 markdown 渲染器，且有的 markdown 渲染器不支持 html 渲染，使用此规范可以规避渲染的错误

## 语法规范  
格式：
需要将 CommonspaceSection 放在六个反引号内，以避免代码块层级冲突。
``````xml
<CommonspaceSection>
// Commonspace 切片
</CommonspaceSection>
``````

采用多个`CommonspaceSection`替代完整的`Commonspace`上下文：

如 ：
User：
``````xml
<CommonspaceSection>
123 // User 创建的 完整内容
</CommonspaceSection>
``````
 
LLM Agent: 
``````xml
<CommonspaceSection>
abc // Agent 创建的 完整内容
</CommonspaceSection>
``````

Commonspace 内容就是：

``````txt
123 // User 创建的 完整内容
abc // Agent 创建的 完整内容
``````
