"""
OCRで抽出したテキストから路線名・行き先・番線を抽出するモジュール
"""
import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class SignInfo:
    """電光掲示板から読み取った情報"""
    line_name: Optional[str] = None      # 路線名（例：山手線）
    destination: Optional[str] = None    # 行き先（例：新宿・渋谷方面）
    platform: Optional[str] = None       # 番線（例：3番線）
    train_type: Optional[str] = None     # 種別（例：各駅停車・急行）


class SignParser:
    # 主要路線名のリスト（必要に応じて追加）
    KNOWN_LINES = [
        "山手線", "京浜東北線", "中央線", "総武線", "埼京線",
        "千代田線", "丸ノ内線", "日比谷線", "東西線", "有楽町線",
        "半蔵門線", "南北線", "副都心線", "銀座線", "東急東横線",
        "東急田園都市線", "京王線", "小田急線", "西武池袋線", "東武東上線",
    ]

    TRAIN_TYPES = ["各駅停車", "急行", "特急", "快速", "準急", "通勤急行"]

    def parse(self, raw_text: str) -> SignInfo:
        """
        OCRテキストから電光掲示板の情報を抽出する

        Args:
            raw_text: OCRで抽出した生テキスト

        Returns:
            SignInfo: パースされた掲示板情報
        """
        info = SignInfo()

        # 路線名を検索
        for line in self.KNOWN_LINES:
            if line in raw_text:
                info.line_name = line
                break

        # 行き先を検索（〇〇方面 or 〇〇行き）
        destination_match = re.search(r'(\w+)(方面|行き|ゆき)', raw_text)
        if destination_match:
            info.destination = destination_match.group(0)

        # 番線を検索（〇番線 or 〇番ホーム）
        platform_match = re.search(r'(\d+)(番線|番ホーム)', raw_text)
        if platform_match:
            info.platform = platform_match.group(0)

        # 種別を検索
        for train_type in self.TRAIN_TYPES:
            if train_type in raw_text:
                info.train_type = train_type
                break

        return info
