"""
電車でGlass - メインエントリーポイント
スマホで撮影した電光掲示板の画像から最適な乗車位置を案内する
"""
import os
import sys
from dotenv import load_dotenv

from src.ocr.vision_client import VisionClient
from src.parser.sign_parser import SignParser
from src.calculator.position_calculator import PositionCalculator, MoveStyle

load_dotenv()


def run(image_path: str, destination: str, move_style: MoveStyle):
    """
    画像から乗車位置を案内するメインフロー

    Args:
        image_path: 電光掲示板の画像パス
        destination: 目的駅名
        move_style: 移動スタイル
    """
    print(f"\n🚃 電車でGlass 起動")
    print(f"目的駅：{destination}")
    print(f"移動スタイル：{move_style.value}\n")

    # Step 1: OCRでテキスト抽出
    print("📷 画像を読み込み中...")
    client = VisionClient()
    raw_text = client.extract_text_from_file(image_path)
    print(f"OCR結果：\n{raw_text}\n")

    # Step 2: テキストをパース
    parser = SignParser()
    sign_info = parser.parse(raw_text)
    print(f"路線名：{sign_info.line_name}")
    print(f"行き先：{sign_info.destination}")
    print(f"番線：{sign_info.platform}\n")

    # Step 3: 乗車位置を計算
    calculator = PositionCalculator()
    position = calculator.calculate(sign_info, destination, move_style)

    # Step 4: 結果を表示（将来：グラスに送信）
    print("=" * 30)
    print(f"👓 {position.car_number} / {position.door_position}")
    print(f"   {position.reason}")
    print("=" * 30)


if __name__ == "__main__":
    # 動作確認用のサンプル実行
    # 使い方: python src/main.py <画像パス> <目的駅> <移動スタイル>
    image_path = sys.argv[1] if len(sys.argv) > 1 else "data/sample.jpg"
    destination = sys.argv[2] if len(sys.argv) > 2 else "新宿"
    style_arg = sys.argv[3] if len(sys.argv) > 3 else "elevator"

    style_map = {
        "elevator": MoveStyle.ELEVATOR,
        "stairs": MoveStyle.STAIRS,
        "exit": MoveStyle.EXIT,
    }
    move_style = style_map.get(style_arg, MoveStyle.ELEVATOR)

    run(image_path, destination, move_style)
