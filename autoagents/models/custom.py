import requests

from langchain.llms.base import LLM


class CustomLLM(LLM):

    model_name: str = "action_longchat_7b"

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(self, prompt: str, stop=None) -> str:
        r = requests.post(
            "http://localhost:8000/v1/chat/completions",
            json={
                "model": self.model_name,
                "messages": [{"role": "user", "content": prompt}],
                "stop": stop
            },
        )
        result = r.json()
        return result["choices"][0]["message"]["content"]

    async def _acall(self, prompt: str, stop=None) -> str:
        r = requests.post(
            "http://localhost:8000/v1/chat/completions",
            json={
                "model": self.model_name,
                "messages": [{"role": "user", "content": prompt}],
                "stop": stop
            },
        )
        result = r.json()
        return result["choices"][0]["message"]["content"]
