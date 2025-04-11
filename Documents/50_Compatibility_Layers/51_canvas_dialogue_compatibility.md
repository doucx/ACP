# ACP Canvas 对话兼容层规范  
## 设计背景  
当用户与`Agent`仅能通过某种对话界面以对话形式交互时，本规范确保：  
1. **上下文完整性** - 在非结构化对话中维持Canvas的XML语义  
2. **行为一致性** - 强制Agent遵守Arena状态机逻辑  
3. **错误预防** - 解决传统对话模式导致的三大问题：  
   - 格式违规（如缺失关键属性）  
   - 响应不完整（如忽略多轮交互需求）  
   - 单单元格谬误（违反Canvas的Cell链式处理原则）  

## 语法规范  
采用分块式XML结构替代完整Canvas封装：  
```xml
<CanvasSection role="User|Agent">
    <!-- 当前产生的完整Cell链 -->
</CanvasSection>
```

### 关键属性  
| 属性     | 取值               | 强制要求         | 说明                                        |
| ------ | ---------------- | ------------ | ----------------------------------------- |
| `role` | `User` / `Agent` | 双方必需         | 声明交互主体类型                                  |

### 实现要求  
1. **Agent义务**  
   - 必须将响应内容包裹在标准的markdown XML代码块中：  
 ```xml
 <CanvasSection role="Agent">
	 <!-- 响应内容：完整Cell链 -->
 </CanvasSection>
 ```
   - 需完整继承并扩展前序`CanvasSection`的上下文  

2. **用户建议**  
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
     <CodeBlock language="python(可以为任何语言)">
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
    这是包含 Markdown 代码块的 Fhrsk 回复。
    <CodeBlock language="javascript">
console.log("Hello, world!");
    </CodeBlock>
</value>
```

通过使用 `<CodeBlock>` 节点，可以清晰地将 Markdown 代码块与其他 XML 元素区分开来，从而提高代码的可读性和可维护性。

## 合规性示例  
### 标准交互流程  
注意：请不要将示例中的注释内容`<!---->`在实际运行时输出。

**用户输入：**
```xml
<CanvasSection role="User">
    <!-- 1. 用户发起 chat 请求 -->
    <Cell originator="AyeL" seq="0" type="EXEC">
        <value>
             chat 请想办法获取现在的时间，然后输出到stdout中
        </value>
    </Cell>
