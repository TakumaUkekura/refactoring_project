import json
import os


def main():
    text = "これはテスト出力です。"
    with open("output.txt", "w", encoding="utf-8") as f:
      f.write(text)
    print("output.txt にテキストを書き込みました。")

if __name__ == "__main__":
    main()
