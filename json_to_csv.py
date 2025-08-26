import json, csv

def format_problems_json(file_path, difficulty, synthetic=True):
    with open(file_path, "r") as f:
        try:
            problems_json = json.load(f)
        except json.decoder.JSONDecodeError:
            return []
        formatted_problems = []
        for problem in problems_json:
            problem["difficulty"] = difficulty
            if synthetic:
                problem["source"] = "AI + Human"
            else:
                problem["source"] = "Human"
            formatted_problems.append(problem)
    return formatted_problems

# Format all the problems into a unified dictionary format for CSV write
hard_length = format_problems_json("human_examples/hard_length.json", "hard_length", synthetic=False)
hard_trick = format_problems_json("human_examples/hard_trick.json", "hard_trick", synthetic=False)
medium = format_problems_json("human_examples/medium.json", "medium", synthetic=False)
hard_length_generated = format_problems_json("problems/hard_length_generated.json", "hard_length")
hard_trick_generated = format_problems_json("problems/hard_trick_generated.json", "hard_trick")
medium_generated = format_problems_json("problems/medium_generated.json", "medium")

# Add all of the problems to all_problems.csv
with open("problems/all_problems.csv", "w") as f:
    problems = hard_length + hard_trick + medium + hard_length_generated + hard_trick_generated + medium_generated
    writer = csv.DictWriter(f, fieldnames = ["problem","answer","solution","category","difficulty","source"])
    writer.writeheader()
    writer.writerows(problems)