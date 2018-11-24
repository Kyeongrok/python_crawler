def getPrice(code):
    # 봉차트 candle
    # 시가(open) 2000
    # 고가(high) 3000
    # 저가(low) 1000
    # 종가(close) 2500
    # price = 종가

    return {"close":1000, "open":2000,
            "high":3000, "low":1000}

result = getPrice("234233")
print(result['open'])