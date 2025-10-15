import os
import requests

# Use a valid model
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

def get_ai_response(word: str) -> str:
    """
    Get a short, simple meaning of a word from Gemini AI.
    Args:
        word (str): The word to explain
    Returns:
        str: AI-generated short meaning
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "⚠️ GEMINI_API_KEY not set in environment variables."

    # Construct a clear, concise prompt
    prompt = (
        f"Explain the meaning of the word '{word}' in very simple language, "
        "in 3-4 short sentences that anyone can understand."
    )

    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    try:
        response = requests.post(f"{GEMINI_API_URL}?key={api_key}", json=payload, headers=headers)
        data = response.json()
        # Debug info
        print("Full API Response:", data)
        # Return generated text safely
        return data["candidates"][0]["content"]["parts"][0]["text"]

    except KeyError:
        return f"⚠️ API response missing expected 'candidates'. Full response: {data}"
    except requests.exceptions.RequestException as e:
        return f"⚠️ Request failed: {e}"
    except Exception as e:
        return f"⚠️ An unexpected error occurred: {e}"
