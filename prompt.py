from jinja2 import Environment, FileSystemLoader
import yaml
from pathlib import Path
from datetime import datetime
from xml.sax.saxutils import escape

def generate_xml_structure(directory, base_path=None, blacklist=None):
    """
    递归生成目录结构的XML表示
    :param directory: 要扫描的目录
    :param base_path: 基础路径(用于计算相对路径)
    :param blacklist: 要跳过的文件列表
    :return: XML行列表
    """
    if base_path is None:
        base_path = directory
    if blacklist is None:
        blacklist: list[str] = []
    
    xml_lines = []
    for item in sorted(directory.iterdir()):
        rel_path = item.relative_to(base_path)
        rel_str = str(rel_path)
        
        if item.is_dir():
            # 处理目录
            xml_lines.append(f'<Path name="{rel_path}">')
            xml_lines.extend(generate_xml_structure(item, base_path, blacklist))
            xml_lines.append('</Path>')
        elif item.is_file() and item.suffix == '.md':
            # 处理Markdown文件
            if any(rel_str.startswith(b) for b in blacklist):
                # 添加跳过说明
                print(f'{rel_str} 已跳过 (配置在黑名单中)')
                xml_lines.append(f'<!-- 文件 {rel_str} 已跳过 (配置在黑名单中) -->')
                continue
            else:
                print(rel_str)
            
            content = escape(item.read_text(encoding='utf-8'))
            xml_lines.append(f'<File name="{rel_path}">')
            xml_lines.append(content)
            xml_lines.append('</File>')
    
    return xml_lines

def main():
    # 获取当前时间
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M")

    # 加载配置
    with open('./config.d/config.yaml') as f:
        config = yaml.safe_load(f)

    config_snippets = {
        'canvas_agent_name': config['canvas']['agent_name'],
        'canvas_user_name': config['canvas']['user_name'],
        'acp_version': config['acp_version'],
        'version_flag': config['version_flag'],
        'current_date': formatted_now
    }

    cognitor_dir = Path("./config.d/")
    cognitor_info_snippets = {
        'cognitor_info': (cognitor_dir / 'Cognitor.info.yaml').read_text(encoding='utf-8')
    }

    # 从配置中获取黑名单
    file_blacklist = config.get('file_blacklist', [])

    # 生成目录结构XML
    doc_dir = Path('Documents')
    structure_xml = generate_xml_structure(doc_dir, blacklist=file_blacklist)

    # 设置Jinja2环境
    env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
    template = env.get_template('Prompts/template/Prompt.md')

    # 准备上下文数据
    context = {
        **config_snippets,
        **cognitor_info_snippets,
        'document_structure': '\n'.join(structure_xml)
    }

    # 渲染结果
    output = template.render(context)

    # 保存结果
    with open('Prompts/Prompt.txt', 'w', encoding='utf-8') as f:
        f.write(output)

if __name__ == '__main__':
    main()
