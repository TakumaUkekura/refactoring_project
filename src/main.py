import json
import os


def main():
    with open("input/INVOICES.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
    with open("input/PLAYS.json", "r", encoding="utf-8") as f:
        plays = json.load(f)

    text = "これはテスト出力です。"
    with open("output.txt", "w", encoding="utf-8") as f:
      f.write(text)
    print("output.txt にテキストを書き込みました。")

if __name__ == "__main__":
    main()
