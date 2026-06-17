# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The first time I ran the game, the hints were completely wrong and didn’t match the real secret number. The hints i was given were completely misleading and wrong. The attempts started at 0 instead of 1, and some attempts were duplicated even though I only guessed once. The UI looked normal, but the logic behind the game was broken from the start.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The New Game button froze and didn’t work until I refreshed the page.
  2. The secret number shown in the developer debug info didn’t match the final answer the game revealed. One time it said the secret number was 70, but the game ended saying the number was 34.
  3. The hints were backwards: the game said “go higher” when the guess was too high and “go lower” when it was too low.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 50 |should say "too high" cause the secret number it gave me at the end was 34 | said "go higher" |none|

|90 |should say "too high" |said "go higher" again |none |

| -1  |should show invalid input |said "go lower" |none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used copilot to inspect the code and understand the bug.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Copilot correctly pointed out that check_guess() had reversed hint messages and that New Game did not reset all session state. I verified this by reading the code and replaying the game

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I did not get a clearly wrong suggestion this time because I asked the AI carefully and checked the code myself. If I had, I would note it, but the main issue was that I still needed to verify the AI’s recommendation.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed when replaying the game showed correct hints and the New Game button started a fresh round. The game had to behave correctly for several steps before I accepted the fix.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran pytest on check_guess(60, 50) and check_guess(40, 50) to confirm the function returned "Too High" and "Too Low". That test showed the hint logic worked correctly.

- Did AI help you design or understand any tests? How?
Yes, AI helped me understand which functions were important and what expected outputs to check. It guided me toward testing the core game logic in check_guess().

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the whole script every time the user interacts with the page. st.session_state is used to keep values like the secret number, score, and attempts across those reruns. If state is not reset correctly, the game can behave as if the old round is still active.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
 - This could be a testing habit, a prompting strategy, or a way you used Git.
 I want to keep reproducing bugs first and then trace the exact code path before making changes.

- What is one thing you would do differently next time you work with AI on a coding task?
I would ask more specific code-level questions and verify AI suggestions with the actual code.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI can give a strong starting point, but I still need to check the logic and test it myself. It taught me that AI code can look right and still have hidden bugs.
