from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_reversed_hint_bug_is_fixed():
    # Regression test for the reversed high/low hint bug.
    # Before the fix, a guess ABOVE the secret was steered the wrong way.
    # These are the exact cases from the bug reproduction log.

    # Guess 90 vs secret 50 must be "Too High" (so the UI says "go LOWER"),
    # NOT "Too Low".
    assert check_guess(90, 50) == "Too High"
    assert check_guess(90, 50) != "Too Low"

    # Guess 9 vs secret 50 must be "Too Low" (so the UI says "go HIGHER"),
    # NOT "Too High".
    assert check_guess(9, 50) == "Too Low"
    assert check_guess(9, 50) != "Too High"
