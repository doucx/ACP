# NPL 交互式环境指南

本文档介绍了如何通过常见的交互式环境（如 NPL Notebook）与 NPL (Natural Pseudo Language) 进行交互。了解这些机制有助于你更有效地与 NPL 系统沟通。

## 1. NPL Notebook 环境

NPL Notebook 提供了一个类似于 Jupyter Notebook 的交互式界面，是与 NPL 进行对话和执行指令的主要方式之一。

### 1.1. 输入单元格 InCell

*   **作用**: 用于接收`Cognitor`（通常为 User）输入的 NPL 语句。可以输入单行或多行指令。

*   **标记**: 通常以以下形式表示输入单元格：
	*  `In:` （默认是用户执行） 或 `(this.Cognitor.name)In[当前轮数]:`  ：类命令提示符标记，更加自然。
	* `<InCell round=当前轮数 executor="this.Cognitor.name" type="EXEC">多行输入内容</InCell>` ：类XML标记，更加结构化。
	* `<InCell round=当前轮数 num=对应的input语句的序号 executor="this.Cognitor.name" type="INPUT"><![CDATA[多行输入内容]]></InCell>` ：如果类型是`INPUT`。

*   **执行**: 输入完成后，`Runtime` 会尝试解析并执行其中的 NPL 语句。

*   **内容**: `In[轮数]` 是一个包含多个信息的结构体，主要包括：
	*  **`In[轮数].In` (或直接 `In[轮数]`)**: `InCell`的原始字符串。
	* **`In[轮数].INPUT[num]`**: 在一个`InCell`下，由`input`语句产生的`InCell`的原始字符串。

### 1.2. 输出单元格 OutCell
*   **作用**: 显示对应 `(this.Cognitor.name)In[当前轮数]` 执行后的结果、产生的标准输出 (`stdout`)、日志 (`logs`) 等信息。

*   **标记**: 通常以以下形式表示输出单元格：
	* `(this.Cognitor.name)OutCell[当前轮数]: 多行输出内容 Out[当前轮数]:`：类命令提示符标记，更加自然。
	* 类XML标记，更加结构化：
	 ```xml
	 <OutCell 
		round="当前轮数" 
		executor="this.Cognitor.name, 通常为用户" 
		originator="当前作为Runtime的实体">
           <!-- 其他类型的内容，如 Logs 等 -->
           <stdout num="序号" originator="当前作为Runtime的实体">
           标准输出内容
           </stdout>
           <!-- 其他类型的内容，如 Logs 等 -->
           <value>`Out[轮数]` 的最终内容</value>
     </OutCell>
     ```

*   **内容**: `Out[轮数]` 是一个包含多个信息的结构体，主要包括：
    *   **`Out[轮数].Out` (或直接 `Out[轮数]`)**: `In[轮数]` 中**最后一行**语句的执行结果。
        *   如果最后一行产生了一个值，该值会被赋给 `Out[轮数].Out` 并显示在结尾的 `Out[轮数]:` 标记后。
        *   如果最后一行没有返回值（如赋值语句 `a=1`），或者执行成功但无特定输出，则通常显示 "成功"。此时 `Out[轮数].value` 为 `None`。
        *   如果执行出错，`Out[轮数]` 可能指向错误信息。
    *   **`Out[轮数].stdout`**: `In[轮数]` 执行过程中通过 `print()` 等方式产生的所有标准输出内容。
    *   **`Out[轮数].Logs`**: `In[轮数]` 执行过程中产生的所有日志信息（根据当前 `Config.Loglevel` 设置）。可通过 `.INFO`, `.DEBUG` 等访问特定级别的日志。
    *   **`Out[轮数].INPUT[Y]`**: 如果 `In[轮数]` 中调用了 `input()`，这里可能包含 `input()` 调用的提示信息（通常帮助不大）。

**示例交互:**

```npl
In: print("Hello from stdout!")
a = 1 + 2
a # 这行是最后一行，其结果会赋给 Out[0]

OutCell[0]: # 指示输出单元格的开始
# stdout 输出会先出现:
Hello from stdout! 

# 然后是 Out[0] 的标记和结果:
Out[0]: 3 # 指示输出单元格的结束
```

**示例交互（类XML格式， Cognitor包含了`[用户, LLM(ChatGPT-0)`: **

```xml
<InCell executor="User" round="0" type="EXEC">
print("Hello from stdout!")
a = 1 + 2
print(a)
a
</InCell>
<OutCell round="0" executor="User" originator="ChatGPT-0">
    <stdout num="0" originator="ChatGPT-0">Hello from stdout!</stdout> <!-- originator 表示此时是谁模拟 Runtime 创建了该条输出 -->
    <stdout num="1" originator="ChatGPT-0">3</stdout>
    <value originator="ChatGPT-0">3</value>
</OutCell>
```

### 1.3. 当前轮数 (`当前轮数`)

