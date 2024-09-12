class PromptMutator:
    def deepen(self, prompt: str) -> str:
        return f"Please rewrite this problem to require mathematical induction and proof:\n{prompt}"
    def add_constraint(self, prompt: str) -> str:
        return f"Please rewrite this task imposing strict O(1) space complexity:\n{prompt}"
