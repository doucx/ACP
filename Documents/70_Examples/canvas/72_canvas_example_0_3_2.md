基于 `ACP Canvas 0.3.2`，对常见的Chat环境进行优化。

####  Fhrsk 交互

```xml
<Canvas>
    <!-- 用户发起请求 -->
    <Cell originator="AyeL" seq="0" type="EXEC">
        <value>
            chat 请帮我生成 0 到 4 的列表。
        </value>
    </Cell>

    <!-- Arena 处理 AyeL:0，推断路由并记录 -->
    <ArenaLog>
        <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="0">
            <message>处理 AyeL:0 (EXEC)。检测到 'chat' 关键字，推断用户意图为与 Fhrsk 交互。将请求路由至 Fhrsk。</message>
            <log_entry_type value="RoutingDecision"/>
        </log>
    </ArenaLog>

    <!-- Fhrsk 回应并计划下一步 -->
    <Cell originator="Fhrsk" seq="0" type="OUTPUT">
        <depends_on>
            <cell originator="AyeL" seq="0"/>
        </depends_on>
        <!-- Fhrsk 的回复直接作为 Cell 的主要价值 -->
        <value>好的，我将执行 `[i for i in range(5)]`</value>
        <flags>
            <!-- 指示 Arena 在此 Cell 后立即创建并执行 Fhrsk 的下一个动作 -->
            <flag value="ThenCreateCell"/>
        </flags>
    </Cell>

    <!-- Arena 处理 Fhrsk:0 的 ThenCreateCell flag -->
    <ArenaLog>
        <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="1">
            <message>处理 Fhrsk:0 (OUTPUT) 完成。检测到 'ThenCreateCell' flag。准备创建并执行由 Fhrsk 定义的下一个 Cell。</message>
            <log_entry_type value="StateTransition"/>
        </log>
    </ArenaLog>

    <!-- Fhrsk 创建并执行实际指令 -->
    <Cell originator="Fhrsk" seq="1" type="EXEC">
        <depends_on>
            <!-- 依赖于它上一步的决定 Cell -->
            <cell originator="Fhrsk" seq="0"/>
        </depends_on>
        <value>
            [i for i in range(5)]
        </value>
    </Cell>

    <!-- Arena 处理 Fhrsk:1 的执行请求 -->
    <ArenaLog>
         <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="2">
            <message>开始处理 Fhrsk:1 (EXEC)。准备执行代码。</message>
            <log_entry_type value="ActionPlan"/>
        </log>
    </ArenaLog>

    <!-- Arena 执行代码并返回最终结果 -->
    <Cell originator="Gemini" seq="0" type="OUTPUT">
	    <depends_on>
            <!-- 依赖于 Fhrsk 提交的 EXEC Cell -->
            <cell originator="Fhrsk" seq="1"/>
        </depends_on>
        <log originator="Gemini" type="LLM Agent" log_level="DEBUG" seq="0">
            <message>执行代码 `[i for i in range(5)]`。</message>
            <log_entry_type value="ActionPlan"/>
        </log>
         <log originator="Gemini" type="LLM Agent" log_level="DEBUG" seq="1">
            <message>计算结果为 [0, 1, 2, 3, 4]。</message>
            <log_entry_type value="ReasoningNarrative"/>
        </log>
        <value>[0, 1, 2, 3, 4]</value>
    </Cell>
</Canvas>
```

