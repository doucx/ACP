# ACP Textual Arena 对话兼容层规范  
## 设计背景  
当`User`与`LLM Agent`仅能通过某种对话界面以对话形式交互时，本规范确保：  
1. **上下文完整性** - 在非结构化对话中，从逻辑上维持整个 Textual Arena Context 完整性
2. **行为一致性** - 强制 Agent 遵守 Arena 逻辑

注：同时作为 ACP Tracer 的兼容层规范。

## 语法规范  
格式：
```txt
<ContextSection role="User|Agent">
// 这里需要换行
// ArenaContext 切片
// 这里也需要换行
</ContextSection>
```

采用多个`ContextSection`替代完整的`ArenaContext`上下文：

如 ：
User（不包括\`\`\`txt）：
```txt
<ContextSection role="User">

// User 生成的 完整内容

 </ContextSection>
 ```
 
Agent （不包括\`\`\`txt）: 
```txt
 <ContextSection role="Agent">
 
// Agent 生成的 完整内容

 </ContextSection>
```

等价于：

```txt
// User 生成的 完整内容
// Agent 生成的 完整内容
```

### 关键属性  
| 属性     | 取值               | 强制要求         | 说明                                        |
| ------ | ---------------- | ------------ | ----------------------------------------- |
| `role` | `User` / `Agent` | 双方必需         | 声明交互主体类型                                  |

### 实现要求  
**Agent 义务**:
   - 回复必须以`<ContextSection role="Agent">`开头。此时它作为页面真正的xml标记使用。因此，请不要将它放在 xml 代码块中。
   
 ```txt
 <ContextSection role="Agent">

// Agent 生成的 完整内容

 </ContextSection>
 ```