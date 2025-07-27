import json
import os

def load_json():
   with open("input/invoices.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
   with open("input/plays.json", "r", encoding="utf-8") as f:
        plays = json.load(f)
   return invoices, plays

def main():
    invoices, plays = load_json()

    # 出力ディレクトリの作成（存在しない場合）
    os.makedirs("output", exist_ok=True)
    
    # ファイルに出力
    with open("output/invoice.txt", "w", encoding="utf-8") as f:
        f.write(invoice_content)
    
    print("請求書が正常に出力されました。")

if __name__ == "__main__":
    main()
