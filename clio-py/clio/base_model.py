import os
import google.generativeai as genai

def load_dotenv():
    """Loads environment variables from a .env file."""
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    if os.path.exists(dotenv_path):
        with open(dotenv_path) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ.setdefault(key.strip(), value.strip())

load_dotenv()

class BaseModel:
    """Base AI model that uses the Gemini API."""
    def __init__(self):
        api_key = os.environ.get("GEMINI_API_KEY")
        model = os.environ.get("model", "gemini-1.5-flash-latest")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)
        self.cache = None

    def formulate_plan(self, prompt, steering=None):
        """Formulates a plan for solving the problem."""
        if self.cache and self.cache.get(prompt):
            return self.cache.get(prompt)['value']
        
        response = self.model.generate_content(f"Formulate a plan to answer the following question: {prompt}")
        plan = response.text.strip().split('\n')
        
        if self.cache:
            self.cache.set(prompt, plan, source=prompt)
        return plan

    def execute_step(self, step, steering=None):
        """Executes a single step of the plan and returns the result and certainty."""
        if self.cache and self.cache.get(step):
            cached_data = self.cache.get(step)
            result = cached_data['value']
            certainty = cached_data['certainty']
        else:
            response = self.model.generate_content(f"Execute the following step: {step}")
            result = response.text.strip()
            certainty = self.calculate_certainty(result)
            if self.cache:
                self.cache.set(step, result, source=step, certainty=certainty)

        return result, certainty

    def reflect(self, prompt, results, steering=None):
        """Reflects on the results of the plan execution."""
        cache_key = f"{prompt}-{results}"
        if self.cache and self.cache.get(cache_key):
            return self.cache.get(cache_key)['value']

        response = self.model.generate_content(f"Reflect on the results of the following plan execution:\nPrompt: {prompt}\nResults: {results}")
        reflection = response.text.strip()

        if self.cache:
            self.cache.set(cache_key, reflection, source=prompt)
        return reflection

    def formulate_conclusion(self, prompt, reflection, steering=None):
        """Formulates a final conclusion."""
        cache_key = f"{prompt}-{reflection}"
        if self.cache and self.cache.get(cache_key):
            return self.cache.get(cache_key)['value']

        response = self.model.generate_content(f"Formulate a final conclusion based on the following reflection:\nPrompt: {prompt}\nReflection: {reflection}")
        conclusion = response.text.strip()

        if self.cache:
            self.cache.set(cache_key, conclusion, source=prompt)
        return conclusion

    def calculate_certainty(self, text):
        """Calculates the certainty of a given text."""
        response = self.model.generate_content(f"Calculate the confidence score (from 0 to 1) of the following text, providing only the number:\nText: {text}")
        try:
            return float(response.text.strip())
        except ValueError:
            return 0.5

    def apply_steering(self, steering_command, plan, results):
        """Applies a steering command to the plan and results."""
        response = self.model.generate_content(f"Apply the following steering command to the plan and results:\nSteering Command: {steering_command}\nPlan: {plan}\nResults: {results}")
        # In a real application, you would parse the response and update the plan and results accordingly.
        return plan, results