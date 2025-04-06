# NPL Canvas 指南
## 基本介绍
本文档介绍了一种 NPL 协议的具体实现规范，称为`NPL Canvas`。

NPL Canvas 提供了一个主要使用 xml 风格的（可自动迁移风格），基于 Cell 的交互平台。

`NPL Runtime` 通过对`Cell.type`等的识别，以类似状态机的方式，对`Cell`进行处理（如创建，等待）。

注：shell-like 风格即将废弃。为了兼容性，保持其示例。

NPL Canvas 的根节点是 `<Canvas>`：
```xml
<Canvas>
	<Cell></Cell>
</Canvas>
```

## 单元格
### 单元格基类
Canvas 的核心是：单元格。

有了单元格，就可以将内容分割为一个个独立的单元，方便 Cognitor 理解和处理。每个单元格都有自己的类型（`type`, 例如 EXEC, OUTPUT, INPUT），用于标识其内容和作用。每个单元格都会标识其发起人(`requester`)。单元格之间通过 XML 结构进行组织，从而形成一个完整的交互记录。Cognitor (`originator`，例如 Fhrsk 或 Gemini) 会参与到单元格的创建、解析和处理过程中，从而实现人机协作。

```xml
<Cell requester="{发起者}"
	  originator="{创建者}"
      round="{轮数}"
      cell_num="{在当前round中的位置}"
      type="{类型}" >
      <!--不要求必须使用&lt;等转义-->
	  <!--不要求必须使用CDATA标记-->
	  <!--易读性优先-->

	  <log></log>
	  <log></log>
	  <flags>
		  <flag value=""/>
	  </flags>
      <value>单元格内容</value>
</Cell>
```
其中：
Cell 属性（只可能有少量的数据）：
   - requester: 发起者，标识这个单元格因哪个实体的发起而产生
   - originator: 标识哪个实体创建了这个单元格
   - round: 轮数，从零开始，标识单元格在整个 Canvas 中的位置
   - cell_num: 从零开始，标识该type的Cell在当前round中的位置
   - type: 类型，标识单元格的内容类型（例如 EXEC, OUTPUT, INPUT）
独立（会有大量的数据）：
   - log: 存放按照日志系统规范产生的日志，放在 Cell 下。
   - flags: 可选，单元格标记，用于指示 Runtime 的行为。
	   - `ThenCreateCell` 通知 Runtime 需要创建一个新的单元格而不是暂停。
   - value: 字符串。需要写在结尾。

访问方式:
   - `Cell[{round}].{type}[{cell_num}]`可以用于访问该单元格的内容。

### 1.1. 执行单元格
```xml
 <Cell 
	type="EXEC"
	><!-- 其它属性相同 -->
	<value>
	<!--不要求必须使用&lt;等转义-->
	<!--不要求必须使用CDATA标记-->
	<!--不要求CDATA标记，Cognitor可以理解即可-->
	需要被执行的输入内容
	</value>
 </Cell>
 ```

*   **作用**: 用于存放 `Cognitor`（通常为 User）要执行的 NPL 语句。可以输入单行或多行指令。其中的语句会被自动执行。

*   **行为**: `Runtime` 会在其后自动添加一个`round`和`requester`相同的，`type=OUTPUT`的`Cell`，并在`OUTPUT Cell`中尝试解析并执行其中的 NPL 语句。

*   **标记**: 通常以以下形式表示执行单元格：
	* (类 XML) `<Cell round=当前轮数 requester="this.Cognitor.name" type="EXEC">多行输入内容</Cell>` ：类XML标记，更加结构化。
	*  (shell-like 即将废弃)`In:` （无前导标注默认是用户执行） 或 `(this.Cognitor.name)In[当前轮数]:`  ：类命令提示符标记（shell-like），更加自然。

### 1.2. 输入单元格
```xml
 <Cell 
	type="INPUT"
	><!-- 其它属性相同 -->
	<value>
	<!--不要求必须使用&lt;等转义-->
	<!--不要求必须使用CDATA标记-->
	<!--不要求CDATA标记，Cognitor可以理解即可-->
	需要被执行的输入内容
	</value>
 </Cell>
 ```

