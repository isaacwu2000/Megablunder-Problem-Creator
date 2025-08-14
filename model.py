from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

class Model:
    @staticmethod
    def get_client():
        load_dotenv()
        return genai.Client()

    @staticmethod
    def generate_problem(system="You are a grammar expert", task="Create a Megablunder problem"):
        class Problem(BaseModel):
            problem: str
            answer: str
            solution: str
            category: str

        client = Model.get_client()
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system,
                response_mime_type="application/json",
                response_schema=Problem,
            ),
            contents=task,
        )
        print(response.text)

    

    @staticmethod
    def generate_hard_length():
        pass

    @staticmethod
    def generate_hard_trick():
        pass

    @staticmethod
    def generate_medium():
        pass

    @staticmethod
    def website_problem_to_mcq():
        pass

    @staticmethod
    def check_problem():
        pass

Model.generate_problem()