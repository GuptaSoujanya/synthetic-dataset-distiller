import re

class QualityFilter:
    def evaluate(self, text: str):
        words = [w.lower() for w in re.findall(r'\b\w+\b', text)]
        diversity = len(set(words)) / len(words) if words else 0.0
        passed = (15 <= len(words) <= 1024) and (diversity >= 0.45)
        return {"passed": passed, "token_count": len(words), "lexical_diversity": round(diversity, 3)}
