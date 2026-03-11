from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

##Tests for check_guess function
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

##NOTES: all provided tests passed after changing from result to result[0] in the assert statements

##Tests for get_range_for_difficulty function
def test_get_range_for_easy():
    result = get_range_for_difficulty("Easy")
    assert result == (1,20)

def test_get_range_for_normal():
    result = get_range_for_difficulty("Normal")
    assert result == (1,50)

def test_get_range_for_hard():
    result = get_range_for_difficulty("Hard")
    assert result == (1,100)

##Tests for parse_guess function
def test_parse_none_guess():
    result = parse_guess(None)
    assert result == (False, None, "Enter a guess.")

def test_parse_empty_guess():
    result = parse_guess("")
    assert result == (False, None, "Enter a guess.")

def test_parse_decimal_guess():
    result = parse_guess("34.3")
    assert result == (True, 34, None)

def test_parse_integer_guess():
    result = parse_guess("68")
    assert result == (True, 68, None)

def test_parse_non_number_guess():
    result = parse_guess("ten")
    assert result == (False, None, "That is not a number.")

##Tests for update_score function
def test_update_score_for_win():
    result = update_score(230, "Win", 1) ##win on first attempt
    assert result == 330

    result = update_score(230, "Win", 5) ##win on fifth attempt
    assert result == 290

    result = update_score(230, "Win", 10) ##win on tenth (last) attempt
    assert result == 240

def test_update_score_for_wrong_guess():
    result = update_score(230, "Too High", 1) 
    assert result == 225

    result = update_score(230, "Too Low", 5) 
    assert result == 225

    result = update_score(124, "Too High", 10) 
    assert result == 119

    result = update_score(302, "Too Low", 8) 
    assert result == 297

    result = update_score(2, "Too High", 3)
    assert result == 0

    result = update_score(3, "Too Low", 4)
    assert result == 0
