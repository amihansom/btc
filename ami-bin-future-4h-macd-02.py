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
        limit = 100
    )

    df = pd.DataFrame( data = btc, columns = [ 'datetime', 'open', 'high', 'low', 'close', 'volume' ] )
    df[ 'datetime' ] = pd.to_datetime( df[ 'datetime' ], unit = 'ms' )
    df.set_index( 'datetime', inplace = True )

    print( df )
    print()


    # 종가받기 90개
    print("========== 4시간봉 종가 받기 ==========")
    print()
    # 0은 아무것도 아님.
    price_0_close = df.iloc[0]['close']
    #price_0_time = df.iloc[0]['datetime']

    # -1은 현재가.
    price_1_close = df.iloc[-1]['close']

    ########################################
    # -2는 1시간전 종가. 여기부터 macd 계산.
    price_2_close = df.iloc[-2]['close']
    price_3_close = df.iloc[-3]['close']
    price_4_close = df.iloc[-4]['close']
    price_5_close = df.iloc[-5]['close']
    price_6_close = df.iloc[-6]['close']
    price_7_close = df.iloc[-7]['close']
    price_8_close = df.iloc[-8]['close']
    price_9_close = df.iloc[-9]['close']
    price_10_close = df.iloc[-10]['close']

    price_11_close = df.iloc[-11]['close']
    price_12_close = df.iloc[-12]['close']
    price_13_close = df.iloc[-13]['close']
    price_14_close = df.iloc[-14]['close']
    price_15_close = df.iloc[-15]['close']
    price_16_close = df.iloc[-16]['close']
    price_17_close = df.iloc[-17]['close']
    price_18_close = df.iloc[-18]['close']
    price_19_close = df.iloc[-19]['close']
    price_20_close = df.iloc[-20]['close']
    price_21_close = df.iloc[-21]['close']
    price_22_close = df.iloc[-22]['close']
    price_23_close = df.iloc[-23]['close']
    price_24_close = df.iloc[-24]['close']
    price_25_close = df.iloc[-25]['close']
    price_26_close = df.iloc[-26]['close']
    price_27_close = df.iloc[-27]['close']
    price_28_close = df.iloc[-28]['close']
    price_29_close = df.iloc[-29]['close']
    price_30_close = df.iloc[-30]['close']

    price_31_close = df.iloc[-31]['close']
    price_32_close = df.iloc[-32]['close']
    price_33_close = df.iloc[-33]['close']
    price_34_close = df.iloc[-34]['close']
    price_35_close = df.iloc[-35]['close']
    price_36_close = df.iloc[-36]['close']
    price_37_close = df.iloc[-37]['close']
    price_38_close = df.iloc[-38]['close']
    price_39_close = df.iloc[-39]['close']
    price_40_close = df.iloc[-40]['close']

    price_41_close = df.iloc[-41]['close']
    price_42_close = df.iloc[-42]['close']
    price_43_close = df.iloc[-43]['close']
    price_44_close = df.iloc[-44]['close']
    price_45_close = df.iloc[-45]['close']
    price_46_close = df.iloc[-46]['close']
    price_47_close = df.iloc[-47]['close']
    price_48_close = df.iloc[-48]['close']
    price_49_close = df.iloc[-49]['close']
    price_50_close = df.iloc[-50]['close']

    price_51_close = df.iloc[-51]['close']
    price_52_close = df.iloc[-52]['close']
    price_53_close = df.iloc[-53]['close']
    price_54_close = df.iloc[-54]['close']
    price_55_close = df.iloc[-55]['close']
    price_56_close = df.iloc[-56]['close']
    price_57_close = df.iloc[-57]['close']
    price_58_close = df.iloc[-58]['close']
    price_59_close = df.iloc[-59]['close']
    price_60_close = df.iloc[-60]['close']

    price_61_close = df.iloc[-61]['close']
    price_62_close = df.iloc[-62]['close']
    price_63_close = df.iloc[-63]['close']
    price_64_close = df.iloc[-64]['close']
    price_65_close = df.iloc[-65]['close']
    price_66_close = df.iloc[-66]['close']
    price_67_close = df.iloc[-67]['close']
    price_68_close = df.iloc[-68]['close']
    price_69_close = df.iloc[-69]['close']
    price_70_close = df.iloc[-70]['close']

    price_71_close = df.iloc[-71]['close']
    price_72_close = df.iloc[-72]['close']
    price_73_close = df.iloc[-73]['close']
    price_74_close = df.iloc[-74]['close']
    price_75_close = df.iloc[-75]['close']
    price_76_close = df.iloc[-76]['close']
    price_77_close = df.iloc[-77]['close']
    price_78_close = df.iloc[-78]['close']
    price_79_close = df.iloc[-79]['close']
    price_80_close = df.iloc[-80]['close']

    price_81_close = df.iloc[-81]['close']
    price_82_close = df.iloc[-82]['close']












        

    # 단기 12 평활상수
    ma12_sc = 2 / ( 1 + 12 )


    # EMA - 단기 12 지수 종가 계산
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

    acc_ma12_10_1 = price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close
    acc_ma12_10 = acc_ma12_10_1 / 12

    acc_ma12_11_1 = price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close
    acc_ma12_11 = acc_ma12_11_1 / 12

    acc_ma12_12_1 = price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close
    acc_ma12_12 = acc_ma12_12_1 / 12

    acc_ma12_13_1 = price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close
    acc_ma12_13 = acc_ma12_13_1 / 12

    acc_ma12_14_1 = price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close
    acc_ma12_14 = acc_ma12_14_1 / 12

    acc_ma12_15_1 = price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close
    acc_ma12_15 = acc_ma12_15_1 / 12

    acc_ma12_16_1 = price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close
    acc_ma12_16 = acc_ma12_16_1 / 12

    acc_ma12_17_1 = price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close
    acc_ma12_17 = acc_ma12_17_1 / 12

    acc_ma12_18_1 = price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close
    acc_ma12_18 = acc_ma12_18_1 / 12

    acc_ma12_19_1 = price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close
    acc_ma12_19 = acc_ma12_19_1 / 12

    acc_ma12_20_1 = price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close
    acc_ma12_20 = acc_ma12_20_1 / 12

    acc_ma12_21_1 = price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close
    acc_ma12_21 = acc_ma12_21_1 / 12

    acc_ma12_22_1 = price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close
    acc_ma12_22 = acc_ma12_22_1 / 12

    acc_ma12_23_1 = price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close
    acc_ma12_23 = acc_ma12_23_1 / 12

    acc_ma12_24_1 = price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close
    acc_ma12_24 = acc_ma12_24_1 / 12

    acc_ma12_25_1 = price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close
    acc_ma12_25 = acc_ma12_25_1 / 12

    acc_ma12_26_1 = price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close
    acc_ma12_26 = acc_ma12_26_1 / 12

    acc_ma12_27_1 = price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close
    acc_ma12_27 = acc_ma12_27_1 / 12

    acc_ma12_28_1 = price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close
    acc_ma12_28 = acc_ma12_28_1 / 12

    acc_ma12_29_1 = price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close
    acc_ma12_30_1 = price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close
    acc_ma12_31_1 = price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close
    acc_ma12_32_1 = price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close
    acc_ma12_33_1 = price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close
    acc_ma12_34_1 = price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close
    acc_ma12_35_1 = price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close
    acc_ma12_36_1 = price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close
    acc_ma12_37_1 = price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close
    acc_ma12_38_1 = price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close
    acc_ma12_39_1 = price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close
    acc_ma12_40_1 = price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close
    acc_ma12_41_1 = price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close
    acc_ma12_42_1 = price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close
    acc_ma12_43_1 = price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close
    acc_ma12_44_1 = price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close
    acc_ma12_45_1 = price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close
    acc_ma12_46_1 = price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close
    acc_ma12_47_1 = price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close
    acc_ma12_48_1 = price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close
    acc_ma12_49_1 = price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close
    acc_ma12_50_1 = price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close
    acc_ma12_51_1 = price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close
    acc_ma12_52_1 = price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close
    acc_ma12_53_1 = price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close
    acc_ma12_54_1 = price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close
    acc_ma12_55_1 = price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close
    acc_ma12_56_1 = price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close


    # EMA - 단기 12 지수이동평균값 구하기
    acc_e_ma12_27 = acc_ma12_28
    acc_e_ma12_26 = ( price_27_close * ma12_sc )  + ( acc_e_ma12_27 * ( 1 - ma12_sc ) )
    acc_e_ma12_25 = ( price_26_close * ma12_sc )  + ( acc_e_ma12_26 * ( 1 - ma12_sc ) )

    acc_e_ma12_24 = ( price_25_close * ma12_sc )  + ( acc_e_ma12_25 * ( 1 - ma12_sc ) )
    acc_e_ma12_23 = ( price_24_close * ma12_sc )  + ( acc_e_ma12_24 * ( 1 - ma12_sc ) )
    acc_e_ma12_22 = ( price_23_close * ma12_sc )  + ( acc_e_ma12_23 * ( 1 - ma12_sc ) )
    acc_e_ma12_21 = ( price_22_close * ma12_sc )  + ( acc_e_ma12_22 * ( 1 - ma12_sc ) )
    acc_e_ma12_20 = ( price_21_close * ma12_sc )  + ( acc_e_ma12_21 * ( 1 - ma12_sc ) )
    acc_e_ma12_19 = ( price_20_close * ma12_sc )  + ( acc_e_ma12_20 * ( 1 - ma12_sc ) )
    acc_e_ma12_18 = ( price_19_close * ma12_sc )  + ( acc_e_ma12_19 * ( 1 - ma12_sc ) )
    acc_e_ma12_17 = ( price_18_close * ma12_sc )  + ( acc_e_ma12_18 * ( 1 - ma12_sc ) )
    acc_e_ma12_16 = ( price_17_close * ma12_sc )  + ( acc_e_ma12_17 * ( 1 - ma12_sc ) )
    acc_e_ma12_15 = ( price_16_close * ma12_sc )  + ( acc_e_ma12_16 * ( 1 - ma12_sc ) )
    acc_e_ma12_14 = ( price_15_close * ma12_sc )  + ( acc_e_ma12_15 * ( 1 - ma12_sc ) )
    acc_e_ma12_13 = ( price_14_close * ma12_sc )  + ( acc_e_ma12_14 * ( 1 - ma12_sc ) )

    acc_e_ma12_12 = ( price_13_close * ma12_sc )  + ( acc_e_ma12_13 * ( 1 - ma12_sc ) )
    acc_e_ma12_11 = ( price_12_close * ma12_sc )  + ( acc_e_ma12_12 * ( 1 - ma12_sc ) )
    acc_e_ma12_10 = ( price_11_close * ma12_sc )  + ( acc_e_ma12_11 * ( 1 - ma12_sc ) )
    acc_e_ma12_9 = ( price_10_close * ma12_sc )  + ( acc_e_ma12_10 * ( 1 - ma12_sc ) )
    acc_e_ma12_8 = ( price_9_close * ma12_sc )  + ( acc_e_ma12_9 * ( 1 - ma12_sc ) )
    acc_e_ma12_7 = ( price_8_close * ma12_sc )  + ( acc_e_ma12_8 * ( 1 - ma12_sc ) )
    acc_e_ma12_6 = ( price_7_close * ma12_sc )  + ( acc_e_ma12_7 * ( 1 - ma12_sc ) )
    acc_e_ma12_5 = ( price_6_close * ma12_sc )  + ( acc_e_ma12_6 * ( 1 - ma12_sc ) )
    acc_e_ma12_4 = ( price_5_close * ma12_sc )  + ( acc_e_ma12_5 * ( 1 - ma12_sc ) )
    acc_e_ma12_3 = ( price_4_close * ma12_sc )  + ( acc_e_ma12_4 * ( 1 - ma12_sc ) )
    acc_e_ma12_2 = ( price_3_close * ma12_sc )  + ( acc_e_ma12_3 * ( 1 - ma12_sc ) )
    acc_e_ma12_1 = ( price_2_close * ma12_sc )  + ( acc_e_ma12_2 * ( 1 - ma12_sc ) )



    # 여기까지






    # 장기 26 평활상수
    ma26_sc = 2 / ( 1 + 26 )


    # EMA - 장기 26 지수 종가 계산
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

    acc_ma26_10_1 = acc_ma12_10_1  +  price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close
    acc_ma26_10 = acc_ma26_10_1 / 26

    acc_ma26_11_1 = acc_ma12_11_1  +  price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close
    acc_ma26_11 = acc_ma26_11_1 / 26

    acc_ma26_12_1 = acc_ma12_12_1  +  price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close
    acc_ma26_12 = acc_ma26_12_1 / 26

    acc_ma26_13_1 = acc_ma12_13_1  +  price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close
    acc_ma26_13 = acc_ma26_13_1 / 26

    acc_ma26_14_1 = acc_ma12_14_1  +  price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close
    acc_ma26_14 = acc_ma26_14_1 / 26

    acc_ma26_15_1 = acc_ma12_15_1  +  price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close
    acc_ma26_15 = acc_ma26_15_1 / 26

    acc_ma26_16_1 = acc_ma12_16_1  +  price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close
    acc_ma26_16 = acc_ma26_16_1 / 26

    acc_ma26_17_1 = acc_ma12_17_1  +  price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close
    acc_ma26_17 = acc_ma26_17_1 / 26

    acc_ma26_18_1 = acc_ma12_18_1  +  price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close
    acc_ma26_18 = acc_ma26_18_1 / 26

    acc_ma26_19_1 = acc_ma12_19_1  +  price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close
    acc_ma26_19 = acc_ma26_19_1 / 26

    acc_ma26_20_1 = acc_ma12_20_1  +  price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close
    acc_ma26_20 = acc_ma26_20_1 / 26

    acc_ma26_21_1 = acc_ma12_21_1  +  price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close
    acc_ma26_21 = acc_ma26_21_1 / 26

    acc_ma26_22_1 = acc_ma12_22_1  +  price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close
    acc_ma26_22 = acc_ma26_22_1 / 26

    acc_ma26_23_1 = acc_ma12_23_1  +  price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close
    acc_ma26_23 = acc_ma26_23_1 / 26

    acc_ma26_24_1 = acc_ma12_24_1  +  price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close
    acc_ma26_24 = acc_ma26_24_1 / 26

    acc_ma26_25_1 = acc_ma12_25_1  +  price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close
    acc_ma26_25 = acc_ma26_25_1 / 26

    acc_ma26_26_1 = acc_ma12_26_1  +  price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close
    acc_ma26_26 = acc_ma26_26_1 / 26

    acc_ma26_27_1 = acc_ma12_27_1  +  price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close
    acc_ma26_27 = acc_ma26_27_1 / 26

    acc_ma26_28_1 = acc_ma12_28_1  +  price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close
    acc_ma26_28 = acc_ma26_28_1 / 26

    acc_ma26_29_1 = acc_ma12_29_1  +  price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close
    acc_ma26_29 = acc_ma26_29_1 / 26

    acc_ma26_30_1 = acc_ma12_30_1  +  price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close
    acc_ma26_30 = acc_ma26_30_1 / 26

    acc_ma26_31_1 = acc_ma12_31_1  +  price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close
    acc_ma26_31 = acc_ma26_31_1 / 26

    acc_ma26_32_1 = acc_ma12_32_1  +  price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close
    acc_ma26_32 = acc_ma26_32_1 / 26

    acc_ma26_33_1 = acc_ma12_33_1  +  price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close
    acc_ma26_33 = acc_ma26_33_1 / 26

    acc_ma26_34_1 = acc_ma12_34_1  +  price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close
    acc_ma26_34 = acc_ma26_34_1 / 26

    acc_ma26_35_1 = acc_ma12_35_1  +  price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close
    acc_ma26_35 = acc_ma26_35_1 / 26

    acc_ma26_36_1 = acc_ma12_36_1  +  price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close
    acc_ma26_36 = acc_ma26_36_1 / 26

    acc_ma26_37_1 = acc_ma12_37_1  +  price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close
    acc_ma26_37 = acc_ma26_37_1 / 26

    acc_ma26_38_1 = acc_ma12_38_1  +  price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close
    acc_ma26_38 = acc_ma26_38_1 / 26

    acc_ma26_39_1 = acc_ma12_39_1  +  price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close
    acc_ma26_39 = acc_ma26_39_1 / 26

    acc_ma26_40_1 = acc_ma12_40_1  +  price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close
    acc_ma26_40 = acc_ma26_40_1 / 26

    acc_ma26_41_1 = acc_ma12_41_1  +  price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close
    acc_ma26_41 = acc_ma26_41_1 / 26

    acc_ma26_42_1 = acc_ma12_42_1  +  price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close
    acc_ma26_42 = acc_ma26_42_1 / 26

    acc_ma26_43_1 = acc_ma12_43_1  +  price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close
    acc_ma26_43 = acc_ma26_43_1 / 26

    acc_ma26_44_1 = acc_ma12_44_1  +  price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close
    acc_ma26_44 = acc_ma26_44_1 / 26

    acc_ma26_45_1 = acc_ma12_45_1  +  price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close
    acc_ma26_45 = acc_ma26_45_1 / 26

    acc_ma26_46_1 = acc_ma12_46_1  +  price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close
    acc_ma26_46 = acc_ma26_46_1 / 26

    acc_ma26_47_1 = acc_ma12_47_1  +  price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close
    acc_ma26_47 = acc_ma26_47_1 / 26

    acc_ma26_48_1 = acc_ma12_48_1  +  price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close
    acc_ma26_48 = acc_ma26_48_1 / 26

    acc_ma26_49_1 = acc_ma12_49_1  +  price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close
    acc_ma26_49 = acc_ma26_49_1 / 26

    acc_ma26_50_1 = acc_ma12_50_1  +  price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close
    acc_ma26_50 = acc_ma26_50_1 / 26

    acc_ma26_51_1 = acc_ma12_51_1  +  price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close
    acc_ma26_51 = acc_ma26_51_1 / 26

    acc_ma26_52_1 = acc_ma12_52_1  +  price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close
    acc_ma26_52 = acc_ma26_52_1 / 26

    acc_ma26_53_1 = acc_ma12_53_1  +  price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close
    acc_ma26_53 = acc_ma26_53_1 / 26

    acc_ma26_54_1 = acc_ma12_54_1  +  price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close
    acc_ma26_54 = acc_ma26_54_1 / 26

    acc_ma26_55_1 = acc_ma12_55_1  +  price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close
    acc_ma26_55 = acc_ma26_55_1 / 26

    acc_ma26_56_1 = acc_ma12_56_1  +  price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close
    acc_ma26_56 = acc_ma26_56_1 / 26


    # EMA - 장기 26 지수이동평균값 구하기
    acc_e_ma26_55 = acc_ma26_56
    acc_e_ma26_54 = ( price_55_close * ma26_sc )  + ( acc_e_ma26_55 * ( 1 - ma26_sc ) )
    acc_e_ma26_53 = ( price_54_close * ma26_sc )  + ( acc_e_ma26_54 * ( 1 - ma26_sc ) )

    acc_e_ma26_52 = ( price_53_close * ma26_sc )  + ( acc_e_ma26_53 * ( 1 - ma26_sc ) )
    acc_e_ma26_51 = ( price_52_close * ma26_sc )  + ( acc_e_ma26_52 * ( 1 - ma26_sc ) )
    acc_e_ma26_50 = ( price_51_close * ma26_sc )  + ( acc_e_ma26_51 * ( 1 - ma26_sc ) )
    acc_e_ma26_49 = ( price_50_close * ma26_sc )  + ( acc_e_ma26_50 * ( 1 - ma26_sc ) )
    acc_e_ma26_48 = ( price_49_close * ma26_sc )  + ( acc_e_ma26_49 * ( 1 - ma26_sc ) )
    acc_e_ma26_47 = ( price_48_close * ma26_sc )  + ( acc_e_ma26_48 * ( 1 - ma26_sc ) )
    acc_e_ma26_46 = ( price_47_close * ma26_sc )  + ( acc_e_ma26_47 * ( 1 - ma26_sc ) )
    acc_e_ma26_45 = ( price_46_close * ma26_sc )  + ( acc_e_ma26_46 * ( 1 - ma26_sc ) )
    acc_e_ma26_44 = ( price_45_close * ma26_sc )  + ( acc_e_ma26_45 * ( 1 - ma26_sc ) )
    acc_e_ma26_43 = ( price_44_close * ma26_sc )  + ( acc_e_ma26_44 * ( 1 - ma26_sc ) )
    acc_e_ma26_42 = ( price_43_close * ma26_sc )  + ( acc_e_ma26_43 * ( 1 - ma26_sc ) )
    acc_e_ma26_41 = ( price_42_close * ma26_sc )  + ( acc_e_ma26_42 * ( 1 - ma26_sc ) )
    acc_e_ma26_40 = ( price_41_close * ma26_sc )  + ( acc_e_ma26_41 * ( 1 - ma26_sc ) )
    acc_e_ma26_39 = ( price_40_close * ma26_sc )  + ( acc_e_ma26_40 * ( 1 - ma26_sc ) )
    acc_e_ma26_38 = ( price_39_close * ma26_sc )  + ( acc_e_ma26_39 * ( 1 - ma26_sc ) )
    acc_e_ma26_37 = ( price_38_close * ma26_sc )  + ( acc_e_ma26_38 * ( 1 - ma26_sc ) )
    acc_e_ma26_36 = ( price_37_close * ma26_sc )  + ( acc_e_ma26_37 * ( 1 - ma26_sc ) )
    acc_e_ma26_35 = ( price_36_close * ma26_sc )  + ( acc_e_ma26_36 * ( 1 - ma26_sc ) )
    acc_e_ma26_34 = ( price_35_close * ma26_sc )  + ( acc_e_ma26_35 * ( 1 - ma26_sc ) )
    acc_e_ma26_33 = ( price_34_close * ma26_sc )  + ( acc_e_ma26_34 * ( 1 - ma26_sc ) )
    acc_e_ma26_32 = ( price_33_close * ma26_sc )  + ( acc_e_ma26_33 * ( 1 - ma26_sc ) )
    acc_e_ma26_31 = ( price_32_close * ma26_sc )  + ( acc_e_ma26_32 * ( 1 - ma26_sc ) )
    acc_e_ma26_30 = ( price_31_close * ma26_sc )  + ( acc_e_ma26_31 * ( 1 - ma26_sc ) )
    acc_e_ma26_29 = ( price_30_close * ma26_sc )  + ( acc_e_ma26_30 * ( 1 - ma26_sc ) )
    acc_e_ma26_28 = ( price_29_close * ma26_sc )  + ( acc_e_ma26_29 * ( 1 - ma26_sc ) )
    acc_e_ma26_27 = ( price_28_close * ma26_sc )  + ( acc_e_ma26_28 * ( 1 - ma26_sc ) )

    acc_e_ma26_26 = ( price_27_close * ma26_sc )  + ( acc_e_ma26_27 * ( 1 - ma26_sc ) )
    acc_e_ma26_25 = ( price_26_close * ma26_sc )  + ( acc_e_ma26_26 * ( 1 - ma26_sc ) )
    acc_e_ma26_24 = ( price_25_close * ma26_sc )  + ( acc_e_ma26_25 * ( 1 - ma26_sc ) )
    acc_e_ma26_23 = ( price_24_close * ma26_sc )  + ( acc_e_ma26_24 * ( 1 - ma26_sc ) )
    acc_e_ma26_22 = ( price_23_close * ma26_sc )  + ( acc_e_ma26_23 * ( 1 - ma26_sc ) )
    acc_e_ma26_21 = ( price_22_close * ma26_sc )  + ( acc_e_ma26_22 * ( 1 - ma26_sc ) )
    acc_e_ma26_20 = ( price_21_close * ma26_sc )  + ( acc_e_ma26_21 * ( 1 - ma26_sc ) )
    acc_e_ma26_19 = ( price_20_close * ma26_sc )  + ( acc_e_ma26_20 * ( 1 - ma26_sc ) )
    acc_e_ma26_18 = ( price_19_close * ma26_sc )  + ( acc_e_ma26_19 * ( 1 - ma26_sc ) )
    acc_e_ma26_17 = ( price_18_close * ma26_sc )  + ( acc_e_ma26_18 * ( 1 - ma26_sc ) )
    acc_e_ma26_16 = ( price_17_close * ma26_sc )  + ( acc_e_ma26_17 * ( 1 - ma26_sc ) )
    acc_e_ma26_15 = ( price_16_close * ma26_sc )  + ( acc_e_ma26_16 * ( 1 - ma26_sc ) )
    acc_e_ma26_14 = ( price_15_close * ma26_sc )  + ( acc_e_ma26_15 * ( 1 - ma26_sc ) )
    acc_e_ma26_13 = ( price_14_close * ma26_sc )  + ( acc_e_ma26_14 * ( 1 - ma26_sc ) )
    acc_e_ma26_12 = ( price_13_close * ma26_sc )  + ( acc_e_ma26_13 * ( 1 - ma26_sc ) )
    acc_e_ma26_11 = ( price_12_close * ma26_sc )  + ( acc_e_ma26_12 * ( 1 - ma26_sc ) )
    acc_e_ma26_10 = ( price_11_close * ma26_sc )  + ( acc_e_ma26_11 * ( 1 - ma26_sc ) )
    acc_e_ma26_9 = ( price_10_close * ma26_sc )  + ( acc_e_ma26_10 * ( 1 - ma26_sc ) )
    acc_e_ma26_8 = ( price_9_close * ma26_sc )  + ( acc_e_ma26_9 * ( 1 - ma26_sc ) )
    acc_e_ma26_7 = ( price_8_close * ma26_sc )  + ( acc_e_ma26_8 * ( 1 - ma26_sc ) )
    acc_e_ma26_6 = ( price_7_close * ma26_sc )  + ( acc_e_ma26_7 * ( 1 - ma26_sc ) )
    acc_e_ma26_5 = ( price_6_close * ma26_sc )  + ( acc_e_ma26_6 * ( 1 - ma26_sc ) )
    acc_e_ma26_4 = ( price_5_close * ma26_sc )  + ( acc_e_ma26_5 * ( 1 - ma26_sc ) )
    acc_e_ma26_3 = ( price_4_close * ma26_sc )  + ( acc_e_ma26_4 * ( 1 - ma26_sc ) )
    acc_e_ma26_2 = ( price_3_close * ma26_sc )  + ( acc_e_ma26_3 * ( 1 - ma26_sc ) )
    acc_e_ma26_1 = ( price_2_close * ma26_sc )  + ( acc_e_ma26_2 * ( 1 - ma26_sc ) )

    # 여기까지






    # macd
    # 단기12일이평선 - 장기26일이평선 = + 는 0선 이상, - 는 0선 이하
    print("macd값")
    print("========== ========== ========== ========== ==========")
    acc_macd_ok_1 = acc_e_ma12_1 - acc_e_ma26_1
    print( f"e_macd_ok_1 ( {acc_macd_ok_1} ) =  acc_e_ma12_1 ( {acc_e_ma12_1} ) - acc_e_ma26_1 ( {acc_e_ma26_1} )")

    acc_macd_ok_2 = acc_e_ma12_2 - acc_e_ma26_2
    print( f"e_macd_ok_2 ( {acc_macd_ok_2} ) =  acc_e_ma12_2 ( {acc_e_ma12_2} ) - acc_e_ma26_2 ( {acc_e_ma26_2} )")

    acc_macd_ok_3 = acc_e_ma12_3 - acc_e_ma26_3
    print( f"e_macd_ok_3 ( {acc_macd_ok_3} ) =  acc_e_ma12_3 ( {acc_e_ma12_3} ) - acc_e_ma26_3 ( {acc_e_ma26_3} )")

    acc_macd_ok_4 = acc_e_ma12_4 - acc_e_ma26_4
    print( f"e_macd_ok_4 ( {acc_macd_ok_4} ) =  acc_e_ma12_4 ( {acc_e_ma12_4} ) - acc_e_ma26_4 ( {acc_e_ma26_4} )")

    acc_macd_ok_5 = acc_e_ma12_5 - acc_e_ma26_5
    print( f"e_macd_ok_5 ( {acc_macd_ok_5} ) =  acc_e_ma12_5 ( {acc_e_ma12_5} ) - acc_e_ma26_5 ( {acc_e_ma26_5} )")

    acc_macd_ok_6 = acc_e_ma12_6 - acc_e_ma26_6
    print( f"e_macd_ok_6 ( {acc_macd_ok_6} ) =  acc_e_ma12_6 ( {acc_e_ma12_6} ) - acc_e_ma26_6 ( {acc_e_ma26_6} )")

    acc_macd_ok_7 = acc_e_ma12_7 - acc_e_ma26_7
    print( f"e_macd_ok_7 ( {acc_macd_ok_7} ) =  acc_e_ma12_7 ( {acc_e_ma12_7} ) - acc_e_ma26_7 ( {acc_e_ma26_7} )")

    acc_macd_ok_8 = acc_e_ma12_8 - acc_e_ma26_8
    print( f"e_macd_ok_8 ( {acc_macd_ok_8} ) =  acc_e_ma12_8 ( {acc_e_ma12_8} ) - acc_e_ma26_8 ( {acc_e_ma26_8} )")

    acc_macd_ok_9 = acc_e_ma12_9 - acc_e_ma26_9
    print( f"e_macd_ok_9 ( {acc_macd_ok_9} ) =  acc_e_ma12_9 ( {acc_e_ma12_9} ) - acc_e_ma26_9 ( {acc_e_ma26_9} )")
    
    acc_macd_ok_10 = acc_e_ma12_10 - acc_e_ma26_10
    print( f"e_macd_ok_10 ( {acc_macd_ok_10} ) =  acc_e_ma12_10 ( {acc_e_ma12_10} ) - acc_e_ma26_10 ( {acc_e_ma26_10} )")

    acc_macd_ok_11 = acc_e_ma12_11 - acc_e_ma26_11
    print( f"e_macd_ok_11 ( {acc_macd_ok_11} ) =  acc_e_ma12_11 ( {acc_e_ma12_11} ) - acc_e_ma26_11 ( {acc_e_ma26_11} )")

    acc_macd_ok_12 = acc_e_ma12_12 - acc_e_ma26_12
    print( f"e_macd_ok_12 ( {acc_macd_ok_12} ) =  acc_e_ma12_12 ( {acc_e_ma12_12} ) - acc_e_ma26_12 ( {acc_e_ma26_12} )")

    acc_macd_ok_13 = acc_e_ma12_13 - acc_e_ma26_13
    print( f"e_macd_ok_13 ( {acc_macd_ok_13} ) =  acc_e_ma12_13 ( {acc_e_ma12_13} ) - acc_e_ma26_13 ( {acc_e_ma26_13} )")

    acc_macd_ok_14 = acc_e_ma12_14 - acc_e_ma26_14
    print( f"e_macd_ok_14 ( {acc_macd_ok_14} ) =  acc_e_ma12_14 ( {acc_e_ma12_14} ) - acc_e_ma26_14 ( {acc_e_ma26_14} )")

    acc_macd_ok_15 = acc_e_ma12_15 - acc_e_ma26_15
    print( f"e_macd_ok_15 ( {acc_macd_ok_15} ) =  acc_e_ma12_15 ( {acc_e_ma12_15} ) - acc_e_ma26_15 ( {acc_e_ma26_15} )")

    acc_macd_ok_16 = acc_e_ma12_16 - acc_e_ma26_16
    print( f"e_macd_ok_16 ( {acc_macd_ok_16} ) =  acc_e_ma12_16 ( {acc_e_ma12_16} ) - acc_e_ma26_16 ( {acc_e_ma26_16} )")

    acc_macd_ok_17 = acc_e_ma12_17 - acc_e_ma26_17
    print( f"e_macd_ok_17 ( {acc_macd_ok_17} ) =  acc_e_ma12_17 ( {acc_e_ma12_17} ) - acc_e_ma26_17 ( {acc_e_ma26_17} )")
    print()





    print("시그널값")
    print("========== ========== ========== ========== ==========")
    # signal = macd 9일선, macd값의 9이평선.
    # + 는 0선 이상, - 는 0선 이하
    acc_signal_1 = ( acc_macd_ok_1 + acc_macd_ok_2 + acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 ) / 9
    print(f"acc_signal_1 = ( {acc_signal_1} )")

    acc_signal_2 = ( acc_macd_ok_2 + acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 ) / 9
    print(f"acc_signal_2 = ( {acc_signal_2} )")

    acc_signal_3 = ( acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 ) / 9
    print(f"acc_signal_3 = ( {acc_signal_3} )")

    acc_signal_4 = ( acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 ) / 9
    print(f"acc_signal_4 = ( {acc_signal_4} )")

    acc_signal_5 = ( acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 ) / 9
    print(f"acc_signal_5 = ( {acc_signal_5} )")

    acc_signal_6 = ( acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 ) / 9
    print(f"acc_signal_6 = ( {acc_signal_6} )")

    acc_signal_7 = ( acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 ) / 9
    print(f"acc_signal_7 = ( {acc_signal_7} )")

    acc_signal_8 = ( acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 + acc_macd_ok_16 ) / 9
    print(f"acc_signal_8 = ( {acc_signal_8} )")

    acc_signal_9 = ( acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 + acc_macd_ok_16 + acc_macd_ok_17 ) / 9
    print(f"acc_signal_9 = ( {acc_signal_9} )")

    print()

    # 최종값
    # macd - 시그널 = + 는 골든크로스, - 는 데드크로스
    print("[최종] 간격 = macd - 시그널")
    print("========== ========== ========== ========== ==========")
    acc_macd1 = acc_macd_ok_1 - acc_signal_1
    print(f"acc_macd1 ( {acc_macd1} ) = acc_macd_ok_1 ( {acc_macd_ok_1} ) - acc_signal_1 ( {acc_signal_1} )")
    acc_macd2 = acc_macd_ok_2 - acc_signal_2
    print(f"acc_macd2 ( {acc_macd2} ) = acc_macd_ok_2 ( {acc_macd_ok_2} ) - acc_signal_2 ( {acc_signal_2} )")
    acc_macd3 = acc_macd_ok_3 - acc_signal_3
    print(f"acc_macd3 ( {acc_macd3} ) = acc_macd_ok_3 ( {acc_macd_ok_3} ) - acc_signal_3 ( {acc_signal_3} )")
    acc_macd4 = acc_macd_ok_4 - acc_signal_4
    print(f"acc_macd4 ( {acc_macd4} ) = acc_macd_ok_4 ( {acc_macd_ok_4} ) - acc_signal_4 ( {acc_signal_4} )")
    acc_macd5 = acc_macd_ok_5 - acc_signal_5
    print(f"acc_macd5 ( {acc_macd5} ) = acc_macd_ok_5 ( {acc_macd_ok_5} ) - acc_signal_5 ( {acc_signal_5} )")
    acc_macd6 = acc_macd_ok_6 - acc_signal_6
    print(f"acc_macd6 ( {acc_macd6} ) = acc_macd_ok_6 ( {acc_macd_ok_6} ) - acc_signal_6 ( {acc_signal_6} )")
    acc_macd7 = acc_macd_ok_7 - acc_signal_7
    print(f"acc_macd7 ( {acc_macd7} ) = acc_macd_ok_7 ( {acc_macd_ok_7} ) - acc_signal_7 ( {acc_signal_7} )")
    print()

    ##### 거래량 동반한 macd 산출. 끝 #####
    #####################################





    #####################################
    ##### macd 매매선택              #####

    # acc_macd_select
    #if acc_signal_1 >= 0:
    #    if acc_macd1 >= 0:
    #        # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 골든크로스
    #        acc_macd_select = 1
    #    else:
    #        # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 데드크로스
    #        acc_macd_select = 2
    #else:
    #    if acc_macd1 >= 0:
    #        # acc_ma26_1이 기준선 아래에 있을때, acc_macd1이 골든크로스
    #        acc_macd_select = 3
    #    else:
    #        # acc_ma26_1이 기준선 아래에 있을때, acc_macd1이 데드크로스
    #        acc_macd_select = 4

    if acc_macd1 >= 0:
        # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 골든크로스
        acc_macd_select = 1
    else:
        # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 데드크로스
        acc_macd_select = 2

    print(f"acc_macd_select = {acc_macd_select}")
    print()

    time.sleep(1)

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
    limit=100
)

