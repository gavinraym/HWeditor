import os
import shutil
from PIL import Image
from modules.pp import new_pp
import json
from . import OUTPUT_PATH, INPUT_PATH

def parse_gif(gif_file):

    if not gif_file:
        # raise error
        raise Exception('No GIF file was uploaded')
    
    image_path = os.path.join('static','practice_problem_gen_temp')
    shutil.rmtree(image_path, ignore_errors=True)
    os.mkdir(image_path)

    name,ext = gif_file.filename.split('.')

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

    return {"success": True, "message": "GIF parsed successfully"}


def save_card(num_mcqs, filename, projectname, card):
# Get 'num_mcqs' 'filename' and 'card' from the request

    # Get the file paths
    project_path = os.path.join(OUTPUT_PATH, projectname )
    assets_path = os.path.join(project_path, 'assets')

    # Create the directories if they don't exist
    for path in [OUTPUT_PATH, project_path, assets_path]:
        if not os.path.exists(path):
            os.makedirs(path)

    # Save the card image to the assets directory
    card.save(os.path.join(assets_path, filename + '.png'))

    # Create the JSON file
    pp_data, course_data = new_pp(filename, num_mcqs)
    with open(os.path.join(project_path, 'project.json'), 'w') as f:
        json.dump(pp_data, f, indent=4)
    with open(os.path.join(OUTPUT_PATH, 'course_data.txt'), 'a') as f:
        f.write(course_data)    