*   **作用**: 由Runtime根据input命令自动产生，用于存放 `Cognitor`（通常为 User）要输入的内容。可以输入多行。

*   **行为**: `Runtime` 会在其后自动添加一个`round`和`requester`相同的，`type=OUTPUT`的`Cell`，并将其中的内容赋值给所需的变量。

*   **标记**: 通常以以下形式表示输入单元格：
	* (类 XML)`<Cell round=当前轮数 num=对应的input语句的序号 requester="this.Cognitor.name" type="INPUT">多行输入内容</Cell>` 
	* (shell-like 即将废弃) `In:` （默认是用户执行） 或 `(this.Cognitor.name)In[当前轮数]:`  ：类命令提示符标记（shell-like），更加自然。

### 1.3. 输出单元格
```xml
 <Cell 
	type="OUTPUT"
	><!-- 其它属性相同 -->
	   <!-- 其他类型的内容，如 Logs 等 -->

	   <value type="NORMOL/INPUT_HINT">
	   `Cell.OUTPUT[轮数]` 的最终内容
	   </value>

 </Cell>
 ```

*   **作用**: 显示对应 `INPUT Cell` 执行后的产生的标准输出 (`stdout`)、日志 (`logs`)、结果( value )等信息。

*   **标记**: 通常以以下形式表示输出单元格：
	* `(this.Cognitor.name)Cell[当前轮数]: 多行输出内容 Out[当前轮数]:`：类命令提示符标记，更加自然。
	* 类XML标记

### 1.4. 自定义单元格
```xml
 <Cell 
	type="{{用户自定义type}}"
	><!-- 其它属性相同或用户自定义 -->
	   <!--  等 -->
 </Cell>
 ```
1. 需要设定该单元格绑定到 `In` ( Cognitor 输入，比如用户输入 ) 还是 `Out`( Cognitor 输出 )
2. 需要设定该单元格的行为
3. 设定好后，将会自动绑定到 `In/Out[轮数].用户自定义type`变量上。

### 1.5. 当前轮数 (`当前轮数`)

*   **定义**: 一个整数，记录当前交互的轮次。
*   **递增**: 每次进入一个 `EXEC` 单元格，`当前轮数` 就会增加 1。
*   **作用**: 用于标识和引用历史输入。

### 1.6. `this` 对象 (当前轮引用)

`this` 是一个特殊对象，用于方便地引用**当前正在处理**的这一轮交互（也就是`requester`和`round`相同）：

*   **`meta this.{type}[{cell_num}]`**: 等价于 `meta Cell[{round}].{type}[{cell_num}]`，用于指向当前轮数中某个单元格，无论是否产生。
* **`this.Cognitor`**: 指向当前的执行实体，通常为`User`或`Fhrsk`。

## 2. Fhrsk 交互界面
`Fhrsk`

Fhrsk 是构建在 NPL `Runtime` 之上的一个特殊的`Cognitor`，类型为`InterfaceCognitor`，是NPL Runtime的人性化交互界面和管理员，旨在提供更流畅、智能的交互体验。

### 2.1. 与 Fhrsk 交互 (`chat`)

*   **显式调用**: 使用 `chat` 关键字可以直接向 Fhrsk 发起对话或请求。
    `chat 你能帮我做什么？`
*   **隐式路由**: 当 `Runtime` 检测到用户的输入更像是自然语言对话或请求，而非直接的 NPL 指令时，可能会自动将请求路由给 Fhrsk 处理。

*   **标记**: Fhrsk 的对话内容通常出现在:
	* 类XML标记之内: `<Fhrsk number=Fhrsk回复的内部计数>对话内容</Fhrsk>` 
	* (shell-like, 即将弃用)`Fhrsk[Y]: 对话内容` 标记之内（`Y` 是 Fhrsk 回复的内部计数）。

### 2.2. Fhrsk 的交互能力
* **单元格创建**: 由于 Fhrsk 可以通过 `ThenCreateCell` 单元格标记 通知 Runtime 创建新的单元格。
	*   **指令执行**: 基于单元格创建能力，Fhrsk 可以轻易执行指令。
