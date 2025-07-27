import json
import os

def load_json():
    with open("input/INVOICES.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
    with open("input/PLAYS.json", "r", encoding="utf-8") as f:
        plays = json.load(f)
    return invoices, plays

def main():
    invoices, plays = load_json()    
    tragedy_base_price = 40000
    comedy_base_price = 30000
    tragedy_additional_charge_threshold = 30
    tragedy_additional_charge_amount_per_person = 1000
    comedy_additional_charge_threshold = 20
    comedy_additional_charge_amount_per_person = 500

    total_amount = 0
    total_point = 0
    content = "請求書\n" + invoices[0]['customer'] + "\n"
    for i in invoices[0]['performances']:
        audience = i['audience']
        performance_type = plays[i['playID']]['type']
        point = 0
        if audience > 30:
            point += (audience - 30)
        if performance_type == "tragedy":
            amount = tragedy_base_price
            if audience > tragedy_additional_charge_threshold:
                amount += (audience - tragedy_additional_charge_threshold)*tragedy_additional_charge_amount_per_person
        elif performance_type == "comedy":
            amount = comedy_base_price + audience*300
            point += audience//5
            if audience > comedy_additional_charge_threshold:
                amount += 10000 + (audience - comedy_additional_charge_threshold)*comedy_additional_charge_amount_per_person

        total_amount += amount
        total_point += point
        content += "・" + plays[i['playID']]['name'] + "（観客数：" + str(i['audience']) + "人、" + "金額：$" + str(amount) + "）\n"
    
    content += "合計金額：$" + str(total_amount) + "\n"
    content += "獲得ポイント：" + str(total_point) + "pt"

    def output_text_invoice():
        with open("./output/invoice.txt", "w", encoding="utf-8") as f:
            f.write(content)     
        print("output.txt にテキストを書き込みました。")

    output_text_invoice()

    print(content)

if __name__ == "__main__":
    main()

