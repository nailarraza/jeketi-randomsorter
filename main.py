import pandas as pd
import random
import gradio as gr
from io import StringIO

# ... (fungsi parse_dataset, generate_random_rows, dan generate_random_sort tetap sama) ...

# Gradio interface
def app_interface():
    with gr.Blocks() as app:
        # ... (antarmuka Gradio tetap sama) ...

    return app

# Launch the application with the correct port
app = app_interface()
app.launch(server_name="0.0.0.0", server_port=int(os.environ.get('PORT', 7860)))