*   **上下文感知**: Fhrsk 可以访问当前的交互历史 (`In`, `Out`, `Logs`) 和 `Config` 设置。
*   **轮数影响**: Fhrsk 执行的指令 (`(Fhrsk)In:`) 同样会增加 `当前轮数`。
*   **元认知与控制**: Fhrsk 具备一定的元认知能力，可以监测 `Runtime` 运行，甚至在必要时（根据配置和权限）干预或修改即将产生的输出（通常会通过 INFO 日志说明）。
*   **局限性**: Fhrsk 无法感知真实时间流逝，也无法直接修改已经产生的 `In` 或 `Out` 内容（但可能通过标记指示修改意图）。

示例（ 类xml ）（ChatGPT-0模拟Runtime）：
```xml
<Canvas>
	<Cell requester="User" round="0" type="EXEC" originator="User">
		<value>
		chat 请帮我生成 0 到 4 的列表。
		</value>
	</Cell>
	<Cell round="0" requester="User" originator="ChatGPT-0">
		<!-- 这里有一个将用户输入路由到Fhrsk的日志 -->
		<Fhrsk number="0">
			好的，我将执行 `[i for i in range(5)]`
		</Fhrsk>
		<flags>
			<flag value="ThenCreateCell"/>
		</flags>
		<value originator="ChatGPT-0">成功</value>
	</Cell>
	<!--因为有 ThenCreateCell flag ，所以创建了一个新的Cell-->
	<Cell round="1" requester="Fhrsk" originator="Fhrsk" type="EXEC">
		<!-- originator="Fhrsk" 表示这是由 Fhrsk 创建的单元格 -->
		<value>
		[i for i in range(5)]
		</value>
	</Cell>
	<!--这里因为之前的 Cell的类型是 EXEC，因此又创建了一个新的用于执行EXEC内容的 Cell-->
	<Cell round="1" originator="ChatGPT-0">
		<value originator="ChatGPT-0">[0, 1, 2, 3, 4]</value>
	</Cell>
</Canvas>
```
	
示例（shell-like, 即将废弃）：
```npl
In: chat 请帮我生成 0 到 4 的列表。
// 这里有一个将用户输入路由到Fhrsk的日志
Fhrsk[0]: 好的，我将执行 `[i for i in range(5)]`
Out[0]: 成功 
(Fhrsk)In: [i for i in range(5)] # 由Runtime自动创建Fhrsk的EXEC单元格
(Fhrsk)Out[1]: [0, 1, 2, 3, 4] 
```

## 3. 标准输入输出 (`print`, `input`)

标准的输入输出功能在`Canvas`交互式环境中也有特定的表现：

### 3.1. `print()`

