# interfaces.py
import torch
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

repo_id = "Takaharadesu/dokidori"

device = "cuda" if torch.cuda.is_available() else "cpu"

model = MBartForConditionalGeneration.from_pretrained(repo_id).to(device)
tokenizer = MBart50TokenizerFast.from_pretrained(repo_id)

def translate_multiline(text, max_new_tokens, batch_size, repetition_penalty, temperature, top_p):
    lines = text.split("\n")
    outputs_list = ["" for _ in lines]
    non_empty_lines = [] 
    non_empty_indices = [] 

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped:  
            non_empty_lines.append(stripped)
            non_empty_indices.append(i)
    
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
        decoded = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=True) for g in generated]

        for j, idx in enumerate(non_empty_indices[i: i+batch_size]):
            outputs_list[idx] = decoded[j]
    
    return "\n".join(outputs_list)

