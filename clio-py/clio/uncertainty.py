
class Uncertainty:
    """Represents the model's uncertainty about a particular conclusion."""
    def __init__(self, confidence_score):
        if not 0 <= confidence_score <= 1:
            raise ValueError("Confidence score must be between 0 and 1.")
        self.confidence_score = confidence_score

    def __repr__(self):
        return f"Uncertainty(confidence_score={self.confidence_score})"
