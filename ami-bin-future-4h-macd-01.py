import ccxt
import pprint
import pandas as pd
import time
import datetime
import math




api_key = "KQ4pmEviUpobvyVHNrDBry0Kd1YgslSAFJ9exQzKzXHignQ1NCd8q3UCrWZYgkkQ"
secret = "A23zFqn5EvolUtP6IzPaGoO1IIAie425Nbh2tPXbfMftOq48VxjVtbBgxNEzLEQp"

# 선물 현재가 출력하기

binance = ccxt.binance( config = {
    'apiKey' : api_key, 
    'secret' : secret,
    'enableRateLimit' : True,
    'options' : {
        'defaultType' : 'future'
    }
} )

exchange = ccxt.binance()

symbol1 = "BTC/USDT"
























# def 함수
####################################
# 거래가능한 선물 보유금 BTC 갯수설정 #
def cal_amount( usdt_balance, cur_price ):
    # 거래금액 비율
    portion = 1
    # 거래금액산정
    usdt_trade = usdt_balance * portion
    # btc 거래갯수산정
    amount = math.floor( ( usdt_trade * 1000 ) / cur_price ) / 1000

    return amount






# def 함수
#########################
# 거래량 동반한 macd 조회.
# get_acc_macd(ticker) 원래 이름
# 사용할땐 get_macd(ticker) 로 바꿈
def get_macd( exchange, symbol ):
    # 단기 이평 = 12일선.
    # 장기 이평 = 26일선.
    # macd = 단기 이평 - 장기 이평.
    # signal = macd 의 9일선.

    btc = exchange.fetch_ohlcv(
        symbol = symbol1,
        timeframe = '4h', 
        since = None, 
        limit = 50
    )

    df = pd.DataFrame( data = btc, columns = [ 'datetime', 'open', 'high', 'low', 'close', 'volume' ] )
    df[ 'datetime' ] = pd.to_datetime( df[ 'datetime' ], unit = 'ms' )
    df.set_index( 'datetime', inplace = True )

    print( df )
    print()


    # 종가받기 40개
    print("========== 4시간봉 종가 받기 ==========")
    print()
    # 0은 아무것도 아님.
    price_0_close = df.iloc[0]['close']
    #price_0_time = df.iloc[0]['datetime']
    price_0_volume = df.iloc[0]['volume']
    price_0_total = price_0_close * price_0_volume
    print( f"0. 현재가 = { price_0_close } USDT * 거래량 = { price_0_volume }  =  총액 = { price_0_total } USDT" )

    # -1은 현재가.
    price_1_close = df.iloc[-1]['close']
    price_1_volume = df.iloc[-1]['volume']
    price_1_total = price_1_close * price_1_volume
    print(f"1. 현재가 = {price_1_close} USDT * 거래량 = {price_1_volume}  =  총액 = {price_1_total} USDT")
    print()

    ########################################
    # -2는 1시간전 종가. 여기부터 macd 계산.
    price_2_close = df.iloc[-2]['close']
    price_2_volume = df.iloc[-2]['volume']
    price_2_total = price_2_close * price_2_volume
    print(f"2. 종가 = {price_2_close} USDT * 거래량 = {price_2_volume}  =  총액 = {price_2_total} USDT")
    
    price_3_close = df.iloc[-3]['close']
    price_3_volume = df.iloc[-3]['volume']
    price_3_total = price_3_close * price_3_volume
    print(f"3. 종가 = {price_3_close} USDT * 거래량 = {price_3_volume}  =  총액 = {price_3_total} USDT")

    price_4_close = df.iloc[-4]['close']
    price_4_volume = df.iloc[-4]['volume']
    price_4_total = price_4_close * price_4_volume
    print(f"4. 종가 = {price_4_close} USDT * 거래량 = {price_4_volume}  =  총액 = {price_4_total} USDT")

    price_5_close = df.iloc[-5]['close']
    price_5_volume = df.iloc[-5]['volume']
    price_5_total = price_5_close * price_5_volume
    print(f"5. 종가 = {price_5_close} USDT * 거래량 = {price_5_volume}  =  총액 = {price_5_total} USDT")

    print()

    price_6_close = df.iloc[-6]['close']
    price_6_volume = df.iloc[-6]['volume']
    price_6_total = price_6_close * price_6_volume
    print(f"6. 종가 = {price_6_close} USDT * 거래량 = {price_6_volume}  =  총액 = {price_6_total} USDT")

    price_7_close = df.iloc[-7]['close']
    price_7_volume = df.iloc[-7]['volume']
    price_7_total = price_7_close * price_7_volume
    print(f"7. 종가 = {price_7_close} USDT * 거래량 = {price_7_volume}  =  총액 = {price_7_total} USDT")
    
    price_8_close = df.iloc[-8]['close']
    price_8_volume = df.iloc[-8]['volume']
    price_8_total = price_8_close * price_8_volume
    print(f"8. 종가 = {price_8_close} USDT * 거래량 = {price_8_volume}  =  총액 = {price_8_total} USDT")

    price_9_close = df.iloc[-9]['close']
    price_9_volume = df.iloc[-9]['volume']
    price_9_total = price_9_close * price_9_volume
    print(f"9. 종가 = {price_9_close} USDT * 거래량 = {price_9_volume}  =  총액 = {price_9_total} USDT")

    price_10_close = df.iloc[-10]['close']
    price_10_volume = df.iloc[-10]['volume']
    price_10_total = price_10_close * price_10_volume
    print(f"10. 종가 = {price_10_close} USDT * 거래량 = {price_10_volume}  =  총액 = {price_10_total} USDT")

    print()

    price_11_close = df.iloc[-11]['close']
    price_11_volume = df.iloc[-11]['volume']
    price_11_total = price_11_close * price_11_volume
    print(f"11. 종가 = {price_11_close} USDT * 거래량 = {price_11_volume}  =  총액 = {price_11_total} USDT")

    price_12_close = df.iloc[-12]['close']
    price_12_volume = df.iloc[-12]['volume']
    price_12_total = price_12_close * price_12_volume
    print(f"12. 종가 = {price_12_close} USDT * 거래량 = {price_12_volume}  =  총액 = {price_12_total} USDT")

    price_13_close = df.iloc[-13]['close']
    price_13_volume = df.iloc[-13]['volume']
    price_13_total = price_13_close * price_13_volume
    print(f"13. 종가 = {price_13_close} USDT * 거래량 = {price_13_volume}  =  총액 = {price_13_total} USDT")

    price_14_close = df.iloc[-14]['close']
    price_14_volume = df.iloc[-14]['volume']
    price_14_total = price_14_close * price_14_volume
    print(f"14. 종가 = {price_14_close} USDT * 거래량 = {price_14_volume}  =  총액 = {price_14_total} USDT")

    price_15_close = df.iloc[-15]['close']
    price_15_volume = df.iloc[-15]['volume']
    price_15_total = price_15_close * price_15_volume
    print(f"15. 종가 = {price_15_close} USDT * 거래량 = {price_15_volume}  =  총액 = {price_15_total} USDT")

    print()

    price_16_close = df.iloc[-16]['close']
    price_16_volume = df.iloc[-16]['volume']
    price_16_total = price_16_close * price_16_volume
    print(f"16. 종가 = {price_16_close} USDT * 거래량 = {price_16_volume}  =  총액 = {price_16_total} USDT")

    price_17_close = df.iloc[-17]['close']
    price_17_volume = df.iloc[-17]['volume']
    price_17_total = price_17_close * price_17_volume
    print(f"17. 종가 = {price_17_close} USDT * 거래량 = {price_17_volume}  =  총액 = {price_17_total} USDT")

    price_18_close = df.iloc[-18]['close']
    price_18_volume = df.iloc[-18]['volume']
    price_18_total = price_18_close * price_18_volume
    print(f"18. 종가 = {price_18_close} USDT * 거래량 = {price_18_volume}  =  총액 = {price_18_total} USDT")

    price_19_close = df.iloc[-19]['close']
    price_19_volume = df.iloc[-19]['volume']
    price_19_total = price_19_close * price_19_volume
    print(f"19. 종가 = {price_19_close} USDT * 거래량 = {price_19_volume}  =  총액 = {price_19_total} USDT")

    price_20_close = df.iloc[-20]['close']
    price_20_volume = df.iloc[-20]['volume']
    price_20_total = price_20_close * price_20_volume
    print(f"20. 종가 = {price_20_close} USDT * 거래량 = {price_20_volume}  =  총액 = {price_20_total} USDT")

    print()

    price_21_close = df.iloc[-21]['close']
    price_21_volume = df.iloc[-21]['volume']
    price_21_total = price_21_close * price_21_volume
    print(f"21. 종가 = {price_21_close} USDT * 거래량 = {price_21_volume}  =  총액 = {price_21_total} USDT")

    price_22_close = df.iloc[-22]['close']
    price_22_volume = df.iloc[-22]['volume']
    price_22_total = price_22_close * price_22_volume
    print(f"22. 종가 = {price_22_close} USDT * 거래량 = {price_22_volume}  =  총액 = {price_22_total} USDT")

    price_23_close = df.iloc[-23]['close']
    price_23_volume = df.iloc[-23]['volume']
    price_23_total = price_23_close * price_23_volume
    print(f"23. 종가 = {price_23_close} USDT * 거래량 = {price_23_volume}  =  총액 = {price_23_total} USDT")

    price_24_close = df.iloc[-24]['close']
    price_24_volume = df.iloc[-24]['volume']
    price_24_total = price_24_close * price_24_volume
    print(f"24. 종가 = {price_24_close} USDT * 거래량 = {price_24_volume}  =  총액 = {price_24_total} USDT")

    price_25_close = df.iloc[-25]['close']
    price_25_volume = df.iloc[-25]['volume']
    price_25_total = price_25_close * price_25_volume
    print(f"25. 종가 = {price_25_close} USDT * 거래량 = {price_25_volume}  =  총액 = {price_25_total} USDT")

    print()

    price_26_close = df.iloc[-26]['close']
    price_26_volume = df.iloc[-26]['volume']
    price_26_total = price_26_close * price_26_volume
    print(f"26. 종가 = {price_26_close} USDT * 거래량 = {price_26_volume}  =  총액 = {price_26_total} USDT")

    price_27_close = df.iloc[-27]['close']
    price_27_volume = df.iloc[-27]['volume']
    price_27_total = price_27_close * price_27_volume
    print(f"27. 종가 = {price_27_close} USDT * 거래량 = {price_27_volume}  =  총액 = {price_27_total} USDT")

    price_28_close = df.iloc[-28]['close']
    price_28_volume = df.iloc[-28]['volume']
    price_28_total = price_28_close * price_28_volume
    print(f"28. 종가 = {price_28_close} USDT * 거래량 = {price_28_volume}  =  총액 = {price_28_total} USDT")

    price_29_close = df.iloc[-29]['close']
    price_29_volume = df.iloc[-29]['volume']
    price_29_total = price_29_close * price_29_volume
    print(f"29. 종가 = {price_29_close} USDT * 거래량 = {price_29_volume}  =  총액 = {price_29_total} USDT")

    price_30_close = df.iloc[-30]['close']
    price_30_volume = df.iloc[-30]['volume']
    price_30_total = price_30_close * price_30_volume
    print(f"30. 종가 = {price_30_close} USDT * 거래량 = {price_30_volume}  =  총액 = {price_30_total} USDT")

    print()

    price_31_close = df.iloc[-31]['close']
    price_31_volume = df.iloc[-31]['volume']
    price_31_total = price_31_close * price_31_volume
    print(f"31. 종가 = {price_31_close} USDT * 거래량 = {price_31_volume}  =  총액 = {price_31_total} USDT")

    price_32_close = df.iloc[-32]['close']
    price_32_volume = df.iloc[-32]['volume']
    price_32_total = price_32_close * price_32_volume
    print(f"32. 종가 = {price_32_close} USDT * 거래량 = {price_32_volume}  =  총액 = {price_32_total} USDT")

    price_33_close = df.iloc[-33]['close']
    price_33_volume = df.iloc[-33]['volume']
    price_33_total = price_33_close * price_33_volume
    print(f"33. 종가 = {price_33_close} USDT * 거래량 = {price_33_volume}  =  총액 = {price_33_total} USDT")

    price_34_close = df.iloc[-34]['close']
    price_34_volume = df.iloc[-34]['volume']
    price_34_total = price_34_close * price_34_volume
    print(f"34. 종가 = {price_34_close} USDT * 거래량 = {price_34_volume}  =  총액 = {price_34_total} USDT")

    price_35_close = df.iloc[-35]['close']
    price_35_volume = df.iloc[-35]['volume']
    price_35_total = price_35_close * price_35_volume
    print(f"35. 종가 = {price_35_close} USDT * 거래량 = {price_35_volume}  =  총액 = {price_35_total} USDT")
    
    print()

    







    # 단기 12이평선
    acc_ma12_1_1 = price_2_close + price_3_close + price_4_close + price_5_close + price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close
    acc_ma12_1 = acc_ma12_1_1 / 12

    acc_ma12_2_1 = price_3_close + price_4_close + price_5_close + price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close
    acc_ma12_2 = acc_ma12_2_1 / 12

    acc_ma12_3_1 = price_4_close + price_5_close + price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close
    acc_ma12_3 = acc_ma12_3_1 / 12
    
    acc_ma12_4_1 = price_5_close + price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close
    acc_ma12_4 = acc_ma12_4_1 / 12
    
    acc_ma12_5_1 = price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close
    acc_ma12_5 = acc_ma12_5_1 / 12
    
    acc_ma12_6_1 = price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close
    acc_ma12_6 = acc_ma12_6_1 / 12
    
    acc_ma12_7_1 = price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close
    acc_ma12_7 = acc_ma12_7_1 / 12
    
    acc_ma12_8_1 = price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close
    acc_ma12_8 = acc_ma12_8_1 / 12
    
    acc_ma12_9_1 = price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close
    acc_ma12_9 = acc_ma12_9_1 / 12

    # 여기까지


        # 거래량 동반한 장기 26이평선
    acc_ma26_1_1 = acc_ma12_1_1  +  price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close
    acc_ma26_1 = acc_ma26_1_1 / 26

    acc_ma26_2_1 = acc_ma12_2_1  +  price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close
    acc_ma26_2 = acc_ma26_2_1 / 26

    acc_ma26_3_1 = acc_ma12_3_1  +  price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close
    acc_ma26_3 = acc_ma26_3_1 / 26

    acc_ma26_4_1 = acc_ma12_4_1  +  price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close
    acc_ma26_4 = acc_ma26_4_1 / 26

    acc_ma26_5_1 = acc_ma12_5_1  +  price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close
    acc_ma26_5 = acc_ma26_5_1 / 26

    acc_ma26_6_1 = acc_ma12_6_1  +  price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close
    acc_ma26_6 = acc_ma26_6_1 / 26

    acc_ma26_7_1 = acc_ma12_7_1  +  price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close
    acc_ma26_7 = acc_ma26_7_1 / 26

    acc_ma26_8_1 = acc_ma12_8_1  +  price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close
    acc_ma26_8 = acc_ma26_8_1 / 26

    acc_ma26_9_1 = acc_ma12_9_1  +  price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close
    acc_ma26_9 = acc_ma26_9_1 / 26

    # 여기까지


    # macd
    # 단기12일이평선 - 장기26일이평선 = + 는 골든크로스, - 는 데드크로스
    # + 는 골드크로스, - 는 데드크로스
    acc_macd_1 = acc_ma12_1 - acc_ma26_1
    print( f"macd_1 ( {acc_macd_1} ) =  acc_ma12_1 ( {acc_ma12_1} ) - acc_ma26_1 ( {acc_ma26_1} )")
    acc_macd_2 = acc_ma12_2 - acc_ma26_2
    print( f"macd_2 ( {acc_macd_2} ) =  acc_ma12_2 ( {acc_ma12_2} ) - acc_ma26_2 ( {acc_ma26_2} )")
    acc_macd_3 = acc_ma12_3 - acc_ma26_3
    print( f"macd_3 ( {acc_macd_3} ) =  acc_ma12_3 ( {acc_ma12_3} ) - acc_ma26_3 ( {acc_ma26_3} )")
    acc_macd_4 = acc_ma12_4 - acc_ma26_4
    print( f"macd_4 ( {acc_macd_4} ) =  acc_ma12_4 ( {acc_ma12_4} ) - acc_ma26_4 ( {acc_ma26_4} )")
    acc_macd_5 = acc_ma12_5 - acc_ma26_5
    print( f"macd_5 ( {acc_macd_5} ) =  acc_ma12_5 ( {acc_ma12_5} ) - acc_ma26_5 ( {acc_ma26_5} )")
    acc_macd_6 = acc_ma12_6 - acc_ma26_6
    print( f"macd_6 ( {acc_macd_6} ) =  acc_ma12_6 ( {acc_ma12_6} ) - acc_ma26_6 ( {acc_ma26_6} )")
    acc_macd_7 = acc_ma12_7 - acc_ma26_7
    print( f"macd_7 ( {acc_macd_7} ) =  acc_ma12_7 ( {acc_ma12_7} ) - acc_ma26_7 ( {acc_ma26_7} )")
    acc_macd_8 = acc_ma12_8 - acc_ma26_8
    print( f"macd_8 ( {acc_macd_8} ) =  acc_ma12_8 ( {acc_ma12_8} ) - acc_ma26_8 ( {acc_ma26_8} )")
    acc_macd_9 = acc_ma12_9 - acc_ma26_9
    print( f"macd_9 ( {acc_macd_9} ) =  acc_ma12_9 ( {acc_ma12_9} ) - acc_ma26_9 ( {acc_ma26_9} )")
    print()

    # signal = macd 9일선, 기준선 위치
    acc_signal_1 = ( acc_macd_1 + acc_macd_2 + acc_macd_3 + acc_macd_4 + acc_macd_5 + acc_macd_6 + acc_macd_7 + acc_macd_8 + acc_macd_9 ) / 9
    print(f"acc_signal_1 = ( {acc_signal_1} )")
    print()

    # 최종값
    # 기준선과 오실레이터와의 간극. + 는 0 기준선 상승돌파, - 는 0 기준선 하락
    acc_macd1 = acc_macd_1 - acc_signal_1
    print(f"acc_macd1 ( {acc_macd1} ) = acc_macd_1 ( {acc_macd_1} ) - acc_signal_1 ( {acc_signal_1} )")
    print()

    ##### 거래량 동반한 macd 산출. 끝 #####
    #####################################


    #####################################
    ##### macd 매매선택              #####

    # acc_macd_select
    if acc_macd1 >= 0:
        if acc_macd_1 >= 0:
            # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 골든크로스
            acc_macd_select = 1
        else:
            # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 데드크로스
            acc_macd_select = 2
    else:
        if acc_macd_1 >= 0:
            # acc_ma26_1이 기준선 아래에 있을때, acc_macd1이 골든크로스
            acc_macd_select = 3
        else:
            # acc_ma26_1이 기준선 아래에 있을때, acc_macd1이 데드크로스
            acc_macd_select = 4

    print(f"acc_macd_select = {acc_macd_select}")
    print()

    return acc_macd_select


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################









































































