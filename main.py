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


lang: str = ""
with open("language.txt", "r") as file:
    lang = file.read()


code: str = ""
with open("code.kelp", "r") as file:
    code = file.read()

t = Tokenizer(lang)
for i in t.tokenize(code):
    print(i)
