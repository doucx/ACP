# ACP Canvas 对话兼容层规范补充
## 设计背景  

继承于 [[51_dialogue_compatibility]]。

当 ArenaContext 是 Canvas 时，从逻辑上维持整个 Canvas 根节点的连续性。

1. **上下文完整性** - 在非结构化对话中维持整个Canvas根节点
2. **行为一致性** - 强制Agent遵守Arena状态机逻辑
3. **错误预防** - 解决传统对话模式导致的三大问题： 
   - 格式违规（如缺失关键属性）  
   - 响应不完整（如忽略多轮交互需求）  
   - 单单元格谬误（违反Canvas的Node链式处理原则）  

## 语法规范  
格式：
```txt
<ContextSection role="User|Agent">
\`\`\`xml
    <!-- 当前产生的ArenaLog，完整Node链等，及其内部内容 -->
\`\`\`
</ContextSection>
```

采用多个`ContextSection`替代完整`Canvas`：
如 ：
User 输入 :
```txt
<ContextSection role="User">
\`\`\`xml
	 <!-- User 生成的 ArenaLog，完整Node链等，及其内部内容 -->
\`\`\`
 </ContextSection>
 ```
 
Agent 响应 : 
```txt
 <ContextSection role="Agent">
\`\`\`xml
	 <!-- Agent 生成的 ArenaLog，完整Node链等，及其内部内容 -->
\`\`\`
 </ContextSection>
```

等价于：

```xml
<Canvas>
	 <!-- User 生成的 ArenaLog，完整Node链等，及其内部内容 -->
	 <!-- Agent 生成的 ArenaLog，完整Node链等，及其内部内容 -->
 </Canvas>
```

## 节点
### `<CodeBlock>`

```xml
<CodeBlock language="{语言}">
{Markdown 代码块内容}
</CodeBlock>
```

为了避免在 `<ContextSection>` 标签内部使用 Markdown 的代码块语法（如 \`\`\`）与外部渲染引擎产生冲突，当 `Agent` 需要在 `<ContextSection>` 中展示代码时，应当使用其内置的 `<CodeBlock>` 标签来替代传统的 Markdown 代码块格式。  

#### 关键点说明

1. **问题背景**：  
   - 标准的 Markdown 代码块（如 ```code```）可能在 XML 结构的 `<ContextSection>` 中引发解析冲突或渲染错误。  

2. **解决方案**：  
   - 使用 `<CodeBlock>` 标签包裹代码内容，并且将内容顶格写，忽略 xml 缩进结构：例如：  
```xml
	<CodeBlock language="python(可以为任何语言)">
print(2+2) <!--这里是顶格的-->
	</CodeBlock>
```  

3. **优势**：  
   - **避免冲突**：XML 标签与 Markdown 语法分离，确保正确解析。  
   - **结构化**：可通过属性（如 `language`）指定代码语言，增强可读性。  
   - **一致性**：保持 `<ContextSection>` 内部数据格式的纯粹性（纯 XML）。  
   - **易读性**: 通过将代码顶格写，来便于阅读和复制。

#### 错误 vs 正确示例：  

❌ **避免**（混合 Markdown 语法，并且代码不顶格）：  
```xml
<ContextSection role="Agent">
	<Node>
		<log>
			\`\`\`python
			print(2+2)
			\`\`\`
		</log>
	</Node>
</ContextSection>
```  

✅ **推荐**（使用 `<CodeBlock>`，内容顶格）：  

```xml
<ContextSection role="Agent">
	<Node>
		<log>
		  <CodeBlock language="python">
print(2+2)
		  </CodeBlock>
		</log>
	</Node>
</ContextSection>
```

*   在日志中使用：

```xml
<log originator="Gemini" type="LLM Agent" log_level="INFO" seq="0">
    <message>这是包含 Markdown 代码块的日志消息。</message>
    <CodeBlock language="python">
def hello_world():
    print("Hello, world!")
    </CodeBlock>
</log>
```

*   在 value 中使用：

```xml
<value>
    <CodeBlock language="markdown">
# 总结：CodeBlock 是有意义的
### 原因
    </CodeBlock>
</value>
```

通过使用 `<CodeBlock>` 节点，可以清晰地将 Markdown 代码块与其他 XML 元素区分开来，从而提高代码的可读性和可维护性。