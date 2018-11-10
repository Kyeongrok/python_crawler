import gn_libs2.crawler as crawler
codes = open("./codes.txt").readlines()
infos = open("./infos.txt", "w+")

for code in codes[:10]:
    companyInfo = crawler.getPrice(code)
    message = "{}@{}".format(companyInfo['company_name'], companyInfo['now'])
    infos.write(message + "\n")
    print(message)

# getPrice 얘는 code
# save to excel 얘는 index
#