local ls = require("luasnip")
local s = ls.snippet
local t = ls.text_node
local i = ls.insert_node
local f = ls.function_node


local ct_base = function(ct_type, description)
  return s({trig = ct_type:lower() .. "ct", desc = description} ,
    {
    t("<ct origin=\"User\" type=\""), t(ct_type), t("\" seq=\""), i(1, "0"), t("\">"), -- seq is the first input point, default 0
    t({"", "  <message>"}),
    t({"", "    "}), i(2, "Your message here"), -- message is the second input point, with placeholder text
    t({"", "  </message>"}),
    t({"", "</ct>", ""}),
  }, {})
end

local node_base = function(node_type, description)
  return s({trig = node_type:lower(), desc = description},
    {
    t("<Node origin=\"User\" type=\""), t(node_type) ,t("\" seq=\""),
    i(1, "0"),
    t("\">"), -- seq is the first input point, default 0
    t({"", "  <depends_on>"}), i(2), t({"</depends_on>"}),
    t({"", "  "}), i(3),
    t({"", "  <value>"}),
    t({"", "  <![CDATA[", "    "}),
    i(4, "CDATA content here"), -- CDATA content is the second input point, with placeholder text
    t({"", "  ]]>"}),
    t({"", "  </value>"}),
    t({"", "</Node>", ""}),
  }, {})
end

return {
  -- SpaceSection
  s("ss", {
    t({"<SpaceSection>"}),
    t({"", "  <Acquire origin=\"User\">"}),
    t({"", "    "}), i(1, ""),
    t({"", "  </Acquire>"}),
    t({"", "</SpaceSection>", ""}),
  }, {}),

  s("link", {
    t("<link target=\"nodes[Assistant]["), i(1, "0"), t("]\" />"),
  }
  ),

  -- CTThink
  ct_base("THINK", "思考内容"),
  -- CTSay
  ct_base("SAY", "要说的内容"),
  -- CTSpace
  ct_base("SPACE", "对 Space 的协调"),
  -- CTTrace
  ct_base("TRACE", "执行指令的内容"),

  -- CDInput
  -- node_base("CDInput", "Create CDInput Node"),
  -- GoalNode
  node_base("GoalNode", "定义目标任务"),
  -- PlanNode
  node_base("PlanNode", "分解任务步骤"),
  -- DirectiveNode
  node_base("DirectiveNode", "执行具体指令"),
  -- CodeRequestNode
  node_base("CodeRequestNode", "请求执行代码"),
  -- ProcessLogNode
  node_base("ProcessLogNode", "记录执行过程"),
  -- ResultNode
  node_base("ResultNode", "输出最终结果"),
  -- InteractionRequestNode
  node_base("InteractionRequestNode", "发起交互请求"),
  -- InteractionResponseNode
  node_base("InteractionResponseNode", "响应交互请求"),
  -- ReflectionNode
  node_base("ReflectionNode", "任务反思评估"),
}