df = pd.DataFrame(data = btc, columns = ['datetime', 'open', 'high', 'low', 'close', 'volume'])
df['datetime'] = pd.to_datetime(df['datetime'], unit = 'ms')
df.set_index('datetime', inplace = True)

print(df)
print()


# 종가받기 90개
print("========== 4시간봉 종가 받기 ==========")
print()
# 0은 아무것도 아님.
price_0_close = df.iloc[0]['close']
#price_0_time = df.iloc[0]['datetime']

# -1은 현재가.
price_1_close = df.iloc[-1]['close']

########################################
# -2는 1시간전 종가. 여기부터 macd 계산.
price_2_close = df.iloc[-2]['close']
price_3_close = df.iloc[-3]['close']
price_4_close = df.iloc[-4]['close']
price_5_close = df.iloc[-5]['close']
price_6_close = df.iloc[-6]['close']
price_7_close = df.iloc[-7]['close']
price_8_close = df.iloc[-8]['close']
price_9_close = df.iloc[-9]['close']
price_10_close = df.iloc[-10]['close']

price_11_close = df.iloc[-11]['close']
price_12_close = df.iloc[-12]['close']
price_13_close = df.iloc[-13]['close']
price_14_close = df.iloc[-14]['close']
price_15_close = df.iloc[-15]['close']
price_16_close = df.iloc[-16]['close']
price_17_close = df.iloc[-17]['close']
price_18_close = df.iloc[-18]['close']
price_19_close = df.iloc[-19]['close']
price_20_close = df.iloc[-20]['close']
price_21_close = df.iloc[-21]['close']
price_22_close = df.iloc[-22]['close']
price_23_close = df.iloc[-23]['close']
price_24_close = df.iloc[-24]['close']
price_25_close = df.iloc[-25]['close']
price_26_close = df.iloc[-26]['close']
price_27_close = df.iloc[-27]['close']
price_28_close = df.iloc[-28]['close']
price_29_close = df.iloc[-29]['close']
price_30_close = df.iloc[-30]['close']

