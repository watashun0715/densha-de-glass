# 電車でGlass 🚃👓

電光掲示板をスマホ（将来：スマートグラス）で見るだけで、目的駅への最適な乗車位置を案内してくれるアプリ。

## 概要

- スマホカメラで電光掲示板を撮影
- Google Cloud Vision OCRで路線・行き先・番線を自動認識
- 目的駅と移動スタイル（エレベーター/階段/出口）に合わせた最適号車を表示
- 将来的にスマートグラス（MentraOS）に対応予定

## ディレクトリ構成

```
densha-de-glass/
├── src/
│   ├── ocr/               # Cloud Vision OCR処理
│   ├── parser/            # 電光掲示板テキストのパース
│   ├── calculator/        # 乗車位置計算
│   └── display/           # 表示モジュール（将来：グラス対応）
├── tests/                 # ユニットテスト
├── data/
│   └── images/            # テスト用画像置き場
├── credentials/           # Google APIキー（gitignore済み）
├── docs/                  # 設計書など
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env.example
```

## セットアップ

### 1. リポジトリをクローン

```bash
git clone https://github.com/your-username/densha-de-glass.git
cd densha-de-glass
```

### 2. 環境変数を設定

```bash
cp .env.example .env
# .envを編集してAPIキーを設定
```

### 3. Google Cloud Vision APIキーを取得

1. [Google Cloud Console](https://console.cloud.google.com/) でプロジェクト作成
2. Vision API を有効化
3. サービスアカウントキー（JSON）をダウンロード
4. `credentials/google_credentials.json` として保存

### 4. Yahoo! APIキーを取得

1. [Yahoo! Developer Network](https://developer.yahoo.co.jp/) でアプリ登録
2. Client IDを `.env` の `YAHOO_API_CLIENT_ID` に設定

### 5. Dockerで起動

```bash
# アプリを起動
docker-compose up

# 画像を指定して実行
docker-compose run app python src/main.py data/images/sample.jpg 新宿 elevator

# テストを実行
docker-compose --profile test run test
```

## 使い方

```bash
# 引数：<画像パス> <目的駅> <移動スタイル>
# 移動スタイル: elevator / stairs / exit

python src/main.py data/images/sample.jpg 新宿 elevator
```

出力例：
```
🚃 電車でGlass 起動
目的駅：新宿
移動スタイル：elevator

📷 画像を読み込み中...
OCR結果：
山手線
新宿・渋谷方面
3番線

路線名：山手線
行き先：新宿方面
番線：3番線

==============================
👓 3号車 / 前扉付近
   エレベーターまで最短
==============================
```

## 開発ロードマップ

- [x] Step 1: OCRで電光掲示板を読む
- [x] Step 2: テキストをパース（路線・行き先・番線）
- [ ] Step 3: Yahoo! APIで乗車位置を計算
- [ ] Step 4: スマホ画面にUI表示
- [ ] Step 5: MentraOS SDK でスマートグラスに通知

## コスト試算（個人利用・月40回想定）

| API | 月額 |
|-----|------|
| Cloud Vision OCR | 約24円 |
| Yahoo!乗換 API | 0円（無料枠内） |
| **合計** | **約24円/月** |

## 参考リンク

- [Google Cloud Vision API](https://cloud.google.com/vision/docs/ocr)
- [Yahoo!乗換案内 API](https://developer.yahoo.co.jp/webapi/map/openlocalplatform/v1/transit.html)
- [MentraOS ドキュメント](https://docs.mentra.glass)
- [設計書](docs/design_v0.2.md)
