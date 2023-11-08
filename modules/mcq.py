import json
import os
import sys
import uuid

def new_mcq():

    try:
        number_of_questions = int(sys.argv[2])
    except IndexError:
        number_of_questions = 1
    except ValueError:
        print("Second argument must be an integer indicating umber of questions.")
        sys.exit(1)

    data = {
        "id": str(uuid.uuid4()),
        "tool": "checkpoint-set",
        "checkpoints": []
    }

    for _ in range(number_of_questions):
        data["checkpoints"].append({
            "id": str(uuid.uuid4()),
            "type": "checkpoint",
            "title": "Question",
            "variant": "multiple_choice",
            "question": [
                {
                    "id": "UUID",
                    "text": "",
                    "type": "text"
                }
            ],
            "choices": [
                {
                    "id": str(uuid.uuid4()),
                    "type": "text",
                    "text": "",
                    "correct": True
                },
                {
                    "id": str(uuid.uuid4()),
                    "type": "text",
                    "text": "",
                    "correct": False
                },
                {
                    "id": str(uuid.uuid4()),
                    "type": "text",
                    "text": "",
                    "correct": False
                },
                {
                    "id": str(uuid.uuid4()),
                    "type": "text",
                    "text": "",
                    "correct": False
                }
            ]
        })
    
    str_data = f'"checkpoint-set": {json.dumps(data, indent=4)}'

    with open(os.path.join("output", "mcq.json"), "w") as f:
        f.write(str_data)