price_31_close = df.iloc[-31]['close']
price_32_close = df.iloc[-32]['close']
price_33_close = df.iloc[-33]['close']
price_34_close = df.iloc[-34]['close']
price_35_close = df.iloc[-35]['close']
price_36_close = df.iloc[-36]['close']
price_37_close = df.iloc[-37]['close']
price_38_close = df.iloc[-38]['close']
price_39_close = df.iloc[-39]['close']
price_40_close = df.iloc[-40]['close']

price_41_close = df.iloc[-41]['close']
price_42_close = df.iloc[-42]['close']
price_43_close = df.iloc[-43]['close']
price_44_close = df.iloc[-44]['close']
price_45_close = df.iloc[-45]['close']
price_46_close = df.iloc[-46]['close']
price_47_close = df.iloc[-47]['close']
price_48_close = df.iloc[-48]['close']
price_49_close = df.iloc[-49]['close']
price_50_close = df.iloc[-50]['close']

price_51_close = df.iloc[-51]['close']
price_52_close = df.iloc[-52]['close']
price_53_close = df.iloc[-53]['close']
price_54_close = df.iloc[-54]['close']
price_55_close = df.iloc[-55]['close']
price_56_close = df.iloc[-56]['close']
price_57_close = df.iloc[-57]['close']
price_58_close = df.iloc[-58]['close']
price_59_close = df.iloc[-59]['close']
price_60_close = df.iloc[-60]['close']

price_61_close = df.iloc[-61]['close']
price_62_close = df.iloc[-62]['close']
price_63_close = df.iloc[-63]['close']
price_64_close = df.iloc[-64]['close']
price_65_close = df.iloc[-65]['close']
price_66_close = df.iloc[-66]['close']
price_67_close = df.iloc[-67]['close']
price_68_close = df.iloc[-68]['close']
price_69_close = df.iloc[-69]['close']
price_70_close = df.iloc[-70]['close']

price_71_close = df.iloc[-71]['close']
price_72_close = df.iloc[-72]['close']
price_73_close = df.iloc[-73]['close']
price_74_close = df.iloc[-74]['close']
price_75_close = df.iloc[-75]['close']
price_76_close = df.iloc[-76]['close']
price_77_close = df.iloc[-77]['close']
price_78_close = df.iloc[-78]['close']
price_79_close = df.iloc[-79]['close']
price_80_close = df.iloc[-80]['close']

