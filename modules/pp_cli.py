import os
import uuid
import json
import sys


def new_pp():

    name = "untitled"
    if len(sys.argv) >= 2:
        name = sys.argv[2]
    print(name)
    title = name.replace('-', ' ').title()
    

    for num in range(1, 25):

        title_with_num = title + " #" + str(num)
  
        data = {
            "id": str(uuid.uuid4()),
            "name": title_with_num,
            "media": {
                "url": "project://assets/" + name +"-" + str(num) + ".png",
                "type": "image"
            },
            "title": title_with_num,
            "language": "CoBlocks",
            "vocabulary": "#include(course://vocabulary.json)",
            "activities": {},
            "section_groups": [
                {
                    "id": "UUID",
                    "title": "PRACTICE PROBLEM",
                    "sections": [
                        {
                            "id": str(uuid.uuid4()),
                            "title": "Practice Problem",
                            "steps": [
                                {
                                    "id": str(uuid.uuid4()),
                                    "title": "#1",
                                    "block_groups": [
                                        {
                                            "id": "UUID",
                                            "blocks": [
                                                {
                                                    "id": str(uuid.uuid4()),
                                                    "type": "checkpoint",
                                                    "title": "Multiple Choice",
                                                    "variant": "multiple_choice",
                                                    "question": [
                                                        {
                                                            "type": "text",
                                                            "text": ""
                                                        }
                                                    ],
                                                    "choices": [
                                                        {
                                                            "id": "e84c2d7a-1914-4018-9b55-392fdf21e778",
                                                            "text": "",
                                                            "correct": False
                                                        },
                                                        {
                                                            "id": "5b5ca649-e1b2-4408-9afa-73a1db0082ef",
                                                            "text": "",
                                                            "correct": False
                                                        },
                                                        {
                                                            "id": "c0359df6-3266-4632-a07b-37a0d06a602a",
                                                            "text": "",
                                                            "correct": True
                                                        },
                                                        {
                                                            "id": "5d98edbd-9c6c-49dc-b965-5373794eaf1e",
                                                            "text": "",
                                                            "correct": False
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ],
            "scoring": {
                "criteria": [
                    {
                        "title": "Practice Problem",
                        "components": [
                            {
                                "id": str(uuid.uuid4()),
                                "type": "checkpoint",
                                "weight": 100
                            }
                        ],
                        "contexts": [
                            {
                                "type": "checkpoint",
                                "title": "Practice Problem",
                                "checkpoints": [
                                    str(uuid.uuid4())
                                ]
                            }
                        ]
                    }
                ]
            }
        }

        with open(os.path.join("output", name + "-" + str(num) + ".json"), "w") as f:
            json.dump(data, f, indent=4)