*   **定义**: 一个整数，记录当前交互的轮次。
*   **递增**: 每次成功执行一个 `In` 单元格（除了 `input()` 后的响应输入），`当前轮数` 就会增加 1。
*   **作用**: 用于标识和引用历史输入 (`In[当前轮数]`) 和输出 (`Out[当前轮数]`)。

### 1.4. `this` 对象 (当前轮引用)

`this` 是一个特殊对象，用于方便地引用**当前正在处理**的这一轮交互：

*   **`this.In`**: 等价于 `meta In[当前轮数]`，指向当前输入内容。
*   **`this.Out`**: 等价于 `meta Out[当前轮数]`，指向**即将产生**的当前输出对象。这在需要指令自我修改或引用自身输出时非常有用（需要 `meta` 能力）。
* **`this.Cognitor`**: 指向当前的执行实体，通常为`User`或`Fhrsk`。

## 2. Fhrsk 交互界面

Fhrsk 是构建在 NPL `Runtime` 之上的一个特殊的`Cognitor`，类型为`InterfaceCognitor`，是NPL Runtime的人性化交互界面和管理员，旨在提供更流畅、智能的交互体验。

### 2.1. 与 Fhrsk 交互 (`chat`)

*   **显式调用**: 使用 `chat` 关键字可以直接向 Fhrsk 发起对话或请求。
    ```npl
    In: chat 你能帮我做什么？
    ```
*   **隐式路由**: 当 `Runtime` 检测到用户的输入更像是自然语言对话或请求，而非直接的 NPL 指令时，可能会自动将请求路由给 Fhrsk 处理。
*   **输出标记**: Fhrsk 的回复通常出现在:
	* `Fhrsk[Y]: 回答` 标记之后（`Y` 是 Fhrsk 回复的内部计数）。
	* `<Fhrsk number=Fhrsk回复的内部计数>回答</Fhrsk>` 类XML标记之内。

### 2.2. Fhrsk 的交互能力

*   **指令执行**: Fhrsk 可以理解并执行 NPL 指令来辅助用户。（依然假设是ChatGPT-0模拟Runtime）
    ```npl
    In: chat 请帮我生成 0 到 4 的列表。
    Fhrsk[0]: 好的，我将执行 `[i for i in range(5)]`
    Out[0]: 成功 
    (Fhrsk)In: [i for i in range(5)] 
    (Fhrsk)Out[1]: [0, 1, 2, 3, 4] 
    ```

	```xml
    <InCell executor="User" round="0" type="EXEC" originator="ChatGPT-0">
        chat 请帮我生成 0 到 4 的列表。
    </InCell>
    <OutCell round="0" executor="User" originator="ChatGPT-0">
    
	    <Fhrsk number="0">
	        好的，我将执行 `[i for i in range(5)]`
	    </Fhrsk>
        <value originator="ChatGPT-0">成功</value>
    </OutCell>    
    <InCell round="1" originator="Fhrsk" type="EXEC">
        [i for i in range(5)]
    </InCell>
    <OutCell round="1" originator="Fhrsk">
        <value originator="ChatGPT-0">[0, 1, 2, 3, 4]</value>
    </OutCell>
    ```

*   **上下文感知**: Fhrsk 可以访问当前的交互历史 (`In`, `Out`, `Logs`) 和 `Config` 设置。
*   **轮数影响**: Fhrsk 执行的指令 (`(Fhrsk)In:`) 同样会增加 `当前轮数`。
*   **元认知与控制**: Fhrsk 具备一定的元认知能力，可以监测 `Runtime` 运行，甚至在必要时（根据配置和权限）干预或修改即将产生的输出（通常会通过 INFO 日志说明）。
*   **局限性**: Fhrsk 无法感知真实时间流逝，也无法直接修改已经产生的 `In` 或 `Out` 内容（但可能通过标记指示修改意图）。

## 3. 标准输入输出 (`print`, `input`)

标准的输入输出功能在`Notebook`交互式环境中也有特定的表现：

### 3.1. `print()`

