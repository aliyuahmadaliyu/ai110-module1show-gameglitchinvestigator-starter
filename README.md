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

- [ X ] Describe the game's purpose.
 A number guessing game where the player guesses a secret number within a limited number of attempts. After each guess, the game gives a hint (Too High or Too Low) to guide the next guess. The player wins by guessing correctly before running out of attempts.

- [ X ] Detail which bugs you found.
- Hints were backwards: the game said "Go HIGHER" when the guess was too high and "Go LOWER" when too low.
- The secret number was randomly converted to a string on even attempts, causing wrong comparisons.
- Hard difficulty had a range of 1–50, which is easier than Normal's 1–100.
- Wrong guesses gave +5 bonus points on even attempts instead of always deducting points.

- [ X ] Explain what fixes you applied.
- Fixed hint messages in check_guess() so Too High → Go LOWER and Too Low → Go HIGHER.
- Removed the string conversion bug in app.py so the secret stays an integer.
- Updated Hard difficulty range to 1–200 so it is genuinely harder than Normal.
- Fixed update_score() to always deduct 5 points for any wrong guess.
- Moved all logic functions into logic_utils.py and updated app.py to import from it.


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->  User selects Normal difficulty (range: 1–100, and attempts allowed)

2. <!-- Describe this step --> User enters a guess of 40, Game returns "Go Higher"

3. <!-- Describe this step --> User enters a guess of 70, Game returns "Go Higher"

4. <!-- Describe this step --> User enters a guess of 55, Game returns "Go Higher"

5. <!-- Add more steps as needed -->  User enters a guess of 63, Game returns correct

6. Balloons appear and final score is displayed

7.  User clicks New Game. Then score, attempts, and secret all reset correctly

8. Score decreases by 5 after each wrong guess




**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
My Answer:
tests/test_game_logic.py::test_guess_too_high PASSED
tests/test_game_logic.py::test_guess_too_low PASSED
tests/test_game_logic.py::test_guess_correct PASSED
tests/test_game_logic.py::test_parse_valid_guess PASSED
tests/test_game_logic.py::test_parse_empty_guess PASSED
tests/test_game_logic.py::test_parse_non_number PASSED
tests/test_game_logic.py::test_parse_decimal_guess PASSED
tests/test_game_logic.py::test_score_increases_on_win PASSED
tests/test_game_logic.py::test_score_decreases_on_wrong_guess PASSED
tests/test_game_logic.py::test_score_decreases_on_too_low PASSED
tests/test_game_logic.py::test_easy_range PASSED
tests/test_game_logic.py::test_normal_range PASSED
tests/test_game_logic.py::test_hard_range_is_harder_than_normal PASSED
========================================= 13 passed in 0.18s =========================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
