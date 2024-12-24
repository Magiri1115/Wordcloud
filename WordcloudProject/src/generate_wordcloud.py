from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# テキストファイルの読み込み
file_path = "input/text_data.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# 除外する単語リスト
exclude_words = ["こと","もの","たち","する","ため"]

# Janomeを使って形態素解析
def tokenize_with_janome(text):
    tokenizer = Tokenizer()
    words = []
    for token in tokenizer.tokenize(text):
        surface = token.surface
        pos = token.part_of_speech.split(',')[0]  # 品詞の取得
        # 名詞、動詞、形容詞を残す（助詞・助動詞は除外）
        # さらに、除外リストにある単語も除外
        if pos in ["名詞", "動詞", "形容詞"] and surface not in exclude_words:
            words.append(surface)
    return words

# ワードクラウド生成用フォントパス（環境に合わせて設定）
font_path = r"fonts\PopRumKiwi-Telop.otf"

# 出力ディレクトリの確認・作成
output_dir = "output"  # outputディレクトリの指定
if not os.path.exists(output_dir):
    os.makedirs(output_dir)  # outputディレクトリが存在しない場合に作成

# ワードクラウド生成
try:
    words = tokenize_with_janome(text)
    word_string = " ".join(words)
    
    wordcloud = WordCloud(
        font_path=font_path,
        width=800,
        height=600,
        background_color="white",
    ).generate(word_string)

    # 保存 (outputディレクトリ内に保存)
    output_path = os.path.join(output_dir, "wordcloud_output.png")
    wordcloud.to_file(output_path)
    print(f"ワードクラウドを {output_path} に保存しました。")
    
    # ワードクラウドを表示
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


except Exception as e:
    print(f"エラーが発生しました: {e}")
