# ACP Textual Arena 对话兼容层规范  
## 设计背景  
当`User`与`LLM Agent`仅能通过某种对话界面以对话形式交互时，本规范确保：  
1. **上下文完整性** - 在非结构化对话中，从逻辑上维持整个 Textual Arena Context 完整性
2. **行为一致性** - 强制 Agent 遵守 Arena 逻辑

注：同时作为 ACP Tracer 的兼容层规范。

## 语法规范  
格式：
<ContextSection role="User|Agent">
// 空行
// ArenaContext 切片
// 空行
</ContextSection>

采用多个`ContextSection`替代完整的`ArenaContext`上下文：

如 ：
User：
<ContextSection role="User">

123 // User 生成的 完整内容

 </ContextSection>
 
Agent: 
 <ContextSection role="Agent">
 
abc // Agent 生成的 完整内容

 </ContextSection>

ArenaContext 就是：

123 // User 生成的 完整内容
abc // Agent 生成的 完整内容

### 关键属性  
| 属性     | 取值               | 强制要求 | 说明       |
| ------ | ---------------- | ---- | -------- |
| `role` | `User` / `Agent` | 双方必需 | 声明交互主体类型 |