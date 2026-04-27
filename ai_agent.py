import streamlit as st

class GuessingAgent:
    """An AI Agent that plans, acts, and checks the game state."""
    
    def __init__(self, secret, history, difficulty_range):
        self.secret = secret
        self.history = [h for h in history if isinstance(h, int)]
        self.low, self.high = difficulty_range

    def analyze_strategy(self):
        """The 'Plan' phase of the agentic workflow."""
        if not self.history:
            return "No data yet. Start by guessing the midpoint!"
        
        last_guess = self.history[-1]
        
        # Agent Logic: Identifying if user is being efficient
        if last_guess > self.secret:
            return f"Analysis: Your guess {last_guess} was too high. Strategy: Try the midpoint between {self.low} and {last_guess}."
        else:
            return f"Analysis: Your guess {last_guess} was too low. Strategy: Try the midpoint between {last_guess} and {self.high}."

    def get_confidence_score(self):
        """Reliability feature: AI rates its own advice."""
        if len(self.history) < 2:
            return 0.5  # Low confidence with little data
        return 0.85 # Higher confidence as more data is gathered