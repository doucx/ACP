from jinja2 import Environment, FileSystemLoader
import yaml
from pathlib import Path

from datetime import datetime

# 获取当前的日期和时间
now = datetime.now()

# 格式化日期和时间，精确到分钟
formatted_now = now.strftime("%Y-%m-%d %H:%M")

print(formatted_now)

# 加载配置
with open('config.yaml') as f:
    config = yaml.safe_load(f)

config_snippets = {
    'canvas_agent_name': config['canvas']['agent_name'],
    'canvas_user_name': config['canvas']['user_name'],
    'acp_version': config['acp_version']
}
# 读取所有Markdown片段
doc_dir = Path('Documents')
examples_dir = [
        '81_canvas_example_0_0_x.md', 
        # '83_canvas_tiny_example_0_0_x.md', 
        '82_canvas_xml_example_0_1_x.md'
        ]
examples = "\n".join([f"{(doc_dir / e).read_text(encoding='utf-8')}" for e in examples_dir])
md_snippets = {
    'introduction_and_core_protocol': (doc_dir / '01_introduction_and_core_protocol.md').read_text(encoding='utf-8'),
    'reference_library': (doc_dir / '02_reference_library.md').read_text(encoding='utf-8'),
    'advanced_concepts': (doc_dir / '04_advanced_concepts.md').read_text(encoding='utf-8'),

    'appendix_symbols': (doc_dir / '11_appendix_symbols.md').read_text(encoding='utf-8'),

    'canvas_protocol': (doc_dir / '20_canvas_protocol.md').read_text(encoding='utf-8'),
    'canvas_implementation': (doc_dir / '21_canvas_implementation.md').read_text(encoding='utf-8'),
    'log_system': (doc_dir / '22_canvas_log_system.md').read_text(encoding='utf-8'),
    'canvas_dialogue_compatibility': (doc_dir / '51_canvas_dialogue_compatibility.md').read_text(encoding='utf-8'),
    'canvas_examples': examples,

    'file_naming_conventions': (doc_dir / '99_file_naming_conventions.md').read_text(encoding='utf-8'),
    'version_changelog': (doc_dir / '98_version_changelog.md').read_text(encoding='utf-8'),
}

cognitor_dir = Path("Cognitor-Data")
yaml_snippets = {
    'cognitor_info': (cognitor_dir / 'Cognitor.info.yaml').read_text(encoding='utf-8')
}

# 设置Jinja2环境
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
template = env.get_template('Prompts/Base/Prompt-Base.md')

# 合并数据
context = {
    "current_date": formatted_now,
    **config_snippets,
    **md_snippets,  # 解包所有Markdown片段
    **yaml_snippets
}

# 渲染结果
output = template.render(context)

# 输出或保存结果
# print(output)
with open('Prompts/Prompt.txt', 'w', encoding='utf-8') as f:
    f.write(output)
