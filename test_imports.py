#!/usr/bin/env python3

import os
os.environ['CLIP'] = 'openai/clip-vit-large-patch14'
os.environ['T5'] = 'google/t5-v1_1-xxl'

try:
    import torch
    print("✓ PyTorch imported successfully")
    print(f"✓ PyTorch version: {torch.__version__}")
    print(f"✓ CUDA available: {torch.cuda.is_available()}")
    
    import gradio as gr
    print("✓ Gradio imported successfully")
    
    from uso.flux.pipeline import USOPipeline
    print("✓ USOPipeline imported successfully")
    
    print("\n✓ All imports successful! The app should be able to run.")
    
except Exception as e:
    print(f"✗ Import error: {e}")
    import traceback
    traceback.print_exc()