################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################




btc = exchange.fetch_ohlcv(
    symbol=symbol1,
    timeframe='4h', 
    since=None, 
    limit=50
)

df = pd.DataFrame(data = btc, columns = ['datetime', 'open', 'high', 'low', 'close', 'volume'])
df['datetime'] = pd.to_datetime(df['datetime'], unit = 'ms')
df.set_index('datetime', inplace = True)

print(df)
print()


# 종가받기 40개
print("========== 4시간봉 종가 받기 ==========")
print()
# 0은 아무것도 아님.
price_0_close = df.iloc[0]['close']
#price_0_time = df.iloc[0]['datetime']
price_0_volume = df.iloc[0]['volume']
price_0_total = price_0_close * price_0_volume
print(f"0. 현재가 = {price_0_close} USDT * 거래량 = {price_0_volume}  =  총액 = {price_0_total} USDT")

# -1은 현재가.
price_1_close = df.iloc[-1]['close']
price_1_volume = df.iloc[-1]['volume']
price_1_total = price_1_close * price_1_volume
print(f"1. 현재가 = {price_1_close} USDT * 거래량 = {price_1_volume}  =  총액 = {price_1_total} USDT")
print()

########################################
# -2는 1시간전 종가. 여기부터 macd 계산.
price_2_close = df.iloc[-2]['close']
price_2_volume = df.iloc[-2]['volume']
price_2_total = price_2_close * price_2_volume
print(f"2. 종가 = {price_2_close} USDT * 거래량 = {price_2_volume}  =  총액 = {price_2_total} USDT")
    
