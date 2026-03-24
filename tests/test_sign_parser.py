"""
SignParser のユニットテスト
実機・APIなしで動作確認できる
"""
import pytest
from src.parser.sign_parser import SignParser, SignInfo


@pytest.fixture
def parser():
    return SignParser()


def test_parse_yamanote_line(parser):
    """山手線の電光掲示板テキストをパースできるか"""
    raw_text = "山手線\n新宿・渋谷方面\n3番線"
    result = parser.parse(raw_text)

    assert result.line_name == "山手線"
    assert "新宿" in result.destination or "渋谷" in result.destination
    assert result.platform == "3番線"


def test_parse_chiyoda_line(parser):
    """千代田線の電光掲示板テキストをパースできるか"""
    raw_text = "千代田線\n代々木上原方面\n各駅停車\n2番線"
    result = parser.parse(raw_text)

    assert result.line_name == "千代田線"
    assert result.train_type == "各駅停車"
    assert result.platform == "2番線"


def test_parse_unknown_line(parser):
    """未知の路線の場合はNoneを返すか"""
    raw_text = "よくわからないテキスト"
    result = parser.parse(raw_text)

    assert result.line_name is None
    assert result.platform is None


def test_parse_empty_text(parser):
    """空文字の場合はエラーにならないか"""
    result = parser.parse("")

    assert result.line_name is None
    assert result.destination is None
    assert result.platform is None
