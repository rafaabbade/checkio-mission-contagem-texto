"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
        "input": ["A prática leva à perfeição. Praticar, praticar e praticar!"],
        "answer": {"a": 1, "prática": 1, "leva": 1, "à": 1, "perfeição": 1, "praticar": 3, "e": 1}
    },
    {
        "input": ["Contar palavras, contar palavras, contar sempre."],
        "answer": {"contar": 3, "palavras": 2, "sempre": 1}
    },
    {
        "input": ["Python! Python? Python."],
        "answer": {"python": 3}
    },
    {
        "input": ["Nada a declarar; apenas palavras comuns."],
        "answer": {"nada": 1, "a": 1, "declarar": 1, "apenas": 1, "palavras": 1, "comuns": 1}
    },
    {
        "input": ["Os testes foram realizados com sucesso."],
        "answer": {"os": 1, "testes": 1, "foram": 1, "realizados": 1, "com": 1, "sucesso": 1}
    }

    ]
}