price_81_close = df.iloc[-81]['close']
price_82_close = df.iloc[-82]['close']












    

# 단기 12 평활상수
ma12_sc = 2 / ( 1 + 12 )


# EMA - 단기 12 지수 종가 계산
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

acc_ma12_10_1 = price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close
acc_ma12_10 = acc_ma12_10_1 / 12

acc_ma12_11_1 = price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close
acc_ma12_11 = acc_ma12_11_1 / 12

acc_ma12_12_1 = price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close
acc_ma12_12 = acc_ma12_12_1 / 12

acc_ma12_13_1 = price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close
acc_ma12_13 = acc_ma12_13_1 / 12

acc_ma12_14_1 = price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close
acc_ma12_14 = acc_ma12_14_1 / 12

acc_ma12_15_1 = price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close
acc_ma12_15 = acc_ma12_15_1 / 12

acc_ma12_16_1 = price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close
acc_ma12_16 = acc_ma12_16_1 / 12

acc_ma12_17_1 = price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close
acc_ma12_17 = acc_ma12_17_1 / 12

acc_ma12_18_1 = price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close
acc_ma12_18 = acc_ma12_18_1 / 12

acc_ma12_19_1 = price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close
acc_ma12_19 = acc_ma12_19_1 / 12

acc_ma12_20_1 = price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close
acc_ma12_20 = acc_ma12_20_1 / 12

acc_ma12_21_1 = price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close
acc_ma12_21 = acc_ma12_21_1 / 12

acc_ma12_22_1 = price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close
acc_ma12_22 = acc_ma12_22_1 / 12

acc_ma12_23_1 = price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close
acc_ma12_23 = acc_ma12_23_1 / 12

acc_ma12_24_1 = price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close
acc_ma12_24 = acc_ma12_24_1 / 12

acc_ma12_25_1 = price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close
acc_ma12_25 = acc_ma12_25_1 / 12

acc_ma12_26_1 = price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close
acc_ma12_26 = acc_ma12_26_1 / 12

acc_ma12_27_1 = price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close
acc_ma12_27 = acc_ma12_27_1 / 12

acc_ma12_28_1 = price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close
acc_ma12_28 = acc_ma12_28_1 / 12

acc_ma12_29_1 = price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close
acc_ma12_30_1 = price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close
acc_ma12_31_1 = price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close
acc_ma12_32_1 = price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close
acc_ma12_33_1 = price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close
acc_ma12_34_1 = price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close
acc_ma12_35_1 = price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close
acc_ma12_36_1 = price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close
acc_ma12_37_1 = price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close
acc_ma12_38_1 = price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close
acc_ma12_39_1 = price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close
acc_ma12_40_1 = price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close
acc_ma12_41_1 = price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close
acc_ma12_42_1 = price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close
acc_ma12_43_1 = price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close
acc_ma12_44_1 = price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close
acc_ma12_45_1 = price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close
acc_ma12_46_1 = price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close
acc_ma12_47_1 = price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close
acc_ma12_48_1 = price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close
acc_ma12_49_1 = price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close
acc_ma12_50_1 = price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close
acc_ma12_51_1 = price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close
acc_ma12_52_1 = price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close
acc_ma12_53_1 = price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close
acc_ma12_54_1 = price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close
acc_ma12_55_1 = price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close
acc_ma12_56_1 = price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close


# EMA - 단기 12 지수이동평균값 구하기
acc_e_ma12_27 = acc_ma12_28
acc_e_ma12_26 = ( price_27_close * ma12_sc )  + ( acc_e_ma12_27 * ( 1 - ma12_sc ) )
acc_e_ma12_25 = ( price_26_close * ma12_sc )  + ( acc_e_ma12_26 * ( 1 - ma12_sc ) )

acc_e_ma12_24 = ( price_25_close * ma12_sc )  + ( acc_e_ma12_25 * ( 1 - ma12_sc ) )
acc_e_ma12_23 = ( price_24_close * ma12_sc )  + ( acc_e_ma12_24 * ( 1 - ma12_sc ) )
acc_e_ma12_22 = ( price_23_close * ma12_sc )  + ( acc_e_ma12_23 * ( 1 - ma12_sc ) )
acc_e_ma12_21 = ( price_22_close * ma12_sc )  + ( acc_e_ma12_22 * ( 1 - ma12_sc ) )
acc_e_ma12_20 = ( price_21_close * ma12_sc )  + ( acc_e_ma12_21 * ( 1 - ma12_sc ) )
acc_e_ma12_19 = ( price_20_close * ma12_sc )  + ( acc_e_ma12_20 * ( 1 - ma12_sc ) )
acc_e_ma12_18 = ( price_19_close * ma12_sc )  + ( acc_e_ma12_19 * ( 1 - ma12_sc ) )
acc_e_ma12_17 = ( price_18_close * ma12_sc )  + ( acc_e_ma12_18 * ( 1 - ma12_sc ) )
acc_e_ma12_16 = ( price_17_close * ma12_sc )  + ( acc_e_ma12_17 * ( 1 - ma12_sc ) )
acc_e_ma12_15 = ( price_16_close * ma12_sc )  + ( acc_e_ma12_16 * ( 1 - ma12_sc ) )
acc_e_ma12_14 = ( price_15_close * ma12_sc )  + ( acc_e_ma12_15 * ( 1 - ma12_sc ) )
acc_e_ma12_13 = ( price_14_close * ma12_sc )  + ( acc_e_ma12_14 * ( 1 - ma12_sc ) )

acc_e_ma12_12 = ( price_13_close * ma12_sc )  + ( acc_e_ma12_13 * ( 1 - ma12_sc ) )
acc_e_ma12_11 = ( price_12_close * ma12_sc )  + ( acc_e_ma12_12 * ( 1 - ma12_sc ) )
acc_e_ma12_10 = ( price_11_close * ma12_sc )  + ( acc_e_ma12_11 * ( 1 - ma12_sc ) )
acc_e_ma12_9 = ( price_10_close * ma12_sc )  + ( acc_e_ma12_10 * ( 1 - ma12_sc ) )
acc_e_ma12_8 = ( price_9_close * ma12_sc )  + ( acc_e_ma12_9 * ( 1 - ma12_sc ) )
acc_e_ma12_7 = ( price_8_close * ma12_sc )  + ( acc_e_ma12_8 * ( 1 - ma12_sc ) )
acc_e_ma12_6 = ( price_7_close * ma12_sc )  + ( acc_e_ma12_7 * ( 1 - ma12_sc ) )
acc_e_ma12_5 = ( price_6_close * ma12_sc )  + ( acc_e_ma12_6 * ( 1 - ma12_sc ) )
acc_e_ma12_4 = ( price_5_close * ma12_sc )  + ( acc_e_ma12_5 * ( 1 - ma12_sc ) )
acc_e_ma12_3 = ( price_4_close * ma12_sc )  + ( acc_e_ma12_4 * ( 1 - ma12_sc ) )
acc_e_ma12_2 = ( price_3_close * ma12_sc )  + ( acc_e_ma12_3 * ( 1 - ma12_sc ) )
acc_e_ma12_1 = ( price_2_close * ma12_sc )  + ( acc_e_ma12_2 * ( 1 - ma12_sc ) )



# 여기까지






# 장기 26 평활상수
ma26_sc = 2 / ( 1 + 26 )


# EMA - 장기 26 지수 종가 계산
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

acc_ma26_10_1 = acc_ma12_10_1  +  price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close
acc_ma26_10 = acc_ma26_10_1 / 26

acc_ma26_11_1 = acc_ma12_11_1  +  price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close
acc_ma26_11 = acc_ma26_11_1 / 26

acc_ma26_12_1 = acc_ma12_12_1  +  price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close
acc_ma26_12 = acc_ma26_12_1 / 26

acc_ma26_13_1 = acc_ma12_13_1  +  price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close
acc_ma26_13 = acc_ma26_13_1 / 26

acc_ma26_14_1 = acc_ma12_14_1  +  price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close
acc_ma26_14 = acc_ma26_14_1 / 26

acc_ma26_15_1 = acc_ma12_15_1  +  price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close
acc_ma26_15 = acc_ma26_15_1 / 26

acc_ma26_16_1 = acc_ma12_16_1  +  price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close
acc_ma26_16 = acc_ma26_16_1 / 26

acc_ma26_17_1 = acc_ma12_17_1  +  price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close
acc_ma26_17 = acc_ma26_17_1 / 26

acc_ma26_18_1 = acc_ma12_18_1  +  price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close
acc_ma26_18 = acc_ma26_18_1 / 26

acc_ma26_19_1 = acc_ma12_19_1  +  price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close
acc_ma26_19 = acc_ma26_19_1 / 26

acc_ma26_20_1 = acc_ma12_20_1  +  price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close
acc_ma26_20 = acc_ma26_20_1 / 26

acc_ma26_21_1 = acc_ma12_21_1  +  price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close
acc_ma26_21 = acc_ma26_21_1 / 26

acc_ma26_22_1 = acc_ma12_22_1  +  price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close
acc_ma26_22 = acc_ma26_22_1 / 26

acc_ma26_23_1 = acc_ma12_23_1  +  price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close
acc_ma26_23 = acc_ma26_23_1 / 26

acc_ma26_24_1 = acc_ma12_24_1  +  price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close
acc_ma26_24 = acc_ma26_24_1 / 26

acc_ma26_25_1 = acc_ma12_25_1  +  price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close
acc_ma26_25 = acc_ma26_25_1 / 26

acc_ma26_26_1 = acc_ma12_26_1  +  price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close
acc_ma26_26 = acc_ma26_26_1 / 26

acc_ma26_27_1 = acc_ma12_27_1  +  price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close
acc_ma26_27 = acc_ma26_27_1 / 26

acc_ma26_28_1 = acc_ma12_28_1  +  price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close
acc_ma26_28 = acc_ma26_28_1 / 26

acc_ma26_29_1 = acc_ma12_29_1  +  price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close
acc_ma26_29 = acc_ma26_29_1 / 26

acc_ma26_30_1 = acc_ma12_30_1  +  price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close
acc_ma26_30 = acc_ma26_30_1 / 26

acc_ma26_31_1 = acc_ma12_31_1  +  price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close
acc_ma26_31 = acc_ma26_31_1 / 26

acc_ma26_32_1 = acc_ma12_32_1  +  price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close
acc_ma26_32 = acc_ma26_32_1 / 26

acc_ma26_33_1 = acc_ma12_33_1  +  price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close
acc_ma26_33 = acc_ma26_33_1 / 26

acc_ma26_34_1 = acc_ma12_34_1  +  price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close
acc_ma26_34 = acc_ma26_34_1 / 26

acc_ma26_35_1 = acc_ma12_35_1  +  price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close
acc_ma26_35 = acc_ma26_35_1 / 26

acc_ma26_36_1 = acc_ma12_36_1  +  price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close
acc_ma26_36 = acc_ma26_36_1 / 26

acc_ma26_37_1 = acc_ma12_37_1  +  price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close
acc_ma26_37 = acc_ma26_37_1 / 26

acc_ma26_38_1 = acc_ma12_38_1  +  price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close
acc_ma26_38 = acc_ma26_38_1 / 26

acc_ma26_39_1 = acc_ma12_39_1  +  price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close
acc_ma26_39 = acc_ma26_39_1 / 26

acc_ma26_40_1 = acc_ma12_40_1  +  price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close
acc_ma26_40 = acc_ma26_40_1 / 26

acc_ma26_41_1 = acc_ma12_41_1  +  price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close
acc_ma26_41 = acc_ma26_41_1 / 26

acc_ma26_42_1 = acc_ma12_42_1  +  price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close
acc_ma26_42 = acc_ma26_42_1 / 26

acc_ma26_43_1 = acc_ma12_43_1  +  price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close
acc_ma26_43 = acc_ma26_43_1 / 26

acc_ma26_44_1 = acc_ma12_44_1  +  price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close
acc_ma26_44 = acc_ma26_44_1 / 26

acc_ma26_45_1 = acc_ma12_45_1  +  price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close
acc_ma26_45 = acc_ma26_45_1 / 26

acc_ma26_46_1 = acc_ma12_46_1  +  price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close
acc_ma26_46 = acc_ma26_46_1 / 26

acc_ma26_47_1 = acc_ma12_47_1  +  price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close
acc_ma26_47 = acc_ma26_47_1 / 26

acc_ma26_48_1 = acc_ma12_48_1  +  price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close
acc_ma26_48 = acc_ma26_48_1 / 26

acc_ma26_49_1 = acc_ma12_49_1  +  price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close
acc_ma26_49 = acc_ma26_49_1 / 26

acc_ma26_50_1 = acc_ma12_50_1  +  price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close
acc_ma26_50 = acc_ma26_50_1 / 26

acc_ma26_51_1 = acc_ma12_51_1  +  price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close
acc_ma26_51 = acc_ma26_51_1 / 26

acc_ma26_52_1 = acc_ma12_52_1  +  price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close
acc_ma26_52 = acc_ma26_52_1 / 26

acc_ma26_53_1 = acc_ma12_53_1  +  price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close
acc_ma26_53 = acc_ma26_53_1 / 26

acc_ma26_54_1 = acc_ma12_54_1  +  price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close
acc_ma26_54 = acc_ma26_54_1 / 26

acc_ma26_55_1 = acc_ma12_55_1  +  price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close
acc_ma26_55 = acc_ma26_55_1 / 26

acc_ma26_56_1 = acc_ma12_56_1  +  price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close
acc_ma26_56 = acc_ma26_56_1 / 26


