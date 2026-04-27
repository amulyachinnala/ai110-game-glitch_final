# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

The purpose of the game is to try to guess the secret number in as few tries as possible and before attempts run out. 
Comments were added to app.py to the lines that were fixed to describe the change

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

Screenshot is titled winning_screen.png

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

## (NEW): final project additions

🧪 Sample Interactions
Scenario 1: Strategic Planning

Input: User guesses 50 (on a range of 1-100). The secret is 72.

AI Agent Output: "Analysis: Your guess 50 was too low. Strategy: Try the midpoint between 50 and 100 (Try 75 next). Agent Confidence: 50%"

Scenario 2: Confidence Scaling

Input: Third guess in the history.

AI Agent Output: "Analysis: You are narrowing the range. Strategy: Try 62. Agent Confidence: 85%" (Confidence increases as the history grows).

🛠️ Design Decisions
Agentic vs. Simple Logic: I chose to implement a separate GuessingAgent class. While simple logic could provide hints, an agentic structure allows the AI to "plan" and "reason" based on the user's specific history, making the system more extensible for future complex strategies.

Stateful Memory: Using Streamlit's session_state was a trade-off. It makes the app fast and easy to build, but it means memory is lost on browser refresh. For a production-level agent, a database like Redis would be a better long-term choice.

📈 Testing Summary
Unit Tests: 3 out of 3 tests passed in reliability_test.py.

Performance: The AI Agent successfully calculated midpoints for all difficulty levels (Easy, Normal, Hard).

Lessons Learned: I learned that AI confidence scoring is highly dependent on data density; with fewer than 2 guesses, the agent's advice is statistically less reliable.

💭 Reflection
This project taught me that AI is most powerful when it acts as a collaborator rather than just a calculator. By adding an agentic layer, a simple game became a tool for teaching strategic thinking. It also highlighted the importance of Guardrails—the logging system caught several "TypeErrors" during development that would have crashed the app for a user.

model_card_content = """# Model Card: Reflection and Ethics

🤖 AI Collaboration Reflection
Helpful Instance: The AI suggested using the logging module to create a game_debug.log. This was crucial for catching an edge case where string inputs were being compared to integers in the scoring logic.

Flawed Instance: The AI initially suggested a hint formula that didn't account for the current difficulty boundaries (e.g., suggesting a guess of 75 on "Easy" mode where the max is 20). I had to add a guardrail to pass the difficulty_range into the agent.

⚖️ Limitations and Biases
Bias: The AI Agent assumes the user wants to play "optimally" (Binary Search). It might discourage "lucky" guessing or creative playstyles.

Limitation: The current agent does not use a Large Language Model (LLM) for natural language; it uses deterministic agentic logic. This ensures speed but lacks the conversational warmth of an LLM.

🛡️ Misuse and Prevention
Misuse: This system could theoretically be used to automate bot-playing of similar games.

Prevention: I implemented an "Attempt Limit" per session. To prevent botting, one could add a CAPTCHA or rate-limiting on the submit button in a production environment.

🎯 Testing Results
Accuracy: 100% (based on deterministic logic checks).

Average Agent Confidence: 0.72.

Stability: No crashes recorded after implementing the parse_guess guardrails.
