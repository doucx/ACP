# ACP Textual Arena 对话兼容层规范  
## 设计背景  
当用户与`LLM Agent`仅能通过某种对话界面以对话形式交互时，本规范确保：  
1. **上下文完整性** - 在非结构化对话中维持整个 Textual Arena Context 完整性
2. **行为一致性** - 强制 Agent 遵守 Arena 逻辑

## 语法规范  
格式：
```xml
<ContextSection role="User|Agent">
    <!-- 当前产生的ArenaLog，完整Cell链等，及其内部内容 -->
</ContextSection>
```

采用多个`ContextSection`替代完整`ArenaContext`：
如 ：
User 输入 :
```xml
<ContextSection role="User">
	 <!-- User 的 ArenaContext 切片 -->
 </ContextSection>
 ```
 
Agent 响应 : 
```xml
 <ContextSection role="Agent">
	 <!-- Agent 的 ArenaContext 切片 -->
 </ContextSection>
```

等价于：

```xml
 <!-- User 的 ArenaContext 切片 -->
 <!-- Agent 的 ArenaContext 切片 -->
```


### 关键属性  
| 属性     | 取值               | 强制要求         | 说明                                        |
| ------ | ---------------- | ------------ | ----------------------------------------- |
| `role` | `User` / `Agent` | 双方必需         | 声明交互主体类型                                  |

### 实现要求  
**Agent 义务**:
   - 必须将响应内容包裹在标准的markdown XML代码块中：  
   
 ```xml
 <ContextSection role="Agent/User">
	 <!-- Agent 响应内容：完整Cell链，ArenaLog等 -->
 </ContextSection>
 ```

需完整继承并扩展前序`ContextSection`的上下文，