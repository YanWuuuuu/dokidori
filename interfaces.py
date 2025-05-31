# interfaces.py
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

repo_id = "Takaharadesu/dokidori"
device = None

model = MBartForConditionalGeneration.from_pretrained(repo_id).to(device)
tokenizer = MBart50TokenizerFast.from_pretrained(repo_id)

def translate_multiline(text, max_new_tokens, batch_size, repetition_penalty, temperature, top_p):

    #文本预处理
    lines = text.split("\n")
    outputs_list = ["" for _ in lines]
    non_empty_lines = []
    non_empty_indices = []

    for row_num, line in enumerate(lines):
        stripped = line.strip()
        if stripped:
            non_empty_lines.append(stripped)
            non_empty_indices.append(row_num)#该数组记录了非空行的索引值
    
    #实际翻译部分，将非空行分批处理，每批的大小（处理行数）为batch_size
    for i in range(0, len(non_empty_lines), batch_size):
        batch_lines = non_empty_lines[i: i+batch_size]
        inputs = tokenizer(batch_lines, return_tensors="pt", padding=True, truncation=True).to(device)
        generated = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            repetition_penalty=repetition_penalty,
            do_sample=True,
            temperature=temperature,
            top_p=top_p,
            forced_bos_token_id=tokenizer.lang_code_to_id["ja_XX"],
        )
        decoded = [tokenizer.decode(item, skip_special_tokens=True, clean_up_tokenization_spaces=True) for item in generated]

        # 将翻译的文本放回原来的结构中
        for row_position, idx in enumerate(non_empty_indices[i: i+batch_size]):
            outputs_list[idx] = decoded[row_position]
    
    return "\n".join(outputs_list)