# EMA - 장기 26 지수이동평균값 구하기
acc_e_ma26_55 = acc_ma26_56
acc_e_ma26_54 = ( price_55_close * ma26_sc )  + ( acc_e_ma26_55 * ( 1 - ma26_sc ) )
acc_e_ma26_53 = ( price_54_close * ma26_sc )  + ( acc_e_ma26_54 * ( 1 - ma26_sc ) )

acc_e_ma26_52 = ( price_53_close * ma26_sc )  + ( acc_e_ma26_53 * ( 1 - ma26_sc ) )
acc_e_ma26_51 = ( price_52_close * ma26_sc )  + ( acc_e_ma26_52 * ( 1 - ma26_sc ) )
acc_e_ma26_50 = ( price_51_close * ma26_sc )  + ( acc_e_ma26_51 * ( 1 - ma26_sc ) )
acc_e_ma26_49 = ( price_50_close * ma26_sc )  + ( acc_e_ma26_50 * ( 1 - ma26_sc ) )
acc_e_ma26_48 = ( price_49_close * ma26_sc )  + ( acc_e_ma26_49 * ( 1 - ma26_sc ) )
acc_e_ma26_47 = ( price_48_close * ma26_sc )  + ( acc_e_ma26_48 * ( 1 - ma26_sc ) )
acc_e_ma26_46 = ( price_47_close * ma26_sc )  + ( acc_e_ma26_47 * ( 1 - ma26_sc ) )
acc_e_ma26_45 = ( price_46_close * ma26_sc )  + ( acc_e_ma26_46 * ( 1 - ma26_sc ) )
acc_e_ma26_44 = ( price_45_close * ma26_sc )  + ( acc_e_ma26_45 * ( 1 - ma26_sc ) )
acc_e_ma26_43 = ( price_44_close * ma26_sc )  + ( acc_e_ma26_44 * ( 1 - ma26_sc ) )
acc_e_ma26_42 = ( price_43_close * ma26_sc )  + ( acc_e_ma26_43 * ( 1 - ma26_sc ) )
acc_e_ma26_41 = ( price_42_close * ma26_sc )  + ( acc_e_ma26_42 * ( 1 - ma26_sc ) )
acc_e_ma26_40 = ( price_41_close * ma26_sc )  + ( acc_e_ma26_41 * ( 1 - ma26_sc ) )
acc_e_ma26_39 = ( price_40_close * ma26_sc )  + ( acc_e_ma26_40 * ( 1 - ma26_sc ) )
acc_e_ma26_38 = ( price_39_close * ma26_sc )  + ( acc_e_ma26_39 * ( 1 - ma26_sc ) )
acc_e_ma26_37 = ( price_38_close * ma26_sc )  + ( acc_e_ma26_38 * ( 1 - ma26_sc ) )
acc_e_ma26_36 = ( price_37_close * ma26_sc )  + ( acc_e_ma26_37 * ( 1 - ma26_sc ) )
acc_e_ma26_35 = ( price_36_close * ma26_sc )  + ( acc_e_ma26_36 * ( 1 - ma26_sc ) )
acc_e_ma26_34 = ( price_35_close * ma26_sc )  + ( acc_e_ma26_35 * ( 1 - ma26_sc ) )
acc_e_ma26_33 = ( price_34_close * ma26_sc )  + ( acc_e_ma26_34 * ( 1 - ma26_sc ) )
acc_e_ma26_32 = ( price_33_close * ma26_sc )  + ( acc_e_ma26_33 * ( 1 - ma26_sc ) )
acc_e_ma26_31 = ( price_32_close * ma26_sc )  + ( acc_e_ma26_32 * ( 1 - ma26_sc ) )
acc_e_ma26_30 = ( price_31_close * ma26_sc )  + ( acc_e_ma26_31 * ( 1 - ma26_sc ) )
acc_e_ma26_29 = ( price_30_close * ma26_sc )  + ( acc_e_ma26_30 * ( 1 - ma26_sc ) )
acc_e_ma26_28 = ( price_29_close * ma26_sc )  + ( acc_e_ma26_29 * ( 1 - ma26_sc ) )
acc_e_ma26_27 = ( price_28_close * ma26_sc )  + ( acc_e_ma26_28 * ( 1 - ma26_sc ) )

acc_e_ma26_26 = ( price_27_close * ma26_sc )  + ( acc_e_ma26_27 * ( 1 - ma26_sc ) )
acc_e_ma26_25 = ( price_26_close * ma26_sc )  + ( acc_e_ma26_26 * ( 1 - ma26_sc ) )
acc_e_ma26_24 = ( price_25_close * ma26_sc )  + ( acc_e_ma26_25 * ( 1 - ma26_sc ) )
acc_e_ma26_23 = ( price_24_close * ma26_sc )  + ( acc_e_ma26_24 * ( 1 - ma26_sc ) )
acc_e_ma26_22 = ( price_23_close * ma26_sc )  + ( acc_e_ma26_23 * ( 1 - ma26_sc ) )
acc_e_ma26_21 = ( price_22_close * ma26_sc )  + ( acc_e_ma26_22 * ( 1 - ma26_sc ) )
acc_e_ma26_20 = ( price_21_close * ma26_sc )  + ( acc_e_ma26_21 * ( 1 - ma26_sc ) )
acc_e_ma26_19 = ( price_20_close * ma26_sc )  + ( acc_e_ma26_20 * ( 1 - ma26_sc ) )
acc_e_ma26_18 = ( price_19_close * ma26_sc )  + ( acc_e_ma26_19 * ( 1 - ma26_sc ) )
acc_e_ma26_17 = ( price_18_close * ma26_sc )  + ( acc_e_ma26_18 * ( 1 - ma26_sc ) )
acc_e_ma26_16 = ( price_17_close * ma26_sc )  + ( acc_e_ma26_17 * ( 1 - ma26_sc ) )
acc_e_ma26_15 = ( price_16_close * ma26_sc )  + ( acc_e_ma26_16 * ( 1 - ma26_sc ) )
acc_e_ma26_14 = ( price_15_close * ma26_sc )  + ( acc_e_ma26_15 * ( 1 - ma26_sc ) )
acc_e_ma26_13 = ( price_14_close * ma26_sc )  + ( acc_e_ma26_14 * ( 1 - ma26_sc ) )
acc_e_ma26_12 = ( price_13_close * ma26_sc )  + ( acc_e_ma26_13 * ( 1 - ma26_sc ) )
acc_e_ma26_11 = ( price_12_close * ma26_sc )  + ( acc_e_ma26_12 * ( 1 - ma26_sc ) )
acc_e_ma26_10 = ( price_11_close * ma26_sc )  + ( acc_e_ma26_11 * ( 1 - ma26_sc ) )
acc_e_ma26_9 = ( price_10_close * ma26_sc )  + ( acc_e_ma26_10 * ( 1 - ma26_sc ) )
acc_e_ma26_8 = ( price_9_close * ma26_sc )  + ( acc_e_ma26_9 * ( 1 - ma26_sc ) )
acc_e_ma26_7 = ( price_8_close * ma26_sc )  + ( acc_e_ma26_8 * ( 1 - ma26_sc ) )
acc_e_ma26_6 = ( price_7_close * ma26_sc )  + ( acc_e_ma26_7 * ( 1 - ma26_sc ) )
acc_e_ma26_5 = ( price_6_close * ma26_sc )  + ( acc_e_ma26_6 * ( 1 - ma26_sc ) )
acc_e_ma26_4 = ( price_5_close * ma26_sc )  + ( acc_e_ma26_5 * ( 1 - ma26_sc ) )
acc_e_ma26_3 = ( price_4_close * ma26_sc )  + ( acc_e_ma26_4 * ( 1 - ma26_sc ) )
acc_e_ma26_2 = ( price_3_close * ma26_sc )  + ( acc_e_ma26_3 * ( 1 - ma26_sc ) )
acc_e_ma26_1 = ( price_2_close * ma26_sc )  + ( acc_e_ma26_2 * ( 1 - ma26_sc ) )

# 여기까지






# macd
# 단기12일이평선 - 장기26일이평선 = + 는 0선 이상, - 는 0선 이하
print("macd값")
print("========== ========== ========== ========== ==========")
acc_macd_ok_1 = acc_e_ma12_1 - acc_e_ma26_1
print( f"e_macd_ok_1 ( {acc_macd_ok_1} ) =  acc_e_ma12_1 ( {acc_e_ma12_1} ) - acc_e_ma26_1 ( {acc_e_ma26_1} )")

acc_macd_ok_2 = acc_e_ma12_2 - acc_e_ma26_2
print( f"e_macd_ok_2 ( {acc_macd_ok_2} ) =  acc_e_ma12_2 ( {acc_e_ma12_2} ) - acc_e_ma26_2 ( {acc_e_ma26_2} )")

acc_macd_ok_3 = acc_e_ma12_3 - acc_e_ma26_3
print( f"e_macd_ok_3 ( {acc_macd_ok_3} ) =  acc_e_ma12_3 ( {acc_e_ma12_3} ) - acc_e_ma26_3 ( {acc_e_ma26_3} )")

acc_macd_ok_4 = acc_e_ma12_4 - acc_e_ma26_4
print( f"e_macd_ok_4 ( {acc_macd_ok_4} ) =  acc_e_ma12_4 ( {acc_e_ma12_4} ) - acc_e_ma26_4 ( {acc_e_ma26_4} )")

acc_macd_ok_5 = acc_e_ma12_5 - acc_e_ma26_5
print( f"e_macd_ok_5 ( {acc_macd_ok_5} ) =  acc_e_ma12_5 ( {acc_e_ma12_5} ) - acc_e_ma26_5 ( {acc_e_ma26_5} )")

acc_macd_ok_6 = acc_e_ma12_6 - acc_e_ma26_6
print( f"e_macd_ok_6 ( {acc_macd_ok_6} ) =  acc_e_ma12_6 ( {acc_e_ma12_6} ) - acc_e_ma26_6 ( {acc_e_ma26_6} )")

acc_macd_ok_7 = acc_e_ma12_7 - acc_e_ma26_7
print( f"e_macd_ok_7 ( {acc_macd_ok_7} ) =  acc_e_ma12_7 ( {acc_e_ma12_7} ) - acc_e_ma26_7 ( {acc_e_ma26_7} )")

acc_macd_ok_8 = acc_e_ma12_8 - acc_e_ma26_8
print( f"e_macd_ok_8 ( {acc_macd_ok_8} ) =  acc_e_ma12_8 ( {acc_e_ma12_8} ) - acc_e_ma26_8 ( {acc_e_ma26_8} )")

acc_macd_ok_9 = acc_e_ma12_9 - acc_e_ma26_9
print( f"e_macd_ok_9 ( {acc_macd_ok_9} ) =  acc_e_ma12_9 ( {acc_e_ma12_9} ) - acc_e_ma26_9 ( {acc_e_ma26_9} )")

acc_macd_ok_10 = acc_e_ma12_10 - acc_e_ma26_10
print( f"e_macd_ok_10 ( {acc_macd_ok_10} ) =  acc_e_ma12_10 ( {acc_e_ma12_10} ) - acc_e_ma26_10 ( {acc_e_ma26_10} )")

acc_macd_ok_11 = acc_e_ma12_11 - acc_e_ma26_11
print( f"e_macd_ok_11 ( {acc_macd_ok_11} ) =  acc_e_ma12_11 ( {acc_e_ma12_11} ) - acc_e_ma26_11 ( {acc_e_ma26_11} )")

acc_macd_ok_12 = acc_e_ma12_12 - acc_e_ma26_12
print( f"e_macd_ok_12 ( {acc_macd_ok_12} ) =  acc_e_ma12_12 ( {acc_e_ma12_12} ) - acc_e_ma26_12 ( {acc_e_ma26_12} )")

acc_macd_ok_13 = acc_e_ma12_13 - acc_e_ma26_13
print( f"e_macd_ok_13 ( {acc_macd_ok_13} ) =  acc_e_ma12_13 ( {acc_e_ma12_13} ) - acc_e_ma26_13 ( {acc_e_ma26_13} )")

acc_macd_ok_14 = acc_e_ma12_14 - acc_e_ma26_14
print( f"e_macd_ok_14 ( {acc_macd_ok_14} ) =  acc_e_ma12_14 ( {acc_e_ma12_14} ) - acc_e_ma26_14 ( {acc_e_ma26_14} )")

acc_macd_ok_15 = acc_e_ma12_15 - acc_e_ma26_15
print( f"e_macd_ok_15 ( {acc_macd_ok_15} ) =  acc_e_ma12_15 ( {acc_e_ma12_15} ) - acc_e_ma26_15 ( {acc_e_ma26_15} )")

acc_macd_ok_16 = acc_e_ma12_16 - acc_e_ma26_16
print( f"e_macd_ok_16 ( {acc_macd_ok_16} ) =  acc_e_ma12_16 ( {acc_e_ma12_16} ) - acc_e_ma26_16 ( {acc_e_ma26_16} )")

acc_macd_ok_17 = acc_e_ma12_17 - acc_e_ma26_17
print( f"e_macd_ok_17 ( {acc_macd_ok_17} ) =  acc_e_ma12_17 ( {acc_e_ma12_17} ) - acc_e_ma26_17 ( {acc_e_ma26_17} )")
print()





print("시그널값")
print("========== ========== ========== ========== ==========")
# signal = macd 9일선, macd값의 9이평선.
# + 는 0선 이상, - 는 0선 이하
acc_signal_1 = ( acc_macd_ok_1 + acc_macd_ok_2 + acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 ) / 9
print(f"acc_signal_1 = ( {acc_signal_1} )")

acc_signal_2 = ( acc_macd_ok_2 + acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 ) / 9
print(f"acc_signal_2 = ( {acc_signal_2} )")

acc_signal_3 = ( acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 ) / 9
print(f"acc_signal_3 = ( {acc_signal_3} )")

