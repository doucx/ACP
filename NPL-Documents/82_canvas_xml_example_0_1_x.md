# NPL Canvas 关键行为示例 0.1.x（正在编写）
基于 `NPL Canvas`，对常见的Chat环境进行优化。

Cognitor包含了`[用户(User), LLM(Gemini), Fhrsk]`
## 基本
**基本示例(LANG=English)：**
```xml
<Canvas>
	<Cell requester="User" type="EXEC" index_of_type="0">
	print("Hello from stdout!")
	a = 1 + 2
	print(a)
	a
	</Cell>
	<Cell type="OUTPUT" round="0" requester="User" originator="Gemini" index_of_type="0">
	    <log entity_id="Gemini" type="LLM Agent" log_level="INFO" log_number="0">
	        <message>收到来自用户的 Cell。推断属性：type="EXEC", round="0", requester="User"。</message>
	        <log_entry_type value="SystemEvent"/>
	    </log>
	    <log entity_id="Gemini" type="LLM Agent" log_level="DEBUG" log_number="1">
	        <message>执行语句 1：print("Hello from stdout!")</message>
	        <log_entry_type value="ActionPlan"/>
	    </log>
	    <stdout num="0" originator="Gemini">Hello from stdout!</stdout>
	    <log entity_id="Gemini" type="LLM Agent" log_level="DEBUG" log_number="2">
	        <message>执行语句 2：a = 1 + 2。计算 1 + 2 = 3。将 3 赋值给变量 'a'。</message>
	        <log_entry_type value="ReasoningNarrative"/>
	    </log>
	    <log entity_id="Gemini" type="LLM Agent" log_level="DEBUG" log_number="3">
	        <message>执行语句 3：print(a)。变量 'a' 的值为 3。</message>
	        <log_entry_type value="ActionPlan"/>
	    </log>
	    <stdout num="1" originator="Gemini">3</stdout>
	    <log entity_id="Gemini" type="LLM Agent" log_level="DEBUG" log_number="4">
	        <message>执行语句 4：a。这是最后一条语句。变量 'a' 的值为 3。将此值设置为 Cell 的最终值。</message>
	        <log_entry_type value="ReasoningNarrative"/>
	    </log>
	    <value originator="Gemini">3</value>
	</Cell>
<Canvas>
```