import json
import os

def load_json():
    with open("input/INVOICES.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
    with open("input/PLAYS.json", "r", encoding="utf-8") as f:
        plays = json.load(f)
    return invoices, plays

def calculation(type, audience):
    point = 0
    if type == "tragedy":
        amount = 40000
        if audience > 30:
            amount += (audience - 30)*1000
            point += (audience - 30)
    elif type == "comedy":
        amount = 30000 + audience*300
        point += audience//5
        if audience > 20:
            amount += 10000 + (audience - 20)*500
            if audience > 30:
                point += (audience - 30)
    return amount, point


def main():

    invoices, plays = load_json()    

    print(invoices[0])
    print(plays)
    for i in invoices[0]['performances']:
        print(i['playID'])
        print(i['audience'])        
        print(plays[i['playID']]['name'])
        print(plays[i['playID']]['type'])
    
    total_amount = 0
    total_point = 0
    content = "請求書\n" + invoices[0]['customer'] + "\n"
    for i in invoices[0]['performances']:
        amount, point = calculation(plays[i['playID']]['type'], i['audience'])
        total_amount += amount
        total_point += point
        content += "・" + plays[i['playID']]['name'] +  "（観客数：" + str(i['audience']) + "人、" + "金額：$" + str(amount) + ")\n"
    
    content += "合計金額：$" + str(total_amount) + "\n"
    content += "獲得ポイント：" + str(total_point) + "pt"

    with open("./output/invoice.txt", "w", encoding="utf-8") as f:
      f.write(content)     
    print("output.txt にテキストを書き込みました。")

    print(content)

if __name__ == "__main__":
    main()