price_3_close = df.iloc[-3]['close']
price_3_volume = df.iloc[-3]['volume']
price_3_total = price_3_close * price_3_volume
print(f"3. 종가 = {price_3_close} USDT * 거래량 = {price_3_volume}  =  총액 = {price_3_total} USDT")

price_4_close = df.iloc[-4]['close']
price_4_volume = df.iloc[-4]['volume']
price_4_total = price_4_close * price_4_volume
print(f"4. 종가 = {price_4_close} USDT * 거래량 = {price_4_volume}  =  총액 = {price_4_total} USDT")

price_5_close = df.iloc[-5]['close']
price_5_volume = df.iloc[-5]['volume']
price_5_total = price_5_close * price_5_volume
print(f"5. 종가 = {price_5_close} USDT * 거래량 = {price_5_volume}  =  총액 = {price_5_total} USDT")

print()

price_6_close = df.iloc[-6]['close']
price_6_volume = df.iloc[-6]['volume']
price_6_total = price_6_close * price_6_volume
print(f"6. 종가 = {price_6_close} USDT * 거래량 = {price_6_volume}  =  총액 = {price_6_total} USDT")

price_7_close = df.iloc[-7]['close']
price_7_volume = df.iloc[-7]['volume']
price_7_total = price_7_close * price_7_volume
print(f"7. 종가 = {price_7_close} USDT * 거래량 = {price_7_volume}  =  총액 = {price_7_total} USDT")
    
price_8_close = df.iloc[-8]['close']
price_8_volume = df.iloc[-8]['volume']
price_8_total = price_8_close * price_8_volume
print(f"8. 종가 = {price_8_close} USDT * 거래량 = {price_8_volume}  =  총액 = {price_8_total} USDT")

price_9_close = df.iloc[-9]['close']
price_9_volume = df.iloc[-9]['volume']
price_9_total = price_9_close * price_9_volume
print(f"9. 종가 = {price_9_close} USDT * 거래량 = {price_9_volume}  =  총액 = {price_9_total} USDT")

price_10_close = df.iloc[-10]['close']
price_10_volume = df.iloc[-10]['volume']
price_10_total = price_10_close * price_10_volume
print(f"10. 종가 = {price_10_close} USDT * 거래량 = {price_10_volume}  =  총액 = {price_10_total} USDT")

print()

price_11_close = df.iloc[-11]['close']
price_11_volume = df.iloc[-11]['volume']
price_11_total = price_11_close * price_11_volume
print(f"11. 종가 = {price_11_close} USDT * 거래량 = {price_11_volume}  =  총액 = {price_11_total} USDT")

price_12_close = df.iloc[-12]['close']
price_12_volume = df.iloc[-12]['volume']
price_12_total = price_12_close * price_12_volume
print(f"12. 종가 = {price_12_close} USDT * 거래량 = {price_12_volume}  =  총액 = {price_12_total} USDT")

price_13_close = df.iloc[-13]['close']
price_13_volume = df.iloc[-13]['volume']
price_13_total = price_13_close * price_13_volume
print(f"13. 종가 = {price_13_close} USDT * 거래량 = {price_13_volume}  =  총액 = {price_13_total} USDT")

price_14_close = df.iloc[-14]['close']
price_14_volume = df.iloc[-14]['volume']
price_14_total = price_14_close * price_14_volume
print(f"14. 종가 = {price_14_close} USDT * 거래량 = {price_14_volume}  =  총액 = {price_14_total} USDT")

price_15_close = df.iloc[-15]['close']
price_15_volume = df.iloc[-15]['volume']
price_15_total = price_15_close * price_15_volume
print(f"15. 종가 = {price_15_close} USDT * 거래량 = {price_15_volume}  =  총액 = {price_15_total} USDT")

print()

price_16_close = df.iloc[-16]['close']
price_16_volume = df.iloc[-16]['volume']
price_16_total = price_16_close * price_16_volume
print(f"16. 종가 = {price_16_close} USDT * 거래량 = {price_16_volume}  =  총액 = {price_16_total} USDT")

price_17_close = df.iloc[-17]['close']
price_17_volume = df.iloc[-17]['volume']
price_17_total = price_17_close * price_17_volume
print(f"17. 종가 = {price_17_close} USDT * 거래량 = {price_17_volume}  =  총액 = {price_17_total} USDT")

price_18_close = df.iloc[-18]['close']
price_18_volume = df.iloc[-18]['volume']
price_18_total = price_18_close * price_18_volume
print(f"18. 종가 = {price_18_close} USDT * 거래량 = {price_18_volume}  =  총액 = {price_18_total} USDT")

price_19_close = df.iloc[-19]['close']
price_19_volume = df.iloc[-19]['volume']
price_19_total = price_19_close * price_19_volume
print(f"19. 종가 = {price_19_close} USDT * 거래량 = {price_19_volume}  =  총액 = {price_19_total} USDT")

price_20_close = df.iloc[-20]['close']
price_20_volume = df.iloc[-20]['volume']
price_20_total = price_20_close * price_20_volume
print(f"20. 종가 = {price_20_close} USDT * 거래량 = {price_20_volume}  =  총액 = {price_20_total} USDT")

print()

price_21_close = df.iloc[-21]['close']
price_21_volume = df.iloc[-21]['volume']
price_21_total = price_21_close * price_21_volume
print(f"21. 종가 = {price_21_close} USDT * 거래량 = {price_21_volume}  =  총액 = {price_21_total} USDT")

