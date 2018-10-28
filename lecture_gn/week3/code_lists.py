import gn_libs2.crawler as crawler
codes = [
    "060310",
    "095570",
    "000660", # 67000
    "161490"
]
for code in codes:
    try:
        print("=>", crawler.getPrice(code))
    except:
        print("error", code)

# print(crawler.getPrice(codes[0]))