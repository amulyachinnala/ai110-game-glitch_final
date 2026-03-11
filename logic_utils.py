def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50    ## normal difficulty should be easier than hard
    if difficulty == "Hard":
        return 1, 100   ## hard difficulty should be harder than normal
    return 1, 100
    ##raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    if raw is None or raw == "": ##combine both if branches since they have the same output
        return False, None, "Enter a guess."
    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None
    ##raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📈 Go LOWER!" ##when the guess is too high, the hint should be "GO LOWER!"
        else:
            return "Too Low", "📉 Go HIGHER!" ##when the guess is too low, the hint should be "GO HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📈 Go LOWER!" ##when the guess is too high, the hint should be "GO LOWER!"
        return "Too Low", "📉 Go HIGHER!"   ##when the guess is too low, the hint should be "GO HIGHER!"
    ##raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1) ##change to -1 so user is awarded full 100 points if guesssed on first attempt
        current_score += points

    elif outcome == "Too High" or outcome == "Too Low":
        current_score -= 5 ##when user guesses wrong, score should always be deducted
        if current_score < 0:
            current_score = 0 ##current_score should never go below zero

    return current_score
    ##raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
