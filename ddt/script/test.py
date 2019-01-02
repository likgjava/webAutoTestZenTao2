import json


def build_data():
    result = []
    with open("../data/login.json", encoding="utf-8") as f:
        data = json.load(f)
        data_list = data.values()
        # print("data_list=", data_list)
        for obj in data_list:
            # print("username=", obj.get("username"))
            result.append((obj.get("username"), obj.get("pwd"), obj.get("expect"), obj.get("is_success")))
    return result


print(build_data())
