# ACP Textual Arena 对话兼容层规范  
## 设计背景  
当`User`与`LLM Agent`仅能通过某种对话界面以对话形式交互时，本规范确保：  
1. **上下文完整性** - 在非结构化对话中，从逻辑上维持整个 Textual Arena Context 完整性
2. **行为一致性** - 强制 Agent 遵守 Arena 逻辑
3. **渲染正确性** - 由于聊天界面通常采用 markdown 渲染器，且有的 markdown 渲染器不支持 html 渲染，使用此规范可以规避渲染的错误

注：同时作为 ACP Tracer 的兼容层规范。

## 语法规范  
格式：
需要将 ArenaSection 放在六个反引号内，以避免代码块层级冲突。
``````xml
<ArenaSection role="User|Agent">
// Arena 切片
</ArenaSection>
``````

采用多个`ArenaSection`替代完整的`Arena`上下文：

如 ：
User：
``````xml
<ArenaSection role="User">
123 // User 创建的 完整内容
</ArenaSection>
``````
 
Agent: 
``````xml
<ArenaSection role="Agent">
abc // Agent 创建的 完整内容
</ArenaSection>
``````

Arena 就是：

``````txt
123 // User 创建的 完整内容
abc // Agent 创建的 完整内容
``````

### 关键属性  
| 属性     | 取值               | 强制要求 | 说明       |
| ------ | ---------------- | ---- | -------- |
| `role` | `User` / `Agent` | 双方必需 | 声明交互主体类型 |
