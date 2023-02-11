from tokenizer import TokenList
from typing import List

TokenMatrix = List[TokenList]

class Aligner():
    """
    Aligner interface.
    """

    def get_alignment_matrix(self, token_strings: List[str], token_lists: List[TokenList]) -> TokenMatrix:
        """
        A function that takes as arguments:
        - a list of token_strings (one row per witness)
        - a list of token lists (one row per witness)

        token_strings and token lists are typically the result of the tokenize() function of a Tokenizer

        It returns an alignment matrix in the form of a matrix of tokens, one column per witness.
        Gaps in the matrix have the value None.
        """
        return None