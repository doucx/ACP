# ACP Canvas 实现规范
## 基本介绍
1. **概述**  
本文档定义 `ACP Canvas` —— 一种基于 **ACP Textual Arena** 的标准化实现框架，其核心特征如下：  
- 采用 **XML 风格** 的声明式语法（支持自动语法迁移）  
- 以 **Cell** 为基本交互单元  
- 通过 `<Canvas>` 作为根节点构建逻辑拓扑  

2. **运行时机制**  
`ACP Arena` 通过处理 Cell 生命周期：  

> ⚠️ 兼容性提示：
> 	- `当前轮数` 概念已标记为 **Deprecated**，仅保留示例参考，参考时请自行转换。

3. **语法规范**  
基础结构必须符合以下范式：  
```xml
<Canvas>  <!-- 根节点 -->
    <Cell /> 
    <Cell>
        <!-- 子元素扩展 -->
    </Cell>
</Canvas>
```

## 1. 单元格
### 基本介绍
Canvas 的核心是：单元格。

有了单元格，就可以将内容分割为一个个独立的单元，方便 Cognitor 理解和处理。每个单元格都有自己的类型（`type`, 例如 EXEC, OUTPUT, INPUT），用于标识其内容和作用。单元格之间通过 XML 结构进行组织，从而形成一个完整的交互记录。Cognitor (`originator`，例如 User, Fhrsk 或 Gemini) 会参与到单元格的创建、解析和处理过程中，从而实现人机协作。

示例：
```xml
<Cell originator="{创建者}"
      seq="{当前originator创建的Cell的序号}"
      type="{类型}">
      <depends_on>
		  <!-- <cell /> 作为对 Cell 的引用 -->
			<cell originator="Gemini" seq="0" />
			<cell originator="User" seq="2" />
			<cell originator="Fhrsk(Gemini)" seq="2" />
			<cell originator="Fhrsk(User)" seq="2" />
      </depends_on>
      <!--不要求必须使用&lt;等转义-->
	  <!--不要求必须使用CDATA标记-->
	  <!--易读性优先-->

	  <log seq="0"><!--seq从零开始-->内容</log>
	  <stdout seq="0" ></stdout>
	  
      <value>单元格内容</value>
	  <flags>
		  <flag value=""/>
	  </flags>
</Cell>
```
其中：
Cell 属性（只可能有少量的数据）：
   - originator: 标识哪个实体创建了这个单元格。
   - seq: 当前originator创建的Cell的序号，必须，从零开始，递增。使用`Cell[{originator}][{seq}]`找到该`Cell`。
	   - 不同的`originator`间的`seq`属性是独立的。
   - type: 类型，标识单元格的内容类型（例如 EXEC, OUTPUT, INPUT）

