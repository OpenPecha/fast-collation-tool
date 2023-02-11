import regex
import re
from normalizer import Normalizer
from tokenizer import Tokenizer, Token, TokenList
from typing import Tuple
from encoder import Encoder
from normalizer_bo import TibetanNormalizer

class TibetanTokenizer(Tokenizer):

    token_pattern = regex.compile(r'(?u)\w+[\s་༌࿒]*|\W+')
    
    default_stop_words = [ "ཏུ", "གི", "ཀྱི", "གིས", "ཀྱིས", "ཡིས", 
        "ཀྱང", "སྟེ", "ཏེ", "མམ", "རམ", "སམ", "ཏམ", "ནོ", "ཏོ", "གིན",
        "ཀྱིན", "གྱིན", "ཅིང", "ཅིག", "ཅེས", "ཞེས", "པ", "པར", "པས",
        "བ", "བར", "བས", "པོ", "པོར", "པོས", "བོ", "བོར", "བོས"]

    def __init__(self, encoder: Encoder, normalizer: Normalizer, stop_words = default_stop_words):
        super().__init__(vocabulary, normalizer)
        self.stop_words = stop_words

    def tokenize(self, arg) -> Tuple[str, TokenList]:
        tokens = []
        tokenstr = ""
        if end is None:
            end = len(s)
        string, correct_position = self.get_input()
        for m in TibetanTokenizer.token_pattern.finditer(string):
            token_s = self.normalizer.normalize_always(m.group(0))
            compare_s = self.normalizer.normalize_pre_token_comparison(token_s)
            start = correct_position(m.start())
            end = correct_position(m.end())
            if token_s == "" or compare_s in self.stop_words:
                t = (start, end, 0, token_s)
                tokens.append(t)
                continue
            token_s_for_diff = self.normalizer.normalize_pre_token_diff(token_s)
            code_str, code_str_len = self.vocabulary.encode_str(token_s_for_diff)
            tokenstr += code_str
            t = (start, end, code_str_len, token_s)
            tokens.append(t)
        return tokens, tokenstr

if __name__ == "__main__":
    test_string = "ཡེ་ཤེས་ཀྱིས་སྦྱངས་ནས། ཆོས་ཐམས་ཅད་ནམ་མཁའི་དཀྱིལ་ལྟ་བུར་ིརང་གི་"
    encoder = Encoder()
    normalizer = TibetanNormalizer()
    tokenizer = TibetanTokenizer(vocabulary=vocabulary, normalizer=normalizer)
    tokens, tokenstr = tokenizer.tokenize(test_string, start=0, end=61)
    print(tokens)