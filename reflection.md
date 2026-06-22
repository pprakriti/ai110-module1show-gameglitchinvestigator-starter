# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked nice at first. It had a clean design and working settings. But it was completely broken. I could not win. The hints did not make sense at all.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. If my guess was too high, the text told me to go higher. The logic was backward.
  2. The "New Game" button ignored the difficulty settings. It always picked a number between 1 and 100. It did not matter if I chose "Easy".

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|---|---|---|---|
| Guess 90 (Secret: 50) | tells me to go lower | tells me to go higher | None |
| Guess 9 (Secret: 50, Turn 2) | tells me to go higher | tells me to go lower | None |
| Click "New Game" on Easy | Secret is between 1 and 20 | Secret is between 1 and 100 | None |
| Guess on an even turn (Secret: 50) | compares numbers, gives a correct hint | game crashes — secret was turned into text | TypeError: '>' not supported between instances of 'int' and 'str' |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude (Claude Code in VS Code).

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI told me how to fix the broken hints. It said to swap the messages so that "Too High" tells me to go LOWER and "Too Low" tells me to go HIGHER. I updated the code and then ran the game in my terminal. I guessed 90 when the secret was 50, and the game correctly told me to "Go LOWER!". So the suggestion was correct, and I verified it by actually playing the game.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
At one point the AI showed me that all my tests "passed," so it looked like my refactor was finished. But that green result came from the AI running `python -m pytest`. When I ran plain `pytest` myself (the command in the README), it failed with `ModuleNotFoundError: No module named 'logic_utils'`. So the "all tests pass" result was misleading for the command I was actually using. I verified the real problem by running `pytest` myself and reading the error, and we fixed it by adding a `conftest.py` file at the project root so pytest could find my `logic_utils.py`. After that, plain `pytest` passed too.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was really fixed when I could confirm it in two ways: by running the tests and by trying the game myself. I did not trust the code just because it looked correct. For the hint bug, I checked that a high guess pointed me lower and a low guess pointed me higher. For the refactor, I only believed it was done once `pytest` actually passed.

- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
I ran `pytest`, which runs the tests in `tests/test_game_logic.py`, including a regression test called `test_reversed_hint_bug_is_fixed` that uses the exact cases from my bug log (guess 90 vs secret 50 must be "Too High", and guess 9 must be "Too Low"). The first time I ran it after moving the code, all 4 tests failed because `check_guess` returned a tuple like `('Win', '🎉 Correct!')` instead of the string `'Win'`. That showed me the function's return shape did not match what the tests expected. After I changed it to return just the outcome string, all 4 tests passed.

- Did AI help you design or understand any tests? How?
Yes. Claude wrote the regression test for the reversed-hint bug and explained why it would fail on the old buggy code (the old function returned a tuple, so `== "Too High"` did not match), which is what makes it a real regression test. It also pointed out that the tests only check the outcome string from `check_guess`, not the hint wording shown in the app, so I still had to play the game to confirm the messages. When `pytest` could not import my module, Claude explained the import-path problem and the `conftest.py` fix.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
In Streamlit there is no loop that keeps running. Every time you click a button or type something, Streamlit re-runs your whole script from top to bottom, almost like reloading the page — that is a "rerun." The catch is that normal variables get recreated on every rerun, so the game would forget the secret number each time. Session state (`st.session_state`) is Streamlit's memory that survives reruns: you store things like the secret, the score, and the attempt count there once, and they stay the same until you change them. I would tell my friend that the rerun is like the page refreshing on every click, and session state is the sticky note that remembers your game between those refreshes.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
The habit I want to reuse is verifying a fix two ways before trusting it: run the automated tests and also try the real thing by playing the game. I also want to keep writing a small regression test for each bug I fix, so the same bug cannot quietly come back later.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time I would run the tests myself with the exact command I will actually use, instead of trusting a "tests pass" result from the AI. Earlier the AI showed passing tests with `python -m pytest`, but plain `pytest` failed for me with an import error. I would also ask the AI for smaller, one-change-at-a-time edits so I can understand and check each one before moving on.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project taught me that AI-generated code can look clean and confident while still being completely broken. I now treat AI code as a first draft that I have to test and verify myself, not as something that is automatically correct.
