# NPL Canvas 关键行为示例 0.1.x（正在编写）
基于 `NPL Canvas`，对常见的Chat环境进行优化。

Cognitor包含了`[用户(User), LLM(Gemini), Fhrsk]`
## 基本
**基本示例(LANG=English)：**
```xml
<Canvas>
	<Cell requester="User">
	print("Hello from stdout!")
	a = 1 + 2
	print(a)
	a
	</Cell>
	<Cell type="OUTPUT" round="0" requester="User" originator="Gemini">
	    <log entity_id="Gemini" type="LLM Agent" log_level="INFO" log_number="0">
	        <message>Received Cell from User. Inferred attributes: type="EXEC", round="0", requester="User".</message>
	        <log_entry_type value="SystemEvent"/>
	    </log>
	    <log entity_id="Gemini" type="LLM Agent" log_level="DEBUG" log_number="1">
	        <message>Executing statement 1: print("Hello from stdout!")</message>
	        <log_entry_type value="ActionPlan"/>
	    </log>
	    <stdout num="0" originator="Gemini">Hello from stdout!</stdout>
	    <log entity_id="Gemini" type="LLM Agent" log_level="DEBUG" log_number="2">
	        <message>Executing statement 2: a = 1 + 2. Calculating 1 + 2 = 3. Assigning 3 to variable 'a'.</message>
	        <log_entry_type value="ReasoningNarrative"/>
	    </log>
	    <log entity_id="Gemini" type="LLM Agent" log_level="DEBUG" log_number="3">
	        <message>Executing statement 3: print(a). Variable 'a' has value 3.</message>
	        <log_entry_type value="ActionPlan"/>
	    </log>
	    <stdout num="1" originator="Gemini">3</stdout>
	    <log entity_id="Gemini" type="LLM Agent" log_level="DEBUG" log_number="4">
	        <message>Executing statement 4: a. This is the last statement. Variable 'a' has value 3. Setting this as the Cell's final value.</message>
	        <log_entry_type value="ReasoningNarrative"/>
	    </log>
	    <value originator="Gemini">3</value>
	</Cell>
<Canvas>
```