price_22_close = df.iloc[-22]['close']
price_22_volume = df.iloc[-22]['volume']
price_22_total = price_22_close * price_22_volume
print(f"22. 종가 = {price_22_close} USDT * 거래량 = {price_22_volume}  =  총액 = {price_22_total} USDT")

price_23_close = df.iloc[-23]['close']
price_23_volume = df.iloc[-23]['volume']
price_23_total = price_23_close * price_23_volume
print(f"23. 종가 = {price_23_close} USDT * 거래량 = {price_23_volume}  =  총액 = {price_23_total} USDT")

price_24_close = df.iloc[-24]['close']
price_24_volume = df.iloc[-24]['volume']
price_24_total = price_24_close * price_24_volume
print(f"24. 종가 = {price_24_close} USDT * 거래량 = {price_24_volume}  =  총액 = {price_24_total} USDT")

price_25_close = df.iloc[-25]['close']
price_25_volume = df.iloc[-25]['volume']
price_25_total = price_25_close * price_25_volume
print(f"25. 종가 = {price_25_close} USDT * 거래량 = {price_25_volume}  =  총액 = {price_25_total} USDT")

print()

price_26_close = df.iloc[-26]['close']
price_26_volume = df.iloc[-26]['volume']
price_26_total = price_26_close * price_26_volume
print(f"26. 종가 = {price_26_close} USDT * 거래량 = {price_26_volume}  =  총액 = {price_26_total} USDT")

price_27_close = df.iloc[-27]['close']
price_27_volume = df.iloc[-27]['volume']
price_27_total = price_27_close * price_27_volume
print(f"27. 종가 = {price_27_close} USDT * 거래량 = {price_27_volume}  =  총액 = {price_27_total} USDT")

price_28_close = df.iloc[-28]['close']
price_28_volume = df.iloc[-28]['volume']
price_28_total = price_28_close * price_28_volume
print(f"28. 종가 = {price_28_close} USDT * 거래량 = {price_28_volume}  =  총액 = {price_28_total} USDT")

price_29_close = df.iloc[-29]['close']
price_29_volume = df.iloc[-29]['volume']
price_29_total = price_29_close * price_29_volume
print(f"29. 종가 = {price_29_close} USDT * 거래량 = {price_29_volume}  =  총액 = {price_29_total} USDT")

price_30_close = df.iloc[-30]['close']
price_30_volume = df.iloc[-30]['volume']
price_30_total = price_30_close * price_30_volume
print(f"30. 종가 = {price_30_close} USDT * 거래량 = {price_30_volume}  =  총액 = {price_30_total} USDT")

print()

price_31_close = df.iloc[-31]['close']
price_31_volume = df.iloc[-31]['volume']
price_31_total = price_31_close * price_31_volume
print(f"31. 종가 = {price_31_close} USDT * 거래량 = {price_31_volume}  =  총액 = {price_31_total} USDT")

price_32_close = df.iloc[-32]['close']
price_32_volume = df.iloc[-32]['volume']
price_32_total = price_32_close * price_32_volume
print(f"32. 종가 = {price_32_close} USDT * 거래량 = {price_32_volume}  =  총액 = {price_32_total} USDT")

price_33_close = df.iloc[-33]['close']
price_33_volume = df.iloc[-33]['volume']
price_33_total = price_33_close * price_33_volume
print(f"33. 종가 = {price_33_close} USDT * 거래량 = {price_33_volume}  =  총액 = {price_33_total} USDT")

price_34_close = df.iloc[-34]['close']
price_34_volume = df.iloc[-34]['volume']
price_34_total = price_34_close * price_34_volume
print(f"34. 종가 = {price_34_close} USDT * 거래량 = {price_34_volume}  =  총액 = {price_34_total} USDT")

price_35_close = df.iloc[-35]['close']
price_35_volume = df.iloc[-35]['volume']
price_35_total = price_35_close * price_35_volume
print(f"35. 종가 = {price_35_close} USDT * 거래량 = {price_35_volume}  =  총액 = {price_35_total} USDT")
    
print()

    







# 단기 12이평선
acc_ma12_1_1 = price_2_close + price_3_close + price_4_close + price_5_close + price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close
acc_ma12_1 = acc_ma12_1_1 / 12

acc_ma12_2_1 = price_3_close + price_4_close + price_5_close + price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close
acc_ma12_2 = acc_ma12_2_1 / 12

acc_ma12_3_1 = price_4_close + price_5_close + price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close
acc_ma12_3 = acc_ma12_3_1 / 12
    
acc_ma12_4_1 = price_5_close + price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close
acc_ma12_4 = acc_ma12_4_1 / 12
    
acc_ma12_5_1 = price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close
acc_ma12_5 = acc_ma12_5_1 / 12
    
acc_ma12_6_1 = price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close
acc_ma12_6 = acc_ma12_6_1 / 12
    
acc_ma12_7_1 = price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close
acc_ma12_7 = acc_ma12_7_1 / 12
    
acc_ma12_8_1 = price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close
acc_ma12_8 = acc_ma12_8_1 / 12
    
acc_ma12_9_1 = price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close
acc_ma12_9 = acc_ma12_9_1 / 12

# 여기까지


# 장기 26이평선
acc_ma26_1_1 = acc_ma12_1_1  +  price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close
acc_ma26_1 = acc_ma26_1_1 / 26

acc_ma26_2_1 = acc_ma12_2_1  +  price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close
acc_ma26_2 = acc_ma26_2_1 / 26

acc_ma26_3_1 = acc_ma12_3_1  +  price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close
acc_ma26_3 = acc_ma26_3_1 / 26

acc_ma26_4_1 = acc_ma12_4_1  +  price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close
acc_ma26_4 = acc_ma26_4_1 / 26

acc_ma26_5_1 = acc_ma12_5_1  +  price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close
acc_ma26_5 = acc_ma26_5_1 / 26

acc_ma26_6_1 = acc_ma12_6_1  +  price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close
acc_ma26_6 = acc_ma26_6_1 / 26

acc_ma26_7_1 = acc_ma12_7_1  +  price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close
acc_ma26_7 = acc_ma26_7_1 / 26

acc_ma26_8_1 = acc_ma12_8_1  +  price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close
acc_ma26_8 = acc_ma26_8_1 / 26

acc_ma26_9_1 = acc_ma12_9_1  +  price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close
acc_ma26_9 = acc_ma26_9_1 / 26

# 여기까지


# macd
# 단기12일이평선 - 장기26일이평선 = + 는 골든크로스, - 는 데드크로스
# + 는 골드크로스, - 는 데드크로스
acc_macd_1 = acc_ma12_1 - acc_ma26_1
print( f"macd_1 ( {acc_macd_1} ) =  acc_ma12_1 ( {acc_ma12_1} ) - acc_ma26_1 ( {acc_ma26_1} )")
acc_macd_2 = acc_ma12_2 - acc_ma26_2
print( f"macd_2 ( {acc_macd_2} ) =  acc_ma12_2 ( {acc_ma12_2} ) - acc_ma26_2 ( {acc_ma26_2} )")
acc_macd_3 = acc_ma12_3 - acc_ma26_3
print( f"macd_3 ( {acc_macd_3} ) =  acc_ma12_3 ( {acc_ma12_3} ) - acc_ma26_3 ( {acc_ma26_3} )")
acc_macd_4 = acc_ma12_4 - acc_ma26_4
print( f"macd_4 ( {acc_macd_4} ) =  acc_ma12_4 ( {acc_ma12_4} ) - acc_ma26_4 ( {acc_ma26_4} )")
acc_macd_5 = acc_ma12_5 - acc_ma26_5
print( f"macd_5 ( {acc_macd_5} ) =  acc_ma12_5 ( {acc_ma12_5} ) - acc_ma26_5 ( {acc_ma26_5} )")
acc_macd_6 = acc_ma12_6 - acc_ma26_6
print( f"macd_6 ( {acc_macd_6} ) =  acc_ma12_6 ( {acc_ma12_6} ) - acc_ma26_6 ( {acc_ma26_6} )")
acc_macd_7 = acc_ma12_7 - acc_ma26_7
print( f"macd_7 ( {acc_macd_7} ) =  acc_ma12_7 ( {acc_ma12_7} ) - acc_ma26_7 ( {acc_ma26_7} )")
acc_macd_8 = acc_ma12_8 - acc_ma26_8
print( f"macd_8 ( {acc_macd_8} ) =  acc_ma12_8 ( {acc_ma12_8} ) - acc_ma26_8 ( {acc_ma26_8} )")
acc_macd_9 = acc_ma12_9 - acc_ma26_9
print( f"macd_9 ( {acc_macd_9} ) =  acc_ma12_9 ( {acc_ma12_9} ) - acc_ma26_9 ( {acc_ma26_9} )")
print()