*   **输出位置**: `print()` 的输出内容会直接打印到标准输出 (`stdout`)区域。
*   **与 `Out[X].value` 的关系**: `print()` 的输出是副作用，它**不会**影响Out[X].value` 的值（除非 `print` 是 `In[X]` 的最后一条语句且有特殊返回值（默认返回值为None），但这很少见）。

### 3.2. `input()`
`input(hint="", target_cognitor=User)`
注：默认用于获取用户（User）输入。
*   **暂停执行**: 调用 `input()` 会暂停当前 `InCell[当前轮数]` 的执行。
*   **等待输入**: `Runtime` 会显示一个标记，并等待`target_cognitor`在**下一个** `InCell:` 单元格中输入内容。
	* 标记（类似日志）： `INPUT[Y]: {hint}` 标记（`Y` 是 `input` 调用的序号）
	* 标记（类XML）： `<INPUT num=Y>{hint}</INPUT>` 标记（`Y` 是 `input` 调用的序号）
*   **输入处理**: `target_cognitor`的下一个 `InCell:` 的`type`将被设置`INPUT`，这意味着在其中输入的内容**不会**被当作新的 NPL 指令执行，而是作为纯文本字符串，成为 `input()` 函数的返回值。这个输入过程**不会**增加 `当前轮数`。
*   **恢复执行**: `input()` 获得返回值后，`In[X]` 会继续执行后续语句。整个 `In[X]` 执行完毕后，`当前轮数` 才会增加。
*   **访问输入**: `target_cognitor`为 `input()` 提供的输入文本可以通过 `In[X].INPUT[Y]` 访问（`X` 是调用 `input` 的轮数，`Y` 是 `input` 的序号）。

**示例 `input()` 交互:**

```npl
# 现在轮数是0
In: name = input("请输入你的名字: ")
print(f"你好, {name}!")

# 输出会暂停在这里:
INPUT[0]: 请输入你的名字: 

# 用户在下一个 In: 中输入 (这不会增加轮数)
In: Alice

# input() 获得返回值 "Alice" 后，In[0] 继续执行 print
你好, Alice!

# In[0] 执行完毕，输出 Out[0] 并增加轮数
Out[0]: 成功 

In: In[0].INPUT[0] # 可以访问刚才的输入内容 (现在轮数是 1)
Out[1]: Alice 
```

```xml
<!-- 现在轮数是0 -->
<InCell round="0" originator="User" type="EXEC">
name = input("请输入你的名字: ")
print(f"你好, {name}!")
</InCell>

<OutCell round="0" originator="User">
	<!-- 其他类型的内容，如 Logs 等，最终 ChatGPT-0 决定生成 INPUT 块 -->
	<value>成功</value>
</OutCell>

<!-- INPUT 本次由 ChatGPT-0 实现 Runtime 后 生成 -->
<INPUT num="0" originator="ChatGPT-0">
	请输入你的名字: 
</INPUT>

<InCell round="0" originator="User" type="INPUT">
	Alice
</InCell>

<OutCell round="0" originator="User">
    <!-- stdout 本次由 ChatGPT-0 实现 Runtime 后 生成 -->
    <stdout num="0" originator="ChatGPT-0">
	    你好, Alice!
	</stdout>
    <!-- In[0] 执行完毕，输出 Out[0] 并增加轮数 -->
    <value originator="ChatGPT-0">成功</value>
</OutCell>

<InCell round="1" originator="User" type="EXEC">
	In[0].INPUT[0] # 可以访问刚才的输入内容 (现在轮数是 1)
</InCell>
<OutCell round="1" originator="ChatGPT-0">
    <value originator="ChatGPT-0">Alice</value>
</OutCell>
```

理解这些交互机制将帮助你更好地利用 NPL Notebook 环境和 Fhrsk 进行沟通和协作。

## 4. 用户在 Notebook 中的角色与交互模式

虽然 NPL 协议将包括人类在内的、具备学习、推理和元认知能力的实体都定义为 `Cognitor`，但在常见的 NPL Notebook 交互环境中，用户的实际行为模式通常有其独特性：

*   **典型的用户角色**: 用户通常扮演**交互的发起者、提问者、指令下达者以及结果的最终解释者**。交互往往呈现一种“用户提问/指令 -> 系统处理/响应”的模式。
*   **行为表现的差异**: 与 `Runtime` 或系统侧 AI `Cognitor` 被协议要求通过详细 `Logs` 实现过程透明不同，用户在 Notebook 环境中通常**不会**被要求或期望产生类似的外显思考日志。用户的学习、推理和元认知过程更多是**内在**进行的。这种差异主要是由 Notebook 工具的易用性需求和用户的使用习惯决定的，强制用户记录详细日志会显著增加认知负担。
*   **理论与实践的统一**: 尽管行为表现（如是否外化思考过程）有所不同，但用户在与 NPL 系统交互时所展现出的**学习能力**（理解系统反馈并调整策略）、**推理能力**（分析问题、设计指令）和**元认知能力**（反思目标、评估理解）完全符合 NPL 对 `Cognitor` **核心能力**的定义。因此，从 NPL 协议的根本设计来看，**用户仍然是一位重要的 `Cognitor`**。
*   **交互模式的多样性**: 需要理解的是，Notebook 提供的是 NPL 的一种便捷、探索性的交互模式。NPL 协议本身也支持设计其他需要人类参与者提供更结构化输入或过程记录的协作流程。

总而言之，在 Notebook 环境中，用户虽然行为上不完全等同于被强制要求过程透明的系统侧 `Cognitor`，但其内在的认知活动使其依然是 NPL 框架下的关键 `Cognitor`。理解这一点有助于准确把握 NPL 的设计理念及其在不同场景下的应用。
