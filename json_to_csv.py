import json, csv

with open("problems/all_problems.csv", "r") as f:
    problems = list(csv.DictReader(f))

with open("problems/hard_length_generated.json", "r") as f:
    hard_length_generated_json = json.load(f)
    hard_length_generated = []
    for problem in hard_length_generated_json:
        problem["difficulty"] = "hard_length"
        problem["synthetic"] = True
        hard_length_generated.append(problem)

with open("problems/all_problems.csv", "w") as f:
    problems += hard_length_generated
    writer = csv.DictWriter(f, fieldnames = ["problem","answer","solution","category","difficulty","synthetic"])
    writer.writeheader()
    writer.writerows(problems)