# signal = macd 9일선, 기준선 위치
acc_signal_1 = ( acc_macd_1 + acc_macd_2 + acc_macd_3 + acc_macd_4 + acc_macd_5 + acc_macd_6 + acc_macd_7 + acc_macd_8 + acc_macd_9 ) / 9
print(f"acc_signal_1 = ( {acc_signal_1} )")
print()

# 최종값
# 기준선과 오실레이터와의 간극. + 는 0 기준선 상승돌파, - 는 0 기준선 하락
acc_macd1 = acc_macd_1 - acc_signal_1
print(f"acc_macd1 ( {acc_macd1} ) = acc_macd_1 ( {acc_macd_1} ) - acc_signal_1 ( {acc_signal_1} )")
print()

##### macd 산출. 끝 #####
#####################################


#####################################
##### macd 매매선택              #####

# acc_macd_select
if acc_macd1 >= 0:
    if acc_macd_1 >= 0:
        # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 골든크로스
        acc_macd_select = 1
    else:
        # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 데드크로스
        acc_macd_select = 2
else:
    if acc_macd_1 >= 0:
        # acc_ma26_1이 기준선 아래에 있을때, acc_macd1이 골든크로스
        acc_macd_select = 3
    else:
        # acc_ma26_1이 기준선 아래에 있을때, acc_macd1이 데드크로스
        acc_macd_select = 4

print(f"acc_macd_select = {acc_macd_select}")
print()

time.sleep(1)



# macd 설정
if acc_macd_select == 1 or acc_macd_select == 3:    # 1, 3 은 골든크로스
    # 골든크로스
    btc_mode = 1
    print(f"btc_mode = 1 -> 골든크로스")
elif acc_macd_select == 2 or acc_macd_select == 4:  # 2, 4 는 데드크로스
    # 데드크로스
    btc_mode = -1
    print(f"btc_mode = -1 -> 데드크로스")


time.sleep(1)






################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

#################
# 선물 잔고 조회 #
#################

print("========== ========== ==========")
print("       선 물  잔 고  조 회")
print("========== ========== ==========")
print()

balance = binance.fetch_balance()
print("보유코인")
pprint.pprint(balance['total'])
pprint.pprint(balance['total']['USDT'])
pprint.pprint(balance['total']['BTC'])
print()

print("포지션")
positions = balance['info']['positions']
print()

for position in positions:
    if position['symbol'] == "BTCUSDT":
        pprint.pprint(position)

        btc_position_amt = float( position['positionAmt'] )
        print(f"현재 포지션은 ? {btc_position_amt}")




        if btc_position_amt > 0:
            print("1. 현재 롱포지션 진입상태")
            btc_position_1 = 1

        elif btc_position_amt == 0:
            print("2. 현재 포지션 진입을 안한상태")
            btc_position_1 = 0

        elif btc_position_amt < 0:
            print("3. 현재 숏포지션 진입상태")
            btc_position_1 = -1

        btc_future_leverage = int( position['leverage'] )



print()
print()






###################
# 선물 현재가 조회 #
###################
print("========== ========== ==========")
print("      선 물  현 재 가  조 회")
print("========== ========== ==========")
print()

btc = binance.fetch_ticker("BTC/USDT")
pprint.pprint( float( btc['last'] ) )
print(f"BTC/USDT 현재가 = {btc['last']}")
print()
print()



######################
# 거래가능한 USDT 갯수 #
######################
print("========== ========== ==========")
print("        거래가능한 BTC 갯수")
print("========== ========== ==========")
print()
balance = binance.fetch_balance()
usdt = float( balance['total']['USDT'] )
print(f"보유 USDT = {usdt}")

btc = binance.fetch_ticker(symbol = "BTC/USDT")
cur_price = float( btc['last'] )
amount_1 = cal_amount(usdt, cur_price)
print(f"보유 USDT로 BTC 거래가능한 갯수 = {amount_1}")
print()
print()






################
# 레버리지 설정 #
################
#markets = binance.load_markets()
#coin_1 = "BTC/USDT"
#market_1 = binance.market(coin_1)
# 레버리지 3배
#leverage_1 = 3

#resp_1 = binance.fapiPrivate_post_leverage({
#    'symbol': market_1['id'],
#    'leverage': leverage_1
#})

# 현재 레버리지 배율 10 배
#btc_leverage = 10  # 현재 레버리지 설정값
btc_leverage = btc_future_leverage  # 레버리지 가져옴

if btc_leverage > 1:   # 레버리지 비율이 1 초과면 
    btc_leverage_1 = btc_leverage - 1  # 진입시 사용할 레버리지 배율
elif btc_leverage <= 1:   # 레버리지 비율이 1 이하이면 
    btc_leverage_1 = btc_leverage   # 진입시 사용할 레버리지 배율


print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"0-1. 재시작시 포지션 유지중이면")
print()
print(f"0-2. 현재 macd 코드는? btc_mode = {btc_mode}")
print()
print(f"0-3. 현재 거래중인 코인갯수는? btc_position_amt = {btc_position_amt}")
print(f"0-3. 현재 거래중인 코인의 포지션 코드는? btc_position_1 = {btc_position_1}")

if btc_position_amt > 0:
    print("0-3-1. 현재 롱포지션 진입상태")
    btc_position_1 = 1

elif btc_position_amt == 0:
    print("0-3-2. 현재 포지션 진입을 안한상태")
    btc_position_1 = 0

elif btc_position_amt < 0:
    print("0-3-3. 현재 숏포지션 진입상태")
    btc_position_1 = -1

print()
print(f"0-4-1. 현재 설정된 레버리지 배율은 btc_leverage = {btc_leverage}")
print(f"0-4-2. 진입시 설정될 레버리지 배율은 btc_leverage_1 = {btc_leverage_1}")
print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")





################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################




print()
print("----- =====  거래 시작 ===== -----")
print()



























































































































































################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################



################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################


















################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

















while True:
    # 현재 시간 불러오기
    now = datetime.datetime.now()

    if now.hour == 1 or now.hour == 5 or now.hour == 9 or now.hour == 13 or now.hour == 17 or now.hour == 21:
        if now.minute == 0:
            time.sleep(5)

            print("")
            print("")
            print("-=-=-=-=-=- ********** -=-=-=-=-=- ********** -=-=-=-=-=-")
            print(f"[ 현재시간 : {now} ]   -   시작")
            print("-=-=-=-=-=- ********** -=-=-=-=-=- ********** -=-=-=-=-=-")
            print("")








            btc = exchange.fetch_ohlcv(
                symbol=symbol1,
                timeframe='4h', 
                since=None, 
                limit=50
            )

            df = pd.DataFrame(data = btc, columns = ['datetime', 'open', 'high', 'low', 'close', 'volume'])
            df['datetime'] = pd.to_datetime(df['datetime'], unit = 'ms')
            df.set_index('datetime', inplace = True)





            # 종가받기 40개
            print("========== 4시간봉 종가 받기 ==========")
            print()
            # 0은 아무것도 아님.
            price_0_close = df.iloc[0]['close']
            #price_0_time = df.iloc[0]['datetime']
            price_0_volume = df.iloc[0]['volume']
            price_0_total = price_0_close * price_0_volume
#            print(f"0. 현재가 = {price_0_close} USDT * 거래량 = {price_0_volume}  =  총액 = {price_0_total} USDT")

            # -1은 현재가.
            price_1_close = df.iloc[-1]['close']
            price_1_volume = df.iloc[-1]['volume']
            price_1_total = price_1_close * price_1_volume
#            print(f"1. 현재가 = {price_1_close} USDT * 거래량 = {price_1_volume}  =  총액 = {price_1_total} USDT")
#            print()

            ########################################
            # -2는 1시간전 종가. 여기부터 macd 계산.
            price_2_close = df.iloc[-2]['close']
            price_2_volume = df.iloc[-2]['volume']
            price_2_total = price_2_close * price_2_volume
#            print(f"2. 종가 = {price_2_close} USDT * 거래량 = {price_2_volume}  =  총액 = {price_2_total} USDT")
                
            price_3_close = df.iloc[-3]['close']
            price_3_volume = df.iloc[-3]['volume']
            price_3_total = price_3_close * price_3_volume
#            print(f"3. 종가 = {price_3_close} USDT * 거래량 = {price_3_volume}  =  총액 = {price_3_total} USDT")

            price_4_close = df.iloc[-4]['close']
            price_4_volume = df.iloc[-4]['volume']
            price_4_total = price_4_close * price_4_volume
#            print(f"4. 종가 = {price_4_close} USDT * 거래량 = {price_4_volume}  =  총액 = {price_4_total} USDT")

            price_5_close = df.iloc[-5]['close']
            price_5_volume = df.iloc[-5]['volume']
            price_5_total = price_5_close * price_5_volume
