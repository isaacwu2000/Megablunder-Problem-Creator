import json
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

def get_client():
    load_dotenv()
    return genai.Client()

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def write_problem_to_json(problem, json_path):
    try:
        with open(json_path, 'r') as f:
            problems = json.load(f)
            problems.append(problem)
        with open(json_path, 'w') as f:
            json.dump(problems, f, indent=4)
    except json.decoder.JSONDecodeError:
        with open(json_path, 'w') as f:
            json.dump(problem, f, indent=4) 

def generate_problem(prompt_path, model="gemini-2.5-flash", category="A"):
    class Problem(BaseModel):
        problem: str
        answer: str
        solution: str
        category: str
    while True:
        try:
            client = get_client()
            response = client.models.generate_content(
                model=model,
                config=types.GenerateContentConfig(
                    system_instruction=read_file(prompt_path),
                    response_mime_type="application/json",
                    response_schema=Problem,
                ),
                contents=f"Create a Megablunder problem of type {category} with only a {category} error in the correct answer choice.",
            )
            return response.parsed.model_dump()
        except Exception as e:
            print(e)
            time.sleep(10)

def generate_hard_length(category):
    problem = generate_problem("prompts/hard_length.txt", category=category)
    write_problem_to_json(problem, "problems/hard_length_generated.json")

def generate_hard_trick(category):
    problem = generate_problem("prompts/hard_trick.txt", category=category)
    write_problem_to_json(problem, "problems/hard_trick_generated.json")

def generate_medium(category):
    problem = generate_problem("prompts/medium.txt", category=category)
    write_problem_to_json(problem, "problems/medium_generated.json")

