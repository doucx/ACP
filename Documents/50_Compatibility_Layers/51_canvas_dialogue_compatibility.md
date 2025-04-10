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
注意：请不要将示例中的注释内容`<!---->`在实际运行时输出。

用户输入：
```xml
<CanvasSection role="User" num="0">
    <!-- 1. User initiates the chat request -->
    <Cell originator="User" seq="0" type="EXEC">
        <value>
             chat 请想办法获取现在的时间，然后输出到stdout中
        </value>
    </Cell>
</CanvasSection>
```

模型（Gemini）输出：
```xml
<CanvasSection role="Agent" num="1">
    <!-- 2. Gemini processes User:0, routes to Fhrsk -->
    <Cell originator="Gemini" seq="0" type="OUTPUT">
        <depends_on>
           <cell originator="User" seq="0" />
        </depends_on>
        <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="0">
             <message>收到 User:0，检测到 chat 请求，将请求转交给 Fhrsk 处理。</message>
             <log_entry_type value="Routing"/>
        </log>
        <Fhrsk seq="0">
            你好！作为一个在模拟环境中的认知界面，我当前无法直接访问你设备或网络的实时时钟。不过，我可以向你询问当前时间，然后帮你记录并打印出来。我接下来会使用 `input()` 来问你时间。
        </Fhrsk>
        <flags>
            <!-- Instructs Arena to create Fhrsk's EXEC cell next -->
            <flag value="ThenCreateCell"/>
        </flags>
        <value originator="Gemini">成功</value> <!-- Marking the routing successful -->
    </Cell>

    <!-- 3. Based on ThenCreateCell flag, Fhrsk creates an EXEC cell -->
    <Cell originator="Fhrsk(Gemini)" seq="0" type="EXEC">
        <depends_on>
            <!-- Depends on the preceding OUTPUT cell where Fhrsk made the decision -->
            <cell originator="Gemini" seq="0" />
        </depends_on>
        <value>
            current_time = input("请告诉我你那边现在的时间 (例如 2023-10-27 10:00): ")
            print(f"好的，你告知的时间是: {current_time}")
        </value>
    </Cell>

    <!-- 4. Gemini processes Fhrsk:0, encounters input(), pauses and waits -->
    <Cell originator="Gemini" seq="1" type="OUTPUT">
         <depends_on>
             <cell originator="Fhrsk(Gemini)" seq="0" />
         </depends_on>
         <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="0">
            <message>开始执行 Fhrsk(Gemini):0。遇到 `input()` 调用。</message>
            <log_entry_type value="ActionPlan"/>
         </log>
         <value type="INPUT_HINT">请告诉我你那边现在的时间 (例如 2023-10-27 10:00): </value>
         <flags>
            <flag value="WAIT"/> <!-- Indicate waiting for user input -->
         </flags>
    </Cell>
</CanvasSection>
```

用户输入：
```xml
<CanvasSection role="User" num="2">
    <!-- 5. User provides the input -->
    <Cell originator="User" seq="1" type="INPUT">
        <depends_on>
            <!-- Depends on the OUTPUT cell that prompted for input -->
            <cell originator="Gemini" seq="1" />
        </depends_on>
        <value>
            2024-04-08 15:30
        </value>
    </Cell>
</CanvasSection>
```

模型（Gemini）输出：
```xml
<CanvasSection role="Agent" num="3">
    <!-- 6. Gemini processes the input and continues Fhrsk:0's execution -->
    <Cell originator="Gemini" seq="2" type="OUTPUT">
        <depends_on>
            <!-- Depends on Fhrsk's original EXEC cell for the code context -->
            <cell originator="Fhrsk(Gemini)" seq="0" />
            <!-- And depends on the User's INPUT cell for the value -->
            <cell originator="User" seq="1" />
        </depends_on>
        <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="0">
             <message>`input()` 收到来自 User:1 的值: "2024-04-08 15:30"。将其赋值给变量 `current_time`。</message>
             <log_entry_type value="ReasoningNarrative"/>
        </log>
         <log originator="Gemini" type="LLM Agent" log_level="INFO" seq="1">
             <message>继续执行 Fhrsk(Gemini):0 中的下一条语句: print(...)</message>
             <log_entry_type value="ActionPlan"/>
        </log>
        <stdout seq="0" originator="Gemini">
            好的，你告知的时间是: 2024-04-08 15:30
        </stdout>
        <value originator="Gemini">成功</value> <!-- Marking the execution of Fhrsk:0 complete -->
    </Cell>

</CanvasSection>
```