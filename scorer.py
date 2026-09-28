def judge(question, expects, answer, results) -> bool:
    """
    q: 'give', expect: 'give'
    The expect is in the answer
    """
    return expects.lower().strip() in answer.lower()

"""
LLM as a judge
rapidfuzz to help write a judge functions

Rapidfuzz works best in smaller chunks
"""

def retrieval_hits(expects, results) -> bool:
    """
    Any part of my expect in the results
    """
    return any(expects.strip().lower() for chunk in results)