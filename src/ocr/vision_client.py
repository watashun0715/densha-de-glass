"""
Google Cloud Vision API を使って画像からテキストを抽出するモジュール
"""
import os
from google.cloud import vision
from PIL import Image
import io


class VisionClient:
    def __init__(self):
        self.client = vision.ImageAnnotatorClient()

    def extract_text_from_file(self, image_path: str) -> str:
        """
        画像ファイルからテキストを抽出する

        Args:
            image_path: 画像ファイルのパス

        Returns:
            抽出されたテキスト文字列
        """
        with open(image_path, "rb") as f:
            content = f.read()

        image = vision.Image(content=content)
        response = self.client.text_detection(image=image)

        if response.error.message:
            raise Exception(f"Vision API エラー: {response.error.message}")

        texts = response.text_annotations
        if not texts:
            return ""

        # texts[0] が全体のテキスト
        return texts[0].description

    def extract_text_from_bytes(self, image_bytes: bytes) -> str:
        """
        バイト列からテキストを抽出する（スマホカメラ画像など）

        Args:
            image_bytes: 画像のバイト列

        Returns:
            抽出されたテキスト文字列
        """
        image = vision.Image(content=image_bytes)
        response = self.client.text_detection(image=image)

        if response.error.message:
            raise Exception(f"Vision API エラー: {response.error.message}")

        texts = response.text_annotations
        if not texts:
            return ""

        return texts[0].description
