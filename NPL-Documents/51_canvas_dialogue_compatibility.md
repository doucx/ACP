# Canvas对话兼容规范
## 简介
在用户与`Agent`只能通过`对话`方式进行互动时，需要一个**兼容规范**来运行**NPL Canvas**。

否则，Agent容易理解错误，导致出现下列问题：
- 不遵守格式
- 回答不全
- 只创建一个单元格

## 规范
```xml
<CanvasSection role="User/Agent" num="{分块编号}">
</CanvasSection>
```
属性：
- role: 标注当前的角色是 User 还是 Agent。
- num: 分块编号，从0开始递增。
	- 用户：在对话模式中，通常为`[0, 2 ,4, 6, ...]`，可以不用填写。
	- Agent：在对话模式中，通常为`[1, 3, 5 , 7, ...]`，Agent 必须填写该项。

不再使用`<Canvas>`标记来表示整个画布，而是采用`<CanvasSection>`来表示`<Canvas>`的各个分块。多个`<CanvasSection>`将表示同一个`<Canvas>`上下文。用户输入和Agent回答都需要被完全包括在该块内。

Agent 必须将 `<CanvasSection>` 块放在markdown代码块中以便观察。

示例：
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
	<!--基于Canvas规则，可能创建其它Cell-->
</CanvasSection>
```