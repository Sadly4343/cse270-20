import pytest
import json
from build_sentences import (get_seven_letter_word, parse_json_from_file, choose_sentence_structure,
                              get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures, pronouns, articles)

def test_get_seven_letter_word(mocker):
    
        mock_input = mocker.patch("builtins.input", return_value="Appless")

        result = get_seven_letter_word()

        assert result == "APPLESS"
        
        mock_input = mocker.patch("builtins.input", return_value="Apple")

        with pytest.raises(ValueError):
             get_seven_letter_word()


    # Test for get_random_item function

def test_parse_json_from_file(tmp_path):
    test_data = '{"key": "value"}'

    file_path = tmp_path / "test.txt"

    with open(file_path, "w") as f:
        f.write(test_data)
    result = parse_json_from_file(file_path)

    assert result == {"key": "value"}

    

def test_choose_sentence_structure():
    choice = choose_sentence_structure()
    assert choice in structures

def test_get_pronoun():
    choice = get_pronoun()
    assert choice in pronouns

def test_get_article():
    choice = get_article()
    assert choice in articles

def test_get_word():
    myList = ['Apple','Pear','Watermelon']
    result = get_word('A', myList)
    assert result =='Apple'

def test_fix_agreement():
    sentence = ['water','she','will','run','towards','ocean' ]
    fix_agreement(sentence)
    assert sentence == ['water','she','will','runs','towards','ocean']
    sentence = ['there', 'was', 'a', 'ocean', 'ocean', 'them']
    fix_agreement(sentence)
    assert sentence == ['there', 'was', 'an', 'ocean', 'ocean', 'them']
    sentence = ['the', 'ocean', 'was','runs','run','runs']
    fix_agreement(sentence)
    assert sentence == ['the', 'ocean', 'was','runs','runs','runs']
def test_build_sentence():
    seed_word = ['run','ocean']
    structuress = ['V','N']
    data = {"verbs": ['run','play'],
    "nouns": ['ocean']}
    result = build_sentence(seed_word,structuress,data)
    assert result == 'run'