acc_signal_4 = ( acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 ) / 9
print(f"acc_signal_4 = ( {acc_signal_4} )")

acc_signal_5 = ( acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 ) / 9
print(f"acc_signal_5 = ( {acc_signal_5} )")

acc_signal_6 = ( acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 ) / 9
print(f"acc_signal_6 = ( {acc_signal_6} )")

acc_signal_7 = ( acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 ) / 9
print(f"acc_signal_7 = ( {acc_signal_7} )")

acc_signal_8 = ( acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 + acc_macd_ok_16 ) / 9
print(f"acc_signal_8 = ( {acc_signal_8} )")

acc_signal_9 = ( acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 + acc_macd_ok_16 + acc_macd_ok_17 ) / 9
print(f"acc_signal_9 = ( {acc_signal_9} )")

print()

# 최종값
# macd - 시그널 = + 는 골든크로스, - 는 데드크로스
print("[최종] 간격 = macd - 시그널")
print("========== ========== ========== ========== ==========")
acc_macd1 = acc_macd_ok_1 - acc_signal_1
print(f"acc_macd1 ( {acc_macd1} ) = acc_macd_ok_1 ( {acc_macd_ok_1} ) - acc_signal_1 ( {acc_signal_1} )")
acc_macd2 = acc_macd_ok_2 - acc_signal_2
print(f"acc_macd2 ( {acc_macd2} ) = acc_macd_ok_2 ( {acc_macd_ok_2} ) - acc_signal_2 ( {acc_signal_2} )")
acc_macd3 = acc_macd_ok_3 - acc_signal_3
print(f"acc_macd3 ( {acc_macd3} ) = acc_macd_ok_3 ( {acc_macd_ok_3} ) - acc_signal_3 ( {acc_signal_3} )")
acc_macd4 = acc_macd_ok_4 - acc_signal_4
print(f"acc_macd4 ( {acc_macd4} ) = acc_macd_ok_4 ( {acc_macd_ok_4} ) - acc_signal_4 ( {acc_signal_4} )")
acc_macd5 = acc_macd_ok_5 - acc_signal_5
print(f"acc_macd5 ( {acc_macd5} ) = acc_macd_ok_5 ( {acc_macd_ok_5} ) - acc_signal_5 ( {acc_signal_5} )")
acc_macd6 = acc_macd_ok_6 - acc_signal_6
print(f"acc_macd6 ( {acc_macd6} ) = acc_macd_ok_6 ( {acc_macd_ok_6} ) - acc_signal_6 ( {acc_signal_6} )")
acc_macd7 = acc_macd_ok_7 - acc_signal_7
print(f"acc_macd7 ( {acc_macd7} ) = acc_macd_ok_7 ( {acc_macd_ok_7} ) - acc_signal_7 ( {acc_signal_7} )")
acc_macd8 = acc_macd_ok_8 - acc_signal_8
print(f"acc_macd8 ( {acc_macd8} ) = acc_macd_ok_8 ( {acc_macd_ok_8} ) - acc_signal_8 ( {acc_signal_8} )")
acc_macd9 = acc_macd_ok_9 - acc_signal_9
print(f"acc_macd9 ( {acc_macd9} ) = acc_macd_ok_9 ( {acc_macd_ok_9} ) - acc_signal_9 ( {acc_signal_9} )")
print()

##### 거래량 동반한 macd 산출. 끝 #####
#####################################





#####################################
##### macd 매매선택              #####

# acc_macd_select
#if acc_signal_1 >= 0:
#    if acc_macd1 >= 0:
#        # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 골든크로스
#        acc_macd_select = 1
#    else:
#        # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 데드크로스
#        acc_macd_select = 2
#else:
#    if acc_macd1 >= 0:
#        # acc_ma26_1이 기준선 아래에 있을때, acc_macd1이 골든크로스
#        acc_macd_select = 3
#    else:
#        # acc_ma26_1이 기준선 아래에 있을때, acc_macd1이 데드크로스
#        acc_macd_select = 4

if acc_macd1 >= 0:
    # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 골든크로스
    acc_macd_select = 1