#            print(f"5. 종가 = {price_5_close} USDT * 거래량 = {price_5_volume}  =  총액 = {price_5_total} USDT")

            print()

            price_6_close = df.iloc[-6]['close']
            price_6_volume = df.iloc[-6]['volume']
            price_6_total = price_6_close * price_6_volume
#            print(f"6. 종가 = {price_6_close} USDT * 거래량 = {price_6_volume}  =  총액 = {price_6_total} USDT")

            price_7_close = df.iloc[-7]['close']
            price_7_volume = df.iloc[-7]['volume']
            price_7_total = price_7_close * price_7_volume
#            print(f"7. 종가 = {price_7_close} USDT * 거래량 = {price_7_volume}  =  총액 = {price_7_total} USDT")
                
            price_8_close = df.iloc[-8]['close']
            price_8_volume = df.iloc[-8]['volume']
            price_8_total = price_8_close * price_8_volume
#            print(f"8. 종가 = {price_8_close} USDT * 거래량 = {price_8_volume}  =  총액 = {price_8_total} USDT")

            price_9_close = df.iloc[-9]['close']
            price_9_volume = df.iloc[-9]['volume']
            price_9_total = price_9_close * price_9_volume
#            print(f"9. 종가 = {price_9_close} USDT * 거래량 = {price_9_volume}  =  총액 = {price_9_total} USDT")

            price_10_close = df.iloc[-10]['close']
            price_10_volume = df.iloc[-10]['volume']
            price_10_total = price_10_close * price_10_volume
#            print(f"10. 종가 = {price_10_close} USDT * 거래량 = {price_10_volume}  =  총액 = {price_10_total} USDT")

            print()

            price_11_close = df.iloc[-11]['close']
            price_11_volume = df.iloc[-11]['volume']
            price_11_total = price_11_close * price_11_volume
#            print(f"11. 종가 = {price_11_close} USDT * 거래량 = {price_11_volume}  =  총액 = {price_11_total} USDT")

            price_12_close = df.iloc[-12]['close']
            price_12_volume = df.iloc[-12]['volume']
            price_12_total = price_12_close * price_12_volume
#            print(f"12. 종가 = {price_12_close} USDT * 거래량 = {price_12_volume}  =  총액 = {price_12_total} USDT")

            price_13_close = df.iloc[-13]['close']
            price_13_volume = df.iloc[-13]['volume']
            price_13_total = price_13_close * price_13_volume
#            print(f"13. 종가 = {price_13_close} USDT * 거래량 = {price_13_volume}  =  총액 = {price_13_total} USDT")

            price_14_close = df.iloc[-14]['close']
            price_14_volume = df.iloc[-14]['volume']
            price_14_total = price_14_close * price_14_volume
#            print(f"14. 종가 = {price_14_close} USDT * 거래량 = {price_14_volume}  =  총액 = {price_14_total} USDT")

            price_15_close = df.iloc[-15]['close']
            price_15_volume = df.iloc[-15]['volume']
            price_15_total = price_15_close * price_15_volume
#            print(f"15. 종가 = {price_15_close} USDT * 거래량 = {price_15_volume}  =  총액 = {price_15_total} USDT")

            print()

            price_16_close = df.iloc[-16]['close']
            price_16_volume = df.iloc[-16]['volume']
            price_16_total = price_16_close * price_16_volume
#            print(f"16. 종가 = {price_16_close} USDT * 거래량 = {price_16_volume}  =  총액 = {price_16_total} USDT")

            price_17_close = df.iloc[-17]['close']
            price_17_volume = df.iloc[-17]['volume']
            price_17_total = price_17_close * price_17_volume
#            print(f"17. 종가 = {price_17_close} USDT * 거래량 = {price_17_volume}  =  총액 = {price_17_total} USDT")

            price_18_close = df.iloc[-18]['close']
            price_18_volume = df.iloc[-18]['volume']
            price_18_total = price_18_close * price_18_volume
#            print(f"18. 종가 = {price_18_close} USDT * 거래량 = {price_18_volume}  =  총액 = {price_18_total} USDT")

            price_19_close = df.iloc[-19]['close']
            price_19_volume = df.iloc[-19]['volume']
            price_19_total = price_19_close * price_19_volume
#            print(f"19. 종가 = {price_19_close} USDT * 거래량 = {price_19_volume}  =  총액 = {price_19_total} USDT")

            price_20_close = df.iloc[-20]['close']
            price_20_volume = df.iloc[-20]['volume']
            price_20_total = price_20_close * price_20_volume
#            print(f"20. 종가 = {price_20_close} USDT * 거래량 = {price_20_volume}  =  총액 = {price_20_total} USDT")

            print()

            price_21_close = df.iloc[-21]['close']
            price_21_volume = df.iloc[-21]['volume']
            price_21_total = price_21_close * price_21_volume
#            print(f"21. 종가 = {price_21_close} USDT * 거래량 = {price_21_volume}  =  총액 = {price_21_total} USDT")

            price_22_close = df.iloc[-22]['close']
            price_22_volume = df.iloc[-22]['volume']
            price_22_total = price_22_close * price_22_volume
#            print(f"22. 종가 = {price_22_close} USDT * 거래량 = {price_22_volume}  =  총액 = {price_22_total} USDT")

            price_23_close = df.iloc[-23]['close']
            price_23_volume = df.iloc[-23]['volume']
            price_23_total = price_23_close * price_23_volume
#            print(f"23. 종가 = {price_23_close} USDT * 거래량 = {price_23_volume}  =  총액 = {price_23_total} USDT")

            price_24_close = df.iloc[-24]['close']
            price_24_volume = df.iloc[-24]['volume']
            price_24_total = price_24_close * price_24_volume
#            print(f"24. 종가 = {price_24_close} USDT * 거래량 = {price_24_volume}  =  총액 = {price_24_total} USDT")

            price_25_close = df.iloc[-25]['close']
            price_25_volume = df.iloc[-25]['volume']
            price_25_total = price_25_close * price_25_volume
#            print(f"25. 종가 = {price_25_close} USDT * 거래량 = {price_25_volume}  =  총액 = {price_25_total} USDT")

            print()

            price_26_close = df.iloc[-26]['close']
            price_26_volume = df.iloc[-26]['volume']
            price_26_total = price_26_close * price_26_volume
#            print(f"26. 종가 = {price_26_close} USDT * 거래량 = {price_26_volume}  =  총액 = {price_26_total} USDT")

            price_27_close = df.iloc[-27]['close']
            price_27_volume = df.iloc[-27]['volume']
            price_27_total = price_27_close * price_27_volume
#            print(f"27. 종가 = {price_27_close} USDT * 거래량 = {price_27_volume}  =  총액 = {price_27_total} USDT")

            price_28_close = df.iloc[-28]['close']
            price_28_volume = df.iloc[-28]['volume']
            price_28_total = price_28_close * price_28_volume
#            print(f"28. 종가 = {price_28_close} USDT * 거래량 = {price_28_volume}  =  총액 = {price_28_total} USDT")

            price_29_close = df.iloc[-29]['close']
            price_29_volume = df.iloc[-29]['volume']
            price_29_total = price_29_close * price_29_volume
#            print(f"29. 종가 = {price_29_close} USDT * 거래량 = {price_29_volume}  =  총액 = {price_29_total} USDT")

            price_30_close = df.iloc[-30]['close']
            price_30_volume = df.iloc[-30]['volume']
            price_30_total = price_30_close * price_30_volume
#            print(f"30. 종가 = {price_30_close} USDT * 거래량 = {price_30_volume}  =  총액 = {price_30_total} USDT")

            print()

            price_31_close = df.iloc[-31]['close']
            price_31_volume = df.iloc[-31]['volume']
            price_31_total = price_31_close * price_31_volume
#            print(f"31. 종가 = {price_31_close} USDT * 거래량 = {price_31_volume}  =  총액 = {price_31_total} USDT")

            price_32_close = df.iloc[-32]['close']
            price_32_volume = df.iloc[-32]['volume']
            price_32_total = price_32_close * price_32_volume
#            print(f"32. 종가 = {price_32_close} USDT * 거래량 = {price_32_volume}  =  총액 = {price_32_total} USDT")

            price_33_close = df.iloc[-33]['close']
            price_33_volume = df.iloc[-33]['volume']
            price_33_total = price_33_close * price_33_volume
#            print(f"33. 종가 = {price_33_close} USDT * 거래량 = {price_33_volume}  =  총액 = {price_33_total} USDT")

            price_34_close = df.iloc[-34]['close']
            price_34_volume = df.iloc[-34]['volume']
            price_34_total = price_34_close * price_34_volume
#            print(f"34. 종가 = {price_34_close} USDT * 거래량 = {price_34_volume}  =  총액 = {price_34_total} USDT")

            price_35_close = df.iloc[-35]['close']
            price_35_volume = df.iloc[-35]['volume']
            price_35_total = price_35_close * price_35_volume
