# ACP Canvas 关键行为示例 0.2.x（正在编写）
基于 `ACP Canvas 0.2.x`，对常见的Chat环境进行优化。

Cognitor包含了`[用户(User), LLM(Gemini), Fhrsk]`
## 基本
**基本示例(LANG=English)：**
```xml
<Canvas>
	<Cell originator="User" seq="0" type="EXEC">
		<value>
		print("Hello from stdout!")
		a = 1 + 2
		print(a)
		a
		</value>
	</Cell>
	<Cell originator="Gemini" seq="0" type="OUTPUT">
	    <depends_on>
           <cell originator="User" seq="0" />
        </depends_on>
	    <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="0">
	        <message>收到来自用户的 Cell。推断属性：type="EXEC",  originator="User"。</message>
	        <log_entry_type value="SystemEvent"/>
	    </log>
	    <log originator="Gemini" type="LLM Agent" log_level="DEBUG" seq="1">
	        <message>执行语句 1：print("Hello from stdout!")</message>
	        <log_entry_type value="ActionPlan"/>
	    </log>
	    <stdout originator="Gemini" seq="0">Hello from stdout!</stdout>
	    <log originator="Gemini" type="LLM Agent" log_level="DEBUG" seq="2">
	        <message>执行语句 2：a = 1 + 2。计算 1 + 2 = 3。将 3 赋值给变量 'a'。</message>
	        <log_entry_type value="ReasoningNarrative"/>
	    </log>
	    <log originator="Gemini" type="LLM Agent" log_level="DEBUG" seq="3">
	        <message>执行语句 3：print(a)。变量 'a' 的值为 3。</message>
	        <log_entry_type value="ActionPlan"/>
	    </log>
	    <stdout originator="Gemini" seq="1">3</stdout>
	    <log originator="Gemini" type="LLM Agent" log_level="DEBUG" seq="4">
	        <message>执行语句 4：a。这是最后一条语句。变量 'a' 的值为 3。将此值设置为 Cell 的最终值。</message>
	        <log_entry_type value="ReasoningNarrative"/>
	    </log>
	    <value originator="Gemini">3</value>
	</Cell>
<Canvas>
```
