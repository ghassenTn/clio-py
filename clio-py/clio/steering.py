class Steering:
    """Represents user-provided steering."""
    def __init__(self, domain_knowledge=None, steering_function=None):
        self.domain_knowledge = domain_knowledge or {}
        self.steering_function = steering_function

    def __repr__(self):
        return f"Steering(domain_knowledge={self.domain_knowledge}, steering_function={self.steering_function})"