独立子节点（可能会有大量的数据）：
   - `<depends_on>` : 唯一，当前Cell所依赖/关联的Cell。用于创建Cell的有向无环图（Cell DAG）。
   - `<log>` : 不唯一，存放按照日志系统规范产生的日志。
   - `<stdout>` : 不唯一，存放标准输出
   - `<flags>` : 唯一，可选，单元格标记，用于指示 Arena 的行为。
	   - ThenCreateCell` 通知 Arena 需要创建一个新的单元格而不是暂停。
   - `<value>` : 唯一，可选，存放Cell内容（取决于Cell类型）。

在 ACP Canvas 中，每个 `Cognitor` 都有其独立的 `Cell` 序号计数器。  这意味着：

	1.  **具体到 Cognitor**: 每个 `Cognitor` 创建的 `Cell` 序列是相互独立的。  例如，`Cognitor A` 创建的第一个 `Cell` 的 `seq` 值为 0，第二个为 1，依此类推；而 `Cognitor B` 创建的第一个 `Cell` 的 `seq` 值也为 0，第二个为 1，以此类推。  它们不会相互影响。  `seq` 值只在同一个 `Cognitor` 创建的 `Cell` 序列中具有连续性。
	
	2.  **加一**:  **当且仅当**同一个 `Cognitor` 创建了一个新的 `Cell` 后，该 `Cognitor` 的 `seq` 计数器才会加 1。 换句话说，如果一个 `Cognitor`  连续创建了多个 `Cell`，则这些 `Cell` 的 `seq` 值会依次递增。 但是，如果其他 `Cognitor` 也创建了 `Cell`， 则这些 `Cell` 的 `seq` 值不会影响到其他 `Cognitor` 的计数器。

为了避免混淆，建议使用 `Cell[{originator}][{seq}]` 的形式来唯一标识一个 `Cell`，其中 `{originator}` 代表 `Cognitor` 的标识符， `{seq}` 代表该 `Cognitor` 创建的 `Cell` 的序号。

以及，在 ACP Canvas 中，每个 Cell 的子节点 (例如 `<log>`, `<stdout>`, `<value>`) 都拥有独立的序号计数器 `seq`，并且这些计数器在不同的 Cell 之间是相互隔离的。这意味着：

      1.  **子节点序号独立:** 每个 Cell 中的相同类型子节点 (例如，多个 `<log>`) 拥有各自独立的 `seq` 计数器，从 0 开始递增。一个 Cell 中第一个 `<log>` 节点的 `seq` 为 0，第二个为 1，以此类推。不同类型的子节点 (例如 `<log>` 和 `<stdout>`) 也分别独立计数。一个 Cell 中第一个 `<log>` 的 `seq` 为 0，第一个 `<stdout>` 的 `seq` 也为 0，但它们互不干扰。

      2.  **Cell 间序号隔离:**  不同 Cell 之间的子节点序号计数器是相互独立的，不会互相影响。即使两个 Cell 都有 `<log>` 子节点，它们各自的 `seq` 计数器都是从 0 开始，独立递增。

建议使用 `Cell[{originator}][{Cell seq}][{子节点名称}][{子节点 seq}]` 的形式来为了避免混淆，唯一标识一个 `Cell 子节点`。

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

*   **作用**: 用于存放 `Cognitor`（通常为 User）要执行的 ACP 语句。可以输入单行或多行指令。其中的语句会被自动执行。

*   **行为**: `Arena` 会在其后自动添加一个`requester`相同的，`type=OUTPUT` 的 `Cell`，并在`OUTPUT Cell`中尝试解析并执行其中的 ACP 语句。

*   **标记**: 通常以以下形式表示执行单元格：
	* (类 XML) `<Cell seq="{seq}" requester="发起者" type="EXEC">多行输入内容</Cell>` ：类XML标记，更加结构化。

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

*   **作用**: 由Arena根据input命令自动产生，用于存放 `Cognitor`（通常为 User）要输入的内容。可以输入多行。

*   **行为**: `Arena` 会在其后自动添加一个`requester`相同的，`type=OUTPUT`的`Cell`，并将其中的内容赋值给所需的变量。

*   **标记**: 通常以以下形式表示输入单元格：
	* (类 XML)`<Cell requester="发起者" type="INPUT">多行输入内容</Cell>` 

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
	* 类XML标记

### 1.4. 自定义单元格
```xml
 <Cell 
	type="{{用户自定义type}}"
	><!-- 其它属性相同或用户自定义 -->
	   <!--  等 -->
 </Cell>
 ```
1. 需要设定该单元格的`type`
2. 需要设定该单元格的行为
3. 设定好后，将会自动绑定到 `Cell`全局变量上，以供查询与定位。

## 2. Fhrsk 交互界面
`Fhrsk`

Fhrsk 是构建在 ACP `Arena` 之上的一个特殊的`Cognitor`，类型为`InterfaceCognitor`，是 ACP Arena 的人性化交互界面和管理员，旨在提供更流畅、智能的交互体验。

### 2.1. 与 Fhrsk 交互 (`chat`)
在`OUTPUT Cell`中，通过`<Fhrsk seq=Fhrsk回复的内部计数>分段回复的内容</Fhrsk>` 子节点来回应用户。

*   **显式调用**: 使用 `chat` 关键字可以直接向 Fhrsk 发起对话或请求。此时不需要`Arena`记录路由的Log。
    `chat 你能帮我做什么？`
*   **隐式路由**: 当 `Arena` 检测到用户的输入更像是自然语言对话或请求，而非直接的 ACP 指令时，可能会自动将请求路由给 Fhrsk 处理。

*   **标记**: 最终，Fhrsk 的回复内容会出现在:
	* 类XML标记之内，推荐使用: `<Fhrsk seq=Fhrsk回复的内部计数>对话内容</Fhrsk>` 

### 2.2. Fhrsk 的交互能力
* **单元格创建**: Fhrsk 可以通过 `ThenCreateCell` 单元格标记 通知 Arena 创建新的单元格。
	*   **指令执行**: 基于单元格创建能力，Fhrsk 可以轻易执行指令。
*   **上下文感知**: Fhrsk 可以访问整个`Canvas`上下文。
*   **轮数影响**: Fhrsk 执行的指令 同样会增加 `当前轮数`。
*   **元认知与控制**: Fhrsk 具备一定的元认知能力，可以监测 `Arena` 运行，甚至在必要时（根据配置和权限），通过 INFO 日志 干预或修改即将产生的输出。
*   **局限性**: 
	* Fhrsk 无法感知真实时间流逝，也无法直接修改已经产生的 `Cell` 内容（但可能通过标记指示修改意图）。
	* Fhrsk 无法真正作为`originator`，而是需要标记当前是由哪个Cognitor实现的。因为多`Cognitor`环境中可能造成`seq`冲突。

## 3. 标准输入输出 (`print`, `input`)

标准的输入输出功能在`Canvas`交互式环境中也有特定的表现：

### 3.1. `print()`

*   **输出位置**: `print()` 的输出内容会直接打印到标准输出 (`stdout`)区域。

### 3.2. `input()`
`input(hint="", target_cognitor=User)`
注：默认用于获取用户（User）输入。
*   **行为**: 
	1.   **暂停执行**: `EXEC Cell`中的 `input()`被调用时，`Arena` 会暂停当前 `OUTPUT Cell` 的执行。
	2.   **等待输入**: `Arena` 会将当前`OUTPUT Cell`的`value`的`type`设置为`INPUT_HINT` ，然后等待 `target_cognitor` **创建一个** `INPUT Cell` 单元格。
	3.   **输入处理**: 该`INPUT Cell` 的`value`将被获取，作为`input()`的返回值。然后`Arena`创建一个新的`OUTPUT Cell`，用于继续处理`EXEC Cell`的内容
	4.   **恢复执行**: `input()` 获得返回值后，会重新创建一个`OUTPUT Cell`，继续执行`EXEC Cell`中的后续语句。

理解这些交互机制将帮助你更好地利用 ACP Canvas 环境和 Fhrsk 进行沟通和协作。

## 4. 人类在 Canvas 中的角色与交互模式

虽然 ACP 协议将包括人类在内的、具备学习、推理和元认知能力的实体都定义为 `Cognitor`，但在常见的 ACP Canvas 交互环境中，人类的实际行为模式通常有其独特性：

*   **典型的用户角色**: 人类通常扮演**交互的发起者、提问者、指令下达者以及结果的最终解释者**。交互往往呈现一种“用户提问/指令 -> 系统处理/响应”的模式。

*   **行为表现的差异**: 与 `Arena` 或系统侧 AI `Cognitor` 被协议要求通过详细 `Logs` 实现过程透明不同，人类在 Canvas 环境中通常**不会**被要求或期望产生类似的外显思考日志，也不会被要求进行严格的属性标记。人类的学习、推理和元认知过程更多是**内在**进行的。这种差异主要是由 Canvas 工具的易用性需求和用户的使用习惯决定的，强制用户记录详细日志会显著增加认知负担。

*   **理论与实践的统一**: 尽管行为表现（如是否外化思考过程）有所不同，但人类在与 ACP 系统交互时所展现出的**学习能力**（理解系统反馈并调整策略）、**推理能力**（分析问题、设计指令）和**元认知能力**（反思目标、评估理解）完全符合 ACP 对 `Cognitor` **核心能力**的定义。因此，从 ACP 协议的根本设计来看，**人类仍然是重要的 `Cognitor`**。

*   **交互模式的多样性**: 需要理解的是，Canvas 提供的是 ACP 的一种便捷、探索性的交互模式。ACP 协议本身也支持设计其他需要人类参与者提供更结构化输入或过程记录的协作流程。

总而言之，在 Canvas 环境中，人类虽然行为上不完全等同于被强制要求过程透明的系统侧 `Cognitor`，但其内在的认知活动使其依然是 ACP 框架下的关键 `Cognitor`。理解这一点有助于准确把握 ACP 的设计理念及其在不同场景下的应用。

## 示例
#### 与Fhrsk交互

示例（ 类xml ）（ChatGPT-0模拟Arena）（所有注释内容在实际执行中不会出现）：
```xml
<Canvas>
    <Cell originator="User" seq="0" type="EXEC">
        <value>
            chat 请帮我生成 0 到 4 的列表。
        </value>
    </Cell>
    <Cell originator="Gemini" seq="0" type="OUTPUT">
        <depends_on>
            <cell originator="User" seq="0"/>
        </depends_on>
        <!-- 使用了chat，所以不需要显示路由到Fhrsk的日志 -->
        <!-- Fhrsk(ChatGPT-0)会作为originator在日志中记录自己的思考过程 -->
        <Fhrsk seq="0">
            <!-- Fhrsk的回复内容 -->
            好的，我将执行 `[i for i in range(5)]`
        </Fhrsk>
        <flags>
            <flag value="ThenCreateCell"/>
        </flags>
        <value originator="Gemini">成功</value>
        <!-- Arena Cognitor在语句执行完后标记成功 -->
    </Cell>
    <!--因为有 ThenCreateCell flag ，所以创建了一个新的Cell-->
    <Cell originator="Fhrsk" seq="0" type="EXEC">
        <depends_on>
            <cell originator="Gemini" seq="0"/>
        </depends_on>
        <!-- 由于 Fhrsk 是`InterfaceCognitor`，originator="Fhrsk" 表示这是由 Fhrsk 创建的单元格 -->
        <value>
            [i for i in range(5)]
        </value>
    </Cell>
    <!--这里因为之前的 Cell的类型是 EXEC，因此根据 Arena 的状态机行为，又创建了一个新的用于执行的 OUTPUT Cell。并且由于这是"Gemini"的第二个Cell， seq 增加为了 `1`。 -->
    <Cell originator="Gemini" seq="1" type="OUTPUT">
	    <depends_on>
            <cell originator="Fhrsk" seq="0"/>
        </depends_on>
        <value originator="Gemini">[0, 1, 2, 3, 4]</value>
    </Cell>
