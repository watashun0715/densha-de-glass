"""
最適な乗車位置を計算するモジュール
TODO: Yahoo!乗換APIと国交省データを使って精度を上げる
"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional
from src.parser.sign_parser import SignInfo


class MoveStyle(Enum):
    ELEVATOR = "elevator"   # エレベーター優先
    STAIRS = "stairs"       # 階段優先
    EXIT = "exit"           # 出口優先


@dataclass
class BoardingPosition:
    """推奨乗車位置"""
    car_number: Optional[str] = None     # 号車（例：3号車）
    door_position: Optional[str] = None  # ドア位置（例：前扉）
    reason: Optional[str] = None         # 理由（例：エレベーターまで最短）


class PositionCalculator:
    def calculate(
        self,
        sign_info: SignInfo,
        destination: str,
        move_style: MoveStyle
    ) -> BoardingPosition:
        """
        最適な乗車位置を計算する

        Args:
            sign_info: 電光掲示板から読み取った情報
            destination: 目的駅
            move_style: 移動スタイル

        Returns:
            BoardingPosition: 推奨乗車位置
        """
        # TODO: Yahoo! APIと国交省データを使った本格実装
        # 現在はダミーデータを返す（Step 2で実装予定）
        position = BoardingPosition()

        if move_style == MoveStyle.ELEVATOR:
            position.car_number = "1号車"
            position.door_position = "後扉"
            position.reason = "エレベーターまで最短"
        elif move_style == MoveStyle.STAIRS:
            position.car_number = "3号車"
            position.door_position = "前扉"
            position.reason = "階段まで最短"
        else:
            position.car_number = "5号車"
            position.door_position = "中扉"
            position.reason = "出口まで最短"

        return position
