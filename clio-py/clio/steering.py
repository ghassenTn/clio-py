
class Steering:
    """Represents user-provided steering."""
    def __init__(self, domain_knowledge=None):
        self.domain_knowledge = domain_knowledge or {}

    def __repr__(self):
        return f"Steering(domain_knowledge={self.domain_knowledge})"