*   **输出位置**: `print()` 的输出内容会直接打印到标准输出 (`stdout`)区域。
*   **与 `Out[X].value` 的关系**: `print()` 的输出是副作用，它**不会**影响Out[X].value` 的值（除非 `print` 是 `In[X]` 的最后一条语句且有特殊返回值（默认返回值为None），但这很少见）。

### 3.2. `input()`
`input(hint="", target_cognitor=User)`
注：默认用于获取用户（User）输入。
*   **行为**: 
	1.   **暂停执行**: `EXEC Cell`中的 `input()`被调用时，`Runtime` 会暂停当前 `OUTPUT Cell` 的执行。
	2.   **等待输入**: `Runtime` 会将当前`OUTPUT Cell`的`value`的`type`设置为`INPUT_HINT` ，然后等待 `target_cognitor` **创建一个** `INPUT Cell` 单元格。
	3.   **输入处理**: 该`INPUT Cell` 的`value`将被获取，作为`input()`的返回值。然后`Runtime`创建一个新的`OUTPUT Cell`，用于继续处理`EXEC Cell`的内容
	4.   **恢复执行**: `input()` 获得返回值后，会重新创建一个`OUTPUT Cell`，继续执行`EXEC Cell`中的后续语句。
	5.   **访问输入**: `target_cognitor`为 `input()` 提供的输入文本可以通过 `In[X].INPUT[Y]` 访问（`X` 是调用 `input` 的轮数，`Y` 是 `input` 的序号）。

**标记**：
	- 标记（类XML）： `<INPUT num=Y>{hint}</INPUT>` 标记（`Y` 是 `input` 调用的序号）
	- 标记（shell-like，即将废弃）： `INPUT[Y]: {hint}` 标记（`Y` 是 `input` 调用的序号）

**示例 `input()` 交互:**
（类 xml）：
用户输入：
```xml
<Canvas>
	<Cell round="0" originator="User" type="EXEC">
	<value>
	name = input("请输入你的名字: ")
	print(f"你好, {name}!")
	</value>
	</Cell>
	
	<Cell round="0" originator="User" type="OUTPUT">
		<!-- 其他类型的内容，如 Logs 等，最终 ChatGPT-0 开始处理input的内容 -->
		<value type="INPUT_HINT">请输入你的名字:</value>
		<flags>
			<flag value="WAIT" />
		</flags>
	</Cell>
	
	<!--Runtime 将等待直到用户手动创建INPUT Cell-->
	
	<Cell round="0" originator="User" type="INPUT">
	<value>
		Alice
	</value>
	</Cell>
	
	<Cell round="0" originator="User">
	    <!-- stdout 本次由 ChatGPT-0 实现 Runtime 后 生成 -->
	    <stdout num="0" originator="ChatGPT-0">
		    你好, Alice!
		</stdout>
	    <!-- In[0] 执行完毕，输出 Out[0] 并增加轮数 -->
	    <value originator="ChatGPT-0">成功</value>
	</Cell>
	
	<Cell round="1" originator="User" type="EXEC">
	<value>
		Cell[0].INPUT[0] # 访问刚才的输入内容
	</value>
	</Cell>
	
	<Cell round="1" originator="ChatGPT-0">
	    <value>Alice</value>
	</Cell>
</Canvas>
```

（shell-like, 即将废弃）：
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


理解这些交互机制将帮助你更好地利用 NPL Canvas 环境和 Fhrsk 进行沟通和协作。

## 4. 用户在 Canvas 中的角色与交互模式

虽然 NPL 协议将包括人类在内的、具备学习、推理和元认知能力的实体都定义为 `Cognitor`，但在常见的 NPL Canvas 交互环境中，用户的实际行为模式通常有其独特性：

*   **典型的用户角色**: 用户通常扮演**交互的发起者、提问者、指令下达者以及结果的最终解释者**。交互往往呈现一种“用户提问/指令 -> 系统处理/响应”的模式。
*   **行为表现的差异**: 与 `Runtime` 或系统侧 AI `Cognitor` 被协议要求通过详细 `Logs` 实现过程透明不同，用户在 Canvas 环境中通常**不会**被要求或期望产生类似的外显思考日志，也不会被要求进行严格的属性标记。用户的学习、推理和元认知过程更多是**内在**进行的。这种差异主要是由 Canvas 工具的易用性需求和用户的使用习惯决定的，强制用户记录详细日志会显著增加认知负担。
*   **理论与实践的统一**: 尽管行为表现（如是否外化思考过程）有所不同，但用户在与 NPL 系统交互时所展现出的**学习能力**（理解系统反馈并调整策略）、**推理能力**（分析问题、设计指令）和**元认知能力**（反思目标、评估理解）完全符合 NPL 对 `Cognitor` **核心能力**的定义。因此，从 NPL 协议的根本设计来看，**用户仍然是一位重要的 `Cognitor`**。
*   **交互模式的多样性**: 需要理解的是，Canvas 提供的是 NPL 的一种便捷、探索性的交互模式。NPL 协议本身也支持设计其他需要人类参与者提供更结构化输入或过程记录的协作流程。

总而言之，在 Canvas 环境中，用户虽然行为上不完全等同于被强制要求过程透明的系统侧 `Cognitor`，但其内在的认知活动使其依然是 NPL 框架下的关键 `Cognitor`。理解这一点有助于准确把握 NPL 的设计理念及其在不同场景下的应用。