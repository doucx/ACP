# NPL Canvas 对话兼容层规范  
## 设计背景  
当用户与`Agent`仅能通过对话形式交互时，本规范确保：  
1. **上下文完整性** - 在非结构化对话中维持Canvas的XML语义  
2. **行为一致性** - 强制Agent遵守Runtime状态机逻辑  
3. **错误预防** - 解决传统对话模式导致的三大问题：  
   - 格式违规（如缺失关键属性）  
   - 响应不完整（如忽略多轮交互需求）  
   - 单单元格谬误（违反Canvas的Cell链式处理原则）  

## 语法规范  
采用分块式XML结构替代完整Canvas封装：  
```xml
<CanvasSection role="User|Agent" num="{区块序号}">
    <!-- 当前产生的完整Cell链 -->
</CanvasSection>
```

### 关键属性  
| 属性     | 取值               | 强制要求            | 说明                                                   |
| ------ | ---------------- | --------------- | ---------------------------------------------------- |
| `role` | `User` / `Agent` | 双方必需            | 声明交互主体类型                                             |
| `num`  | 整数序列             | Agent强制，用户可选 | 对话轮次编号，遵循：用户发起端：0,2,4,... 代理响应端：1,3,5,... |

### 实现要求  
1. **Agent义务**  
   - 必须将响应内容包裹在标准的markdown XML代码块中：  
 ```xml
 <CanvasSection role="Agent" num="3">
	 <!-- 响应内容：完整Cell链 -->
 </CanvasSection>
 ```
   - 需完整继承并扩展前序`CanvasSection`的上下文  

2. **用户建议**  
    - 推荐但不强制使用`num`属性  
    - 允许简化属性标注（如仅声明`role="User"`）  

## 合规性示例  
### 标准交互流程  
用户（Alice）输入：
```xml
<CanvasSection role="User">
	<Cell requester="Alice">
		print("Hello from stdout!")
		a = 1 + 2
		print(a)
		a
	</Cell>
</CanvasSection>
```
Agent（Gemini）回答（包括"\`\`\`"代码块）：
```xml
<CanvasSection role="Agent">
	<Cell type="OUTPUT" round="0" requester="User" originator="Gemini">
		<stdout num="0" originator="Gemini">Hello from stdout!</stdout>
	</Cell>
	<!--基于Canvas Runtime规则，可能创建其它Cell-->
</CanvasSection>
```