else:
    # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 데드크로스
    acc_macd_select = 2

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
                limit=100
            )

            df = pd.DataFrame(data = btc, columns = ['datetime', 'open', 'high', 'low', 'close', 'volume'])
            df['datetime'] = pd.to_datetime(df['datetime'], unit = 'ms')
            df.set_index('datetime', inplace = True)





            # 종가받기 90개
            print("========== 4시간봉 종가 받기 ==========")
            print()
            # 0은 아무것도 아님.
            price_0_close = df.iloc[0]['close']
            #price_0_time = df.iloc[0]['datetime']

            # -1은 현재가.
            price_1_close = df.iloc[-1]['close']

            ########################################
            # -2는 1시간전 종가. 여기부터 macd 계산.
            price_2_close = df.iloc[-2]['close']
            price_3_close = df.iloc[-3]['close']
            price_4_close = df.iloc[-4]['close']
            price_5_close = df.iloc[-5]['close']
            price_6_close = df.iloc[-6]['close']
            price_7_close = df.iloc[-7]['close']
            price_8_close = df.iloc[-8]['close']
            price_9_close = df.iloc[-9]['close']
            price_10_close = df.iloc[-10]['close']

            price_11_close = df.iloc[-11]['close']
            price_12_close = df.iloc[-12]['close']
            price_13_close = df.iloc[-13]['close']
            price_14_close = df.iloc[-14]['close']
            price_15_close = df.iloc[-15]['close']
            price_16_close = df.iloc[-16]['close']
            price_17_close = df.iloc[-17]['close']
            price_18_close = df.iloc[-18]['close']
            price_19_close = df.iloc[-19]['close']
            price_20_close = df.iloc[-20]['close']
            price_21_close = df.iloc[-21]['close']
            price_22_close = df.iloc[-22]['close']
            price_23_close = df.iloc[-23]['close']
            price_24_close = df.iloc[-24]['close']
            price_25_close = df.iloc[-25]['close']
            price_26_close = df.iloc[-26]['close']
            price_27_close = df.iloc[-27]['close']
            price_28_close = df.iloc[-28]['close']
            price_29_close = df.iloc[-29]['close']
            price_30_close = df.iloc[-30]['close']

            price_31_close = df.iloc[-31]['close']
            price_32_close = df.iloc[-32]['close']
            price_33_close = df.iloc[-33]['close']
            price_34_close = df.iloc[-34]['close']
            price_35_close = df.iloc[-35]['close']
            price_36_close = df.iloc[-36]['close']
            price_37_close = df.iloc[-37]['close']
            price_38_close = df.iloc[-38]['close']
            price_39_close = df.iloc[-39]['close']
            price_40_close = df.iloc[-40]['close']

            price_41_close = df.iloc[-41]['close']
            price_42_close = df.iloc[-42]['close']
            price_43_close = df.iloc[-43]['close']
            price_44_close = df.iloc[-44]['close']
            price_45_close = df.iloc[-45]['close']
            price_46_close = df.iloc[-46]['close']
            price_47_close = df.iloc[-47]['close']
            price_48_close = df.iloc[-48]['close']
            price_49_close = df.iloc[-49]['close']
            price_50_close = df.iloc[-50]['close']

            price_51_close = df.iloc[-51]['close']
            price_52_close = df.iloc[-52]['close']
            price_53_close = df.iloc[-53]['close']
            price_54_close = df.iloc[-54]['close']
            price_55_close = df.iloc[-55]['close']
            price_56_close = df.iloc[-56]['close']
            price_57_close = df.iloc[-57]['close']
            price_58_close = df.iloc[-58]['close']
            price_59_close = df.iloc[-59]['close']
            price_60_close = df.iloc[-60]['close']

            price_61_close = df.iloc[-61]['close']
            price_62_close = df.iloc[-62]['close']
            price_63_close = df.iloc[-63]['close']
            price_64_close = df.iloc[-64]['close']
            price_65_close = df.iloc[-65]['close']
            price_66_close = df.iloc[-66]['close']
            price_67_close = df.iloc[-67]['close']
            price_68_close = df.iloc[-68]['close']
            price_69_close = df.iloc[-69]['close']
            price_70_close = df.iloc[-70]['close']

            price_71_close = df.iloc[-71]['close']
            price_72_close = df.iloc[-72]['close']
            price_73_close = df.iloc[-73]['close']
            price_74_close = df.iloc[-74]['close']
            price_75_close = df.iloc[-75]['close']
            price_76_close = df.iloc[-76]['close']
            price_77_close = df.iloc[-77]['close']
            price_78_close = df.iloc[-78]['close']
            price_79_close = df.iloc[-79]['close']
            price_80_close = df.iloc[-80]['close']

            price_81_close = df.iloc[-81]['close']
            price_82_close = df.iloc[-82]['close']












                

            # 단기 12 평활상수
            ma12_sc = 2 / ( 1 + 12 )


            # EMA - 단기 12 지수 종가 계산
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

            acc_ma12_10_1 = price_11_close + price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close
            acc_ma12_10 = acc_ma12_10_1 / 12

            acc_ma12_11_1 = price_12_close + price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close
            acc_ma12_11 = acc_ma12_11_1 / 12

            acc_ma12_12_1 = price_13_close + price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close
            acc_ma12_12 = acc_ma12_12_1 / 12

            acc_ma12_13_1 = price_14_close + price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close
            acc_ma12_13 = acc_ma12_13_1 / 12

            acc_ma12_14_1 = price_15_close + price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close
            acc_ma12_14 = acc_ma12_14_1 / 12

            acc_ma12_15_1 = price_16_close + price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close
            acc_ma12_15 = acc_ma12_15_1 / 12

            acc_ma12_16_1 = price_17_close + price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close
            acc_ma12_16 = acc_ma12_16_1 / 12

            acc_ma12_17_1 = price_18_close + price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close
            acc_ma12_17 = acc_ma12_17_1 / 12

            acc_ma12_18_1 = price_19_close + price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close
            acc_ma12_18 = acc_ma12_18_1 / 12

            acc_ma12_19_1 = price_20_close + price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close
            acc_ma12_19 = acc_ma12_19_1 / 12

            acc_ma12_20_1 = price_21_close + price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close
            acc_ma12_20 = acc_ma12_20_1 / 12

            acc_ma12_21_1 = price_22_close + price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close
            acc_ma12_21 = acc_ma12_21_1 / 12

            acc_ma12_22_1 = price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close
            acc_ma12_22 = acc_ma12_22_1 / 12

            acc_ma12_23_1 = price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close
            acc_ma12_23 = acc_ma12_23_1 / 12

            acc_ma12_24_1 = price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close
            acc_ma12_24 = acc_ma12_24_1 / 12

            acc_ma12_25_1 = price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close
            acc_ma12_25 = acc_ma12_25_1 / 12

            acc_ma12_26_1 = price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close
            acc_ma12_26 = acc_ma12_26_1 / 12

            acc_ma12_27_1 = price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close
            acc_ma12_27 = acc_ma12_27_1 / 12

            acc_ma12_28_1 = price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close
            acc_ma12_28 = acc_ma12_28_1 / 12

            acc_ma12_29_1 = price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close
            acc_ma12_30_1 = price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close
            acc_ma12_31_1 = price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close
            acc_ma12_32_1 = price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close
            acc_ma12_33_1 = price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close
            acc_ma12_34_1 = price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close
            acc_ma12_35_1 = price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close
            acc_ma12_36_1 = price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close
            acc_ma12_37_1 = price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close
            acc_ma12_38_1 = price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close
            acc_ma12_39_1 = price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close
            acc_ma12_40_1 = price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close
            acc_ma12_41_1 = price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close
            acc_ma12_42_1 = price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close
            acc_ma12_43_1 = price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close
            acc_ma12_44_1 = price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close
            acc_ma12_45_1 = price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close
            acc_ma12_46_1 = price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close
            acc_ma12_47_1 = price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close
            acc_ma12_48_1 = price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close
            acc_ma12_49_1 = price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close
            acc_ma12_50_1 = price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close
            acc_ma12_51_1 = price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close
            acc_ma12_52_1 = price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close
            acc_ma12_53_1 = price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close
            acc_ma12_54_1 = price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close
            acc_ma12_55_1 = price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close
            acc_ma12_56_1 = price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close


            # EMA - 단기 12 지수이동평균값 구하기
            acc_e_ma12_27 = acc_ma12_28
            acc_e_ma12_26 = ( price_27_close * ma12_sc )  + ( acc_e_ma12_27 * ( 1 - ma12_sc ) )
            acc_e_ma12_25 = ( price_26_close * ma12_sc )  + ( acc_e_ma12_26 * ( 1 - ma12_sc ) )

            acc_e_ma12_24 = ( price_25_close * ma12_sc )  + ( acc_e_ma12_25 * ( 1 - ma12_sc ) )
            acc_e_ma12_23 = ( price_24_close * ma12_sc )  + ( acc_e_ma12_24 * ( 1 - ma12_sc ) )
            acc_e_ma12_22 = ( price_23_close * ma12_sc )  + ( acc_e_ma12_23 * ( 1 - ma12_sc ) )
            acc_e_ma12_21 = ( price_22_close * ma12_sc )  + ( acc_e_ma12_22 * ( 1 - ma12_sc ) )
            acc_e_ma12_20 = ( price_21_close * ma12_sc )  + ( acc_e_ma12_21 * ( 1 - ma12_sc ) )
            acc_e_ma12_19 = ( price_20_close * ma12_sc )  + ( acc_e_ma12_20 * ( 1 - ma12_sc ) )
            acc_e_ma12_18 = ( price_19_close * ma12_sc )  + ( acc_e_ma12_19 * ( 1 - ma12_sc ) )
            acc_e_ma12_17 = ( price_18_close * ma12_sc )  + ( acc_e_ma12_18 * ( 1 - ma12_sc ) )
            acc_e_ma12_16 = ( price_17_close * ma12_sc )  + ( acc_e_ma12_17 * ( 1 - ma12_sc ) )
            acc_e_ma12_15 = ( price_16_close * ma12_sc )  + ( acc_e_ma12_16 * ( 1 - ma12_sc ) )
            acc_e_ma12_14 = ( price_15_close * ma12_sc )  + ( acc_e_ma12_15 * ( 1 - ma12_sc ) )
            acc_e_ma12_13 = ( price_14_close * ma12_sc )  + ( acc_e_ma12_14 * ( 1 - ma12_sc ) )

            acc_e_ma12_12 = ( price_13_close * ma12_sc )  + ( acc_e_ma12_13 * ( 1 - ma12_sc ) )
            acc_e_ma12_11 = ( price_12_close * ma12_sc )  + ( acc_e_ma12_12 * ( 1 - ma12_sc ) )
            acc_e_ma12_10 = ( price_11_close * ma12_sc )  + ( acc_e_ma12_11 * ( 1 - ma12_sc ) )
            acc_e_ma12_9 = ( price_10_close * ma12_sc )  + ( acc_e_ma12_10 * ( 1 - ma12_sc ) )
            acc_e_ma12_8 = ( price_9_close * ma12_sc )  + ( acc_e_ma12_9 * ( 1 - ma12_sc ) )
            acc_e_ma12_7 = ( price_8_close * ma12_sc )  + ( acc_e_ma12_8 * ( 1 - ma12_sc ) )
            acc_e_ma12_6 = ( price_7_close * ma12_sc )  + ( acc_e_ma12_7 * ( 1 - ma12_sc ) )
            acc_e_ma12_5 = ( price_6_close * ma12_sc )  + ( acc_e_ma12_6 * ( 1 - ma12_sc ) )
            acc_e_ma12_4 = ( price_5_close * ma12_sc )  + ( acc_e_ma12_5 * ( 1 - ma12_sc ) )
            acc_e_ma12_3 = ( price_4_close * ma12_sc )  + ( acc_e_ma12_4 * ( 1 - ma12_sc ) )
            acc_e_ma12_2 = ( price_3_close * ma12_sc )  + ( acc_e_ma12_3 * ( 1 - ma12_sc ) )
            acc_e_ma12_1 = ( price_2_close * ma12_sc )  + ( acc_e_ma12_2 * ( 1 - ma12_sc ) )



            # 여기까지






            # 장기 26 평활상수
            ma26_sc = 2 / ( 1 + 26 )


            # EMA - 장기 26 지수 종가 계산
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

            acc_ma26_10_1 = acc_ma12_10_1  +  price_23_close + price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close
            acc_ma26_10 = acc_ma26_10_1 / 26

            acc_ma26_11_1 = acc_ma12_11_1  +  price_24_close + price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close
            acc_ma26_11 = acc_ma26_11_1 / 26

            acc_ma26_12_1 = acc_ma12_12_1  +  price_25_close + price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close
            acc_ma26_12 = acc_ma26_12_1 / 26

            acc_ma26_13_1 = acc_ma12_13_1  +  price_26_close + price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close
            acc_ma26_13 = acc_ma26_13_1 / 26

            acc_ma26_14_1 = acc_ma12_14_1  +  price_27_close + price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close
            acc_ma26_14 = acc_ma26_14_1 / 26

            acc_ma26_15_1 = acc_ma12_15_1  +  price_28_close + price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close
            acc_ma26_15 = acc_ma26_15_1 / 26

            acc_ma26_16_1 = acc_ma12_16_1  +  price_29_close + price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close
            acc_ma26_16 = acc_ma26_16_1 / 26

            acc_ma26_17_1 = acc_ma12_17_1  +  price_30_close + price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close
            acc_ma26_17 = acc_ma26_17_1 / 26

            acc_ma26_18_1 = acc_ma12_18_1  +  price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close
            acc_ma26_18 = acc_ma26_18_1 / 26

            acc_ma26_19_1 = acc_ma12_19_1  +  price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close
            acc_ma26_19 = acc_ma26_19_1 / 26

            acc_ma26_20_1 = acc_ma12_20_1  +  price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close
            acc_ma26_20 = acc_ma26_20_1 / 26

            acc_ma26_21_1 = acc_ma12_21_1  +  price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close
            acc_ma26_21 = acc_ma26_21_1 / 26

            acc_ma26_22_1 = acc_ma12_22_1  +  price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close
            acc_ma26_22 = acc_ma26_22_1 / 26

            acc_ma26_23_1 = acc_ma12_23_1  +  price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close
            acc_ma26_23 = acc_ma26_23_1 / 26

            acc_ma26_24_1 = acc_ma12_24_1  +  price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close
            acc_ma26_24 = acc_ma26_24_1 / 26

            acc_ma26_25_1 = acc_ma12_25_1  +  price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close
            acc_ma26_25 = acc_ma26_25_1 / 26

            acc_ma26_26_1 = acc_ma12_26_1  +  price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close
            acc_ma26_26 = acc_ma26_26_1 / 26

            acc_ma26_27_1 = acc_ma12_27_1  +  price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close
            acc_ma26_27 = acc_ma26_27_1 / 26

            acc_ma26_28_1 = acc_ma12_28_1  +  price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close
            acc_ma26_28 = acc_ma26_28_1 / 26

            acc_ma26_29_1 = acc_ma12_29_1  +  price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close
            acc_ma26_29 = acc_ma26_29_1 / 26

            acc_ma26_30_1 = acc_ma12_30_1  +  price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close
            acc_ma26_30 = acc_ma26_30_1 / 26

            acc_ma26_31_1 = acc_ma12_31_1  +  price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close
            acc_ma26_31 = acc_ma26_31_1 / 26

            acc_ma26_32_1 = acc_ma12_32_1  +  price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close
            acc_ma26_32 = acc_ma26_32_1 / 26

            acc_ma26_33_1 = acc_ma12_33_1  +  price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close
            acc_ma26_33 = acc_ma26_33_1 / 26

            acc_ma26_34_1 = acc_ma12_34_1  +  price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close
            acc_ma26_34 = acc_ma26_34_1 / 26

            acc_ma26_35_1 = acc_ma12_35_1  +  price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close
            acc_ma26_35 = acc_ma26_35_1 / 26

            acc_ma26_36_1 = acc_ma12_36_1  +  price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close
            acc_ma26_36 = acc_ma26_36_1 / 26

            acc_ma26_37_1 = acc_ma12_37_1  +  price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close
            acc_ma26_37 = acc_ma26_37_1 / 26

            acc_ma26_38_1 = acc_ma12_38_1  +  price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close
            acc_ma26_38 = acc_ma26_38_1 / 26

            acc_ma26_39_1 = acc_ma12_39_1  +  price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close
            acc_ma26_39 = acc_ma26_39_1 / 26

            acc_ma26_40_1 = acc_ma12_40_1  +  price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close
            acc_ma26_40 = acc_ma26_40_1 / 26

            acc_ma26_41_1 = acc_ma12_41_1  +  price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close
            acc_ma26_41 = acc_ma26_41_1 / 26

            acc_ma26_42_1 = acc_ma12_42_1  +  price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close
            acc_ma26_42 = acc_ma26_42_1 / 26

            acc_ma26_43_1 = acc_ma12_43_1  +  price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close
            acc_ma26_43 = acc_ma26_43_1 / 26

            acc_ma26_44_1 = acc_ma12_44_1  +  price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close
            acc_ma26_44 = acc_ma26_44_1 / 26

            acc_ma26_45_1 = acc_ma12_45_1  +  price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close
            acc_ma26_45 = acc_ma26_45_1 / 26

            acc_ma26_46_1 = acc_ma12_46_1  +  price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close
            acc_ma26_46 = acc_ma26_46_1 / 26

            acc_ma26_47_1 = acc_ma12_47_1  +  price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close
            acc_ma26_47 = acc_ma26_47_1 / 26

            acc_ma26_48_1 = acc_ma12_48_1  +  price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close
            acc_ma26_48 = acc_ma26_48_1 / 26

            acc_ma26_49_1 = acc_ma12_49_1  +  price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close
            acc_ma26_49 = acc_ma26_49_1 / 26

            acc_ma26_50_1 = acc_ma12_50_1  +  price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close
            acc_ma26_50 = acc_ma26_50_1 / 26

            acc_ma26_51_1 = acc_ma12_51_1  +  price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close
            acc_ma26_51 = acc_ma26_51_1 / 26

            acc_ma26_52_1 = acc_ma12_52_1  +  price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close
            acc_ma26_52 = acc_ma26_52_1 / 26

            acc_ma26_53_1 = acc_ma12_53_1  +  price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close
            acc_ma26_53 = acc_ma26_53_1 / 26

            acc_ma26_54_1 = acc_ma12_54_1  +  price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close
            acc_ma26_54 = acc_ma26_54_1 / 26

            acc_ma26_55_1 = acc_ma12_55_1  +  price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close
            acc_ma26_55 = acc_ma26_55_1 / 26

            acc_ma26_56_1 = acc_ma12_56_1  +  price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close
            acc_ma26_56 = acc_ma26_56_1 / 26


            # EMA - 장기 26 지수이동평균값 구하기
            acc_e_ma26_55 = acc_ma26_56
            acc_e_ma26_54 = ( price_55_close * ma26_sc )  + ( acc_e_ma26_55 * ( 1 - ma26_sc ) )
            acc_e_ma26_53 = ( price_54_close * ma26_sc )  + ( acc_e_ma26_54 * ( 1 - ma26_sc ) )

            acc_e_ma26_52 = ( price_53_close * ma26_sc )  + ( acc_e_ma26_53 * ( 1 - ma26_sc ) )
            acc_e_ma26_51 = ( price_52_close * ma26_sc )  + ( acc_e_ma26_52 * ( 1 - ma26_sc ) )
            acc_e_ma26_50 = ( price_51_close * ma26_sc )  + ( acc_e_ma26_51 * ( 1 - ma26_sc ) )
            acc_e_ma26_49 = ( price_50_close * ma26_sc )  + ( acc_e_ma26_50 * ( 1 - ma26_sc ) )
            acc_e_ma26_48 = ( price_49_close * ma26_sc )  + ( acc_e_ma26_49 * ( 1 - ma26_sc ) )
            acc_e_ma26_47 = ( price_48_close * ma26_sc )  + ( acc_e_ma26_48 * ( 1 - ma26_sc ) )
            acc_e_ma26_46 = ( price_47_close * ma26_sc )  + ( acc_e_ma26_47 * ( 1 - ma26_sc ) )
            acc_e_ma26_45 = ( price_46_close * ma26_sc )  + ( acc_e_ma26_46 * ( 1 - ma26_sc ) )
            acc_e_ma26_44 = ( price_45_close * ma26_sc )  + ( acc_e_ma26_45 * ( 1 - ma26_sc ) )
            acc_e_ma26_43 = ( price_44_close * ma26_sc )  + ( acc_e_ma26_44 * ( 1 - ma26_sc ) )
            acc_e_ma26_42 = ( price_43_close * ma26_sc )  + ( acc_e_ma26_43 * ( 1 - ma26_sc ) )
            acc_e_ma26_41 = ( price_42_close * ma26_sc )  + ( acc_e_ma26_42 * ( 1 - ma26_sc ) )
            acc_e_ma26_40 = ( price_41_close * ma26_sc )  + ( acc_e_ma26_41 * ( 1 - ma26_sc ) )
            acc_e_ma26_39 = ( price_40_close * ma26_sc )  + ( acc_e_ma26_40 * ( 1 - ma26_sc ) )
            acc_e_ma26_38 = ( price_39_close * ma26_sc )  + ( acc_e_ma26_39 * ( 1 - ma26_sc ) )
            acc_e_ma26_37 = ( price_38_close * ma26_sc )  + ( acc_e_ma26_38 * ( 1 - ma26_sc ) )
            acc_e_ma26_36 = ( price_37_close * ma26_sc )  + ( acc_e_ma26_37 * ( 1 - ma26_sc ) )
            acc_e_ma26_35 = ( price_36_close * ma26_sc )  + ( acc_e_ma26_36 * ( 1 - ma26_sc ) )
            acc_e_ma26_34 = ( price_35_close * ma26_sc )  + ( acc_e_ma26_35 * ( 1 - ma26_sc ) )
            acc_e_ma26_33 = ( price_34_close * ma26_sc )  + ( acc_e_ma26_34 * ( 1 - ma26_sc ) )
            acc_e_ma26_32 = ( price_33_close * ma26_sc )  + ( acc_e_ma26_33 * ( 1 - ma26_sc ) )
            acc_e_ma26_31 = ( price_32_close * ma26_sc )  + ( acc_e_ma26_32 * ( 1 - ma26_sc ) )
            acc_e_ma26_30 = ( price_31_close * ma26_sc )  + ( acc_e_ma26_31 * ( 1 - ma26_sc ) )
            acc_e_ma26_29 = ( price_30_close * ma26_sc )  + ( acc_e_ma26_30 * ( 1 - ma26_sc ) )
            acc_e_ma26_28 = ( price_29_close * ma26_sc )  + ( acc_e_ma26_29 * ( 1 - ma26_sc ) )
            acc_e_ma26_27 = ( price_28_close * ma26_sc )  + ( acc_e_ma26_28 * ( 1 - ma26_sc ) )

            acc_e_ma26_26 = ( price_27_close * ma26_sc )  + ( acc_e_ma26_27 * ( 1 - ma26_sc ) )
            acc_e_ma26_25 = ( price_26_close * ma26_sc )  + ( acc_e_ma26_26 * ( 1 - ma26_sc ) )
            acc_e_ma26_24 = ( price_25_close * ma26_sc )  + ( acc_e_ma26_25 * ( 1 - ma26_sc ) )
            acc_e_ma26_23 = ( price_24_close * ma26_sc )  + ( acc_e_ma26_24 * ( 1 - ma26_sc ) )
            acc_e_ma26_22 = ( price_23_close * ma26_sc )  + ( acc_e_ma26_23 * ( 1 - ma26_sc ) )
            acc_e_ma26_21 = ( price_22_close * ma26_sc )  + ( acc_e_ma26_22 * ( 1 - ma26_sc ) )
            acc_e_ma26_20 = ( price_21_close * ma26_sc )  + ( acc_e_ma26_21 * ( 1 - ma26_sc ) )
            acc_e_ma26_19 = ( price_20_close * ma26_sc )  + ( acc_e_ma26_20 * ( 1 - ma26_sc ) )
            acc_e_ma26_18 = ( price_19_close * ma26_sc )  + ( acc_e_ma26_19 * ( 1 - ma26_sc ) )
            acc_e_ma26_17 = ( price_18_close * ma26_sc )  + ( acc_e_ma26_18 * ( 1 - ma26_sc ) )
            acc_e_ma26_16 = ( price_17_close * ma26_sc )  + ( acc_e_ma26_17 * ( 1 - ma26_sc ) )
            acc_e_ma26_15 = ( price_16_close * ma26_sc )  + ( acc_e_ma26_16 * ( 1 - ma26_sc ) )
            acc_e_ma26_14 = ( price_15_close * ma26_sc )  + ( acc_e_ma26_15 * ( 1 - ma26_sc ) )
            acc_e_ma26_13 = ( price_14_close * ma26_sc )  + ( acc_e_ma26_14 * ( 1 - ma26_sc ) )
            acc_e_ma26_12 = ( price_13_close * ma26_sc )  + ( acc_e_ma26_13 * ( 1 - ma26_sc ) )
            acc_e_ma26_11 = ( price_12_close * ma26_sc )  + ( acc_e_ma26_12 * ( 1 - ma26_sc ) )
            acc_e_ma26_10 = ( price_11_close * ma26_sc )  + ( acc_e_ma26_11 * ( 1 - ma26_sc ) )
            acc_e_ma26_9 = ( price_10_close * ma26_sc )  + ( acc_e_ma26_10 * ( 1 - ma26_sc ) )
            acc_e_ma26_8 = ( price_9_close * ma26_sc )  + ( acc_e_ma26_9 * ( 1 - ma26_sc ) )
            acc_e_ma26_7 = ( price_8_close * ma26_sc )  + ( acc_e_ma26_8 * ( 1 - ma26_sc ) )
            acc_e_ma26_6 = ( price_7_close * ma26_sc )  + ( acc_e_ma26_7 * ( 1 - ma26_sc ) )
            acc_e_ma26_5 = ( price_6_close * ma26_sc )  + ( acc_e_ma26_6 * ( 1 - ma26_sc ) )
            acc_e_ma26_4 = ( price_5_close * ma26_sc )  + ( acc_e_ma26_5 * ( 1 - ma26_sc ) )
            acc_e_ma26_3 = ( price_4_close * ma26_sc )  + ( acc_e_ma26_4 * ( 1 - ma26_sc ) )
            acc_e_ma26_2 = ( price_3_close * ma26_sc )  + ( acc_e_ma26_3 * ( 1 - ma26_sc ) )
            acc_e_ma26_1 = ( price_2_close * ma26_sc )  + ( acc_e_ma26_2 * ( 1 - ma26_sc ) )

            # 여기까지






            # macd
            # 단기12일이평선 - 장기26일이평선 = + 는 0선 이상, - 는 0선 이하
            print("macd값")
            print("========== ========== ========== ========== ==========")
            acc_macd_ok_1 = acc_e_ma12_1 - acc_e_ma26_1
            print( f"e_macd_ok_1 ( {acc_macd_ok_1} ) =  acc_e_ma12_1 ( {acc_e_ma12_1} ) - acc_e_ma26_1 ( {acc_e_ma26_1} )")

            acc_macd_ok_2 = acc_e_ma12_2 - acc_e_ma26_2
            print( f"e_macd_ok_2 ( {acc_macd_ok_2} ) =  acc_e_ma12_2 ( {acc_e_ma12_2} ) - acc_e_ma26_2 ( {acc_e_ma26_2} )")

            acc_macd_ok_3 = acc_e_ma12_3 - acc_e_ma26_3
            print( f"e_macd_ok_3 ( {acc_macd_ok_3} ) =  acc_e_ma12_3 ( {acc_e_ma12_3} ) - acc_e_ma26_3 ( {acc_e_ma26_3} )")

            acc_macd_ok_4 = acc_e_ma12_4 - acc_e_ma26_4
            print( f"e_macd_ok_4 ( {acc_macd_ok_4} ) =  acc_e_ma12_4 ( {acc_e_ma12_4} ) - acc_e_ma26_4 ( {acc_e_ma26_4} )")

            acc_macd_ok_5 = acc_e_ma12_5 - acc_e_ma26_5
            print( f"e_macd_ok_5 ( {acc_macd_ok_5} ) =  acc_e_ma12_5 ( {acc_e_ma12_5} ) - acc_e_ma26_5 ( {acc_e_ma26_5} )")

            acc_macd_ok_6 = acc_e_ma12_6 - acc_e_ma26_6
            print( f"e_macd_ok_6 ( {acc_macd_ok_6} ) =  acc_e_ma12_6 ( {acc_e_ma12_6} ) - acc_e_ma26_6 ( {acc_e_ma26_6} )")

            acc_macd_ok_7 = acc_e_ma12_7 - acc_e_ma26_7
            print( f"e_macd_ok_7 ( {acc_macd_ok_7} ) =  acc_e_ma12_7 ( {acc_e_ma12_7} ) - acc_e_ma26_7 ( {acc_e_ma26_7} )")

            acc_macd_ok_8 = acc_e_ma12_8 - acc_e_ma26_8
            print( f"e_macd_ok_8 ( {acc_macd_ok_8} ) =  acc_e_ma12_8 ( {acc_e_ma12_8} ) - acc_e_ma26_8 ( {acc_e_ma26_8} )")

            acc_macd_ok_9 = acc_e_ma12_9 - acc_e_ma26_9
            print( f"e_macd_ok_9 ( {acc_macd_ok_9} ) =  acc_e_ma12_9 ( {acc_e_ma12_9} ) - acc_e_ma26_9 ( {acc_e_ma26_9} )")

            acc_macd_ok_10 = acc_e_ma12_10 - acc_e_ma26_10
            print( f"e_macd_ok_10 ( {acc_macd_ok_10} ) =  acc_e_ma12_10 ( {acc_e_ma12_10} ) - acc_e_ma26_10 ( {acc_e_ma26_10} )")

            acc_macd_ok_11 = acc_e_ma12_11 - acc_e_ma26_11
            print( f"e_macd_ok_11 ( {acc_macd_ok_11} ) =  acc_e_ma12_11 ( {acc_e_ma12_11} ) - acc_e_ma26_11 ( {acc_e_ma26_11} )")

            acc_macd_ok_12 = acc_e_ma12_12 - acc_e_ma26_12
            print( f"e_macd_ok_12 ( {acc_macd_ok_12} ) =  acc_e_ma12_12 ( {acc_e_ma12_12} ) - acc_e_ma26_12 ( {acc_e_ma26_12} )")

            acc_macd_ok_13 = acc_e_ma12_13 - acc_e_ma26_13
            print( f"e_macd_ok_13 ( {acc_macd_ok_13} ) =  acc_e_ma12_13 ( {acc_e_ma12_13} ) - acc_e_ma26_13 ( {acc_e_ma26_13} )")

            acc_macd_ok_14 = acc_e_ma12_14 - acc_e_ma26_14
            print( f"e_macd_ok_14 ( {acc_macd_ok_14} ) =  acc_e_ma12_14 ( {acc_e_ma12_14} ) - acc_e_ma26_14 ( {acc_e_ma26_14} )")

            acc_macd_ok_15 = acc_e_ma12_15 - acc_e_ma26_15
            print( f"e_macd_ok_15 ( {acc_macd_ok_15} ) =  acc_e_ma12_15 ( {acc_e_ma12_15} ) - acc_e_ma26_15 ( {acc_e_ma26_15} )")

            acc_macd_ok_16 = acc_e_ma12_16 - acc_e_ma26_16
            print( f"e_macd_ok_16 ( {acc_macd_ok_16} ) =  acc_e_ma12_16 ( {acc_e_ma12_16} ) - acc_e_ma26_16 ( {acc_e_ma26_16} )")

            acc_macd_ok_17 = acc_e_ma12_17 - acc_e_ma26_17
            print( f"e_macd_ok_17 ( {acc_macd_ok_17} ) =  acc_e_ma12_17 ( {acc_e_ma12_17} ) - acc_e_ma26_17 ( {acc_e_ma26_17} )")
            print()





            print("시그널값")
            print("========== ========== ========== ========== ==========")
            # signal = macd 9일선, macd값의 9이평선.
            # + 는 0선 이상, - 는 0선 이하
            acc_signal_1 = ( acc_macd_ok_1 + acc_macd_ok_2 + acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 ) / 9
            print(f"acc_signal_1 = ( {acc_signal_1} )")

            acc_signal_2 = ( acc_macd_ok_2 + acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 ) / 9
            print(f"acc_signal_2 = ( {acc_signal_2} )")

            acc_signal_3 = ( acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 ) / 9
            print(f"acc_signal_3 = ( {acc_signal_3} )")

            acc_signal_4 = ( acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 ) / 9
            print(f"acc_signal_4 = ( {acc_signal_4} )")

            acc_signal_5 = ( acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 ) / 9
            print(f"acc_signal_5 = ( {acc_signal_5} )")

            acc_signal_6 = ( acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 ) / 9
            print(f"acc_signal_6 = ( {acc_signal_6} )")

            acc_signal_7 = ( acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 ) / 9
            print(f"acc_signal_7 = ( {acc_signal_7} )")

            acc_signal_8 = ( acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 + acc_macd_ok_16 ) / 9
            print(f"acc_signal_8 = ( {acc_signal_8} )")

            acc_signal_9 = ( acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 + acc_macd_ok_16 + acc_macd_ok_17 ) / 9
            print(f"acc_signal_9 = ( {acc_signal_9} )")

            print()

            # 최종값
            # macd - 시그널 = + 는 골든크로스, - 는 데드크로스
            print("[최종] 간격 = macd - 시그널")
            print("========== ========== ========== ========== ==========")
            acc_macd1 = acc_macd_ok_1 - acc_signal_1
            print(f"acc_macd1 ( {acc_macd1} ) = acc_macd_ok_1 ( {acc_macd_ok_1} ) - acc_signal_1 ( {acc_signal_1} )")
            acc_macd2 = acc_macd_ok_2 - acc_signal_2
            print(f"acc_macd2 ( {acc_macd2} ) = acc_macd_ok_2 ( {acc_macd_ok_2} ) - acc_signal_2 ( {acc_signal_2} )")
            acc_macd3 = acc_macd_ok_3 - acc_signal_3
            print(f"acc_macd3 ( {acc_macd3} ) = acc_macd_ok_3 ( {acc_macd_ok_3} ) - acc_signal_3 ( {acc_signal_3} )")
            acc_macd4 = acc_macd_ok_4 - acc_signal_4
            print(f"acc_macd4 ( {acc_macd4} ) = acc_macd_ok_4 ( {acc_macd_ok_4} ) - acc_signal_4 ( {acc_signal_4} )")
            acc_macd5 = acc_macd_ok_5 - acc_signal_5
            print(f"acc_macd5 ( {acc_macd5} ) = acc_macd_ok_5 ( {acc_macd_ok_5} ) - acc_signal_5 ( {acc_signal_5} )")
            acc_macd6 = acc_macd_ok_6 - acc_signal_6
            print(f"acc_macd6 ( {acc_macd6} ) = acc_macd_ok_6 ( {acc_macd_ok_6} ) - acc_signal_6 ( {acc_signal_6} )")
            acc_macd7 = acc_macd_ok_7 - acc_signal_7
            print(f"acc_macd7 ( {acc_macd7} ) = acc_macd_ok_7 ( {acc_macd_ok_7} ) - acc_signal_7 ( {acc_signal_7} )")
            print()

            ##### 거래량 동반한 macd 산출. 끝 #####
            #####################################





            #####################################
            ##### macd 매매선택              #####

            # acc_macd_select
            #if acc_signal_1 >= 0:
            #    if acc_macd1 >= 0:
            #        # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 골든크로스
            #        acc_macd_select = 1
            #    else:
            #        # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 데드크로스
            #        acc_macd_select = 2
            #else:
            #    if acc_macd1 >= 0:
            #        # acc_ma26_1이 기준선 아래에 있을때, acc_macd1이 골든크로스
            #        acc_macd_select = 3
            #    else:
            #        # acc_ma26_1이 기준선 아래에 있을때, acc_macd1이 데드크로스
            #        acc_macd_select = 4

            if acc_macd1 >= 0:
                # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 골든크로스
                acc_macd_select = 1
            else:
                # acc_ma26_1이 기준선 위에 있을때, acc_macd1이 데드크로스
                acc_macd_select = 2

            print(f"acc_macd_select = {acc_macd_select}")
            print()

            time.sleep(1)







            print("========== MACD 계산 ==========")
            print()




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


            