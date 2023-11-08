from flask import Flask, request, jsonify, render_template, url_for
from PIL import Image
import os
import shutil
import webbrowser
import threading
import subprocess
from modules.pp import new_pp
import json

# Configuration settings
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Routes
@app.route('/')
def index():
    static_url = url_for('static', filename='images/')
    return render_template('index.html', static_url=static_url)

@app.route('/parse_gif', methods=['POST'])
def parse_gif():
    image_path = os.path.join('static', 'images')
    shutil.rmtree(image_path, ignore_errors=True)
    os.mkdir(image_path)

    try:
        # Get the GIF file from the request
        gif_file = request.files['gif']

        if not gif_file:
            return jsonify({'error': 'No GIF file uploaded'}), 400
        
        name = gif_file.filename.split('.')[0]

        # Open the GIF file using Pillow (PIL)
        gif = Image.open(gif_file)

        # Calculate the total number of frames in the GIF
        total_frames = gif.n_frames

        # Determine the frame interval to obtain 20 evenly spaced frames
        frame_interval = max(total_frames // 20, 1)

        count = 0
        # Extract the evenly spaced frames from the GIF
        for i in range(0, total_frames, frame_interval):
            gif.seek(i)
            frame = gif.copy()
            frame.save(os.path.join(image_path,f'{name}-{count}.png'))
            count += 1

        return jsonify(), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/save_card', methods=['POST'])
def save_card():
    # Get 'num_mcqs' 'filename' and 'card' from the request
    num_mcqs = int(request.form['num_mcqs'])
    filename = request.form['filename']
    projectname = request.form['projectname']
    card = request.files['card']

    # Get the file paths
    save_path = 'output'
    project_path = os.path.join(save_path, projectname )
    assets_path = os.path.join(project_path, 'assets')

    # Create the directories if they don't exist
    for path in [save_path, project_path, assets_path]:
        if not os.path.exists(path):
            os.makedirs(path)

    # Save the card image to the assets directory
    card.save(os.path.join(assets_path, filename + '.png'))

    # Create the JSON file
    pp_data, course_data = new_pp(filename, num_mcqs)
    with open(os.path.join(project_path, filename + '.json'), 'w') as f:
        json.dump(pp_data, f, indent=4)
    with open(os.path.join(save_path, 'course_data.txt'), 'a') as f:
        f.write(course_data)

    return jsonify(), 200

@app.route('/open_save_dir', methods=['GET'])
def open_save_dir():
    # Open the save directory
    subprocess.run(['open', '-a', 'Finder', 'output/.'])
    return jsonify(), 200


def open_browser():
    # Wait for a moment to ensure the Flask app has started
    import time
    time.sleep(2)  # Adjust the sleep duration as needed

    # Open a web browser to the specified URL (e.g., http://localhost:5000)
    url = 'http://127.0.0.1:5000'  # Change the port number as needed
    webbrowser.open(url)

# Entry point
def start_app():
    # Create a thread to open the web browser
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.start()

    # Start the Flask app in the main thread
    app.run(debug=True)

# Allows for running the app from the command line
if __name__ == '__main__':
    start_app()