#            print(f"35. 종가 = {price_35_close} USDT * 거래량 = {price_35_volume}  =  총액 = {price_35_total} USDT")
                
            print()







            print("========== MACD 계산 ==========")
            print()




            # 단기 12이평선
            acc_ma12_1_1 = price_2_close + price_3_close + price_4_close + price_5_close + price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close
            acc_ma12_1 = acc_ma12_1_1 / 12

            acc_ma12_2_1 = price_3_close + price_4_close + price_5_close + price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close
            acc_ma12_2 = acc_ma12_2_1 / 12

            acc_ma12_3_1 = price_4_close + price_5_close + price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close
            acc_ma12_3 = acc_ma12_3_1 / 12
                
            acc_ma12_4_1 = price_5_close + price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close
            acc_ma12_4 = acc_ma12_4_1 / 12
                
            acc_ma12_5_1 = price_6_close + price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close
            acc_ma12_5 = acc_ma12_5_1 / 12
                
            acc_ma12_6_1 = price_7_close + price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close
            acc_ma12_6 = acc_ma12_6_1 / 12
                
            acc_ma12_7_1 = price_8_close + price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close
            acc_ma12_7 = acc_ma12_7_1 / 12
                
            acc_ma12_8_1 = price_9_close + price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close
            acc_ma12_8 = acc_ma12_8_1 / 12
                
            acc_ma12_9_1 = price_10_close + price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close
            acc_ma12_9 = acc_ma12_9_1 / 12

            # 여기까지


            # 장기 26이평선
            acc_ma26_1_1 = acc_ma12_1_1  +  price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close
            acc_ma26_1 = acc_ma26_1_1 / 26

            acc_ma26_2_1 = acc_ma12_2_1  +  price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close
            acc_ma26_2 = acc_ma26_2_1 / 26

            acc_ma26_3_1 = acc_ma12_3_1  +  price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close
            acc_ma26_3 = acc_ma26_3_1 / 26

            acc_ma26_4_1 = acc_ma12_4_1  +  price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close
            acc_ma26_4 = acc_ma26_4_1 / 26

            acc_ma26_5_1 = acc_ma12_5_1  +  price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close
            acc_ma26_5 = acc_ma26_5_1 / 26

            acc_ma26_6_1 = acc_ma12_6_1  +  price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close
            acc_ma26_6 = acc_ma26_6_1 / 26

            acc_ma26_7_1 = acc_ma12_7_1  +  price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close
            acc_ma26_7 = acc_ma26_7_1 / 26

            acc_ma26_8_1 = acc_ma12_8_1  +  price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close
            acc_ma26_8 = acc_ma26_8_1 / 26

            acc_ma26_9_1 = acc_ma12_9_1  +  price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close
            acc_ma26_9 = acc_ma26_9_1 / 26

            # 여기까지


            # macd
            # 단기12일이평선 - 장기26일이평선 = + 는 골든크로스, - 는 데드크로스
            # + 는 골드크로스, - 는 데드크로스
            acc_macd_1 = acc_ma12_1 - acc_ma26_1
            print( f"macd_1 ( {acc_macd_1} ) =  acc_ma12_1 ( {acc_ma12_1} ) - acc_ma26_1 ( {acc_ma26_1} )")
            print()
            acc_macd_2 = acc_ma12_2 - acc_ma26_2
            print( f"macd_2 ( {acc_macd_2} ) =  acc_ma12_2 ( {acc_ma12_2} ) - acc_ma26_2 ( {acc_ma26_2} )")
            acc_macd_3 = acc_ma12_3 - acc_ma26_3
            print( f"macd_3 ( {acc_macd_3} ) =  acc_ma12_3 ( {acc_ma12_3} ) - acc_ma26_3 ( {acc_ma26_3} )")
            acc_macd_4 = acc_ma12_4 - acc_ma26_4
            print( f"macd_4 ( {acc_macd_4} ) =  acc_ma12_4 ( {acc_ma12_4} ) - acc_ma26_4 ( {acc_ma26_4} )")
            acc_macd_5 = acc_ma12_5 - acc_ma26_5
            print( f"macd_5 ( {acc_macd_5} ) =  acc_ma12_5 ( {acc_ma12_5} ) - acc_ma26_5 ( {acc_ma26_5} )")
            acc_macd_6 = acc_ma12_6 - acc_ma26_6
            print( f"macd_6 ( {acc_macd_6} ) =  acc_ma12_6 ( {acc_ma12_6} ) - acc_ma26_6 ( {acc_ma26_6} )")
            acc_macd_7 = acc_ma12_7 - acc_ma26_7
            print( f"macd_7 ( {acc_macd_7} ) =  acc_ma12_7 ( {acc_ma12_7} ) - acc_ma26_7 ( {acc_ma26_7} )")
            acc_macd_8 = acc_ma12_8 - acc_ma26_8
            print( f"macd_8 ( {acc_macd_8} ) =  acc_ma12_8 ( {acc_ma12_8} ) - acc_ma26_8 ( {acc_ma26_8} )")
            acc_macd_9 = acc_ma12_9 - acc_ma26_9
            print( f"macd_9 ( {acc_macd_9} ) =  acc_ma12_9 ( {acc_ma12_9} ) - acc_ma26_9 ( {acc_ma26_9} )")
            print()

            # signal = macd 9일선, 기준선 위치
            acc_signal_1 = ( acc_macd_1 + acc_macd_2 + acc_macd_3 + acc_macd_4 + acc_macd_5 + acc_macd_6 + acc_macd_7 + acc_macd_8 + acc_macd_9 ) / 9


            # 최종값
            # 기준선과 오실레이터와의 간극. + 는 0 기준선 상승돌파, - 는 0 기준선 하락
            acc_macd1 = acc_macd_1 - acc_signal_1

            print()
            print()


            ##### macd 산출. 끝 #####
            #####################################


            #####################################
            ##### macd 매매선택              #####

            # acc_macd_select
            if acc_macd1 >= 0:
                if acc_macd_1 >= 0:
                    # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 골든크로스
                    acc_macd_select = 1
                else:
                    # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 데드크로스
                    acc_macd_select = 2
            else:
                if acc_macd_1 >= 0:
                    # acc_ma26_1이 기준선 아래에 있을때, acc_macd1이 골든크로스
                    acc_macd_select = 3
                else:
                    # acc_ma26_1이 기준선 아래에 있을때, acc_macd1이 데드크로스
                    acc_macd_select = 4

            print(f"acc_macd_select = {acc_macd_select}")


            # macd 설정
            if acc_macd_select == 1 or acc_macd_select == 3:    # 1, 3 은 골든크로스
                # 골든크로스
                now_macd = 1
                print(f"btc_mode = 1 -> 골든크로스")
            elif acc_macd_select == 2 or acc_macd_select == 4:  # 2, 4 는 데드크로스
                # 데드크로스
                now_macd = -1
                print(f"btc_mode = -1 -> 데드크로스")

            time.sleep(1)






            ################
            # 레버리지 설정 #
            ################
#            markets = binance.load_markets()
#            coin_1 = "BTC/USDT"
#            market_1 = binance.market(coin_1)
            # 레버리지 3배
#            leverage_1 = 3

