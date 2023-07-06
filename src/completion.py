import os
import openai

class Completion:
    _cwd = os.getcwd()

    def __init__(self) -> None:
        openai.api_key = os.getenv('OPENAI_API_KEY')
        pass

    def set_cwd(self,cwd) -> None:
        self._cwd = cwd
    
    def complete(self, prompt) -> list[str]:
        response = openai.Completion.create(
            engine="davinci",
            prompt=self.build_prompt(prompt),
            temperature=0.9,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["\n", " >"]
        )
        return response.choices[0].text.split('\n')
    
    def build_prompt(self, prompt) -> str:
        return f"{self._cwd}> {prompt}\n"
    