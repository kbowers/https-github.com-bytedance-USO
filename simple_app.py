#!/usr/bin/env python3

import os
os.environ['CLIP'] = 'openai/clip-vit-large-patch14'
os.environ['T5'] = 'google/t5-v1_1-xxl'

import gradio as gr
import torch
from uso.flux.pipeline import USOPipeline

def create_simple_demo():
    try:
        # Try to create the pipeline
        pipeline = USOPipeline(
            "flux-dev", 
            "cpu", 
            False, 
            only_lora=True, 
            lora_rank=128, 
            hf_download=True
        )
        print("✓ Pipeline created successfully")
        
        with gr.Blocks() as demo:
            gr.Markdown("# USO - Unified Style and Subject-Driven Generation")
            gr.Markdown("This is a simplified version of the USO app.")
            
            with gr.Row():
                with gr.Column():
                    prompt = gr.Textbox(label="Prompt", value="A beautiful landscape")
                    generate_btn = gr.Button("Generate")
                
                with gr.Column():
                    output_image = gr.Image(label="Generated Image")
            
            def generate_image(prompt_text):
                try:
                    # This would normally generate an image
                    # For now, just return a placeholder
                    return "Image generation would happen here"
                except Exception as e:
                    return f"Error: {str(e)}"
            
            generate_btn.click(
                fn=generate_image,
                inputs=[prompt],
                outputs=[output_image]
            )
        
        return demo
        
    except Exception as e:
        print(f"✗ Error creating pipeline: {e}")
        import traceback
        traceback.print_exc()
        
        # Return a simple error demo
        with gr.Blocks() as demo:
            gr.Markdown("# USO - Error")
            gr.Markdown(f"Error loading the model: {str(e)}")
            gr.Markdown("Please check that all required model weights are available.")
        
        return demo

if __name__ == "__main__":
    demo = create_simple_demo()
    demo.launch(server_port=7860, share=True)