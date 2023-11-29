import os
import uuid
import json


def new_id(): return str(uuid.uuid4())


# Check if the script is being run from the root level
output_dir = os.path.join("output")
if not os.path.exists(output_dir):
    print("Please create an directory called 'output' at the root.")
    exit(1)


def rubric(data):
    # Rubric IDs will be recorded by order of appearance for use later on.
    for rubric in data["rubric"]:
        for requirement in rubric["requirements"]:
            requirement["id"] = new_id()


def section_groups(data):

    # Lowest level of nesting, the block
    def blocks(block, block_group, step, section, section_group):
        block["id"] = "UUID"

        if block.get("type") and block["type"] == "checkpoint":
            block["id"] = new_id()
            data["temp"]["checkpoints"].append({
                "title": step["title"],
                "block": block,
            })

        if block.get("choices"):
            for choice in block["choices"]:
                choice["id"] = new_id()

    def block_groups(block_group, step, section, section_group):
        block_group["id"] = "UUID"
        for block in block_group["blocks"]:
            blocks(block, block_group, step, section, section_group)

    def steps(step, section, section_group):
        step["id"] = new_id()
        if step.get("block_groups"):
            for block_group in step["block_groups"]:
                block_groups(block_group, step, section, section_group)

    def sections(section, section_group):
        section["id"] = new_id()
        for step in section["steps"]:
            steps(step, section, section_group)

    for section_group in data["section_groups"]:
        section_group["id"] = "UUID"
        for section in section_group["sections"]:
            sections(section, section_group)


def activities(data):

    def questions(question):
        question["id"] = "UUID"

    def choices(choice):
        choice["id"] = new_id()

    def checkpoints(checkpoint, checkpoint_set, name, data):
        checkpoint["id"] = new_id()
        data["temp"]["checkpoints"].append({
            "title": name,
            "block": checkpoint,
        })

        for question in checkpoint["question"]:
            questions(question)

        for choice in checkpoint["choices"]:
            choices(choice)

    def checkpoint_sets(checkpoint_set, name, data):
        checkpoint_set["id"] = new_id()
        for checkpoint in checkpoint_set["checkpoints"]:
            checkpoints(checkpoint, checkpoint_set, name, data)

    for name, activity in data["activities"].items():
        if activity["tool"] == "checkpoint-set":
            checkpoint_sets(activity, name, data)

def guide(data):
    
    def block_groups(block_group, step, section, section_group):
        block_group["id"] = "UUID"
        for block in block_group["blocks"]:
            block["id"] = "UUID"
    
    def steps(step, section, section_group):
        step["id"] = new_id()
        for block_group in step["block_groups"]:
            block_groups(block_group, step, section, section_group)
    
    def sections(section, section_group):
        section["id"] = new_id()
        for step in section["steps"]:
            steps(step, section, section_group)
    
    def section_groups(section_group):
        section_group["id"] = "UUID"
        for section in section_group["sections"]:
            sections(section, section_group)
            
    for section_group in data["section_groups"]:
        section_groups(section_group)

def criteria(data):
    project_checkpoints = {
                "title": "Project Checkpoints",
                "components": [],
                "contexts": [
                    {
                        "type": "checkpoint",
                        "title": "Project Example",
                        "checkpoints": []
                    },
                    {
                        "type": "checkpoint",
                        "title": "Debugging Challenges",
                        "checkpoints": []
                    },
                    {
                        "type": "checkpoint",
                        "title": "Core Concept Review",
                        "checkpoints": []
                    },
                    {
                        "type": "checkpoint",
                        "title": "Vocabulary Check",
                        "checkpoints": []
                    },
                    {
                        "type": "checkpoint",
                        "title": "Code Review",
                        "checkpoints": []
                    },
                ],
            }
    criteria = [project_checkpoints]

    def add_component(checkpoint):
        project_checkpoints["components"].append({
            "id": checkpoint["block"]["id"],
            "type": checkpoint["block"]["type"],
            # You can add weight to checkpoints in section group blocks
            # and it will fill it in here!
            "weight": checkpoint["block"].get("weight", 1),
        })

    def add_context(id, context_type):
        for context in project_checkpoints["contexts"]:
            if context["title"] == context_type:
                context["checkpoints"].append(id)
        
    def rubric(checkpoint):
        for category in checkpoint["block"]["categories"]:
            rubric = {
                "title": category["type"].replace("-", " ").title(),
                "components": [{
                    "id": checkpoint["block"]["id"],
                    "type": "checkpoint",
                    "variant": "rubric",
                    "categories": [category["type"]],
                    "weight": 1
                }],
                "contexts": [{
                    "type": "activity",
                    "activity": "student-project",
                    "title": "Project"
                }]
            }
            if category.get("required"):
                rubric["components"][0]["required"] = category["required"]
            criteria.append(rubric)

    # This is where checkpoints are separated by type (rubric, debug, etc.)
    for checkpoint in data["temp"]["checkpoints"]:

        # checkpoints with variant 'short_answer' will be ignored
        if checkpoint["block"].get("variant", "") == "short_answer":
            continue

        elif checkpoint["block"].get("variant", "") == "rubric":
            rubric(checkpoint)
            
        elif "Debugging Challenge" in checkpoint["title"]:
            add_component(checkpoint)
            add_context(checkpoint["block"]["id"], "Debugging Challenges")
            
        elif "Project Example" in checkpoint["title"]:
            add_component(checkpoint)
            add_context(checkpoint["block"]["id"], "Project Example")
            
        elif "Vocabulary" in checkpoint["title"]:
            add_component(checkpoint)
            add_context(checkpoint["block"]["id"], "Vocabulary Check")

        elif "Code Review" in checkpoint["title"]:
            add_component(checkpoint)
            add_context(checkpoint["block"]["id"], "Code Review")

        elif "checkpoint-set" in checkpoint["title"]:
            add_component(checkpoint)
            add_context(checkpoint["block"]["id"], "Core Concept Review")

    # Removing unused contexts
    contexts_to_remove = []
    for context in project_checkpoints["contexts"]:
        if len(context["checkpoints"]) == 0:
            contexts_to_remove.append(context)
    for context in contexts_to_remove:
        project_checkpoints["contexts"].remove(context)

    # Adding criteria to data
    data["scoring"]["criteria"] = criteria

def process_dict(data):
        
    # Add temp fields for storing checkpoint UUIDs
    data["temp"] = dict()
    data["temp"]["checkpoints"] = list()
    data["scoring"] = dict()
    
    # Process project data
    if not data.get("id"): data = {"id": new_id(), **data}
    if data.get("rubric"): rubric(data)
    section_groups(data)
    if data.get("activities"): activities(data)
    criteria(data)
    
    # Delete temp and save
    del data["temp"]
    return data

def process_file(file):
    data = json.load(file)
    data = process_dict(data)
    with open(os.path.join(output_dir, "project.json"), "w") as f:
        json.dump(data, f, indent=4)
        
def run():
    for file in os.listdir(input_dir):
        if file.endswith(".json"):
            process_file(file)


if __name__ == "__main__":
    run()