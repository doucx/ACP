def replace_and_write(npl_doc_path, prompt_base_path, prompt_txt_path):
    """
    用 npl_doc_path 的内容替换 prompt_base_path 中 {{NPL-Document}}，
    并将结果写入 prompt_txt_path。
    """
    try:
        with open(npl_doc_path, 'r', encoding='utf-8') as npl_file:
            npl_content = npl_file.read()

        with open(prompt_base_path, 'r', encoding='utf-8') as base_file:
            base_content = base_file.read()

        modified_content = npl_content.join(base_content.split("{{NPL-Document}}"))
        # print(modified_content)

        with open(prompt_txt_path, 'w', encoding='utf-8') as output_file:
            output_file.write(modified_content)

        print(f"成功将 {npl_doc_path} 的内容替换 {prompt_base_path} 中的 {{NPL-Document}} 并写入 {prompt_txt_path}。")

    except FileNotFoundError as e:
        print(f"错误: 文件未找到 - {e}")
    except Exception as e:
        print(f"错误: 发生异常 - {e}")

# 设置文件路径
npl_doc_path = "NPL-Document.md"
prompt_base_path = "Prompt-Base.md"
prompt_txt_path = "Prompt.txt"

# 执行替换和写入操作
replace_and_write(npl_doc_path, prompt_base_path, prompt_txt_path)
