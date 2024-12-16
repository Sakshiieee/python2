class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def forward_reasoning(self):
        new_facts = set()
        for rule in self.rules:
            if all(condition in self.facts for condition in rule.conditions):
                new_facts.add(rule.conclusion)
        self.facts.update(new_facts)

    def query(self, query):
        return query in self.facts

class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion

def main():
    kb = KnowledgeBase()
    kb.add_fact("Dog is a mammal")
    kb.add_fact("Cat is a mammal")
    kb.add_fact("Mammal is an animal")
    rule1 = Rule(conditions=["Dog is a mammal"], conclusion="Dog is an animal")
    rule2 = Rule(conditions=["Cat is a mammal"], conclusion="Cat is an animal")
    kb.add_rule(rule1)
    kb.add_rule(rule2)
    print("Initial Facts:")
    print(kb.facts)
    kb.forward_reasoning()
    print("\nFacts after Forward Reasoning:")
    print(kb.facts)
    query_result = kb.query("Dog is an animal")
    print("\nQuery Result:")
    print(query_result)

if __name__ == "__main__":
    main()
