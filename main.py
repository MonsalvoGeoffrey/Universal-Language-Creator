import re


class Tokenizer:
    def __init__(self, language: str):
        self.language = [
            line.split(":", maxsplit=1) for line in language.split("\n") if line != ""
        ]
        for token in self.language:
            token[1] = re.compile(token[1])

    def tokenize(self, code: str):
        tokens = []
        while (code := code.lstrip()) != "":
            for token in self.language:
                result = token[1].match(code)
                if result:
                    tokens.append((token[0], result.group(0)))
                    code = code[len(result.group(0)) :]
                    break
            else:
                raise RuntimeError("Something's wrong")
        return tokens

    def parse(self, tokens):
        pass


class Rule:
    def __init__(self, rule: str):
        self.tokens = self.tokenize(rule)

    def tokenize(self, rule: str):
        self.name, rule_content = rule.split(":", maxsplit=1)
        tokens = []
        while (rule_content := rule_content.lstrip()) != "":
            print("abc, ", rule_content)
            if result := re.match("[a-z]+", rule_content):
                tokens.append(("RULE", result.group(0)))
            elif result := re.match("[A-Z]+", rule_content):
                tokens.append(("TOKEN", result.group(0)))
            elif result := re.match("\(", rule_content):
                tokens.append(("LPAREN",))
            elif result := re.match("\)", rule_content):
                tokens.append(("RPAREN",))
            elif result := re.match("\|", rule_content):
                tokens.append(("OR",))
            elif result := re.match("\*", rule_content):
                tokens.append(("WILD",))
            elif result := re.match("\+", rule_content):
                tokens.append(("OVER",))
            # tokens.append((token[0], result.group(0)))
            if result:
                rule_content = rule_content[len(result.group(0)) :]
                continue
            raise RuntimeError("Something's wrong")
        return tokens

    def __repr__(self):
        return str(self.tokens)


class Parser:
    def __init__(self, grammar: str, tokens):
        self.grammar = [Rule(line) for line in grammar.split("\n") if line != ""]


lang: str = ""
with open("language.txt", "r") as file:
    lang = file.read()


code: str = ""
with open("code.kelp", "r") as file:
    code = file.read()

t = Tokenizer(lang)
for i in t.tokenize(code):
    print(i)


grammar: str = ""
with open("grammar.txt", "r") as file:
    grammar = file.read()

p = Parser(grammar, None)
for i in p.grammar:
    print(i)
