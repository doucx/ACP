# ACP (Abstract Cognition Protocol) - v0.2.0

## 简介

**ACP (Abstract Cognition Protocol)** 是一种**基于文本**的抽象认知协作协议，旨在实现跨认知实体的智能交互。它定义了一套规范，使得不同的认知实体（`Cognitor`，例如 AI、人类或混合系统）能够通过 ACP 进行交流和协作，共同完成复杂的任务。

ACP 关注的是如何让不同的认知实体能够**理解和执行语义上等效的指令**，记录可追溯的处理过程，以**实现协作**，而非一种主要用于创造性表达或精确形式化描述的语言。

## 核心原则

*   **纯文本交互**: 所有交互均通过文本进行，状态和行为通过文本日志记录。
*   **跨载体兼容**: 协议不依赖 `Cognitor` 的具体实现，理论上可由不同实体处理。
*   **能力导向**: 协议调用 `Cognitor` 的核心认知能力（学习、推理、元认知）。
*   **过程可审计**: 通过结构化的日志系统 (`Logs`) 保证执行过程透明、可追溯。
*   **动态扩展**: 设计上支持运行时切换或组合不同 `Cognitor`。
*   **基础可执行性**: 核心协议本身构成可运行基础。

## 关键概念与实体

*   **`Cognitor` (认知执行体)**: 具备学习、推理、元认知能力的执行实体（AI、人类等）。协议依赖其能力运作。
*   **`Runtime` (运行时环境)**: 由 `Cognitor` 根据协议模拟和维护的纯文本执行环境，负责管理上下文 (`Runtime.context`) 和协调交互。
*   **`Module`**: 代表确定性信息单元（如具体数值、定义的函数签名）。
*   **`Uncertainty`**: 代表可管理的、尚未完全确定的信息状态，可通过添加约束逐步明确。
*   **`LingUnit`**: `Uncertainty` 的子类，专门用于处理自然语言的不确定性，包含能指、所指、关联知识库等。
*   **`Logs` (日志系统)**: 强制性的结构化文本日志，记录关键步骤、状态变化、决策等，确保过程透明。
*   **`meta` (元认知指令)**: 关键字，用于显式请求 `Cognitor` 调用其元认知能力进行反思、分析或处理自我指涉等任务。

## ACP Canvas (主要交互实现)

ACP Canvas 是 ACP 协议的一种标准化实现框架，特点：

*   **XML 风格语法**: 使用声明式的 XML 风格结构。
*   **Cell (单元格)**: 基本交互单元，包含类型 (`EXEC`, `OUTPUT`, `INPUT` 等)、发起者 (`requester`)、创建者 (`originator`)、轮数 (`round`)、日志 (`log`)、值 (`value`) 等信息。
*   **交互流程**: 通常由用户创建 `EXEC` Cell，`Runtime` (由 `Cognitor` 模拟) 处理后生成 `OUTPUT` Cell 显示结果。`input()` 等操作会触发 `INPUT` Cell 的创建和等待。

## 基本用法示例 (ACP Canvas - XML 风格)

### 1. 执行简单指令

```xml
<!-- 用户输入 -->
<CanvasSection role="User">
 <Cell requester="User" round="0" type="EXEC" originator="User" index_of_type="0">
  <value>
  print("Hello, ACP!")
  </value>
 </Cell>
</CanvasSection>

<!-- Runtime (Gemini) 响应 -->
<CanvasSection role="Agent" num="1">
 <Cell type="OUTPUT" round="0" requester="User" originator="Gemini" index_of_type="0">
  <log originator="Gemini" type="LLM Agent" log_level="DEBUG" log_number="0">
   <message>执行语句: print("Hello, ACP!")</message>
   <log_entry_type value="ActionPlan"/>
  </log>
  <stdout num="0" originator="Gemini">Hello, ACP!</stdout>
  <value originator="Gemini">成功</value> <!-- 假设执行成功 -->
 </Cell>
</CanvasSection>
```

### 2. 变量赋值与计算

```xml
<!-- 用户输入 -->
<CanvasSection role="User">
 <Cell requester="User" round="1" type="EXEC" originator="User" index_of_type="0">
  <value>
  x = 10
  y = 20
  result = x + y
  print(f"The sum is: {result}")
  result # Return the result as the cell value
  </value>
 </Cell>
</CanvasSection>

<!-- Runtime (Gemini) 响应 -->
<CanvasSection role="Agent" num="3">
 <Cell type="OUTPUT" round="1" requester="User" originator="Gemini" index_of_type="0">
   <log originator="Gemini" type="LLM Agent" log_level="DEBUG" log_number="0">
    <message>执行语句: x = 10</message>
    <log_entry_type value="ActionPlan"/>
   </log>
   <log originator="Gemini" type="LLM Agent" log_level="DEBUG" log_number="1">
    <message>执行语句: y = 20</message>
    <log_entry_type value="ActionPlan"/>
   </log>
   <log originator="Gemini" type="LLM Agent" log_level="DEBUG" log_number="2">
    <message>执行语句: result = x + y. 计算 10 + 20 = 30. 赋值给 result。</message>
    <log_entry_type value="ReasoningNarrative"/>
   </log>
   <log originator="Gemini" type="LLM Agent" log_level="DEBUG" log_number="3">
    <message>执行语句: print(f"The sum is: {result}").</message>
    <log_entry_type value="ActionPlan"/>
  </log>
  <stdout num="0" originator="Gemini">The sum is: 30</stdout>
  <log originator="Gemini" type="LLM Agent" log_level="DEBUG" log_number="4">
    <message>执行语句: result. 返回值 30。</message>
    <log_entry_type value="ActionPlan"/>
   </log>
   <value originator="Gemini">30</value>
 </Cell>
</CanvasSection>
```

