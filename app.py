from engine.audio_chunk import AudioChunk
from engine.speech2text import Speech2Text
import glob
import time
import gradio as gr
import os

audio_chunk = AudioChunk()
speech2text = Speech2Text()



def recorded_process(recorded_audio_file) -> str:
    text = speech2text.process_voice(recorded_audio_file)
    result =  text["text"]      
    return result


def uploaded_process(uploaded_audio_file) -> str:
    text = speech2text.process_voice(uploaded_audio_file)
    result =  text["text"]      
    return result


def clear_inputs_and_outputs() -> list:
    """
    Clears all inputs and outputs when the user clicks "Clear" button
    """

    return [None, None]

with gr.Blocks() as demo:
    """
    buld gradio app

    """
    gr.Markdown(
        """
        # Automatic Speech Recognition
         
        #####  Experience accurate, and multilingual speech-to-text conversion with our cutting-edge ASR technology.
        """
    )

    with gr.Tab("Record File"):
        with gr.Row():  
            with gr.Column():
                mic_input = gr.Microphone( type="filepath",label="Record voice")
                with gr.Row():
                    clr_btn = gr.Button(value="Clear", variant="secondary")
                    sub_btn = gr.Button(value="submit")
            with gr.Column():
                lbl_output = gr.Textbox(label="Result")

            clr_btn.click(
                fn=clear_inputs_and_outputs,
                    inputs=[],
                    outputs=[mic_input, lbl_output]
            )

            sub_btn.click(
                fn=recorded_process,
                inputs=[mic_input],
                outputs=[lbl_output]
            )


    with gr.Tab("Upload File"):
        with gr.Row():  
            with gr.Column():
                upl_input = gr.Audio( type="filepath", label="Upload a file")   
                with gr.Row():
                        clr_btn = gr.Button(value="Clear", variant="secondary")
                        sub_btn = gr.Button(value="submit")
                gr.Examples(examples=[
                    os.path.join(os.path.dirname(__file__),"examples/politics.mp3"),
                    os.path.join(os.path.dirname(__file__),"examples/law1.mp3"),
                    os.path.join(os.path.dirname(__file__),"examples/law2.mp3"),
                    os.path.join(os.path.dirname(__file__),"examples/law3.mp3"),
                    os.path.join(os.path.dirname(__file__),"examples/economy.mp3"),
                    os.path.join(os.path.dirname(__file__),"examples/general.mp3")
                    ],
                    inputs = upl_input)
            with gr.Column():
                lbl_output = gr.Textbox(label="Result")

            clr_btn.click(
                fn=clear_inputs_and_outputs,
                inputs=[],
                outputs=[upl_input, lbl_output]
            )
            sub_btn.click(
                fn=uploaded_process,
                inputs=[upl_input],
                outputs=[lbl_output]
            )

demo.launch(favicon_path = "./image/test_logo.png", server_name="127.0.0.1", server_port=8000) 