# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

When I opened the game for the first time, everything looked right in the UI with the settings on the left panel and the main game in the center. However, I noticed that the normal setting was more difficult than the hard one as the range was larger but the number of attempts was smaller. One bug that I noticed was that when I guessed too high, it said it was too low and vice versa. Another bug was that whenever I tried to start a new game, that button didn't do anything. Also, it seemed like the game ended early since I still had one more attempt.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---I used the built in Copilot on VSCode along with Gemini. One AI suggestion with was partially incorrect was when I asked Gemini what was causing the development info to be one attempt off from the guesses, it correctly found that the ordering of the code made it so the states were changed after the development info was displayed in the UI (thus, not reflecting those changes until the next attempt). However, when I tried to swap the order like it suggested, it introduced even more errors. I was able to verify this by playing a game and immediately finding a bug when I won. After the winning screen appeared, I could still see the message with the instructions and attempts left so I had to add more code to wrap it in a conditional statement so that it would only display that message when the status was "playing".

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided that a bug was really fixed after I played the game multiple times without noting anything off and also when all my methods passed the test cases I wrote. One test case I wrote was for the update score method. As I was writing the test cases and picking which input values to use, I noticed that two cases had the same exact output so I could simplify the function. Although this didn't help me catch any bugs in the function, it did help me improve the readability of it. AI helped me understand the tests because when I first tried to run the tests, it wasn't synced up properly and kept raising the not implemented error even after I finished implementing the tests. When I asked AI for help, it explained that my old test cases (before implementation) must be stored in a cache and gave me a commmand I could run to clear it and that worked.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number seemed like it kept changing because the hints were misleading and made it impossible to guess what the actual number was. To get a stable secret number I had to swap the hints for the guesses. I would explain Streamlit reruns as running the entire code from the start each time you interact with the app (like clicking a button). Because of this, it can't keep track of important details so it needs to use st.session_state to remember them whenever it reruns.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One strategy that I want to reuse is trying to figure out the bugs myself first and turning to AI when I need a hint or am completely stuck so I can still sharpen my own critical thinking skills without becoming overreliant on AI. One thing I would do differently is spending more time using AI to explain the portions of code that I don't fully understand. I think this project changed the way I think about AI generated code because it helped me realize that just because something may look right doesn't necessarily mean that it is. This reminds me to be more careful about when and how I use AI.