from redis import Redis



r=Redis(
    host='localhost',
    port=6379,
    password='123456',
    db=3,
    decode_responses=True
    )
# r.set("name","渣渣辉")
# result=r.get("name")
# print(result)

r.zadd("xiangyan",{"中华":50,"利群":18})