</CanvasSection>
```

**模型（Gemini）输出：**
```xml
<CanvasSection role="Agent">
    <!-- Arena 处理 AyeL:0，推断路由至 Fhrsk -->
    <ArenaLog>
        <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="0">
             <message>处理 AyeL:0 (EXEC)。检测到 'chat' 关键字，推断用户意图为与 Fhrsk 交互。将请求路由至 Fhrsk。</message>
             <log_entry_type value="RoutingDecision"/>
        </log>
    </ArenaLog>

    <!-- 2. Fhrsk 回应并说明计划 -->
    <Cell originator="Fhrsk(Gemini)" seq="0" type="OUTPUT">
        <depends_on>
           <cell originator="AyeL" seq="0" />
        </depends_on>
        <!-- Fhrsk 的回复直接作为 Cell 的主要价值 -->
        <value>你好！作为一个在模拟环境中的认知界面，我当前无法直接访问你设备或网络的实时时钟。不过，我可以向你询问当前时间，然后帮你记录并打印出来。我接下来会使用 `input()` 来问你时间。</value>
        <flags>
            <!-- 指示 Arena 在此 Cell 后立即创建并执行 Fhrsk 的下一个动作 -->
            <flag value="ThenCreateCell"/>
        </flags>
    </Cell>

    <!-- Arena 处理 Fhrsk(Gemini):0 的 ThenCreateCell 指令 -->
     <ArenaLog>
        <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="1">
            <message>处理 Fhrsk(Gemini):0 (OUTPUT) 完成。检测到 'ThenCreateCell' flag。准备创建并执行由 Fhrsk(Gemini) 定义的下一个 Cell。</message>
            <log_entry_type value="StateTransition"/>
        </log>
    </ArenaLog>

    <!-- 3. Fhrsk 创建 EXEC Cell 以执行 input() -->
    <Cell originator="Fhrsk(Gemini)" seq="1" type="EXEC">
        <depends_on>
            <!-- 依赖于它上一步的决定 Cell -->
            <cell originator="Fhrsk(Gemini)" seq="0" />
        </depends_on>
        <value>
            current_time = input("请告诉我你那边现在的时间 (例如 2023-10-27 10:00): ")
            print(f"好的，你告知的时间是: {current_time}")
        </value>
    </Cell>

    <!-- Arena 处理 Fhrsk(Gemini):1，遇到 input() 并记录状态 -->
    <ArenaLog>
         <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="2">
            <message>开始处理 Fhrsk(Gemini):1 (EXEC)。执行第一行 `current_time = input(...)`。遇到 `input()` 调用，需要暂停并等待用户输入。</message>
            <log_entry_type value="StateTransition"/>
         </log>
    </ArenaLog>

    <!-- 4. Arena 生成等待输入的 OUTPUT Cell -->
    <Cell originator="Gemini" seq="0" type="OUTPUT">
         <depends_on>
             <cell originator="Fhrsk(Gemini)" seq="1" />
         </depends_on>
         <!-- Cell 内部日志记录具体执行情况 -->
         <log originator="Gemini" type="LLM Agent" log_level="DEBUG" seq="0">
            <message>执行 `input("请告诉我你那边现在的时间 (例如 2023-10-27 10:00): ")`</message>
            <log_entry_type value="ActionPlan"/>
         </log>
         <value type="INPUT_HINT">请告诉我你那边现在的时间 (例如 2023-10-27 10:00): </value>
         <flags>
            <flag value="WAIT"/> <!-- 表明 Arena 正在等待输入 -->
         </flags>
    </Cell>
</CanvasSection>
```

**用户输入：**
```xml
<CanvasSection role="User">
    <!-- 5. 用户提供输入 -->
    <Cell originator="AyeL" seq="1" type="INPUT">
        <depends_on>
            <!-- 依赖于提示输入的 Cell -->
            <cell originator="Gemini" seq="0" />
        </depends_on>
        <value>
            2024-04-08 15:30
        </value>
    </Cell>
</CanvasSection>
```

**模型（Gemini）输出：**
```xml
<CanvasSection role="Agent">
    <!-- Arena 收到用户输入 AyeL:1，记录状态变更 -->
     <ArenaLog>
         <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="3">
            <message>收到来自 AyeL:1 的 INPUT。内容为 "2024-04-08 15:30"。现在可以继续执行 Fhrsk(Gemini):1 中 `input()` 之后的代码。</message>
            <log_entry_type value="StateTransition"/>
         </log>
    </ArenaLog>

    <!-- 6. Arena 继续执行 Fhrsk(Gemini):1 的剩余代码并输出结果 -->
    <Cell originator="Gemini" seq="1" type="OUTPUT">
        <depends_on>
            <!-- 依赖于 Fhrsk 的原始 EXEC Cell 获取代码 -->
            <cell originator="Fhrsk(Gemini)" seq="1" />
            <!-- 依赖于用户的 INPUT Cell 获取值 -->
            <cell originator="AyeL" seq="1" />
        </depends_on>
        <!-- Cell 内部日志记录具体执行步骤 -->
        <log originator="Gemini" type="LLM Agent" log_level="DEBUG" seq="0">
             <message>将 `input()` 返回值 "2024-04-08 15:30" 赋值给变量 `current_time`。</message>
             <log_entry_type value="ReasoningNarrative"/>
        </log>
         <log originator="Gemini" type="LLM Agent" log_level="DEBUG" seq="1">
             <message>继续执行 Fhrsk(Gemini):1 中的下一条语句: `print(f"好的，你告知的时间是: {current_time}")`</message>
             <log_entry_type value="ActionPlan"/>
        </log>
        <stdout seq="0">
            好的，你告知的时间是: 2024-04-08 15:30
        </stdout>
        <value>成功</value> <!-- 标记 Fhrsk(Gemini):1 的整体执行成功完成 -->
    </Cell>
</CanvasSection>
```
