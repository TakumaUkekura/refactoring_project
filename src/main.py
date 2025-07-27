import json
import os

def calculation(type, audience):
    if type == "tragedy":
        amount = 40000
        if audience > 30:
            amount += (audience - 30)*1000
    elif type == "comedy":
        amount = 30000 + audience*300
        if audience > 20:
            amount += 10000 + (audience - 20)*500
    return amount         


def main():
    with open("input/INVOICES.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
    with open("input/PLAYS.json", "r", encoding="utf-8") as f:
        plays = json.load(f)

    print(invoices[0])
    print(plays)
    for i in invoices[0]['performances']:
        print(i['playID'])
        print(i['audience'])        
        print(plays[i['playID']]['name'])
        print(plays[i['playID']]['type'])

    content = "請求書\n" + invoices[0]['customer'] + "\n"
    for i in invoices[0]['performances']:
        content += "・" + plays[i['playID']]['name'] +  "（観客数：" + str(i['audience']) + "人、" + "金額：$" + str(calculation(plays[i['playID']]['type'], i['audience'])) + ")\n"

    with open("./output/output.txt", "w", encoding="utf-8") as f:
      f.write(content)     
    print("output.txt にテキストを書き込みました。")

    print(content)

if __name__ == "__main__":
    main()
