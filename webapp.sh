

#!/bin/bash

<<COMMENT
This script is meant to start the web application.

If you see this script opened in a code editor and need to make it executable, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where this script is located:
        % cd /path/to/HWeditor

3. Set the execute permission on this script:
        % chmod +x webapp.sh

4. You can now run the script as an executable:
        % ./webapp.sh

COMMENT

# Create a virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Start the application
python3 app.py
