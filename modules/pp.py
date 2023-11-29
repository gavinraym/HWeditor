import os
import uuid
import json
import sys

# Receives practice problem name and number of questions
def new_pp(name, num_qs):

    # Change name from kebab-case to title case with number sign
    title = name.split('-')
    title[-1] = '#' + title[-1]
    title = " ".join(title).title()

    data = {
        "id": str(uuid.uuid4()),
        "name": title,
        "media": {
            "url": "project://assets/" + name + '.png',
            "type": "image"
        },
        "title": title,
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
                        ]
                    }
                ]
            }
        ],
        "scoring": {
            "criteria": [
                {
                    "title": "Practice Problem",
                    "components": [ ],
                    "contexts": [
                        {
                            "type": "checkpoint",
                            "title": "Practice Problem",
                            "checkpoints": [ ]
                        }
                    ]
                }
            ]
        }
    }

    for n in range(1, num_qs + 1):

        checkpoint_uuid = str(uuid.uuid4())

        data['section_groups'][0]['sections'][0]['steps'].append({
        "id": str(uuid.uuid4()),
        "title": "#" + str(n),
        "block_groups": [
            {
                "id": "UUID",
                "blocks": [
                    {
                        "id": checkpoint_uuid,
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
                                "id": str(uuid.uuid4()),
                                "text": "",
                                "correct": False
                            },
                            {
                                "id": str(uuid.uuid4()),
                                "text": "",
                                "correct": False
                            },
                            {
                                "id": str(uuid.uuid4()),
                                "text": "",
                                "correct": True
                            },
                            {
                                "id": str(uuid.uuid4()),
                                "text": "",
                                "correct": False
                            }
                        ]
                    }
                ]
            }
        ]
    })
        
        data['scoring']['criteria'][0]['components'].append({
            "id": checkpoint_uuid,
            "type": "checkpoint",
            "weight": 100
        })

        data['scoring']['criteria'][0]['contexts'][0]['checkpoints'].append(checkpoint_uuid)

    course_data = str({
                            "id": data["id"],
                            "weight": 1
                        }) + ","

 
    return data, course_data