#            resp_1 = binance.fapiPrivate_post_leverage({
#                'symbol': market_1['id'],
#                'leverage': leverage_1
#            })





            #################
            # 선물 잔고 조회 #
            #################
            print("========== ========== ==========")
            print("       선 물  잔 고  조 회")
            print("========== ========== ==========")
            print()

            balance = binance.fetch_balance()
            print("보유코인")
            pprint.pprint(balance['total'])
            #pprint.pprint(balance['total']['USDT'])
            #pprint.pprint(balance['total']['BTC'])
            print("포지션")
            positions = balance['info']['positions']

            for position in positions:
                if position['symbol'] == "BTCUSDT":
                    pprint.pprint(position)

                    btc_position_amt = float( position['positionAmt'] )
                    print(f"현재 포지션은 ? {btc_position_amt}")


                    if btc_position_amt > 0:
                        print("1. 현재 롱포지션 진입상태")
                        btc_position_1 = 1

                    elif btc_position_amt == 0:
                        print("2. 현재 포지션 진입을 안한상태")
                        btc_position_1 = 0

                    elif btc_position_amt < 0:
                        print("3. 현재 숏포지션 진입상태")
                        btc_position_1 = -1
                    
                    # 레버리지 값 가져옴
                    btc_future_leverage = int( position['leverage'] )

                    if btc_leverage > 1:   # 레버리지 비율이 1 초과면 
                        btc_leverage_1 = btc_leverage - 1  # 진입시 사용할 레버리지 배율
                    elif btc_leverage <= 1:   # 레버리지 비율이 1 이하이면 
                        btc_leverage_1 = btc_leverage   # 진입시 사용할 레버리지 배율

                        

            print(f"현재 내 포지션 코드는? btc_position = {btc_position_1}")
            print()


            print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print(f"1-1. 현재시간 포지션 유지중이면")
            print(f"     값.")
            print(f"1-2-1. 이전 macd 코드는? btc_mode = {btc_mode}")
            print(f"1-2-2. 현재 macd 코드는? btc_macd = {now_macd}")
            print()
            print(f"1-3. 현재 거래중인 코인갯수는? btc_position_amt = {btc_position_amt}")
            print(f"1-3. 현재 거래중인 코인의 포지션 코드는? btc_position_1 = {btc_position_1}")

            if btc_position_amt > 0:
                print("0-3-1. 현재 롱포지션 진입상태")
                btc_position_1 = 1

            elif btc_position_amt == 0:
                print("0-3-2. 현재 포지션 진입을 안한상태")
                btc_position_1 = 0

            elif btc_position_amt < 0:
                print("0-3-3. 현재 숏포지션 진입상태")
                btc_position_1 = -1
            print()
            print(f"1-4-1. 현재 설정된 레버리지 배율은 btc_leverage = {btc_leverage}")
            print(f"1-4-2. 진입시 설정될 레버리지 배율은 btc_leverage_1 = {btc_leverage_1}")
            print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print()
            print()

            time.sleep(1)

            



            ###################
            # 선물 현재가 조회 #
            ###################
#            print("========== ========== ==========")
#            print("      선 물  현 재 가  조 회")
#            print("========== ========== ==========")
#            print()

#            btc = binance.fetch_ticker("BTC/USDT")
            #pprint.pprint(btc['last'])
#            print(f"BTC/USDT 현재가 = { float( btc['last'] ) }")
#            print()
#            print()



            ######################
            # 거래가능한 USDT 갯수 #
            ######################
#            print("========== ========== ==========")
#            print("        거래가능한 BTC 갯수")
#            print("========== ========== ==========")
#            print()
#            balance = binance.fetch_balance()
#            usdt = balance['total']['USDT']
#            print(f"보유 USDT = { float( usdt )}")

#            btc = binance.fetch_ticker(symbol = "BTC/USDT")
#            cur_price = float( btc['last'] )
            #amount_1 = cal_amount(usdt, cur_price)
#            amount_1 = amount_2
#            amount_1_1 = amount_1 * btc_leverage_1
            # 코인 진입시 사용하는 코인 갯수 저장하는 변수
            #amount_2 = 0
#            print(f"보유 USDT로 BTC 거래가능한 갯수 = {amount_1}")
#            print()
#            print()





            
            
                
            
                

            # macd 조건문
            if btc_mode == 1:   # 이전 macd코드가 1은 골든크로스
                if now_macd == 1:    # 현재 macd코드가 1은 골든크로스
                    print("골든크로스 -> 골든크로스")
                elif now_macd == -1:  # 현재 macd코드가 -1은 데드크로스
                    print("골든크로스 -> 데드크로스")
                    # 포지션 정리
                    print("1-1. 롱 포지션 정리")
                    print(f"1-2. 롱 포지션 정리할 코인 갯수 = {btc_position_amt}")
                    print(f"1-3. 포지션 코드 = {btc_position_1}")

                    if btc_position_1 == 1:   # 롱 포지션 정리
                        if btc_position_amt != 0:
                            order = binance.create_market_sell_order(symbol = "BTC/USDT", amount = btc_position_amt)

                            print("1-3. 롱 포지션 정리완료")

                            time.sleep(1)
                        
                            # 무 포지션으로 코드 변경
                            btc_position_1 = 0
                            print(f"1-4. btc_position_1 = {btc_position_1} 무 포지션으로 변경")
                    
                    # 숏 포지션 진입
                    if btc_position_1 == 0:   # 무 포지션 상태
                        balance = binance.fetch_balance()
                        usdt = float( balance['total']['USDT'] )
                        print(f"2-1. 보유 USDT = { usdt }")

                        btc = binance.fetch_ticker(symbol = "BTC/USDT")
                        cur_price = float( btc['last'] )
                        amount_1 = float( cal_amount(usdt, cur_price) )
                        #amount_1 = amount_2
                        amount_1_1 = amount_1 * btc_leverage_1
                        # btc_leverage_1 진입 레버리지 배율
                        
                        print("2-2. 숏 포지션 진입")
                        print(f"2-3. 숏 포지션 진입할 코인 갯수 = {amount_1_1}")
                        order = binance.create_market_sell_order(symbol = "BTC/USDT", amount = amount_1_1)
                        print("2-4. 숏 포지션 진입완료")

                        # 숏 포지션 진입시 들어간 코인 갯수
                        #amount_2 = amount_1_1
                        print(f"2-5. 진입코인갯수 저장 btc_position_amt = {amount_1_1}")

                        time.sleep(1)

                    # macd 코드 변경 - 이전 macd 인 btc_mode 에 입력
                    btc_mode = -1
                    print(f"1, 2. 거래후 btc_macd = -1 -> 데드크로스")
                    # 포지션 숏으로 코드 변경
                    btc_position_1 = -1
                    print(f"1, 2. 거래후 btc_position_1 = -1 -> 숏 포지션")
            elif btc_mode == -1:    # 이전 macd코드가 -1은 데드크로스
                if now_macd == 1:    # 현재 macd코드가 1은 골든크로스
                    print("데드크로스 -> 골든크로스")
                    # 포지션 정리
                    print("3-1. 숏 포지션 정리")
                    print(f"3-2. 숏 포지션 정리할 코인 갯수 = {btc_position_amt}")
                    print(f"3-3. 포지션 코드 = {btc_position_1}")

                    if btc_position_1 == -1:   # 숏 포지션 정리
                        if btc_position_amt != 0:
                            print("3-3-0. 숏 포지션 정리하기 전 테스트용")
                            order = binance.create_market_buy_order(symbol = "BTC/USDT", amount = btc_position_amt)

                            print("3-3. 숏 포지션 정리완료")

                            time.sleep(1)
                        
                        # 무 포지션으로 코드 변경
                        btc_position_1 = 0
                        print(f"3-4. btc_position = {btc_position_1} 무 포지션으로 변경")
                        
                    
                    # 롱 포지션 진입
                    if btc_position_1 == 0:   # 무 포지션 상태
                        balance = binance.fetch_balance()
                        usdt = float( balance['total']['USDT'] )
                        print(f"4-1. 보유 USDT = { usdt }")

                        btc = binance.fetch_ticker(symbol = "BTC/USDT")
                        cur_price = float( btc['last'] )
                        amount_1 = float( cal_amount(usdt, cur_price) )
                        amount_1_1 = amount_1 * btc_leverage_1
                        # amount_2_2 진입 레버리지 배율
                        
                        print("4-2. 롱 포지션 진입")
                        print(f"4-3. 롱 포지션 진입할 코인 갯수 = {amount_1_1}")
                        order = binance.create_market_buy_order(symbol = "BTC/USDT", amount = amount_1_1)
                        print("4-4. 롱 포지션 진입완료")


                        # 숏 포지션 진입시 들어간 코인 갯수
                        #amount_2 = amount_1_1
                        print(f"4-5. 진입코인갯수 저장 btc_position_amt = {amount_1_1}")

                        time.sleep(1)
                    
                    # macd 코드 변경
                    btc_mode = 1
                    print(f"3, 4. 거래후 btc_macd = 1 -> 골든크로스")
                    # 포지션 롱으로 코드 변경
                    btc_position_1 = 1
                    print(f"3, 4. 거래후 btc_position = 1 -> 롱 포지션")
                elif now_macd == -1:  # 현재 macd코드가 -1은 데드크로스
                    print("데드크로스 -> 데드크로스")

                

            ######################
            # 매수/롱 포지션 진입 #
            ######################
            #order = binance.creat_market_buy_order(symbol = "BTC/USDT", amount = amount_1)


            ######################
            # 매수/롱 포지션 정리 #
            ######################
            #order = binance.creat_market_sell_order(symbol = "BTC/USDT", amount = amount_1)

            ################################################################################################################################################################

            # 재시작시 매매중인 코인을 재설정하였습니다.
            # 재조정이 필요하면 3440번째 줄을 보면 됩니다.

            ################################################################################################################################################################


            print("")
            print("-=-=-=-=-=- ********** -=-=-=-=-=- ********** -=-=-=-=-=-")
            print(f"[ 현재시간 : {now} ]   -   종료")
            print("-=-=-=-=-=- ********** -=-=-=-=-=- ********** -=-=-=-=-=-")
            print("")
            print("")



            # 60초 딜레이.
            time.sleep(60)


            