from flask import Flask, render_template, request, send_file
import uuid
import os

# Create Flask app
app = Flask(__name__)

# Ensure visualizations directory exists
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# Import algorithm visual functions
from algorithms.sort_search import (
    bubble_sort_visual, insertion_sort_visual, selection_sort_visual,
    quick_sort_visual, merge_sort_visual, linear_search_visual, binary_search_visual
)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Visualization route
@app.route('/visualize', methods=['POST'])
def visualize():
    data = request.json
    algorithm = data['algorithm']
    array = list(map(int, data['array'].split(',')))
    filename = f"visualizations/{uuid.uuid4().hex}.png"

    if algorithm == 'bubble_sort':
        bubble_sort_visual(array, filename)
    elif algorithm == 'insertion_sort':
        insertion_sort_visual(array, filename)
    elif algorithm == 'selection_sort':
        selection_sort_visual(array, filename)
    elif algorithm == 'quick_sort':
        quick_sort_visual(array, filename)
    elif algorithm == 'merge_sort':
        merge_sort_visual(array, filename)
    elif algorithm == 'linear_search':
        target = int(data['target'])
        linear_search_visual(array, target, filename)
    elif algorithm == 'binary_search':
        target = int(data['target'])
        binary_search_visual(array, target, filename)
    else:
        return "Algorithm not supported", 400

    return send_file(filename, mimetype='image/png')

# Run server
if __name__ == '__main__':
    app.run(debug=True)