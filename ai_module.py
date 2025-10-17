import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def generate_quote(category: str) -> str:
    prompt = f"Generate a short, original motivational quote about {category}."
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)

    # Safe extraction from Gemini response
    try:
        return response.text.strip()
    except Exception:
        if response and hasattr(response, "candidates") and len(response.candidates) > 0:
            return response.candidates[0].content.parts[0].text.strip()
        else:
            return "Unable to generate quote at this moment."
