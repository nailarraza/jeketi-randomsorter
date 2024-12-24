import pandas as pd
import random
import gradio as gr
from io import StringIO

# Function to parse input dataset from text input
def parse_dataset(input_text):
    try:
        # Convert input text into a DataFrame
        data = pd.read_csv(StringIO(input_text), header=None, names=['Name', 'Availability'])
        return data
    except Exception as e:
        raise ValueError(f"Error parsing input data: {e}")

# Generate random rows based on availability
def generate_random_rows(data):
    result = []
    for _, row in data.iterrows():
        result.extend([row['Name']] * row['Availability'])  # Use the availability value to repeat names
    random.shuffle(result)  # Shuffle the names
    return result

# Function to handle random sort generation
def generate_random_sort(input_text):
    try:
        # Parse the dataset from the input text
        data = parse_dataset(input_text)

        # Generate multiple random rows based on availability
        randomized_rows = generate_random_rows(data)

        # Group results into rows of fixed length for output
        group_size = 5  # Number of names per row
        grouped_results = [randomized_rows[i:i + group_size] for i in range(0, len(randomized_rows), group_size)]

        # Prepare output as a DataFrame for display with a sequential "No" column and names
        output_table = pd.DataFrame({
            "No": range(1, len(grouped_results) + 1),  # Sequential numbering starting from 1
            "Names": [' - '.join(group) for group in grouped_results]
        })

        return output_table
    except Exception as e:
        return pd.DataFrame({"Error": [str(e)]})

# Gradio interface
def app_interface():
    with gr.Blocks() as app:
        gr.Markdown("# Random Photopack JKT48 Sorting - By Nailar Raza and Friends")

        with gr.Row():
            gr.Markdown(" ")

        with gr.Row():
            gr.Markdown(" ")

        with gr.Row():
            gr.Markdown("### Input Dataset JKT48 Photopack (Member Name & Availability) ###")

        with gr.Row():
            gr.Markdown(" ")

        with gr.Row():
            dataset_input = gr.Textbox(placeholder="Enter dataset as CSV format, contoh: \n Christy,60 \n Freya,50 \n Muthe,75 \n Fiony,65",
                                          lines=5, label="Input Data here :")

        with gr.Row():
            gr.Markdown(" ")

        with gr.Row():
            generate_button = gr.Button("Acak Isi Produk Photopack")

        with gr.Row():
            gr.Markdown("### Nb. Acak Minimal 10X agar dapat hasil yang relevan ###")

        with gr.Row():
            gr.Markdown(" ")

        with gr.Row():
            gr.Markdown(" ")

        with gr.Row():
            gr.Markdown("# Hasil :")

        with gr.Row():
            # Output table with interactive checkboxes
            output_table = gr.Dataframe(headers=["No", "Names"],
                                            value=[],  # Set initial empty value
                                            interactive=True)  # Enable interaction with the table

        # When the button is clicked, generate the randomized sort and show the result
        generate_button.click(generate_random_sort,
                              inputs=[dataset_input],  # Pass input only as the dataset
                              outputs=[output_table])

    return app  # Mengembalikan objek app

app = app_interface()