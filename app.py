
import gradio as gr
from interfaces import translate_multiline

with gr.Blocks() as demo:
    gr.Markdown("## 邦邦对话风格化翻译器")

    with gr.Row():
        with gr.Column(scale=0, min_width=500):
            with gr.Row():
                kasumi_btn = gr.Button("香澄", variant="secondary", scale=0, min_width=82)
                tae_btn = gr.Button("多惠", variant="secondary", scale=0, min_width=82)
                rimi_btn = gr.Button("里美", variant="secondary", scale=0, min_width=82)
                saaya_btn = gr.Button("沙绫", variant="secondary", scale=0, min_width=82)
                arisa_btn = gr.Button("有咲", variant="secondary", scale=0, min_width=82)
            with gr.Row():
                ran_btn = gr.Button("兰", variant="secondary", scale=0, min_width=82)
                moka_btn = gr.Button("摩卡", variant="secondary", scale=0, min_width=82)
                himari_btn = gr.Button("绯玛丽", variant="secondary", scale=0, min_width=82)
                tomo_btn = gr.Button("巴", variant="secondary", scale=0, min_width=82)
                tsugumi_btn = gr.Button("鸫", variant="secondary", scale=0, min_width=82)
            with gr.Row():
                kokoro_btn = gr.Button("心", variant="secondary", scale=0, min_width=82)
                kaoru_btn = gr.Button("薰", variant="secondary", scale=0, min_width=82)
                hagumi_btn = gr.Button("育美", variant="secondary", scale=0, min_width=82)
                kanon_btn = gr.Button("花音", variant="secondary", scale=0, min_width=82)
                misaki_btn = gr.Button("美咲", variant="secondary", scale=0, min_width=82)
            with gr.Row():
                aya_btn = gr.Button("彩", variant="secondary", scale=0, min_width=82)
                hina_btn = gr.Button("日菜", variant="secondary", scale=0, min_width=82)
                chisato_btn = gr.Button("千圣", variant="secondary", scale=0, min_width=82)
                maya_btn = gr.Button("麻弥", variant="secondary", scale=0, min_width=82)
                eve_btn = gr.Button("伊芙", variant="secondary", scale=0, min_width=82)
        with gr.Column(scale=0, min_width=500):
            with gr.Row():
                yukina_btn = gr.Button("友希那", variant="secondary", scale=0, min_width=82)
                sayo_btn = gr.Button("纱夜", variant="secondary", scale=0, min_width=82)
                lisa_btn = gr.Button("莉莎", variant="secondary", scale=0, min_width=82)
                ako_btn = gr.Button("亚子", variant="secondary", scale=0, min_width=82)
                rinko_btn = gr.Button("燐子", variant="secondary", scale=0, min_width=82)
            with gr.Row():
                mashiro_btn = gr.Button("真白", variant="secondary", scale=0, min_width=82)
                toko_btn = gr.Button("透子", variant="secondary", scale=0, min_width=82)
                nanami_btn = gr.Button("七深", variant="secondary", scale=0, min_width=82)
                tsukushi_btn = gr.Button("筑紫", variant="secondary", scale=0, min_width=82)
                rui_btn = gr.Button("瑠唯", variant="secondary", scale=0, min_width=82)
            with gr.Row():
                layer_btn = gr.Button("瑞依", variant="secondary", scale=0, min_width=82)
                lock_btn = gr.Button("六花", variant="secondary", scale=0, min_width=82)   
                masking_btn = gr.Button("益木", variant="secondary", scale=0, min_width=82)
                pareo_btn = gr.Button("PAREO", variant="secondary", scale=0, min_width=82) 
                chuchu_btn = gr.Button("CHU²", variant="secondary", scale=0, min_width=82)
            with gr.Row():    
                tomori_btn = gr.Button("灯", variant="secondary", scale=0, min_width=82)
                anon_btn = gr.Button("爱音", variant="secondary", scale=0, min_width=82)
                rana_btn = gr.Button("乐奈", variant="secondary", scale=0, min_width=82)
                soyo_btn = gr.Button("素世", variant="secondary", scale=0, min_width=82)
                taki_btn = gr.Button("立希", variant="secondary", scale=0, min_width=82)
        with gr.Column():
            gr.Markdown("""
                        #### 输入样例: 
                            <kasumi> 哇，有咲今天的便当，看起来超级好吃的！\n
                            <arisa> 话说…… 你每天看我的便当，都要说看起来很好吃
                        """)

    with gr.Row():
        input_text = gr.Textbox(label="输入中文文本", placeholder="输入需要翻译的文本", lines=16)
        output_text = gr.Textbox(label="翻译结果", lines=16)
    
    with gr.Row():
        translate_button = gr.Button("翻译")

    with gr.Row():
        max_new_tokens_slider = gr.Slider(minimum=32, maximum=96, step=1, value=64, label="max_new_tokens")
        batch_size = gr.Slider(minimum=1, maximum=32, step=1, value=8, label="batch_size")

    with gr.Row():    
        temperature_slider = gr.Slider(minimum=0.3, maximum=1.5, step=0.05, value=0.75, label="temperature")
        top_p_slider = gr.Slider(minimum=0.5, maximum=1.0, step=0.05, value=0.9, label="top_p")
        repetition_penalty = gr.Slider(minimum=1.0, maximum=2.0, step=0.05, value=1.2, label="repetition_penalty")   
  
    kasumi_btn.click(lambda text: text + "<kasumi> ", inputs=input_text, outputs=input_text)
    tae_btn.click(lambda text: text + "<tae> ", inputs=input_text, outputs=input_text)
    rimi_btn.click(lambda text: text + "<rimi> ", inputs=input_text, outputs=input_text)
    saaya_btn.click(lambda text: text + "<saaya> ", inputs=input_text, outputs=input_text)
    arisa_btn.click(lambda text: text + "<arisa> ", inputs=input_text, outputs=input_text)
    ran_btn.click(lambda text: text + "<ran> ", inputs=input_text, outputs=input_text)
    moka_btn.click(lambda text: text + "<moka> ", inputs=input_text, outputs=input_text)
    himari_btn.click(lambda text: text + "<himari> ", inputs=input_text, outputs=input_text)
    tomo_btn.click(lambda text: text + "<tomo> ", inputs=input_text, outputs=input_text)
    tsugumi_btn.click(lambda text: text + "<tsugumi> ", inputs=input_text, outputs=input_text)
    kokoro_btn.click(lambda text: text + "<kokoro> ", inputs=input_text, outputs=input_text)
    kaoru_btn.click(lambda text: text + "<kaoru> ", inputs=input_text, outputs=input_text)
    hagumi_btn.click(lambda text: text + "<hagumi> ", inputs=input_text, outputs=input_text)
    kanon_btn.click(lambda text: text + "<kanon> ", inputs=input_text, outputs=input_text)
    misaki_btn.click(lambda text: text + "<misaki> ", inputs=input_text, outputs=input_text)
    aya_btn.click(lambda text: text + "<aya> ", inputs=input_text, outputs=input_text)
    hina_btn.click(lambda text: text + "<hina> ", inputs=input_text, outputs=input_text)
    chisato_btn.click(lambda text: text + "<chisato> ", inputs=input_text, outputs=input_text)
    maya_btn.click(lambda text: text + "<maya> ", inputs=input_text, outputs=input_text)
    eve_btn.click(lambda text: text + "<eve> ", inputs=input_text, outputs=input_text)
    yukina_btn.click(lambda text: text + "<yukina> ", inputs=input_text, outputs=input_text)
    sayo_btn.click(lambda text: text + "<sayo> ", inputs=input_text, outputs=input_text)
    lisa_btn.click(lambda text: text + "<lisa> ", inputs=input_text, outputs=input_text)
    ako_btn.click(lambda text: text + "<ako> ", inputs=input_text, outputs=input_text)
    rinko_btn.click(lambda text: text + "<rinko> ", inputs=input_text, outputs=input_text)
    mashiro_btn.click(lambda text: text + "<mashiro> ", inputs=input_text, outputs=input_text)
    toko_btn.click(lambda text: text + "<toko> ", inputs=input_text, outputs=input_text)
    nanami_btn.click(lambda text: text + "<nanami> ", inputs=input_text, outputs=input_text)
    tsukushi_btn.click(lambda text: text + "<tsukushi> ", inputs=input_text, outputs=input_text)
    rui_btn.click(lambda text: text + "<rui> ", inputs=input_text, outputs=input_text)
    layer_btn.click(lambda text: text + "<layer> ", inputs=input_text, outputs=input_text)
    lock_btn.click(lambda text: text + "<lock> ", inputs=input_text, outputs=input_text)
    masking_btn.click(lambda text: text + "<masking> ", inputs=input_text, outputs=input_text)
    pareo_btn.click(lambda text: text + "<pareo> ", inputs=input_text, outputs=input_text)
    chuchu_btn.click(lambda text: text + "<chuchu> ", inputs=input_text, outputs=input_text)
    tomori_btn.click(lambda text: text + "<tomori> ", inputs=input_text, outputs=input_text)
    anon_btn.click(lambda text: text + "<anon> ", inputs=input_text, outputs=input_text)
    rana_btn.click(lambda text: text + "<rana> ", inputs=input_text, outputs=input_text)
    soyo_btn.click(lambda text: text + "<soyo> ", inputs=input_text, outputs=input_text)
    taki_btn.click(lambda text: text + "<taki> ", inputs=input_text, outputs=input_text)
    
    translate_button.click(fn=translate_multiline, inputs=[input_text, max_new_tokens_slider, batch_size, repetition_penalty, temperature_slider, top_p_slider], outputs=output_text)

demo.launch(share=True)
