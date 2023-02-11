from typing import List
from aligner import TokenMatrix
from tokenizer import Token
from encoder import Encoder
import logging

def token_row_to_text_row(token_row: List[Token], basestr: str, text_for_gap: str = "-"):
    text_row = []
    for t in token_row:
        if t is None:
            text_row.append(text_for_gap)
        else:
            text_row.append(basestr[t[0]:t[1]])
    return text_row

def token_row_to_token_str_rows(token_row: List[Token], text_for_gap: str = "-"):
    text_row = []
    for t in token_row:
        if t is None:
            text_row.append(text_for_gap)
        else:
            text_row.append(t[3])
    return text_row

def column_matrix_to_row_matrix(column_matrix):
    nb_columns_transformed = len(column_matrix)
    nb_rows_transformed = len(column_matrix[0])
    row_matrix = [[None for _ in range(nb_columns_transformed)] for _ in range(nb_rows_transformed)]
    for i, column_transformed in enumerate(column_matrix):
        for j, cell in enumerate(column_transformed):
            row_matrix[j][i] = cell
    return row_matrix

def token_row_to_string(token_row: List[Token], basestr: str):
    string_row = []
    for t in token_row:
        if t is None:
            string_row.append()
        string_row.append()

def get_debug_token_matrix_str(token_matrix: TokenMatrix, text_for_gap: str = "-", original_strings: List[str] = None):
    # print the table horizontally
    from prettytable import PrettyTable
    x = PrettyTable()
    x.header = False
    horizontal_matrix = column_matrix_to_row_matrix(token_matrix)
    for row_i, token_row in enumerate(horizontal_matrix):
        string_row = None
        if original_strings:
            string_row = token_row_to_text_row(token_row, original_strings[row_i], text_for_gap)
        else:
            string_row = token_row_to_token_str_rows(token_row, text_for_gap)
        x.add_row(string_row)
    x.align = "l"
    return x.get_string()

def debug_token_matrix(logger, token_matrix, text_for_gap="-", original_strings: List[str] = None):
    if not logger.isEnabledFor(logging.DEBUG):
        return
    debug_str = get_debug_token_matrix_str(token_matrix, text_for_gap, original_strings)
    logger.debug("\n"+debug_str)

def debug_token_lists(logger, token_lists, string_list = None):
    if not logger.isEnabledFor(logging.DEBUG):
        return
    for i, token_list in enumerate(token_lists):
        row_string = ""
        for t in token_list:
            if t is None:
                row_string.append(" - ")
            elif string_list:
                token_in_string = string_list[i][t[0]:t[1]]
                row_string += " '%s'[%d:%d:%d;%s] " % (token_in_string, t[0], t[1], t[2], t[3])
            else:
                row_string += " '%s'[%d:%d:%d] " % (t[3], t[0], t[1], t[2])
        logger.debug(row_string)

def debug_token_strings(logger, token_strings: List[str], vocabulary: Vocabulary):
    if not logger.isEnabledFor(logging.DEBUG):
        return
    for token_string in token_strings:
        print(vocabulary.decode_string(token_string))