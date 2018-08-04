json_obj = {"name":"kyeongrok",
            "age":"32",
            "where":"역삼동",
            "phone_number":"010-3588-6265",
            "friends":[
                {"name":"doyeon", "age":"32"},
                {"name":"kuri", "age":"24"}
            ]
            }

friends = json_obj['friends']
for friend in friends:
    print(friend['name'])
