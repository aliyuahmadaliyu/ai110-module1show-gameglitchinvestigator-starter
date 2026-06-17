from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty


# --- check_guess tests ---

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_guess_correct():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

# --- parse_guess tests ---

def test_parse_valid_guess():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_empty_guess():
    ok, value, err = parse_guess("")
    assert ok is False
    assert err == "Enter a guess."

def test_parse_non_number():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."

def test_parse_decimal_guess():
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7

# --- update_score tests ---

def test_score_increases_on_win():
    new_score = update_score(0, "Win", 1)
    assert new_score > 0

def test_score_decreases_on_wrong_guess():
    new_score = update_score(50, "Too High", 1)
    assert new_score < 50

def test_score_decreases_on_too_low():
    new_score = update_score(50, "Too Low", 2)
    assert new_score < 50

# --- get_range_for_difficulty tests ---

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100

def test_hard_range_is_harder_than_normal():
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high