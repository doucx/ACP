# ACP Canvas 对话兼容层规范补充
## 设计背景  

继承于 [[51_diactue_compatibility]]。

当 Arena 是 Canvas 时，从逻辑上维持整个 Canvas 根节点内容的连续性。

确保：
1. **行为一致性** - 强制Agent遵守Arena状态机逻辑
2. **错误预防** - 解决传统对话模式导致的三大问题： 
   - 格式违规（如缺失关键属性）  
   - 响应不完整（如忽略多轮交互需求）  
   - 单单元谬误（违反Canvas的Node链式处理原则）  

## 语法规范  

格式：

<ArenaSection role="User|Agent">
// 空行
<!-- 当前产生的ct，完整Node链等，及其内部内容 -->
// 空行
</ArenaSection>

采用多个`ArenaSection`替代完整的`Canvas`上下文：
如 ：
User：
<ArenaSection role="User">

 <!-- User 创建的 ct，完整Node链等，及其内部内容 -->

 </ArenaSection>
 
Agent: 

 <ArenaSection role="Agent">
 
 <!-- Agent 创建的 ct，完整Node链等，及其内部内容 -->

 </ArenaSection>



等价于：


<Canvas>
     <!-- User 创建的 ct，完整Node链等，及其内部内容 -->
     <!-- Agent 创建的 ct，完整Node链等，及其内部内容 -->
</Canvas>


## 节点
### `<CodeBlock>`

<CodeBlock language="{语言}">
{Markdown 代码块内容}
</CodeBlock>

为了避免在 `<ArenaSection>` 标签内部使用 Markdown 的代码块语法（如 ```）与外部渲染引擎产生冲突，当 `Agent` 需要在 `<ArenaSection>` 中展示代码时，应当使用 `<CodeBlock>` 标签来替代传统的 Markdown 代码块格式。  

#### 关键点说明

1. **问题背景**：  
   - 标准的 Markdown 代码块（如 ```code```）可能在 XML 结构的 `<ArenaSection>` 中引发解析冲突或渲染错误。  

2. **解决方案**：  
   - 使用 `<CodeBlock>` 标签包裹代码内容，并且将内容顶格写，忽略 xml 缩进结构：例如：  
	<CodeBlock language="python(可以为任何语言)">
print(2+2) <!--这里是顶格的-->
	</CodeBlock>

3. **优势**：  
   - **避免冲突**：XML 标签与 Markdown 语法分离，确保正确解析。  
   - **结构化**：可通过属性（如 `language`）指定代码语言，增强可读性。  
   - **一致性**：保持 `<ArenaSection>` 内部数据格式的纯粹性（纯 XML）。  
   - **易读性**: 通过将代码顶格写，来便于阅读和复制。

#### 错误 vs 正确示例：  

❌ **避免**（混合 Markdown 语法，并且代码不顶格）：  
<ArenaSection role="Agent">

<Node>
    <ct>
        ```python
        print(2+2)
        ```
    </ct>
</Node>

</ArenaSection>

✅ **推荐**（使用 `<CodeBlock>`，内容顶格）：  

<ArenaSection role="Agent">

<Node>
    <ct>
      <CodeBlock language="python">
print(2+2)
      </CodeBlock>
    </ct>
</Node>

</ArenaSection>

*   在认知轨迹中使用：

<ct originator="Gemini" type="LLM Agent" type="INFO" seq="0">
    <message>这是包含 Markdown 代码块的认知轨迹消息。</message>
    <CodeBlock language="python">
def hello_world():
    print("Hello, world!")
    </CodeBlock>
</ct>

*   在 value 中使用：

<value>
    <CodeBlock language="markdown">
# 总结：CodeBlock 是有意义的
### 原因
    </CodeBlock>
</value>

通过使用 `<CodeBlock>` 节点，可以清晰地将 Markdown 代码块与其他 XML 元素区分开来，从而提高代码的可读性和可维护性。
