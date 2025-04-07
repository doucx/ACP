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


## 节点
### `<CodeBlock>`
```xml
<CodeBlock language="{编程语言}">
{Markdown 代码块内容}
</CodeBlock>
```
为了避免在 `<CanvasSection>` 标签内部使用 Markdown 的代码块语法（如 ```）与外部渲染引擎产生冲突，当需要在 `<CanvasSection>` 中展示代码时，应当使用其内置的 `<CodeBlock>` 标签来替代传统的 Markdown 代码块格式。  

### 关键点说明：  
1. **问题背景**：  
   - 标准的 Markdown 代码块（如 ```code```）可能在 XML 结构的 `<CanvasSection>` 中引发解析冲突或渲染错误。  

2. **解决方案**：  
   - 使用 `<CanvasSection>` 原生的 `<CodeBlock>` 标签包裹代码内容，例如：  
     ```xml
     <CodeBlock language="python">
     print(2+2)
     </CodeBlock>
     ```  

3. **优势**：  
   - **避免冲突**：XML 标签与 Markdown 语法分离，确保正确解析。  
   - **结构化**：可通过属性（如 `language`）指定代码语言，增强可读性。  
   - **一致性**：保持 `<CanvasSection>` 内部数据格式的纯粹性（纯 XML）。  

### 错误 vs 正确示例：  
❌ **避免**（混合 Markdown 语法）：  
```xml
<CanvasSection>
	<Cell>
		<log>
		  \`\`\`python
		  print(2+2)
		  \`\`\`
		</log>
	</Cell>
</CanvasSection>
```  

✅ **推荐**（使用 `<CodeBlock>`）：  

```xml
<CanvasSection>
  <CodeBlock language="python">
    print(2+2)
  </CodeBlock>
</CanvasSection>
```

*   在日志中使用：
```xml
<log originator="Gemini" type="LLM Agent" log_level="INFO" log_number="0">
    <message>这是包含 Markdown 代码块的日志消息。</message>
    <CodeBlock language="python">
def hello_world():
    print("Hello, world!")
    </CodeBlock>
</log>
```

*   在 Fhrsk 的回复中使用：
```xml
<Fhrsk number="0">
    这是包含 Markdown 代码块的 Fhrsk 回复。
    <CodeBlock language="javascript">
console.log("Hello, world!");
    </CodeBlock>
</Fhrsk>
```

通过使用 `<CodeBlock>` 节点，可以清晰地将 Markdown 代码块与其他 XML 元素区分开来，从而提高代码的可读性和可维护性。

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
Agent（Gemini）回答：
```xml
\`\`\`
<CanvasSection role="Agent">
	<Cell type="OUTPUT" round="0" requester="User" originator="Gemini">
		<stdout num="0" originator="Gemini">Hello from stdout!</stdout>
	</Cell>
	<!--基于Canvas Runtime规则，可能创建其它Cell-->
</CanvasSection>
\`\`\`
```