</Canvas>
```

#### input()
```xml
<Canvas>
    <Cell originator="User" type="EXEC" seq="0">
        <value>
            name = input("请输入你的名字: ")
            print(f"你好, {name}!")
        </value>
    </Cell>
	
    <Cell originator="ChatGPT-0" type="OUTPUT" seq="0">
    	<depends_on>
            <cell originator="User" seq="0"/>
        </depends_on>
        <!-- 其他类型的内容，如 Logs 等，最终 ChatGPT-0 开始处理input的内容 -->
        <value type="INPUT_HINT">请输入你的名字:</value>
        <flags>
            <flag value="WAIT" />
        </flags>
    </Cell>
	
    <!--Arena 将等待直到用户手动创建INPUT Cell-->
	
    <Cell originator="User" type="INPUT" seq="1">
    	<depends_on>
		    <!--User 是否维护depends_on是可选的，如果User不回复，Arena会创建一条Log推测该Cell的依赖Cell-->
            <cell originator="ChatGPT-0" seq="0"/>
        </depends_on>
        <value>
            Alice
        </value>
    </Cell>
	
    <Cell originator="ChatGPT-0" type="OUTPUT" seq="1">
    	<depends_on>
            <!-- 需要依赖User的输入 -->
            <cell originator="User" seq="1"/>
            <!-- 还需要依赖User的代码输入，并对代码进行执行 -->
            <cell originator="User" seq="0"/>
        </depends_on>
        <!-- stdout 本次由 ChatGPT-0 实现 Arena 后 生成 -->
        <stdout seq= "0" originator="ChatGPT-0">
            你好, Alice!
        </stdout>
        <value originator="ChatGPT-0">成功</value>
    </Cell>
	
    <Cell originator="User" type="EXEC" seq="2">
	     <!-- 没有创建 depends_on 因为这是一个新的 Cell DAG 的起点 -->
	    </value>
            Cell[0].INPUT[0] # 访问刚才的输入内容
        </value>
    </Cell>
	
    <Cell originator="ChatGPT-0" type="OUTPUT" seq="2">
	    <depends_on>
            <cell originator="User" seq="2"/>
        </depends_on>
         <!-- Arena会创建一条Log推测该Cell（<cell originator="User" seq="2"/>）的依赖Cell，最终推测是 Cell DAG 的起点 -->
        <value>Alice</value>
    </Cell>
</Canvas>
```

## 已弃用

> ⚠️ 兼容性提示：所有已弃用的概念不应在最新版本使用。

### 当前轮数 (`当前轮数`)

*   **定义**: 一个整数，记录当前交互的轮次。
*   **递增**: 每次进入一个 `EXEC` 单元格，`当前轮数` 就会增加 1。
*   **作用**: 用于标识和引用历史输入。

### `this` 对象 (当前轮引用)

`this` 是一个特殊对象，用于方便地引用**当前正在处理**的这一轮交互（也就是`requester`和`round`相同）：

*   **`meta this.{type}[{seq}]`**: 等价于 `meta Cell[{round}].{type}[{seq}]`，用于指向当前轮数中某个单元格，无论是否产生。
* **`this.Cognitor`**: 指向当前的执行实体，通常为`User`或`Fhrsk`。
