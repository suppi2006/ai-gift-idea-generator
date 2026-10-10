from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import genai
import os


# Load .env
load_dotenv()


# Create Flask app
app = Flask(__name__)


# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Please check your .env file."
    )


# Create Gemini client
client = genai.Client(api_key=api_key)


@app.route("/", methods=["GET", "POST"])
def home():

    gift_ideas = None
    error = None

    if request.method == "POST":

        # Get user inputs
        relationship = request.form.get("relationship", "").strip()
        age = request.form.get("age", "").strip()
        budget = request.form.get("budget", "").strip()
        interest = request.form.get("interest", "").strip()

        # Validate inputs
        if not relationship or not age or not budget or not interest:

            error = "Please fill in all the fields."

        else:

            # Create AI prompt
            prompt = f"""
You are an AI Gift Idea Generator.

Suggest suitable gifts for this person:

Relationship: {relationship}
Age: {age}
Budget: ₹{budget}
Interest/Hobby: {interest}

Requirements:

- Give exactly 5 gift suggestions.
- Keep suggestions suitable for the person's age.
- Match the person's interests.
- Try to stay within the budget.
- Give an approximate price for every gift.
- Give a short reason for every gift.
- Use Indian Rupees.

Format:

1. Gift Name
Price: ₹xxx
Reason: Short reason.

2. Gift Name
Price: ₹xxx
Reason: Short reason.

3. Gift Name
Price: ₹xxx
Reason: Short reason.

4. Gift Name
Price: ₹xxx
Reason: Short reason.

5. Gift Name
Price: ₹xxx
Reason: Short reason.
"""

            try:

                # Try multiple Gemini models
                models = [
                    "gemini-3.8-flash",
                    "gemini-3.7-flash",
                    "gemini-3.6-flash",
                    "gemini-2.5-flash"
                ]

                response = None
                last_error = None

                for model in models:

                    try:

                        print(f"Trying model: {model}")

                        response = client.models.generate_content(
                            model=model,
                            contents=prompt
                        )

                        if response.text:
                            print(f"Success using: {model}")
                            break

                    except Exception as e:

                        print(f"Model {model} failed: {e}")
                        last_error = e
                        continue


                # Check whether any model worked
                if response is None or not response.text:

                    raise Exception(last_error)


                # Store AI response
                gift_ideas = response.text


            except Exception as e:

                print("Gemini Error:", e)

                error = (
                    "Gemini is temporarily unavailable. "
                    "Please try again in a few seconds."
                )


    return render_template(
        "index.html",
        gift_ideas=gift_ideas,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)