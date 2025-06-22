import re


def handle_health_setting(user_text: str) -> str:

    match = re.search(r"(\d{3})\D+(\d{2,3})", user_text)
    if match:
        height = float(match.group(1))
        weight = float(match.group(2))
        bmi = round(weight / ((height / 100) ** 2), 2)

        if bmi < 18.5:
            status = "過輕"
        elif 18.5 <= bmi < 24:
            status = "正常"
        elif 24 <= bmi < 27:
            status = "過重"
        elif 27 <= bmi < 30:
            status = "輕度肥胖"
        elif 30 <= bmi < 35:
            status = "中度肥胖"
        else:
            status = "重度肥胖"

        return f"您的 BMI 是 {bmi}，屬於「{status}」"

    return ("請輸入您的身高體重，例如：\n"
            "160 60\n"
            "或\n"
            "身高（公分）:160 體重（公斤）:60")
