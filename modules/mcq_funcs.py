import os
import uuid
import json
from . import OUTPUT_PATH, INPUT_PATH


def new_mcq(number_of_questions=1):
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
    
    return {"checkpoint-set": data}

def new_exam(number_of_questions=1):
    data = {
        "id": "a5f05d24-1d00-45bb-b642-df6521645b3b",
        "name": "Level *# Exam",
        "media": {
            "url": "project://assets/*IMAGE-PATH.gif",
            "type": "image"
        },
        "title": "Level *# Exam",
        "language": "None",
        "activities": new_mcq(number_of_questions),
        "section_groups": [
        {
      "id": "UUID",
      "title": "INTRO",
      "sections": [
        {
          "id": "3f4bab2f-75d7-468a-925a-29add05deb85",
          "title": "Overview",
          "steps": [
            {
              "id": "6e09c5b5-955a-4f79-8726-32795c24a08d",
              "title": "Exam Introduction",
              "block_groups": [
                {
                  "id": "UUID",
                  "blocks": [
                    {
                      "id": "UUID",
                      "text": "This practice exam will help you prepare for the *COURSE exam. Questions are modeled after real exam questions and will give you the opportunity to reflect on what you've learned so far and see where you can improve.",
                      "type": "text"
                    },
                    {
                      "id": "UUID",
                      "text": "Once you begin, you will not be able to go back and review or change your answers, so be sure to carefully respond to each question.",
                      "type": "text"
                    }
                  ]
                },
                {
                  "id": "UUID",
                  "blocks": [
                    {
                      "id": "UUID",
                      "text": "You may use the exam reference sheet <a target='_blank' href='course://assets/*REF-SHEET.pdf'>linked here</a>linked here</a> to help answer the following questions. This is the same exam reference sheet that will be available to you during the exam.",
                      "type": "text"
                    }
                  ]
                },
                {
                  "id": "UUID",
                  "blocks": [
                    {
                      "id": "UUID",
                      "text": "<img style='width: 100%; max-width: 500px; display: block; margin-left: auto; margin-right: auto' src='course://assets/project-theme-exams.png'>",
                      "type": "text"
                    }
                  ],
                  "variant": "transparent"
                }
              ]
            }
          ]
        }
      ]
    },
        {
      "id": "UUID",
      "title": "EXAM",
      "sections": [
        {
          "id": "d2f5f380-8251-4b3a-acc1-02fee794254e",
          "title": "Multiple Choice",
          "steps": [
            {
              "id": "701147ff-ebc9-4cac-8ec0-435fd9cc9806",
              "title": "Questions",
              "activity_id": "checkpoint-set"
            }
          ]
        }
      ]
    },
        {
      "id": "UUID",
      "title": "SUBMIT",
      "sections": [
        {
          "id": "4322a1b7-9e20-49d6-ab34-6e376e7a3467",
          "title": "Submit Your Response",
          "steps": [
            {
              "id": "392b4f28-00cc-470b-85b9-984d8b629795",
              "title": "Submit",
              "block_groups": [
                {
                  "id": "UUID",
                  "blocks": [
                    {
                      "id": "UUID",
                      "text": "Click <img style='margin: 0; vertical-align: -6px;' src='course://assets/inline-images/submit-button.svg'> to submit your exam.",
                      "type": "text"
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
    }
    print("Outputting mcq data to output/test.json")
    with open(os.path.join(OUTPUT_PATH, "test.json"), "w") as f:
        json.dump(data, f, indent=4)

    from modules.uuids import process_dict
    return process_dict(data)



if __name__ == "__main__":

    new_mcq()