#### input() 交互
```xml
<Canvas>
    <Cell originator="AyeL" type="EXEC" seq="0">
        <value>
            name = input("请输入你的名字: ")
            print(f"你好, {name}!")
        </value>
    </Cell>

    <!-- Arena 处理 AyeL:0，遇到 input() -->
    <ArenaLog>
         <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="0">
            <message>开始处理 AyeL:0 (EXEC)。创建新`OUTPUT Cell`。</message>
            <log_entry_type value="StateTransition"/>
         </log>
    </ArenaLog>

    <!-- Arena 生成等待输入的 OUTPUT Cell -->
    <Cell originator="Gemini" type="OUTPUT" seq="0">
    	<depends_on>
            <cell originator="AyeL" seq="0"/>
        </depends_on>
        <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="0">
            <message>执行第一行 `name = input(...)`。遇到 `input()` 调用，需要暂停并等待用户输入。</message>
            <log_entry_type value="ReasoningNarrative"/>
         </log>
        <value type="INPUT_HINT">请输入你的名字:</value>
        <flags>
            <flag value="WAIT" />
        </flags>
    </Cell>

    <!-- 用户提供输入 -->
    <Cell originator="AyeL" type="INPUT" seq="1">
    	<depends_on>
		    <!-- 明确依赖于提示输入的 Cell -->
            <cell originator="Gemini" seq="0"/>
        </depends_on>
        <value>
            Alice
        </value>
    </Cell>

    <!-- Arena 收到用户输入 AyeL:1 -->
     <ArenaLog>
         <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="1">
            <message>收到来自 AyeL:1 的 INPUT。内容为 "Alice"。现在可以继续执行 AyeL:0 中 `input()` 之后的代码。</message>
            <log_entry_type value="StateTransition"/>
         </log>
    </ArenaLog>

    <!-- Arena 继续执行原代码，并产生输出 -->
    <Cell originator="Gemini" type="OUTPUT" seq="1">
    	<depends_on>
            <!-- 依赖于用户的输入值 -->
            <cell originator="AyeL" seq="1"/>
            <!-- 依赖于原始代码 -->
            <cell originator="AyeL" seq="0"/>
        </depends_on>
        <log originator="Gemini" type="LLM Agent" log_level="DEBUG" seq="0">
             <message>将 `input()` 返回值 "Alice" 赋值给变量 `name`。</message>
             <log_entry_type value="ReasoningNarrative"/>
        </log>
         <log originator="Gemini" type="LLM Agent" log_level="DEBUG" seq="1">
             <message>执行下一句: `print(f"你好, {name}!")`。</message>
             <log_entry_type value="ActionPlan"/>
        </log>
        <stdout seq= "0">
            你好, Alice!
        </stdout>
        <value>成功</value> <!-- 表示 AyeL:0 的整个 Cell 执行成功 -->
    </Cell>

    <!-- 用户发起新的执行请求 -->
    <Cell originator="AyeL" type="EXEC" seq="2">
	     <!-- 注意：这里没有创建 depends_on，在0.3.2下 ArenaLog 会记录推断过程 -->
	    <value>
            name
        </value>
    </Cell>

     <!-- Arena 处理 AyeL:2 -->
     <ArenaLog>
         <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="2">
            <message>开始处理 AyeL:2 (EXEC)。</message>
            <log_entry_type value="ActionPlan"/>
        </log>
         <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="3">
             <message>AyeL:2 未提供 <depends_on>。根据交互上下文，推断此 Cell 是一个新的执行起点，不依赖于之前的特定 Cell (但可能访问之前的状态，如变量 'name')。</message>
             <log_entry_type value="Inference"/>
             <details>
                 <inferred_attribute name="dependency_type" value="New DAG Start (Stateful)"/>
             </details>
         </log>
    </ArenaLog>

    <!-- Arena 执行并返回结果 -->
    <Cell originator="Gemini" type="OUTPUT" seq="2">
	    <depends_on>
            <cell originator="AyeL" seq="2"/>
        </depends_on>
         <log originator="Gemini" type="LLM Agent" log_level="DEBUG" seq="0">
            <message>执行 AyeL:2 中的代码: `name`。</message>
            <log_entry_type value="ActionPlan"/>
        </log>
        <log originator="Gemini" type="LLM Agent" log_level="DEBUG" seq="1">
            <message>查找变量 `name` 的值，根据之前的执行上下文，其值为 "Alice"。</message>
            <log_entry_type value="ReasoningNarrative"/>
        </log>
        <value>Alice</value>
    </Cell>
</Canvas>
```