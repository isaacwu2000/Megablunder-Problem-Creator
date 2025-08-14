import json
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
        


def generate_problem(prompt_path, category="CASE"):
    class Problem(BaseModel):
        problem: str
        answer: str
        solution: str
        category: str

    client = get_client()
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=read_file(prompt_path),
            response_mime_type="application/json",
            response_schema=Problem,
        ),
        contents=f"Create a Megablunder problem for the {category} category",
    )

    return response.parsed.model_dump()

def generate_hard_length(category):
    problem = generate_problem("prompts/hard_length.txt", category=category)
    write_problem_to_json(problem, "problems/hard_length_generated.json")

def generate_hard_trick():
    pass

def generate_medium():
    pass

def check_problem():
    pass

generate_hard_length("A")