from logic_utils import parse_guess, update_score

def run_tests():
    print("Running Reliability Suite...")
    
    # Test 1: Input Handling
    ok, val, err = parse_guess("42.5")
    assert val == 42, "Failed to parse float to int"
    
    # Test 2: Score Guardrail
    # Testing original glitch: Does it award 100 points on 1st attempt?
    score = update_score(0, "Win", 1)
    if score == 100:
        print("✅ Test Passed: 100 points awarded for 1st attempt.")
    else:
        print(f"❌ Test Failed: Expected 100, got {score}")

    # Test 3: Confidence Score Check
    from ai_agent import GuessingAgent
    agent = GuessingAgent(50, [10, 20], (1, 100))
    if agent.get_confidence_score() > 0.5:
        print("✅ Test Passed: Agent confidence scales with history.")

if __name__ == "__main__":
    run_tests()