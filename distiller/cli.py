import argparse
from .mutators import PromptMutator
from .filters import QualityFilter

def main():
    mut = PromptMutator()
    qf = QualityFilter()
    sample = "Write a function to detect cycles in a directed graph."
    mutated = mut.deepen(sample)
    qual = qf.evaluate(mutated)

    print("\n" + "="*52)
    print("      SYNTHETIC DATA DISTILLATION PIPELINE")
    print("="*52)
    print(f" Seed Prompt : {sample}")
    print(f" Mutated     : {mutated}")
    print(f" Quality Gate: {'[PASSED]' if qual['passed'] else '[REJECTED]'} (Diversity: {qual['lexical_diversity']})")
    print("="*52 + "\n")

if __name__ == "__main__":
    main()
