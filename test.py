import pyupbit

access = "kcAKnVsJ3wSf0WilC1zaZ2N5hko0t9Q3E3fxBJBR"          # 본인 값으로 변경
secret = "AzS0BP1bOM6bBAcEgFbpOzofpqka43DP6IlPe147"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회