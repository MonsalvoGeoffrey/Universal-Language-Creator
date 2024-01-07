import re


def split_all(input_list: list | str, split_string: str):
    if isinstance(input_list, str):
        return input_list.split(split_string)
    result = []
    for item in input_list:
        result.append(split_all(item, split_string))
    return result


#
def split_in_sequence(input_item, *split_strings):
    for string in split_strings:
        input_item = split_all(input_item, string)
    return input_item


class Tokenizer:
    def __init__(self, language: str):
        # self.language = split_in_sequence(language, "\n", ":")
        self.language = [
            line.split(":", maxsplit=1) for line in language.split("\n") if line != ""
        ]
        for token in self.language:
            token[1] = re.compile(token[1])

    def tokenize(self, code: str):
        tokens = []
        while (code := code.lstrip()) != "":
            # print(code)
            for token in self.language:
                # print(token)
                result = token[1].match(code)
                if result:
                    tokens.append((token[0], result.group(0)))
                    code = code[len(result.group(0)) :]
                    # print(token[0], result.group(0), len(result.group(0)), code)
                    break
            else:
                # print(code)
                raise RuntimeError("Something's wrong")
        return tokens


lang: str = ""
with open("language.txt", "r") as file:
    lang = file.read()


code: str = ""
with open("code.kelp", "r") as file:
    code = file.read()

t = Tokenizer(lang)
for i in t.tokenize(code):
    print(i)