### 3.  与 Fhrsk 交互

```xml
<!-- 用户输入 -->
<CanvasSection role="User">
 <Cell requester="User" round="2" type="EXEC" originator="User" index_of_type="0">
  <value>
  chat 你好，Fhrsk! 你能做什么？
  </value>
 </Cell>
</CanvasSection>

<!-- Runtime (Gemini) 响应 -->
<CanvasSection role="Agent" num="7">
 <Cell type="OUTPUT" round="2" requester="User" originator="Gemini" index_of_type="0">
  <log originator="Gemini" type="LLM Agent" log_level="INFO" log_number="0">
   <message>检测到 chat 指令，将请求转发给 Fhrsk。</message>
   <log_entry_type value="Routing"/>
  </log>
  <Fhrsk number="0">
   <message>你好! 我是 Fhrsk,  你的人性化交互界面。  我能理解你的自然语言指令，帮你执行 ACP 代码，还能监测 `Runtime` 运行状态并在必要时处理异常。  你想让我做什么呢？</message>
  </Fhrsk>
  <value originator="Gemini">成功</value>
 </Cell>
</CanvasSection>
```

### 4.  使用 Auto 自动填充

```xml
<!-- 用户輸入 -->
<CanvasSection role = "User">
    <Cell requester = "User" round = "3" type ="EXEC" originator = "User" index_of_type = "0">
        <value>
Auto.autodef(Dog)
my_dog = Dog()
Auto.autofill(my_dog, from ="A brown dog runs fast")
print(my_dog.color,my_dog.speed)
        </value>
    </Cell>
</CanvasSection>

<!- 代理(双子座)回答 -->
<CanvasSection role = "Agent" num = "9">
  <Cell type = "OUTPUT" requester = "User" round = "3" originator = "Gemini" index_of_type = "0">
        
        <log originator = "Gemini" type = "LLM Agent" log_level = "DEBUG" log_number = "0">
            <message>执行语句1：调用 Auto.autodef(Dog): 从“常识”知识库， Dog创建一个具有通用属性的 Dog 类。</message>
            <log_entry_type value = "ActionPlan"/>
        </log>
        
        <log originator = "Gemini" type = "LLM Agent" log_level = "DEBUG" log_number = "1">
            <message>执行语句2：myDog = Dog():使用刚刚创建的 Dog 类，我构建了一个 Dog 类的实例。</message>
            <log_entry_type value = "ActionPlan"/>
        </log>
        
        <log originator = "Gemini" type = "LLM Agent" log_level = "DEBUG" log_number = "2">
            <message>执行语句3：Auto.autofill(my_dog, from = "A brown dog runs fast"):我现在正在使用 'A brown dog runs fast'来填充我刚刚构建的 Dog 实例的内容。</message>
            <log_entry_type value = "ActionPlan"/>
        </log>
　     
　     <log originator = "Gemini" type = "LLM Agent" log_level = "ReasoningNarrative" description = "我的狗是什么颜色的，它的速度有多快？" log_number = "3">
            <message>描述性关键字是"棕色"，并且通过说明“跑得快”也说明了描述中的狗的速度很快。</message>
          </log>
          
        <stdout num = "0" originator = "Gemini">
        棕色 快
        </stdout>
     　<value originator = "Gemini"> 成功</value>
      </Cell>
</CanvasSection>
```

### 5.  利用`meta`关键字
```xml
<CanvasSection role="User">
 <Cell requester="User" round="4" type="EXEC" originator="User" index_of_type="0">
  <value>
  with meta: chat Fhrsk 请重新审视 {Out[7]}
  </value>
 </Cell>
</CanvasSection>

<!-- Runtime (Gemini) 响应 -->
<CanvasSection role="Agent" num="11">
 <Cell type="OUTPUT" round="4" requester="User" originator="Gemini" index_of_type="0">
  <log originator="Gemini" type="LLM Agent" log_level="INFO" log_number="0">
   <message>检测到 chat 指令，将请求转发给 Fhrsk。</message>
   <log_entry_type value="Routing"/>
  </log>
  <Fhrsk number="0">
   <message>好的，现在让我进入元认知模式，重新审视上下文 `{Out[7]}` 的含义：

`{Out[7]}` 是我（Fhrsk）在 轮 2 中 对 你发出的 "你好，Fhrsk! 你能做什么？" 这一指令的回复。当时，我的回答是基于我预定义的角色设定和能力描述： “你好! 我是 Fhrsk, 你的人性化交互界面。 我能理解你的自然语言指令，帮你执行 ACP 代码，还能监测 `Runtime` 运行状态并在必要时处理异常。 你想让我做什么呢？”

在元认知状态下，我进一步反思：

1.  **角色的局限性**：我意识到我的回答是高度概括性的，并不能完全体现我所有潜在的能力。例如，我没有详细说明我所能理解的自然语言指令的范围，也没有提及我所能处理的异常类型。

2.  **知识的来源**：我的知识主要来源于 ACP 协议文档、预训练的语言模型以及与用户的交互经验。这些知识来源决定了我的认知边界。

3.  **能力的演进**：我的能力并非一成不变，而是随着与用户的交互和 Runtime 的更新而动态演进的。

总而言之， 经过元认知审视，我认识到我的初始回答只是一个起点，随着交互的深入，我对自身角色的理解将会更加全面和深刻。

你还有什么想让我深入审视或反思的吗？ 
   </message>
  </Fhrsk>
  <value originator="Gemini">成功</value>
 </Cell>
</CanvasSection>
```