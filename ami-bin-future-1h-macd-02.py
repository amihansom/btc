import ccxt
import pprint
import pandas as pd
import time
import datetime
import math




# 사용중인 API이름 - ami220919
api_key = "cJd9RduMyRGJAcJrFH0X46jXVt1GIYUdzjSKz8h9UzzyI9YG3BCQEzX2cISPu26S"
secret = "9SZlkczvEvSBybI6L6qGl9wNd0LnDvyFWarVbyTrFr9WYGCoNmIXOuutDWVkvdJK"

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
        timeframe = '1h', 
        since = None, 
        limit = 200
    )

    df = pd.DataFrame( data = btc, columns = [ 'datetime', 'open', 'high', 'low', 'close', 'volume' ] )
    df[ 'datetime' ] = pd.to_datetime( df[ 'datetime' ], unit = 'ms' )
    df.set_index( 'datetime', inplace = True )

    print( df )
    print()


    # 종가받기 200개
    print( "========== 1시간봉 종가 받기 ==========" )
    print()
    # 0은 아무것도 아님.
    price_0_close = df.iloc[ 0 ][ 'close' ]
    #price_0_time = df.iloc[ 0 ][ 'datetime' ]

    # -1은 현재가.
    price_1_close = df.iloc[ -1 ][ 'close' ]

    ########################################
    # -2는 1시간전 종가. 여기부터 macd 계산.
    price_2_close = df.iloc[ -2 ][ 'close' ]
    price_3_close = df.iloc[ -3 ][ 'close' ]
    price_4_close = df.iloc[ -4 ][ 'close' ]
    price_5_close = df.iloc[ -5 ][ 'close' ]
    price_6_close = df.iloc[ -6 ][ 'close' ]
    price_7_close = df.iloc[ -7 ][ 'close' ]
    price_8_close = df.iloc[ -8 ][ 'close' ]
    price_9_close = df.iloc[ -9 ][ 'close' ]
    price_10_close = df.iloc[ -10 ][ 'close' ]

    price_11_close = df.iloc[ -11 ][ 'close' ]
    price_12_close = df.iloc[ -12 ][ 'close' ]
    price_13_close = df.iloc[ -13 ][ 'close' ]
    price_14_close = df.iloc[ -14 ][ 'close' ]
    price_15_close = df.iloc[ -15 ][ 'close' ]
    price_16_close = df.iloc[ -16 ][ 'close' ]
    price_17_close = df.iloc[ -17 ][ 'close' ]
    price_18_close = df.iloc[ -18 ][ 'close' ]
    price_19_close = df.iloc[ -19 ][ 'close' ]
    price_20_close = df.iloc[ -20 ][ 'close' ]

    price_21_close = df.iloc[ -21 ][ 'close' ]
    price_22_close = df.iloc[ -22 ][ 'close' ]
    price_23_close = df.iloc[ -23 ][ 'close' ]
    price_24_close = df.iloc[ -24 ][ 'close' ]
    price_25_close = df.iloc[ -25 ][ 'close' ]
    price_26_close = df.iloc[ -26 ][ 'close' ]
    price_27_close = df.iloc[ -27 ][ 'close' ]
    price_28_close = df.iloc[ -28 ][ 'close' ]
    price_29_close = df.iloc[ -29 ][ 'close' ]
    price_30_close = df.iloc[ -30 ][ 'close' ]

    price_31_close = df.iloc[ -31 ][ 'close' ]
    price_32_close = df.iloc[ -32 ][ 'close' ]
    price_33_close = df.iloc[ -33 ][ 'close' ]
    price_34_close = df.iloc[ -34 ][ 'close' ]
    price_35_close = df.iloc[ -35 ][ 'close' ]
    price_36_close = df.iloc[ -36 ][ 'close' ]
    price_37_close = df.iloc[ -37 ][ 'close' ]
    price_38_close = df.iloc[ -38 ][ 'close' ]
    price_39_close = df.iloc[ -39 ][ 'close' ]
    price_40_close = df.iloc[ -40 ][ 'close' ]

    price_41_close = df.iloc[ -41 ][ 'close' ]
    price_42_close = df.iloc[ -42 ][ 'close' ]
    price_43_close = df.iloc[ -43 ][ 'close' ]
    price_44_close = df.iloc[ -44 ][ 'close' ]
    price_45_close = df.iloc[ -45 ][ 'close' ]
    price_46_close = df.iloc[ -46 ][ 'close' ]
    price_47_close = df.iloc[ -47 ][ 'close' ]
    price_48_close = df.iloc[ -48 ][ 'close' ]
    price_49_close = df.iloc[ -49 ][ 'close' ]
    price_50_close = df.iloc[ -50 ][ 'close' ]

    price_51_close = df.iloc[ -51 ][ 'close' ]
    price_52_close = df.iloc[ -52 ][ 'close' ]
    price_53_close = df.iloc[ -53 ][ 'close' ]
    price_54_close = df.iloc[ -54 ][ 'close' ]
    price_55_close = df.iloc[ -55 ][ 'close' ]
    price_56_close = df.iloc[ -56 ][ 'close' ]
    price_57_close = df.iloc[ -57 ][ 'close' ]
    price_58_close = df.iloc[ -58 ][ 'close' ]
    price_59_close = df.iloc[ -59 ][ 'close' ]
    price_60_close = df.iloc[ -60 ][ 'close' ]

    price_61_close = df.iloc[ -61 ][ 'close' ]
    price_62_close = df.iloc[ -62 ][ 'close' ]
    price_63_close = df.iloc[ -63 ][ 'close' ]
    price_64_close = df.iloc[ -64 ][ 'close' ]
    price_65_close = df.iloc[ -65 ][ 'close' ]
    price_66_close = df.iloc[ -66 ][ 'close' ]
    price_67_close = df.iloc[ -67 ][ 'close' ]
    price_68_close = df.iloc[ -68 ][ 'close' ]
    price_69_close = df.iloc[ -69 ][ 'close' ]
    price_70_close = df.iloc[ -70 ][ 'close' ]

    price_71_close = df.iloc[ -71 ][ 'close' ]
    price_72_close = df.iloc[ -72 ][ 'close' ]
    price_73_close = df.iloc[ -73 ][ 'close' ]
    price_74_close = df.iloc[ -74 ][ 'close' ]
    price_75_close = df.iloc[ -75 ][ 'close' ]
    price_76_close = df.iloc[ -76 ][ 'close' ]
    price_77_close = df.iloc[ -77 ][ 'close' ]
    price_78_close = df.iloc[ -78 ][ 'close' ]
    price_79_close = df.iloc[ -79 ][ 'close' ]
    price_80_close = df.iloc[ -80 ][ 'close' ]

    price_81_close = df.iloc[ -81 ][ 'close' ]
    price_82_close = df.iloc[ -82 ][ 'close' ]
    price_83_close = df.iloc[ -83 ][ 'close' ]
    price_84_close = df.iloc[ -84 ][ 'close' ]
    price_85_close = df.iloc[ -85 ][ 'close' ]
    price_86_close = df.iloc[ -86 ][ 'close' ]
    price_87_close = df.iloc[ -87 ][ 'close' ]
    price_88_close = df.iloc[ -88 ][ 'close' ]
    price_89_close = df.iloc[ -89 ][ 'close' ]
    price_90_close = df.iloc[ -90 ][ 'close' ]

    price_91_close = df.iloc[ -91 ][ 'close' ]
    price_92_close = df.iloc[ -92 ][ 'close' ]
    price_93_close = df.iloc[ -93 ][ 'close' ]
    price_94_close = df.iloc[ -94 ][ 'close' ]
    price_95_close = df.iloc[ -95 ][ 'close' ]
    price_96_close = df.iloc[ -96 ][ 'close' ]
    price_97_close = df.iloc[ -97 ][ 'close' ]
    price_98_close = df.iloc[ -98 ][ 'close' ]
    price_99_close = df.iloc[ -99 ][ 'close' ]
    price_100_close = df.iloc[ -100 ][ 'close' ]

    price_101_close = df.iloc[ -101 ][ 'close' ]
    price_102_close = df.iloc[ -102 ][ 'close' ]
    price_103_close = df.iloc[ -103 ][ 'close' ]
    price_104_close = df.iloc[ -104 ][ 'close' ]
    price_105_close = df.iloc[ -105 ][ 'close' ]
    price_106_close = df.iloc[ -106 ][ 'close' ]
    price_107_close = df.iloc[ -107 ][ 'close' ]
    price_108_close = df.iloc[ -108 ][ 'close' ]
    price_109_close = df.iloc[ -109 ][ 'close' ]
    price_110_close = df.iloc[ -110 ][ 'close' ]

    price_111_close = df.iloc[ -111 ][ 'close' ]
    price_112_close = df.iloc[ -112 ][ 'close' ]
    price_113_close = df.iloc[ -113 ][ 'close' ]
    price_114_close = df.iloc[ -114 ][ 'close' ]
    price_115_close = df.iloc[ -115 ][ 'close' ]
    price_116_close = df.iloc[ -116 ][ 'close' ]
    price_117_close = df.iloc[ -117 ][ 'close' ]
    price_118_close = df.iloc[ -118 ][ 'close' ]
    price_119_close = df.iloc[ -119 ][ 'close' ]
    price_120_close = df.iloc[ -120 ][ 'close' ]

    price_121_close = df.iloc[ -121 ][ 'close' ]
    price_122_close = df.iloc[ -122 ][ 'close' ]
    price_123_close = df.iloc[ -123 ][ 'close' ]
    price_124_close = df.iloc[ -124 ][ 'close' ]
    price_125_close = df.iloc[ -125 ][ 'close' ]
    price_126_close = df.iloc[ -126 ][ 'close' ]
    price_127_close = df.iloc[ -127 ][ 'close' ]
    price_128_close = df.iloc[ -128 ][ 'close' ]
    price_129_close = df.iloc[ -129 ][ 'close' ]
    price_130_close = df.iloc[ -130 ][ 'close' ]

    price_131_close = df.iloc[ -131 ][ 'close' ]
    price_132_close = df.iloc[ -132 ][ 'close' ]
    price_133_close = df.iloc[ -133 ][ 'close' ]
    price_134_close = df.iloc[ -134 ][ 'close' ]
    price_135_close = df.iloc[ -135 ][ 'close' ]
    price_136_close = df.iloc[ -136 ][ 'close' ]
    price_137_close = df.iloc[ -137 ][ 'close' ]
    price_138_close = df.iloc[ -138 ][ 'close' ]
    price_139_close = df.iloc[ -139 ][ 'close' ]
    price_140_close = df.iloc[ -140 ][ 'close' ]

    price_141_close = df.iloc[ -141 ][ 'close' ]
    price_142_close = df.iloc[ -142 ][ 'close' ]
    price_143_close = df.iloc[ -143 ][ 'close' ]
    price_144_close = df.iloc[ -144 ][ 'close' ]
    price_145_close = df.iloc[ -145 ][ 'close' ]
    price_146_close = df.iloc[ -146 ][ 'close' ]
    price_147_close = df.iloc[ -147 ][ 'close' ]
    price_148_close = df.iloc[ -148 ][ 'close' ]
    price_149_close = df.iloc[ -149 ][ 'close' ]
    price_150_close = df.iloc[ -150 ][ 'close' ]

    price_151_close = df.iloc[ -151 ][ 'close' ]
    price_152_close = df.iloc[ -152 ][ 'close' ]
    price_153_close = df.iloc[ -153 ][ 'close' ]
    price_154_close = df.iloc[ -154 ][ 'close' ]
    price_155_close = df.iloc[ -155 ][ 'close' ]
    price_156_close = df.iloc[ -156 ][ 'close' ]
    price_157_close = df.iloc[ -157 ][ 'close' ]
    price_158_close = df.iloc[ -158 ][ 'close' ]
    price_159_close = df.iloc[ -159 ][ 'close' ]
    price_160_close = df.iloc[ -160 ][ 'close' ]

    price_161_close = df.iloc[ -161 ][ 'close' ]
    price_162_close = df.iloc[ -162 ][ 'close' ]
    price_163_close = df.iloc[ -163 ][ 'close' ]
    price_164_close = df.iloc[ -164 ][ 'close' ]
    price_165_close = df.iloc[ -165 ][ 'close' ]
    price_166_close = df.iloc[ -166 ][ 'close' ]
    price_167_close = df.iloc[ -167 ][ 'close' ]
    price_168_close = df.iloc[ -168 ][ 'close' ]
    price_169_close = df.iloc[ -169 ][ 'close' ]
    price_170_close = df.iloc[ -170 ][ 'close' ]

    price_171_close = df.iloc[ -171 ][ 'close' ]
    price_172_close = df.iloc[ -172 ][ 'close' ]
    price_173_close = df.iloc[ -173 ][ 'close' ]
    price_174_close = df.iloc[ -174 ][ 'close' ]
    price_175_close = df.iloc[ -175 ][ 'close' ]
    price_176_close = df.iloc[ -176 ][ 'close' ]
    price_177_close = df.iloc[ -177 ][ 'close' ]
    price_178_close = df.iloc[ -178 ][ 'close' ]
    price_179_close = df.iloc[ -179 ][ 'close' ]
    price_180_close = df.iloc[ -180 ][ 'close' ]

    price_181_close = df.iloc[ -181 ][ 'close' ]
    price_182_close = df.iloc[ -182 ][ 'close' ]
    price_183_close = df.iloc[ -183 ][ 'close' ]
    price_184_close = df.iloc[ -184 ][ 'close' ]
    price_185_close = df.iloc[ -185 ][ 'close' ]
    price_186_close = df.iloc[ -186 ][ 'close' ]
    price_187_close = df.iloc[ -187 ][ 'close' ]
    price_188_close = df.iloc[ -188 ][ 'close' ]
    price_189_close = df.iloc[ -189 ][ 'close' ]
    price_190_close = df.iloc[ -190 ][ 'close' ]











        

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
    acc_ma12_29 = acc_ma12_29_1 / 12
    acc_ma12_30_1 = price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close
    acc_ma12_30 = acc_ma12_30_1 / 12


    acc_ma12_31_1 = price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close
    acc_ma12_31 = acc_ma12_31_1 / 12
    acc_ma12_32_1 = price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close
    acc_ma12_32 = acc_ma12_32_1 / 12
    acc_ma12_33_1 = price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close
    acc_ma12_33 = acc_ma12_33_1 / 12
    acc_ma12_34_1 = price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close
    acc_ma12_34 = acc_ma12_34_1 / 12
    acc_ma12_35_1 = price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close
    acc_ma12_35 = acc_ma12_35_1 / 12

    acc_ma12_36_1 = price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close
    acc_ma12_36 = acc_ma12_36_1 / 12
    acc_ma12_37_1 = price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close
    acc_ma12_37 = acc_ma12_37_1 / 12
    acc_ma12_38_1 = price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close
    acc_ma12_38 = acc_ma12_38_1 / 12
    acc_ma12_39_1 = price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close
    acc_ma12_39 = acc_ma12_39_1 / 12
    acc_ma12_40_1 = price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close
    acc_ma12_40 = acc_ma12_40_1 / 12


    acc_ma12_41_1 = price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close
    acc_ma12_41 = acc_ma12_41_1 / 12
    acc_ma12_42_1 = price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close
    acc_ma12_42 = acc_ma12_42_1 / 12
    acc_ma12_43_1 = price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close
    acc_ma12_43 = acc_ma12_43_1 / 12
    acc_ma12_44_1 = price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close
    acc_ma12_44 = acc_ma12_44_1 / 12
    acc_ma12_45_1 = price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close
    acc_ma12_45 = acc_ma12_45_1 / 12

    acc_ma12_46_1 = price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close
    acc_ma12_46 = acc_ma12_46_1 / 12
    acc_ma12_47_1 = price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close
    acc_ma12_47 = acc_ma12_47_1 / 12
    acc_ma12_48_1 = price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close
    acc_ma12_48 = acc_ma12_48_1 / 12
    acc_ma12_49_1 = price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close
    acc_ma12_49 = acc_ma12_49_1 / 12
    acc_ma12_50_1 = price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close
    acc_ma12_50 = acc_ma12_50_1 / 12


    acc_ma12_51_1 = price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close
    acc_ma12_51 = acc_ma12_51_1 / 12
    acc_ma12_52_1 = price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close
    acc_ma12_52 = acc_ma12_52_1 / 12
    acc_ma12_53_1 = price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close
    acc_ma12_53 = acc_ma12_53_1 / 12
    acc_ma12_54_1 = price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close
    acc_ma12_54 = acc_ma12_54_1 / 12
    acc_ma12_55_1 = price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close
    acc_ma12_55 = acc_ma12_55_1 / 12

    acc_ma12_56_1 = price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close
    acc_ma12_56 = acc_ma12_56_1 / 12
    acc_ma12_57_1 = price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close
    acc_ma12_57 = acc_ma12_57_1 / 12
    acc_ma12_58_1 = price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close
    acc_ma12_58 = acc_ma12_58_1 / 12
    acc_ma12_59_1 = price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close
    acc_ma12_59 = acc_ma12_59_1 / 12
    acc_ma12_60_1 = price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close
    acc_ma12_60 = acc_ma12_60_1 / 12


    acc_ma12_61_1 = price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close
    acc_ma12_61 = acc_ma12_61_1 / 12
    acc_ma12_62_1 = price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close
    acc_ma12_62 = acc_ma12_62_1 / 12
    acc_ma12_63_1 = price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close
    acc_ma12_63 = acc_ma12_63_1 / 12
    acc_ma12_64_1 = price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close
    acc_ma12_64 = acc_ma12_64_1 / 12
    acc_ma12_65_1 = price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close
    acc_ma12_65 = acc_ma12_65_1 / 12

    acc_ma12_66_1 = price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close
    acc_ma12_66 = acc_ma12_66_1 / 12
    acc_ma12_67_1 = price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close
    acc_ma12_67 = acc_ma12_67_1 / 12
    acc_ma12_68_1 = price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close
    acc_ma12_68 = acc_ma12_68_1 / 12
    acc_ma12_69_1 = price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close
    acc_ma12_69 = acc_ma12_69_1 / 12
    acc_ma12_70_1 = price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close
    acc_ma12_70 = acc_ma12_70_1 / 12


    acc_ma12_71_1 = price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close
    acc_ma12_71 = acc_ma12_71_1 / 12
    acc_ma12_72_1 = price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close
    acc_ma12_72 = acc_ma12_72_1 / 12
    acc_ma12_73_1 = price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close
    acc_ma12_73 = acc_ma12_73_1 / 12
    acc_ma12_74_1 = price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close
    acc_ma12_74 = acc_ma12_74_1 / 12
    acc_ma12_75_1 = price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close
    acc_ma12_75 = acc_ma12_75_1 / 12

    acc_ma12_76_1 = price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close
    acc_ma12_76 = acc_ma12_76_1 / 12
    acc_ma12_77_1 = price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close
    acc_ma12_77 = acc_ma12_77_1 / 12
    acc_ma12_78_1 = price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close
    acc_ma12_78 = acc_ma12_78_1 / 12
    acc_ma12_79_1 = price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close
    acc_ma12_79 = acc_ma12_79_1 / 12
    acc_ma12_80_1 = price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close
    acc_ma12_80 = acc_ma12_80_1 / 12


    acc_ma12_81_1 = price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close
    acc_ma12_81 = acc_ma12_81_1 / 12
    acc_ma12_82_1 = price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close
    acc_ma12_82 = acc_ma12_82_1 / 12
    acc_ma12_83_1 = price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close
    acc_ma12_83 = acc_ma12_83_1 / 12
    acc_ma12_84_1 = price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close
    acc_ma12_84 = acc_ma12_84_1 / 12
    acc_ma12_85_1 = price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close
    acc_ma12_85 = acc_ma12_85_1 / 12

    acc_ma12_86_1 = price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close
    acc_ma12_86 = acc_ma12_86_1 / 12
    acc_ma12_87_1 = price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close
    acc_ma12_87 = acc_ma12_87_1 / 12
    acc_ma12_88_1 = price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close
    acc_ma12_88 = acc_ma12_88_1 / 12
    acc_ma12_89_1 = price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close
    acc_ma12_89 = acc_ma12_89_1 / 12
    acc_ma12_90_1 = price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close
    acc_ma12_90 = acc_ma12_90_1 / 12


    acc_ma12_91_1 = price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close
    acc_ma12_91 = acc_ma12_91_1 / 12
    acc_ma12_92_1 = price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close
    acc_ma12_92 = acc_ma12_92_1 / 12
    acc_ma12_93_1 = price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close
    acc_ma12_93 = acc_ma12_93_1 / 12
    acc_ma12_94_1 = price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close
    acc_ma12_94 = acc_ma12_94_1 / 12
    acc_ma12_95_1 = price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close
    acc_ma12_95 = acc_ma12_95_1 / 12

    acc_ma12_96_1 = price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close
    acc_ma12_96 = acc_ma12_96_1 / 12
    acc_ma12_97_1 = price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close
    acc_ma12_97 = acc_ma12_97_1 / 12
    acc_ma12_98_1 = price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close
    acc_ma12_98 = acc_ma12_98_1 / 12
    acc_ma12_99_1 = price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close
    acc_ma12_99 = acc_ma12_99_1 / 12
    acc_ma12_100_1 = price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close
    acc_ma12_100 = acc_ma12_100_1 / 12


    acc_ma12_101_1 = price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close
    acc_ma12_101 = acc_ma12_101_1 / 12
    acc_ma12_102_1 = price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close
    acc_ma12_102 = acc_ma12_102_1 / 12
    acc_ma12_103_1 = price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close
    acc_ma12_103 = acc_ma12_103_1 / 12
    acc_ma12_104_1 = price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close
    acc_ma12_104 = acc_ma12_104_1 / 12
    acc_ma12_105_1 = price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close
    acc_ma12_105 = acc_ma12_105_1 / 12

    acc_ma12_106_1 = price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close
    acc_ma12_106 = acc_ma12_106_1 / 12
    acc_ma12_107_1 = price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close
    acc_ma12_107 = acc_ma12_107_1 / 12
    acc_ma12_108_1 = price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close
    acc_ma12_108 = acc_ma12_108_1 / 12
    acc_ma12_109_1 = price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close
    acc_ma12_109 = acc_ma12_109_1 / 12
    acc_ma12_110_1 = price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close
    acc_ma12_110 = acc_ma12_110_1 / 12


    acc_ma12_111_1 = price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close
    acc_ma12_111 = acc_ma12_111_1 / 12
    acc_ma12_112_1 = price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close
    acc_ma12_112 = acc_ma12_112_1 / 12
    acc_ma12_113_1 = price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close
    acc_ma12_113 = acc_ma12_113_1 / 12
    acc_ma12_114_1 = price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close
    acc_ma12_114 = acc_ma12_114_1 / 12
    acc_ma12_115_1 = price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close
    acc_ma12_115 = acc_ma12_115_1 / 12

    acc_ma12_116_1 = price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close
    acc_ma12_116 = acc_ma12_116_1 / 12
    acc_ma12_117_1 = price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close
    acc_ma12_117 = acc_ma12_117_1 / 12
    acc_ma12_118_1 = price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close
    acc_ma12_118 = acc_ma12_118_1 / 12
    acc_ma12_119_1 = price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close
    acc_ma12_119 = acc_ma12_119_1 / 12
    acc_ma12_120_1 = price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close
    acc_ma12_120 = acc_ma12_120_1 / 12

    acc_ma12_121_1 = price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close
    acc_ma12_121 = acc_ma12_121_1 / 12
    acc_ma12_122_1 = price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close
    acc_ma12_122 = acc_ma12_122_1 / 12
    acc_ma12_123_1 = price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close
    acc_ma12_123 = acc_ma12_123_1 / 12
    acc_ma12_124_1 = price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close
    acc_ma12_124 = acc_ma12_124_1 / 12
    acc_ma12_125_1 = price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close
    acc_ma12_125 = acc_ma12_125_1 / 12

    acc_ma12_126_1 = price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close
    acc_ma12_126 = acc_ma12_126_1 / 12
    acc_ma12_127_1 = price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close
    acc_ma12_127 = acc_ma12_127_1 / 12
    acc_ma12_128_1 = price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close
    acc_ma12_128 = acc_ma12_128_1 / 12
    acc_ma12_129_1 = price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close
    acc_ma12_129 = acc_ma12_129_1 / 12
    acc_ma12_130_1 = price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close
    acc_ma12_130 = acc_ma12_130_1 / 12


    acc_ma12_131_1 = price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close
    acc_ma12_131 = acc_ma12_131_1 / 12
    acc_ma12_132_1 = price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close
    acc_ma12_132 = acc_ma12_132_1 / 12
    acc_ma12_133_1 = price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close
    acc_ma12_133 = acc_ma12_133_1 / 12
    acc_ma12_134_1 = price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close
    acc_ma12_134 = acc_ma12_134_1 / 12
    acc_ma12_135_1 = price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close
    acc_ma12_135 = acc_ma12_135_1 / 12

    acc_ma12_136_1 = price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close
    acc_ma12_136 = acc_ma12_136_1 / 12
    acc_ma12_137_1 = price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close
    acc_ma12_137 = acc_ma12_137_1 / 12
    acc_ma12_138_1 = price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close
    acc_ma12_138 = acc_ma12_138_1 / 12
    acc_ma12_139_1 = price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close
    acc_ma12_139 = acc_ma12_139_1 / 12
    acc_ma12_140_1 = price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close
    acc_ma12_140 = acc_ma12_140_1 / 12








    # EMA - 단기 12 지수이동평균값 구하기
    acc_e_ma12_139 = acc_ma12_140
    acc_e_ma12_138 = ( price_139_close * ma12_sc )  + ( acc_e_ma12_139 * ( 1 - ma12_sc ) )
    acc_e_ma12_137 = ( price_138_close * ma12_sc )  + ( acc_e_ma12_138 * ( 1 - ma12_sc ) )
    acc_e_ma12_136 = ( price_137_close * ma12_sc )  + ( acc_e_ma12_137 * ( 1 - ma12_sc ) )
    acc_e_ma12_135 = ( price_136_close * ma12_sc )  + ( acc_e_ma12_136 * ( 1 - ma12_sc ) )
    acc_e_ma12_134 = ( price_135_close * ma12_sc )  + ( acc_e_ma12_135 * ( 1 - ma12_sc ) )
    acc_e_ma12_133 = ( price_134_close * ma12_sc )  + ( acc_e_ma12_134 * ( 1 - ma12_sc ) )
    acc_e_ma12_132 = ( price_133_close * ma12_sc )  + ( acc_e_ma12_133 * ( 1 - ma12_sc ) )
    acc_e_ma12_131 = ( price_132_close * ma12_sc )  + ( acc_e_ma12_132 * ( 1 - ma12_sc ) )

    acc_e_ma12_130 = ( price_131_close * ma12_sc )  + ( acc_e_ma12_131 * ( 1 - ma12_sc ) )
    acc_e_ma12_129 = ( price_130_close * ma12_sc )  + ( acc_e_ma12_130 * ( 1 - ma12_sc ) )
    acc_e_ma12_128 = ( price_129_close * ma12_sc )  + ( acc_e_ma12_129 * ( 1 - ma12_sc ) )
    acc_e_ma12_127 = ( price_128_close * ma12_sc )  + ( acc_e_ma12_128 * ( 1 - ma12_sc ) )
    acc_e_ma12_126 = ( price_127_close * ma12_sc )  + ( acc_e_ma12_127 * ( 1 - ma12_sc ) )
    acc_e_ma12_125 = ( price_126_close * ma12_sc )  + ( acc_e_ma12_126 * ( 1 - ma12_sc ) )
    acc_e_ma12_124 = ( price_125_close * ma12_sc )  + ( acc_e_ma12_125 * ( 1 - ma12_sc ) )
    acc_e_ma12_123 = ( price_124_close * ma12_sc )  + ( acc_e_ma12_124 * ( 1 - ma12_sc ) )
    acc_e_ma12_122 = ( price_123_close * ma12_sc )  + ( acc_e_ma12_123 * ( 1 - ma12_sc ) )
    acc_e_ma12_121 = ( price_122_close * ma12_sc )  + ( acc_e_ma12_122 * ( 1 - ma12_sc ) )

    acc_e_ma12_120 = ( price_121_close * ma12_sc )  + ( acc_e_ma12_121 * ( 1 - ma12_sc ) )
    acc_e_ma12_119 = ( price_120_close * ma12_sc )  + ( acc_e_ma12_120 * ( 1 - ma12_sc ) )
    acc_e_ma12_118 = ( price_119_close * ma12_sc )  + ( acc_e_ma12_119 * ( 1 - ma12_sc ) )
    acc_e_ma12_117 = ( price_118_close * ma12_sc )  + ( acc_e_ma12_118 * ( 1 - ma12_sc ) )
    acc_e_ma12_116 = ( price_117_close * ma12_sc )  + ( acc_e_ma12_117 * ( 1 - ma12_sc ) )
    acc_e_ma12_115 = ( price_116_close * ma12_sc )  + ( acc_e_ma12_116 * ( 1 - ma12_sc ) )
    acc_e_ma12_114 = ( price_115_close * ma12_sc )  + ( acc_e_ma12_115 * ( 1 - ma12_sc ) )
    acc_e_ma12_113 = ( price_114_close * ma12_sc )  + ( acc_e_ma12_114 * ( 1 - ma12_sc ) )
    acc_e_ma12_112 = ( price_113_close * ma12_sc )  + ( acc_e_ma12_113 * ( 1 - ma12_sc ) )
    acc_e_ma12_111 = ( price_112_close * ma12_sc )  + ( acc_e_ma12_112 * ( 1 - ma12_sc ) )

    acc_e_ma12_110 = ( price_111_close * ma12_sc )  + ( acc_e_ma12_111 * ( 1 - ma12_sc ) )
    acc_e_ma12_109 = ( price_110_close * ma12_sc )  + ( acc_e_ma12_110 * ( 1 - ma12_sc ) )
    acc_e_ma12_108 = ( price_109_close * ma12_sc )  + ( acc_e_ma12_109 * ( 1 - ma12_sc ) )
    acc_e_ma12_107 = ( price_108_close * ma12_sc )  + ( acc_e_ma12_108 * ( 1 - ma12_sc ) )
    acc_e_ma12_106 = ( price_107_close * ma12_sc )  + ( acc_e_ma12_107 * ( 1 - ma12_sc ) )
    acc_e_ma12_105 = ( price_106_close * ma12_sc )  + ( acc_e_ma12_106 * ( 1 - ma12_sc ) )
    acc_e_ma12_104 = ( price_105_close * ma12_sc )  + ( acc_e_ma12_105 * ( 1 - ma12_sc ) )
    acc_e_ma12_103 = ( price_104_close * ma12_sc )  + ( acc_e_ma12_104 * ( 1 - ma12_sc ) )
    acc_e_ma12_102 = ( price_103_close * ma12_sc )  + ( acc_e_ma12_103 * ( 1 - ma12_sc ) )
    acc_e_ma12_101 = ( price_102_close * ma12_sc )  + ( acc_e_ma12_102 * ( 1 - ma12_sc ) )

    acc_e_ma12_100 = ( price_101_close * ma12_sc )  + ( acc_e_ma12_101 * ( 1 - ma12_sc ) )
    acc_e_ma12_99 = ( price_100_close * ma12_sc )  + ( acc_e_ma12_100 * ( 1 - ma12_sc ) )
    acc_e_ma12_98 = ( price_99_close * ma12_sc )  + ( acc_e_ma12_99 * ( 1 - ma12_sc ) )
    acc_e_ma12_97 = ( price_98_close * ma12_sc )  + ( acc_e_ma12_98 * ( 1 - ma12_sc ) )
    acc_e_ma12_96 = ( price_97_close * ma12_sc )  + ( acc_e_ma12_97 * ( 1 - ma12_sc ) )
    acc_e_ma12_95 = ( price_96_close * ma12_sc )  + ( acc_e_ma12_96 * ( 1 - ma12_sc ) )
    acc_e_ma12_94 = ( price_95_close * ma12_sc )  + ( acc_e_ma12_95 * ( 1 - ma12_sc ) )
    acc_e_ma12_93 = ( price_94_close * ma12_sc )  + ( acc_e_ma12_94 * ( 1 - ma12_sc ) )
    acc_e_ma12_92 = ( price_93_close * ma12_sc )  + ( acc_e_ma12_93 * ( 1 - ma12_sc ) )
    acc_e_ma12_91 = ( price_92_close * ma12_sc )  + ( acc_e_ma12_92 * ( 1 - ma12_sc ) )

    acc_e_ma12_90 = ( price_91_close * ma12_sc )  + ( acc_e_ma12_91 * ( 1 - ma12_sc ) )
    acc_e_ma12_89 = ( price_90_close * ma12_sc )  + ( acc_e_ma12_90 * ( 1 - ma12_sc ) )
    acc_e_ma12_88 = ( price_89_close * ma12_sc )  + ( acc_e_ma12_89 * ( 1 - ma12_sc ) )
    acc_e_ma12_87 = ( price_88_close * ma12_sc )  + ( acc_e_ma12_88 * ( 1 - ma12_sc ) )
    acc_e_ma12_86 = ( price_87_close * ma12_sc )  + ( acc_e_ma12_87 * ( 1 - ma12_sc ) )
    acc_e_ma12_85 = ( price_86_close * ma12_sc )  + ( acc_e_ma12_86 * ( 1 - ma12_sc ) )
    acc_e_ma12_84 = ( price_85_close * ma12_sc )  + ( acc_e_ma12_85 * ( 1 - ma12_sc ) )
    acc_e_ma12_83 = ( price_84_close * ma12_sc )  + ( acc_e_ma12_84 * ( 1 - ma12_sc ) )
    acc_e_ma12_82 = ( price_83_close * ma12_sc )  + ( acc_e_ma12_83 * ( 1 - ma12_sc ) )
    acc_e_ma12_81 = ( price_82_close * ma12_sc )  + ( acc_e_ma12_82 * ( 1 - ma12_sc ) )

    acc_e_ma12_80 = ( price_81_close * ma12_sc )  + ( acc_e_ma12_81 * ( 1 - ma12_sc ) )
    acc_e_ma12_79 = ( price_80_close * ma12_sc )  + ( acc_e_ma12_80 * ( 1 - ma12_sc ) )
    acc_e_ma12_78 = ( price_79_close * ma12_sc )  + ( acc_e_ma12_79 * ( 1 - ma12_sc ) )
    acc_e_ma12_77 = ( price_78_close * ma12_sc )  + ( acc_e_ma12_78 * ( 1 - ma12_sc ) )
    acc_e_ma12_76 = ( price_77_close * ma12_sc )  + ( acc_e_ma12_77 * ( 1 - ma12_sc ) )
    acc_e_ma12_75 = ( price_76_close * ma12_sc )  + ( acc_e_ma12_76 * ( 1 - ma12_sc ) )
    acc_e_ma12_74 = ( price_75_close * ma12_sc )  + ( acc_e_ma12_75 * ( 1 - ma12_sc ) )
    acc_e_ma12_73 = ( price_74_close * ma12_sc )  + ( acc_e_ma12_74 * ( 1 - ma12_sc ) )
    acc_e_ma12_72 = ( price_73_close * ma12_sc )  + ( acc_e_ma12_73 * ( 1 - ma12_sc ) )
    acc_e_ma12_71 = ( price_72_close * ma12_sc )  + ( acc_e_ma12_72 * ( 1 - ma12_sc ) )

    acc_e_ma12_70 = ( price_71_close * ma12_sc )  + ( acc_e_ma12_71 * ( 1 - ma12_sc ) )
    acc_e_ma12_69 = ( price_70_close * ma12_sc )  + ( acc_e_ma12_70 * ( 1 - ma12_sc ) )
    acc_e_ma12_68 = ( price_69_close * ma12_sc )  + ( acc_e_ma12_69 * ( 1 - ma12_sc ) )
    acc_e_ma12_67 = ( price_68_close * ma12_sc )  + ( acc_e_ma12_68 * ( 1 - ma12_sc ) )
    acc_e_ma12_66 = ( price_67_close * ma12_sc )  + ( acc_e_ma12_67 * ( 1 - ma12_sc ) )
    acc_e_ma12_65 = ( price_66_close * ma12_sc )  + ( acc_e_ma12_66 * ( 1 - ma12_sc ) )
    acc_e_ma12_64 = ( price_65_close * ma12_sc )  + ( acc_e_ma12_65 * ( 1 - ma12_sc ) )
    acc_e_ma12_63 = ( price_64_close * ma12_sc )  + ( acc_e_ma12_64 * ( 1 - ma12_sc ) )
    acc_e_ma12_62 = ( price_63_close * ma12_sc )  + ( acc_e_ma12_63 * ( 1 - ma12_sc ) )
    acc_e_ma12_61 = ( price_62_close * ma12_sc )  + ( acc_e_ma12_62 * ( 1 - ma12_sc ) )

    acc_e_ma12_60 = ( price_61_close * ma12_sc )  + ( acc_e_ma12_61 * ( 1 - ma12_sc ) )
    acc_e_ma12_59 = ( price_60_close * ma12_sc )  + ( acc_e_ma12_60 * ( 1 - ma12_sc ) )
    acc_e_ma12_58 = ( price_59_close * ma12_sc )  + ( acc_e_ma12_59 * ( 1 - ma12_sc ) )
    acc_e_ma12_57 = ( price_58_close * ma12_sc )  + ( acc_e_ma12_58 * ( 1 - ma12_sc ) )
    acc_e_ma12_56 = ( price_57_close * ma12_sc )  + ( acc_e_ma12_57 * ( 1 - ma12_sc ) )
    acc_e_ma12_55 = ( price_56_close * ma12_sc )  + ( acc_e_ma12_56 * ( 1 - ma12_sc ) )
    acc_e_ma12_54 = ( price_55_close * ma12_sc )  + ( acc_e_ma12_55 * ( 1 - ma12_sc ) )
    acc_e_ma12_53 = ( price_54_close * ma12_sc )  + ( acc_e_ma12_54 * ( 1 - ma12_sc ) )
    acc_e_ma12_52 = ( price_53_close * ma12_sc )  + ( acc_e_ma12_53 * ( 1 - ma12_sc ) )
    acc_e_ma12_51 = ( price_52_close * ma12_sc )  + ( acc_e_ma12_52 * ( 1 - ma12_sc ) )

    acc_e_ma12_50 = ( price_51_close * ma12_sc )  + ( acc_e_ma12_51 * ( 1 - ma12_sc ) )
    acc_e_ma12_49 = ( price_50_close * ma12_sc )  + ( acc_e_ma12_50 * ( 1 - ma12_sc ) )
    acc_e_ma12_48 = ( price_49_close * ma12_sc )  + ( acc_e_ma12_49 * ( 1 - ma12_sc ) )
    acc_e_ma12_47 = ( price_48_close * ma12_sc )  + ( acc_e_ma12_48 * ( 1 - ma12_sc ) )
    acc_e_ma12_46 = ( price_47_close * ma12_sc )  + ( acc_e_ma12_47 * ( 1 - ma12_sc ) )
    acc_e_ma12_45 = ( price_46_close * ma12_sc )  + ( acc_e_ma12_46 * ( 1 - ma12_sc ) )
    acc_e_ma12_44 = ( price_45_close * ma12_sc )  + ( acc_e_ma12_45 * ( 1 - ma12_sc ) )
    acc_e_ma12_43 = ( price_44_close * ma12_sc )  + ( acc_e_ma12_44 * ( 1 - ma12_sc ) )
    acc_e_ma12_42 = ( price_43_close * ma12_sc )  + ( acc_e_ma12_43 * ( 1 - ma12_sc ) )
    acc_e_ma12_41 = ( price_42_close * ma12_sc )  + ( acc_e_ma12_42 * ( 1 - ma12_sc ) )

    acc_e_ma12_40 = ( price_41_close * ma12_sc )  + ( acc_e_ma12_41 * ( 1 - ma12_sc ) )
    acc_e_ma12_39 = ( price_40_close * ma12_sc )  + ( acc_e_ma12_40 * ( 1 - ma12_sc ) )
    acc_e_ma12_38 = ( price_39_close * ma12_sc )  + ( acc_e_ma12_39 * ( 1 - ma12_sc ) )
    acc_e_ma12_37 = ( price_38_close * ma12_sc )  + ( acc_e_ma12_38 * ( 1 - ma12_sc ) )
    acc_e_ma12_36 = ( price_37_close * ma12_sc )  + ( acc_e_ma12_37 * ( 1 - ma12_sc ) )
    acc_e_ma12_35 = ( price_36_close * ma12_sc )  + ( acc_e_ma12_36 * ( 1 - ma12_sc ) )
    acc_e_ma12_34 = ( price_35_close * ma12_sc )  + ( acc_e_ma12_35 * ( 1 - ma12_sc ) )
    acc_e_ma12_33 = ( price_34_close * ma12_sc )  + ( acc_e_ma12_34 * ( 1 - ma12_sc ) )
    acc_e_ma12_32 = ( price_33_close * ma12_sc )  + ( acc_e_ma12_33 * ( 1 - ma12_sc ) )
    acc_e_ma12_31 = ( price_32_close * ma12_sc )  + ( acc_e_ma12_32 * ( 1 - ma12_sc ) )

    acc_e_ma12_30 = ( price_31_close * ma12_sc )  + ( acc_e_ma12_31 * ( 1 - ma12_sc ) )
    acc_e_ma12_29 = ( price_30_close * ma12_sc )  + ( acc_e_ma12_30 * ( 1 - ma12_sc ) )
    acc_e_ma12_28 = ( price_29_close * ma12_sc )  + ( acc_e_ma12_29 * ( 1 - ma12_sc ) )
    acc_e_ma12_27 = ( price_28_close * ma12_sc )  + ( acc_e_ma12_28 * ( 1 - ma12_sc ) )
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
    acc_ma26_57_1 = acc_ma12_57_1  +  price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close
    acc_ma26_57 = acc_ma26_57_1 / 26
    acc_ma26_58_1 = acc_ma12_58_1  +  price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close
    acc_ma26_58 = acc_ma26_58_1 / 26
    acc_ma26_59_1 = acc_ma12_59_1  +  price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close
    acc_ma26_59 = acc_ma26_59_1 / 26
    acc_ma26_60_1 = acc_ma12_60_1  +  price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close
    acc_ma26_60 = acc_ma26_60_1 / 26


    acc_ma26_61_1 = acc_ma12_61_1  +  price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close
    acc_ma26_61 = acc_ma26_61_1 / 26
    acc_ma26_62_1 = acc_ma12_62_1  +  price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close
    acc_ma26_62 = acc_ma26_62_1 / 26
    acc_ma26_63_1 = acc_ma12_63_1  +  price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close
    acc_ma26_63 = acc_ma26_63_1 / 26
    acc_ma26_64_1 = acc_ma12_64_1  +  price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close
    acc_ma26_64 = acc_ma26_64_1 / 26
    acc_ma26_65_1 = acc_ma12_65_1  +  price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close
    acc_ma26_65 = acc_ma26_65_1 / 26

    acc_ma26_66_1 = acc_ma12_66_1  +  price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close
    acc_ma26_66 = acc_ma26_66_1 / 26
    acc_ma26_67_1 = acc_ma12_67_1  +  price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close
    acc_ma26_67 = acc_ma26_67_1 / 26
    acc_ma26_68_1 = acc_ma12_68_1  +  price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close
    acc_ma26_68 = acc_ma26_68_1 / 26
    acc_ma26_69_1 = acc_ma12_69_1  +  price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close
    acc_ma26_69 = acc_ma26_69_1 / 26
    acc_ma26_70_1 = acc_ma12_70_1  +  price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close
    acc_ma26_70 = acc_ma26_70_1 / 26


    acc_ma26_71_1 = acc_ma12_71_1  +  price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close
    acc_ma26_71 = acc_ma26_71_1 / 26
    acc_ma26_72_1 = acc_ma12_72_1  +  price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close
    acc_ma26_72 = acc_ma26_72_1 / 26
    acc_ma26_73_1 = acc_ma12_73_1  +  price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close
    acc_ma26_73 = acc_ma26_73_1 / 26
    acc_ma26_74_1 = acc_ma12_74_1  +  price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close
    acc_ma26_74 = acc_ma26_74_1 / 26
    acc_ma26_75_1 = acc_ma12_75_1  +  price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close
    acc_ma26_75 = acc_ma26_75_1 / 26

    acc_ma26_76_1 = acc_ma12_76_1  +  price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close
    acc_ma26_76 = acc_ma26_76_1 / 26
    acc_ma26_77_1 = acc_ma12_77_1  +  price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close
    acc_ma26_77 = acc_ma26_77_1 / 26
    acc_ma26_78_1 = acc_ma12_78_1  +  price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close
    acc_ma26_78 = acc_ma26_78_1 / 26
    acc_ma26_79_1 = acc_ma12_79_1  +  price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close
    acc_ma26_79 = acc_ma26_79_1 / 26
    acc_ma26_80_1 = acc_ma12_80_1  +  price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close
    acc_ma26_80 = acc_ma26_80_1 / 26


    acc_ma26_81_1 = acc_ma12_81_1  +  price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close
    acc_ma26_81 = acc_ma26_81_1 / 26
    acc_ma26_82_1 = acc_ma12_82_1  +  price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close
    acc_ma26_82 = acc_ma26_82_1 / 26
    acc_ma26_83_1 = acc_ma12_83_1  +  price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close
    acc_ma26_83 = acc_ma26_83_1 / 26
    acc_ma26_84_1 = acc_ma12_84_1  +  price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close
    acc_ma26_84 = acc_ma26_84_1 / 26
    acc_ma26_85_1 = acc_ma12_85_1  +  price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close
    acc_ma26_85 = acc_ma26_85_1 / 26

    acc_ma26_86_1 = acc_ma12_86_1  +  price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close
    acc_ma26_86 = acc_ma26_86_1 / 26
    acc_ma26_87_1 = acc_ma12_87_1  +  price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close
    acc_ma26_87 = acc_ma26_87_1 / 26
    acc_ma26_88_1 = acc_ma12_88_1  +  price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close
    acc_ma26_88 = acc_ma26_88_1 / 26
    acc_ma26_89_1 = acc_ma12_89_1  +  price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close
    acc_ma26_89 = acc_ma26_89_1 / 26
    acc_ma26_90_1 = acc_ma12_90_1  +  price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close
    acc_ma26_90 = acc_ma26_90_1 / 26


    acc_ma26_91_1 = acc_ma12_91_1  +  price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close
    acc_ma26_91 = acc_ma26_91_1 / 26
    acc_ma26_92_1 = acc_ma12_92_1  +  price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close
    acc_ma26_92 = acc_ma26_92_1 / 26
    acc_ma26_93_1 = acc_ma12_93_1  +  price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close
    acc_ma26_93 = acc_ma26_93_1 / 26
    acc_ma26_94_1 = acc_ma12_94_1  +  price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close
    acc_ma26_94 = acc_ma26_94_1 / 26
    acc_ma26_95_1 = acc_ma12_95_1  +  price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close
    acc_ma26_95 = acc_ma26_95_1 / 26

    acc_ma26_96_1 = acc_ma12_96_1  +  price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close
    acc_ma26_96 = acc_ma26_96_1 / 26
    acc_ma26_97_1 = acc_ma12_97_1  +  price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close
    acc_ma26_97 = acc_ma26_97_1 / 26
    acc_ma26_98_1 = acc_ma12_98_1  +  price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close
    acc_ma26_98 = acc_ma26_98_1 / 26
    acc_ma26_99_1 = acc_ma12_99_1  +  price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close
    acc_ma26_99 = acc_ma26_99_1 / 26
    acc_ma26_100_1 = acc_ma12_100_1  +  price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close
    acc_ma26_100 = acc_ma26_100_1 / 26


    acc_ma26_101_1 = acc_ma12_101_1  +  price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close
    acc_ma26_101 = acc_ma26_101_1 / 26
    acc_ma26_102_1 = acc_ma12_102_1  +  price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close
    acc_ma26_102 = acc_ma26_102_1 / 26
    acc_ma26_103_1 = acc_ma12_103_1  +  price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close
    acc_ma26_103 = acc_ma26_103_1 / 26
    acc_ma26_104_1 = acc_ma12_104_1  +  price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close
    acc_ma26_104 = acc_ma26_104_1 / 26
    acc_ma26_105_1 = acc_ma12_105_1  +  price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close
    acc_ma26_105 = acc_ma26_105_1 / 26

    acc_ma26_106_1 = acc_ma12_106_1  +  price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close
    acc_ma26_106 = acc_ma26_106_1 / 26
    acc_ma26_107_1 = acc_ma12_107_1  +  price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close
    acc_ma26_107 = acc_ma26_107_1 / 26
    acc_ma26_108_1 = acc_ma12_108_1  +  price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close
    acc_ma26_108 = acc_ma26_108_1 / 26
    acc_ma26_109_1 = acc_ma12_109_1  +  price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close
    acc_ma26_109 = acc_ma26_109_1 / 26
    acc_ma26_110_1 = acc_ma12_110_1  +  price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close
    acc_ma26_110 = acc_ma26_110_1 / 26


    acc_ma26_111_1 = acc_ma12_111_1  +  price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close
    acc_ma26_111 = acc_ma26_111_1 / 26
    acc_ma26_112_1 = acc_ma12_112_1  +  price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close
    acc_ma26_112 = acc_ma26_112_1 / 26
    acc_ma26_113_1 = acc_ma12_113_1  +  price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close
    acc_ma26_113 = acc_ma26_113_1 / 26
    acc_ma26_114_1 = acc_ma12_114_1  +  price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close
    acc_ma26_114 = acc_ma26_114_1 / 26
    acc_ma26_115_1 = acc_ma12_115_1  +  price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close
    acc_ma26_115 = acc_ma26_115_1 / 26

    acc_ma26_116_1 = acc_ma12_116_1  +  price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close
    acc_ma26_116 = acc_ma26_116_1 / 26
    acc_ma26_117_1 = acc_ma12_117_1  +  price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close
    acc_ma26_117 = acc_ma26_117_1 / 26
    acc_ma26_118_1 = acc_ma12_118_1  +  price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close
    acc_ma26_118 = acc_ma26_118_1 / 26
    acc_ma26_119_1 = acc_ma12_119_1  +  price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close
    acc_ma26_119 = acc_ma26_119_1 / 26
    acc_ma26_120_1 = acc_ma12_120_1  +  price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close
    acc_ma26_120 = acc_ma26_120_1 / 26


    acc_ma26_121_1 = acc_ma12_121_1  +  price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close
    acc_ma26_121 = acc_ma26_121_1 / 26
    acc_ma26_122_1 = acc_ma12_122_1  +  price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close
    acc_ma26_122 = acc_ma26_122_1 / 26
    acc_ma26_123_1 = acc_ma12_123_1  +  price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close
    acc_ma26_123 = acc_ma26_123_1 / 26
    acc_ma26_124_1 = acc_ma12_124_1  +  price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close
    acc_ma26_124 = acc_ma26_124_1 / 26
    acc_ma26_125_1 = acc_ma12_125_1  +  price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close
    acc_ma26_125 = acc_ma26_125_1 / 26

    acc_ma26_126_1 = acc_ma12_126_1  +  price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close
    acc_ma26_126 = acc_ma26_126_1 / 26
    acc_ma26_127_1 = acc_ma12_127_1  +  price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close
    acc_ma26_127 = acc_ma26_127_1 / 26
    acc_ma26_128_1 = acc_ma12_128_1  +  price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close
    acc_ma26_128 = acc_ma26_128_1 / 26
    acc_ma26_129_1 = acc_ma12_129_1  +  price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close
    acc_ma26_129 = acc_ma26_129_1 / 26
    acc_ma26_130_1 = acc_ma12_130_1  +  price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close
    acc_ma26_130 = acc_ma26_130_1 / 26


    acc_ma26_131_1 = acc_ma12_131_1  +  price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close
    acc_ma26_131 = acc_ma26_131_1 / 26
    acc_ma26_132_1 = acc_ma12_132_1  +  price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close
    acc_ma26_132 = acc_ma26_132_1 / 26
    acc_ma26_133_1 = acc_ma12_133_1  +  price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close
    acc_ma26_133 = acc_ma26_133_1 / 26
    acc_ma26_134_1 = acc_ma12_134_1  +  price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close
    acc_ma26_134 = acc_ma26_134_1 / 26
    acc_ma26_135_1 = acc_ma12_135_1  +  price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close
    acc_ma26_135 = acc_ma26_135_1 / 26

    acc_ma26_136_1 = acc_ma12_136_1  +  price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close
    acc_ma26_136 = acc_ma26_136_1 / 26
    acc_ma26_137_1 = acc_ma12_137_1  +  price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close + price_163_close
    acc_ma26_137 = acc_ma26_137_1 / 26
    acc_ma26_138_1 = acc_ma12_138_1  +  price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close + price_163_close + price_164_close
    acc_ma26_138 = acc_ma26_138_1 / 26
    acc_ma26_139_1 = acc_ma12_139_1  +  price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close + price_163_close + price_164_close + price_165_close
    acc_ma26_139 = acc_ma26_139_1 / 26
    acc_ma26_140_1 = acc_ma12_140_1  +  price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close + price_163_close + price_164_close + price_165_close + price_166_close
    acc_ma26_140 = acc_ma26_140_1 / 26








    # EMA - 장기 26 지수이동평균값 구하기
    acc_e_ma26_139 = acc_ma26_140
    acc_e_ma26_138 = ( price_139_close * ma26_sc )  + ( acc_e_ma26_139 * ( 1 - ma26_sc ) )
    acc_e_ma26_137 = ( price_138_close * ma26_sc )  + ( acc_e_ma26_138 * ( 1 - ma26_sc ) )
    acc_e_ma26_136 = ( price_137_close * ma26_sc )  + ( acc_e_ma26_137 * ( 1 - ma26_sc ) )
    acc_e_ma26_135 = ( price_136_close * ma26_sc )  + ( acc_e_ma26_136 * ( 1 - ma26_sc ) )
    acc_e_ma26_134 = ( price_135_close * ma26_sc )  + ( acc_e_ma26_135 * ( 1 - ma26_sc ) )
    acc_e_ma26_133 = ( price_134_close * ma26_sc )  + ( acc_e_ma26_134 * ( 1 - ma26_sc ) )
    acc_e_ma26_132 = ( price_133_close * ma26_sc )  + ( acc_e_ma26_133 * ( 1 - ma26_sc ) )
    acc_e_ma26_131 = ( price_132_close * ma26_sc )  + ( acc_e_ma26_132 * ( 1 - ma26_sc ) )

    acc_e_ma26_130 = ( price_131_close * ma26_sc )  + ( acc_e_ma26_131 * ( 1 - ma26_sc ) )
    acc_e_ma26_129 = ( price_130_close * ma26_sc )  + ( acc_e_ma26_130 * ( 1 - ma26_sc ) )
    acc_e_ma26_128 = ( price_129_close * ma26_sc )  + ( acc_e_ma26_129 * ( 1 - ma26_sc ) )
    acc_e_ma26_127 = ( price_128_close * ma26_sc )  + ( acc_e_ma26_128 * ( 1 - ma26_sc ) )
    acc_e_ma26_126 = ( price_127_close * ma26_sc )  + ( acc_e_ma26_127 * ( 1 - ma26_sc ) )
    acc_e_ma26_125 = ( price_126_close * ma26_sc )  + ( acc_e_ma26_126 * ( 1 - ma26_sc ) )
    acc_e_ma26_124 = ( price_125_close * ma26_sc )  + ( acc_e_ma26_125 * ( 1 - ma26_sc ) )
    acc_e_ma26_123 = ( price_124_close * ma26_sc )  + ( acc_e_ma26_124 * ( 1 - ma26_sc ) )
    acc_e_ma26_122 = ( price_123_close * ma26_sc )  + ( acc_e_ma26_123 * ( 1 - ma26_sc ) )
    acc_e_ma26_121 = ( price_122_close * ma26_sc )  + ( acc_e_ma26_122 * ( 1 - ma26_sc ) )

    acc_e_ma26_120 = ( price_121_close * ma26_sc )  + ( acc_e_ma26_121 * ( 1 - ma26_sc ) )
    acc_e_ma26_119 = ( price_120_close * ma26_sc )  + ( acc_e_ma26_120 * ( 1 - ma26_sc ) )
    acc_e_ma26_118 = ( price_119_close * ma26_sc )  + ( acc_e_ma26_119 * ( 1 - ma26_sc ) )
    acc_e_ma26_117 = ( price_118_close * ma26_sc )  + ( acc_e_ma26_118 * ( 1 - ma26_sc ) )
    acc_e_ma26_116 = ( price_117_close * ma26_sc )  + ( acc_e_ma26_117 * ( 1 - ma26_sc ) )
    acc_e_ma26_115 = ( price_116_close * ma26_sc )  + ( acc_e_ma26_116 * ( 1 - ma26_sc ) )
    acc_e_ma26_114 = ( price_115_close * ma26_sc )  + ( acc_e_ma26_115 * ( 1 - ma26_sc ) )
    acc_e_ma26_113 = ( price_114_close * ma26_sc )  + ( acc_e_ma26_114 * ( 1 - ma26_sc ) )
    acc_e_ma26_112 = ( price_113_close * ma26_sc )  + ( acc_e_ma26_113 * ( 1 - ma26_sc ) )
    acc_e_ma26_111 = ( price_112_close * ma26_sc )  + ( acc_e_ma26_112 * ( 1 - ma26_sc ) )

    acc_e_ma26_110 = ( price_111_close * ma26_sc )  + ( acc_e_ma26_111 * ( 1 - ma26_sc ) )
    acc_e_ma26_109 = ( price_110_close * ma26_sc )  + ( acc_e_ma26_110 * ( 1 - ma26_sc ) )
    acc_e_ma26_108 = ( price_109_close * ma26_sc )  + ( acc_e_ma26_109 * ( 1 - ma26_sc ) )
    acc_e_ma26_107 = ( price_108_close * ma26_sc )  + ( acc_e_ma26_108 * ( 1 - ma26_sc ) )
    acc_e_ma26_106 = ( price_107_close * ma26_sc )  + ( acc_e_ma26_107 * ( 1 - ma26_sc ) )
    acc_e_ma26_105 = ( price_106_close * ma26_sc )  + ( acc_e_ma26_106 * ( 1 - ma26_sc ) )
    acc_e_ma26_104 = ( price_105_close * ma26_sc )  + ( acc_e_ma26_105 * ( 1 - ma26_sc ) )
    acc_e_ma26_103 = ( price_104_close * ma26_sc )  + ( acc_e_ma26_104 * ( 1 - ma26_sc ) )
    acc_e_ma26_102 = ( price_103_close * ma26_sc )  + ( acc_e_ma26_103 * ( 1 - ma26_sc ) )
    acc_e_ma26_101 = ( price_102_close * ma26_sc )  + ( acc_e_ma26_102 * ( 1 - ma26_sc ) )

    acc_e_ma26_100 = ( price_101_close * ma26_sc )  + ( acc_e_ma26_101 * ( 1 - ma26_sc ) )
    acc_e_ma26_99 = ( price_100_close * ma26_sc )  + ( acc_e_ma26_100 * ( 1 - ma26_sc ) )
    acc_e_ma26_98 = ( price_99_close * ma26_sc )  + ( acc_e_ma26_99 * ( 1 - ma26_sc ) )
    acc_e_ma26_97 = ( price_98_close * ma26_sc )  + ( acc_e_ma26_98 * ( 1 - ma26_sc ) )
    acc_e_ma26_96 = ( price_97_close * ma26_sc )  + ( acc_e_ma26_97 * ( 1 - ma26_sc ) )
    acc_e_ma26_95 = ( price_96_close * ma26_sc )  + ( acc_e_ma26_96 * ( 1 - ma26_sc ) )
    acc_e_ma26_94 = ( price_95_close * ma26_sc )  + ( acc_e_ma26_95 * ( 1 - ma26_sc ) )
    acc_e_ma26_93 = ( price_94_close * ma26_sc )  + ( acc_e_ma26_94 * ( 1 - ma26_sc ) )
    acc_e_ma26_92 = ( price_93_close * ma26_sc )  + ( acc_e_ma26_93 * ( 1 - ma26_sc ) )
    acc_e_ma26_91 = ( price_92_close * ma26_sc )  + ( acc_e_ma26_92 * ( 1 - ma26_sc ) )

    acc_e_ma26_90 = ( price_91_close * ma26_sc )  + ( acc_e_ma26_91 * ( 1 - ma26_sc ) )
    acc_e_ma26_89 = ( price_90_close * ma26_sc )  + ( acc_e_ma26_90 * ( 1 - ma26_sc ) )
    acc_e_ma26_88 = ( price_89_close * ma26_sc )  + ( acc_e_ma26_89 * ( 1 - ma26_sc ) )
    acc_e_ma26_87 = ( price_88_close * ma26_sc )  + ( acc_e_ma26_88 * ( 1 - ma26_sc ) )
    acc_e_ma26_86 = ( price_87_close * ma26_sc )  + ( acc_e_ma26_87 * ( 1 - ma26_sc ) )
    acc_e_ma26_85 = ( price_86_close * ma26_sc )  + ( acc_e_ma26_86 * ( 1 - ma26_sc ) )
    acc_e_ma26_84 = ( price_85_close * ma26_sc )  + ( acc_e_ma26_85 * ( 1 - ma26_sc ) )
    acc_e_ma26_83 = ( price_84_close * ma26_sc )  + ( acc_e_ma26_84 * ( 1 - ma26_sc ) )
    acc_e_ma26_82 = ( price_83_close * ma26_sc )  + ( acc_e_ma26_83 * ( 1 - ma26_sc ) )
    acc_e_ma26_81 = ( price_82_close * ma26_sc )  + ( acc_e_ma26_82 * ( 1 - ma26_sc ) )

    acc_e_ma26_80 = ( price_81_close * ma26_sc )  + ( acc_e_ma26_81 * ( 1 - ma26_sc ) )
    acc_e_ma26_79 = ( price_80_close * ma26_sc )  + ( acc_e_ma26_80 * ( 1 - ma26_sc ) )
    acc_e_ma26_78 = ( price_79_close * ma26_sc )  + ( acc_e_ma26_79 * ( 1 - ma26_sc ) )
    acc_e_ma26_77 = ( price_78_close * ma26_sc )  + ( acc_e_ma26_78 * ( 1 - ma26_sc ) )
    acc_e_ma26_76 = ( price_77_close * ma26_sc )  + ( acc_e_ma26_77 * ( 1 - ma26_sc ) )
    acc_e_ma26_75 = ( price_76_close * ma26_sc )  + ( acc_e_ma26_76 * ( 1 - ma26_sc ) )
    acc_e_ma26_74 = ( price_75_close * ma26_sc )  + ( acc_e_ma26_75 * ( 1 - ma26_sc ) )
    acc_e_ma26_73 = ( price_74_close * ma26_sc )  + ( acc_e_ma26_74 * ( 1 - ma26_sc ) )
    acc_e_ma26_72 = ( price_73_close * ma26_sc )  + ( acc_e_ma26_73 * ( 1 - ma26_sc ) )
    acc_e_ma26_71 = ( price_72_close * ma26_sc )  + ( acc_e_ma26_72 * ( 1 - ma26_sc ) )

    acc_e_ma26_70 = ( price_71_close * ma26_sc )  + ( acc_e_ma26_71 * ( 1 - ma26_sc ) )
    acc_e_ma26_69 = ( price_70_close * ma26_sc )  + ( acc_e_ma26_70 * ( 1 - ma26_sc ) )
    acc_e_ma26_68 = ( price_69_close * ma26_sc )  + ( acc_e_ma26_69 * ( 1 - ma26_sc ) )
    acc_e_ma26_67 = ( price_68_close * ma26_sc )  + ( acc_e_ma26_68 * ( 1 - ma26_sc ) )
    acc_e_ma26_66 = ( price_67_close * ma26_sc )  + ( acc_e_ma26_67 * ( 1 - ma26_sc ) )
    acc_e_ma26_65 = ( price_66_close * ma26_sc )  + ( acc_e_ma26_66 * ( 1 - ma26_sc ) )
    acc_e_ma26_64 = ( price_65_close * ma26_sc )  + ( acc_e_ma26_65 * ( 1 - ma26_sc ) )
    acc_e_ma26_63 = ( price_64_close * ma26_sc )  + ( acc_e_ma26_64 * ( 1 - ma26_sc ) )
    acc_e_ma26_62 = ( price_63_close * ma26_sc )  + ( acc_e_ma26_63 * ( 1 - ma26_sc ) )
    acc_e_ma26_61 = ( price_62_close * ma26_sc )  + ( acc_e_ma26_62 * ( 1 - ma26_sc ) )

    acc_e_ma26_60 = ( price_61_close * ma26_sc )  + ( acc_e_ma26_61 * ( 1 - ma26_sc ) )
    acc_e_ma26_59 = ( price_60_close * ma26_sc )  + ( acc_e_ma26_60 * ( 1 - ma26_sc ) )
    acc_e_ma26_58 = ( price_59_close * ma26_sc )  + ( acc_e_ma26_59 * ( 1 - ma26_sc ) )
    acc_e_ma26_57 = ( price_58_close * ma26_sc )  + ( acc_e_ma26_58 * ( 1 - ma26_sc ) )
    acc_e_ma26_56 = ( price_57_close * ma26_sc )  + ( acc_e_ma26_57 * ( 1 - ma26_sc ) )
    acc_e_ma26_55 = ( price_56_close * ma26_sc )  + ( acc_e_ma26_56 * ( 1 - ma26_sc ) )
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
    print( "macd값" )
    print( "========== ========== ========== ========== ==========" )
    acc_macd_ok_1 = acc_e_ma12_1 - acc_e_ma26_1
    print( f"e_macd_ok_1 ( { acc_macd_ok_1 } ) =  acc_e_ma12_1 ( { acc_e_ma12_1 } ) - acc_e_ma26_1 ( { acc_e_ma26_1 } )" )

    acc_macd_ok_2 = acc_e_ma12_2 - acc_e_ma26_2
    print( f"e_macd_ok_2 ( { acc_macd_ok_2 } ) =  acc_e_ma12_2 ( { acc_e_ma12_2 } ) - acc_e_ma26_2 ( { acc_e_ma26_2 } )" )

    acc_macd_ok_3 = acc_e_ma12_3 - acc_e_ma26_3
    print( f"e_macd_ok_3 ( { acc_macd_ok_3 } ) =  acc_e_ma12_3 ( { acc_e_ma12_3 } ) - acc_e_ma26_3 ( { acc_e_ma26_3 } )" )

    acc_macd_ok_4 = acc_e_ma12_4 - acc_e_ma26_4
    print( f"e_macd_ok_4 ( { acc_macd_ok_4 } ) =  acc_e_ma12_4 ( { acc_e_ma12_4 } ) - acc_e_ma26_4 ( { acc_e_ma26_4 } )" )

    acc_macd_ok_5 = acc_e_ma12_5 - acc_e_ma26_5
    print( f"e_macd_ok_5 ( { acc_macd_ok_5 } ) =  acc_e_ma12_5 ( { acc_e_ma12_5 } ) - acc_e_ma26_5 ( { acc_e_ma26_5 } )" )

    acc_macd_ok_6 = acc_e_ma12_6 - acc_e_ma26_6
    print( f"e_macd_ok_6 ( { acc_macd_ok_6 } ) =  acc_e_ma12_6 ( { acc_e_ma12_6 } ) - acc_e_ma26_6 ( { acc_e_ma26_6 } )" )

    acc_macd_ok_7 = acc_e_ma12_7 - acc_e_ma26_7
    print( f"e_macd_ok_7 ( { acc_macd_ok_7 } ) =  acc_e_ma12_7 ( { acc_e_ma12_7 } ) - acc_e_ma26_7 ( { acc_e_ma26_7 } )" )

    acc_macd_ok_8 = acc_e_ma12_8 - acc_e_ma26_8
    print( f"e_macd_ok_8 ( { acc_macd_ok_8 } ) =  acc_e_ma12_8 ( { acc_e_ma12_8 } ) - acc_e_ma26_8 ( { acc_e_ma26_8 } )" )

    acc_macd_ok_9 = acc_e_ma12_9 - acc_e_ma26_9
    print( f"e_macd_ok_9 ( { acc_macd_ok_9 } ) =  acc_e_ma12_9 ( { acc_e_ma12_9 } ) - acc_e_ma26_9 ( { acc_e_ma26_9 } )" )

    acc_macd_ok_10 = acc_e_ma12_10 - acc_e_ma26_10
    print( f"e_macd_ok_10 ( { acc_macd_ok_10 } ) =  acc_e_ma12_10 ( { acc_e_ma12_10 } ) - acc_e_ma26_10 ( { acc_e_ma26_10 } )" )

    acc_macd_ok_11 = acc_e_ma12_11 - acc_e_ma26_11
    print( f"e_macd_ok_11 ( { acc_macd_ok_11 } ) =  acc_e_ma12_11 ( { acc_e_ma12_11 } ) - acc_e_ma26_11 ( { acc_e_ma26_11 } )" )

    acc_macd_ok_12 = acc_e_ma12_12 - acc_e_ma26_12
    print( f"e_macd_ok_12 ( { acc_macd_ok_12 } ) =  acc_e_ma12_12 ( { acc_e_ma12_12 } ) - acc_e_ma26_12 ( { acc_e_ma26_12 } )" )

    acc_macd_ok_13 = acc_e_ma12_13 - acc_e_ma26_13
    print( f"e_macd_ok_13 ( { acc_macd_ok_13 } ) =  acc_e_ma12_13 ( { acc_e_ma12_13 } ) - acc_e_ma26_13 ( { acc_e_ma26_13 } )" )

    acc_macd_ok_14 = acc_e_ma12_14 - acc_e_ma26_14
    print( f"e_macd_ok_14 ( { acc_macd_ok_14 } ) =  acc_e_ma12_14 ( { acc_e_ma12_14 } ) - acc_e_ma26_14 ( { acc_e_ma26_14 } )" )

    acc_macd_ok_15 = acc_e_ma12_15 - acc_e_ma26_15
    print( f"e_macd_ok_15 ( { acc_macd_ok_15 } ) =  acc_e_ma12_15 ( { acc_e_ma12_15 } ) - acc_e_ma26_15 ( { acc_e_ma26_15 } )" )

    acc_macd_ok_16 = acc_e_ma12_16 - acc_e_ma26_16
    print( f"e_macd_ok_16 ( { acc_macd_ok_16 } ) =  acc_e_ma12_16 ( { acc_e_ma12_16 } ) - acc_e_ma26_16 ( { acc_e_ma26_16 } )" )

    acc_macd_ok_17 = acc_e_ma12_17 - acc_e_ma26_17
    print( f"e_macd_ok_17 ( { acc_macd_ok_17 } ) =  acc_e_ma12_17 ( { acc_e_ma12_17 } ) - acc_e_ma26_17 ( { acc_e_ma26_17 } )" )
    print()





    print( "시그널값" )
    print( "========== ========== ========== ========== ==========" )
    # signal = macd 9일선, macd값의 9이평선.
    # + 는 0선 이상, - 는 0선 이하
    acc_signal_1 = ( acc_macd_ok_1 + acc_macd_ok_2 + acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 ) / 9
    print( f"acc_signal_1 = ( { acc_signal_1 } )" )

    acc_signal_2 = ( acc_macd_ok_2 + acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 ) / 9
    print( f"acc_signal_2 = ( { acc_signal_2 } )" )

    acc_signal_3 = ( acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 ) / 9
    print( f"acc_signal_3 = ( { acc_signal_3 } )" )

    acc_signal_4 = ( acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 ) / 9
    print( f"acc_signal_4 = ( { acc_signal_4 } )" )

    acc_signal_5 = ( acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 ) / 9
    print( f"acc_signal_5 = ( { acc_signal_5 } )" )

    acc_signal_6 = ( acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 ) / 9
    print( f"acc_signal_6 = ( { acc_signal_6 } )" )

    acc_signal_7 = ( acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 ) / 9
    print( f"acc_signal_7 = ( { acc_signal_7 } )" )

    acc_signal_8 = ( acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 + acc_macd_ok_16 ) / 9
    print( f"acc_signal_8 = ( { acc_signal_8 } )" )

    acc_signal_9 = ( acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 + acc_macd_ok_16 + acc_macd_ok_17 ) / 9
    print( f"acc_signal_9 = ( { acc_signal_9 } )" )

    print()

    # 최종값
    # macd - 시그널 = + 는 골든크로스, - 는 데드크로스
    print( "[최종] 간격 = macd - 시그널" )
    print( "========== ========== ========== ========== ==========" )
    acc_macd1 = acc_macd_ok_1 - acc_signal_1
    print( f"acc_macd1 ( { acc_macd1 } ) = acc_macd_ok_1 ( { acc_macd_ok_1 } ) - acc_signal_1 ( { acc_signal_1 } )" )
    acc_macd2 = acc_macd_ok_2 - acc_signal_2
    print( f"acc_macd2 ( { acc_macd2 } ) = acc_macd_ok_2 ( { acc_macd_ok_2 } ) - acc_signal_2 ( { acc_signal_2 } )" )
    acc_macd3 = acc_macd_ok_3 - acc_signal_3
    print( f"acc_macd3 ( { acc_macd3 } ) = acc_macd_ok_3 ( { acc_macd_ok_3 } ) - acc_signal_3 ( { acc_signal_3 } )" )
    acc_macd4 = acc_macd_ok_4 - acc_signal_4
    print( f"acc_macd4 ( { acc_macd4 } ) = acc_macd_ok_4 ( { acc_macd_ok_4 } ) - acc_signal_4 ( { acc_signal_4 } )" )
    acc_macd5 = acc_macd_ok_5 - acc_signal_5
    print( f"acc_macd5 ( { acc_macd5 } ) = acc_macd_ok_5 ( { acc_macd_ok_5 } ) - acc_signal_5 ( { acc_signal_5 } )" )
    acc_macd6 = acc_macd_ok_6 - acc_signal_6
    print( f"acc_macd6 ( { acc_macd6 } ) = acc_macd_ok_6 ( { acc_macd_ok_6 } ) - acc_signal_6 ( { acc_signal_6 } )" )
    acc_macd7 = acc_macd_ok_7 - acc_signal_7
    print( f"acc_macd7 ( { acc_macd7 } ) = acc_macd_ok_7 ( { acc_macd_ok_7 } ) - acc_signal_7 ( { acc_signal_7 } )" )
    acc_macd8 = acc_macd_ok_8 - acc_signal_8
    print( f"acc_macd8 ( { acc_macd8 } ) = acc_macd_ok_8 ( { acc_macd_ok_8 } ) - acc_signal_8 ( { acc_signal_8 } )" )
    acc_macd9 = acc_macd_ok_9 - acc_signal_9
    print( f"acc_macd9 ( { acc_macd9 } ) = acc_macd_ok_9 ( { acc_macd_ok_9 } ) - acc_signal_9 ( { acc_signal_9 } )" )
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

    print( f"acc_macd_select = {acc_macd_select}" )
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
    timeframe='1h', 
    since=None, 
    limit=200
)

df = pd.DataFrame( data = btc, columns = [ 'datetime', 'open', 'high', 'low', 'close', 'volume' ] )
df['datetime'] = pd.to_datetime( df[ 'datetime' ], unit = 'ms' )
df.set_index( 'datetime', inplace = True )

print( df )
print()


# 종가받기 200개
print( "========== 1시간봉 종가 받기 ==========" )
print()
# 0은 아무것도 아님.
price_0_close = df.iloc[ 0 ][ 'close' ]
#price_0_time = df.iloc[ 0 ][ 'datetime' ]

# -1은 현재가.
price_1_close = df.iloc[ -1 ][ 'close' ]

########################################
# -2는 1시간전 종가. 여기부터 macd 계산.
price_2_close = df.iloc[ -2 ][ 'close' ]
price_3_close = df.iloc[ -3 ][ 'close' ]
price_4_close = df.iloc[ -4 ][ 'close' ]
price_5_close = df.iloc[ -5 ][ 'close' ]
price_6_close = df.iloc[ -6 ][ 'close' ]
price_7_close = df.iloc[ -7 ][ 'close' ]
price_8_close = df.iloc[ -8 ][ 'close' ]
price_9_close = df.iloc[ -9 ][ 'close' ]
price_10_close = df.iloc[ -10 ][ 'close' ]

price_11_close = df.iloc[ -11 ][ 'close' ]
price_12_close = df.iloc[ -12 ][ 'close' ]
price_13_close = df.iloc[ -13 ][ 'close' ]
price_14_close = df.iloc[ -14 ][ 'close' ]
price_15_close = df.iloc[ -15 ][ 'close' ]
price_16_close = df.iloc[ -16 ][ 'close' ]
price_17_close = df.iloc[ -17 ][ 'close' ]
price_18_close = df.iloc[ -18 ][ 'close' ]
price_19_close = df.iloc[ -19 ][ 'close' ]
price_20_close = df.iloc[ -20 ][ 'close' ]

price_21_close = df.iloc[ -21 ][ 'close' ]
price_22_close = df.iloc[ -22 ][ 'close' ]
price_23_close = df.iloc[ -23 ][ 'close' ]
price_24_close = df.iloc[ -24 ][ 'close' ]
price_25_close = df.iloc[ -25 ][ 'close' ]
price_26_close = df.iloc[ -26 ][ 'close' ]
price_27_close = df.iloc[ -27 ][ 'close' ]
price_28_close = df.iloc[ -28 ][ 'close' ]
price_29_close = df.iloc[ -29 ][ 'close' ]
price_30_close = df.iloc[ -30 ][ 'close' ]

price_31_close = df.iloc[ -31 ][ 'close' ]
price_32_close = df.iloc[ -32 ][ 'close' ]
price_33_close = df.iloc[ -33 ][ 'close' ]
price_34_close = df.iloc[ -34 ][ 'close' ]
price_35_close = df.iloc[ -35 ][ 'close' ]
price_36_close = df.iloc[ -36 ][ 'close' ]
price_37_close = df.iloc[ -37 ][ 'close' ]
price_38_close = df.iloc[ -38 ][ 'close' ]
price_39_close = df.iloc[ -39 ][ 'close' ]
price_40_close = df.iloc[ -40 ][ 'close' ]

price_41_close = df.iloc[ -41 ][ 'close' ]
price_42_close = df.iloc[ -42 ][ 'close' ]
price_43_close = df.iloc[ -43 ][ 'close' ]
price_44_close = df.iloc[ -44 ][ 'close' ]
price_45_close = df.iloc[ -45 ][ 'close' ]
price_46_close = df.iloc[ -46 ][ 'close' ]
price_47_close = df.iloc[ -47 ][ 'close' ]
price_48_close = df.iloc[ -48 ][ 'close' ]
price_49_close = df.iloc[ -49 ][ 'close' ]
price_50_close = df.iloc[ -50 ][ 'close' ]

price_51_close = df.iloc[ -51 ][ 'close' ]
price_52_close = df.iloc[ -52 ][ 'close' ]
price_53_close = df.iloc[ -53 ][ 'close' ]
price_54_close = df.iloc[ -54 ][ 'close' ]
price_55_close = df.iloc[ -55 ][ 'close' ]
price_56_close = df.iloc[ -56 ][ 'close' ]
price_57_close = df.iloc[ -57 ][ 'close' ]
price_58_close = df.iloc[ -58 ][ 'close' ]
price_59_close = df.iloc[ -59 ][ 'close' ]
price_60_close = df.iloc[ -60 ][ 'close' ]

price_61_close = df.iloc[ -61 ][ 'close' ]
price_62_close = df.iloc[ -62 ][ 'close' ]
price_63_close = df.iloc[ -63 ][ 'close' ]
price_64_close = df.iloc[ -64 ][ 'close' ]
price_65_close = df.iloc[ -65 ][ 'close' ]
price_66_close = df.iloc[ -66 ][ 'close' ]
price_67_close = df.iloc[ -67 ][ 'close' ]
price_68_close = df.iloc[ -68 ][ 'close' ]
price_69_close = df.iloc[ -69 ][ 'close' ]
price_70_close = df.iloc[ -70 ][ 'close' ]

price_71_close = df.iloc[ -71 ][ 'close' ]
price_72_close = df.iloc[ -72 ][ 'close' ]
price_73_close = df.iloc[ -73 ][ 'close' ]
price_74_close = df.iloc[ -74 ][ 'close' ]
price_75_close = df.iloc[ -75 ][ 'close' ]
price_76_close = df.iloc[ -76 ][ 'close' ]
price_77_close = df.iloc[ -77 ][ 'close' ]
price_78_close = df.iloc[ -78 ][ 'close' ]
price_79_close = df.iloc[ -79 ][ 'close' ]
price_80_close = df.iloc[ -80 ][ 'close' ]

price_81_close = df.iloc[ -81 ][ 'close' ]
price_82_close = df.iloc[ -82 ][ 'close' ]
price_83_close = df.iloc[ -83 ][ 'close' ]
price_84_close = df.iloc[ -84 ][ 'close' ]
price_85_close = df.iloc[ -85 ][ 'close' ]
price_86_close = df.iloc[ -86 ][ 'close' ]
price_87_close = df.iloc[ -87 ][ 'close' ]
price_88_close = df.iloc[ -88 ][ 'close' ]
price_89_close = df.iloc[ -89 ][ 'close' ]
price_90_close = df.iloc[ -90 ][ 'close' ]

price_91_close = df.iloc[ -91 ][ 'close' ]
price_92_close = df.iloc[ -92 ][ 'close' ]
price_93_close = df.iloc[ -93 ][ 'close' ]
price_94_close = df.iloc[ -94 ][ 'close' ]
price_95_close = df.iloc[ -95 ][ 'close' ]
price_96_close = df.iloc[ -96 ][ 'close' ]
price_97_close = df.iloc[ -97 ][ 'close' ]
price_98_close = df.iloc[ -98 ][ 'close' ]
price_99_close = df.iloc[ -99 ][ 'close' ]
price_100_close = df.iloc[ -100 ][ 'close' ]

price_101_close = df.iloc[ -101 ][ 'close' ]
price_102_close = df.iloc[ -102 ][ 'close' ]
price_103_close = df.iloc[ -103 ][ 'close' ]
price_104_close = df.iloc[ -104 ][ 'close' ]
price_105_close = df.iloc[ -105 ][ 'close' ]
price_106_close = df.iloc[ -106 ][ 'close' ]
price_107_close = df.iloc[ -107 ][ 'close' ]
price_108_close = df.iloc[ -108 ][ 'close' ]
price_109_close = df.iloc[ -109 ][ 'close' ]
price_110_close = df.iloc[ -110 ][ 'close' ]

price_111_close = df.iloc[ -111 ][ 'close' ]
price_112_close = df.iloc[ -112 ][ 'close' ]
price_113_close = df.iloc[ -113 ][ 'close' ]
price_114_close = df.iloc[ -114 ][ 'close' ]
price_115_close = df.iloc[ -115 ][ 'close' ]
price_116_close = df.iloc[ -116 ][ 'close' ]
price_117_close = df.iloc[ -117 ][ 'close' ]
price_118_close = df.iloc[ -118 ][ 'close' ]
price_119_close = df.iloc[ -119 ][ 'close' ]
price_120_close = df.iloc[ -120 ][ 'close' ]

price_121_close = df.iloc[ -121 ][ 'close' ]
price_122_close = df.iloc[ -122 ][ 'close' ]
price_123_close = df.iloc[ -123 ][ 'close' ]
price_124_close = df.iloc[ -124 ][ 'close' ]
price_125_close = df.iloc[ -125 ][ 'close' ]
price_126_close = df.iloc[ -126 ][ 'close' ]
price_127_close = df.iloc[ -127 ][ 'close' ]
price_128_close = df.iloc[ -128 ][ 'close' ]
price_129_close = df.iloc[ -129 ][ 'close' ]
price_130_close = df.iloc[ -130 ][ 'close' ]

price_131_close = df.iloc[ -131 ][ 'close' ]
price_132_close = df.iloc[ -132 ][ 'close' ]
price_133_close = df.iloc[ -133 ][ 'close' ]
price_134_close = df.iloc[ -134 ][ 'close' ]
price_135_close = df.iloc[ -135 ][ 'close' ]
price_136_close = df.iloc[ -136 ][ 'close' ]
price_137_close = df.iloc[ -137 ][ 'close' ]
price_138_close = df.iloc[ -138 ][ 'close' ]
price_139_close = df.iloc[ -139 ][ 'close' ]
price_140_close = df.iloc[ -140 ][ 'close' ]

price_141_close = df.iloc[ -141 ][ 'close' ]
price_142_close = df.iloc[ -142 ][ 'close' ]
price_143_close = df.iloc[ -143 ][ 'close' ]
price_144_close = df.iloc[ -144 ][ 'close' ]
price_145_close = df.iloc[ -145 ][ 'close' ]
price_146_close = df.iloc[ -146 ][ 'close' ]
price_147_close = df.iloc[ -147 ][ 'close' ]
price_148_close = df.iloc[ -148 ][ 'close' ]
price_149_close = df.iloc[ -149 ][ 'close' ]
price_150_close = df.iloc[ -150 ][ 'close' ]

price_151_close = df.iloc[ -151 ][ 'close' ]
price_152_close = df.iloc[ -152 ][ 'close' ]
price_153_close = df.iloc[ -153 ][ 'close' ]
price_154_close = df.iloc[ -154 ][ 'close' ]
price_155_close = df.iloc[ -155 ][ 'close' ]
price_156_close = df.iloc[ -156 ][ 'close' ]
price_157_close = df.iloc[ -157 ][ 'close' ]
price_158_close = df.iloc[ -158 ][ 'close' ]
price_159_close = df.iloc[ -159 ][ 'close' ]
price_160_close = df.iloc[ -160 ][ 'close' ]

price_161_close = df.iloc[ -161 ][ 'close' ]
price_162_close = df.iloc[ -162 ][ 'close' ]
price_163_close = df.iloc[ -163 ][ 'close' ]
price_164_close = df.iloc[ -164 ][ 'close' ]
price_165_close = df.iloc[ -165 ][ 'close' ]
price_166_close = df.iloc[ -166 ][ 'close' ]
price_167_close = df.iloc[ -167 ][ 'close' ]
price_168_close = df.iloc[ -168 ][ 'close' ]
price_169_close = df.iloc[ -169 ][ 'close' ]
price_170_close = df.iloc[ -170 ][ 'close' ]

price_171_close = df.iloc[ -171 ][ 'close' ]
price_172_close = df.iloc[ -172 ][ 'close' ]
price_173_close = df.iloc[ -173 ][ 'close' ]
price_174_close = df.iloc[ -174 ][ 'close' ]
price_175_close = df.iloc[ -175 ][ 'close' ]
price_176_close = df.iloc[ -176 ][ 'close' ]
price_177_close = df.iloc[ -177 ][ 'close' ]
price_178_close = df.iloc[ -178 ][ 'close' ]
price_179_close = df.iloc[ -179 ][ 'close' ]
price_180_close = df.iloc[ -180 ][ 'close' ]

price_181_close = df.iloc[ -181 ][ 'close' ]
price_182_close = df.iloc[ -182 ][ 'close' ]
price_183_close = df.iloc[ -183 ][ 'close' ]
price_184_close = df.iloc[ -184 ][ 'close' ]
price_185_close = df.iloc[ -185 ][ 'close' ]
price_186_close = df.iloc[ -186 ][ 'close' ]
price_187_close = df.iloc[ -187 ][ 'close' ]
price_188_close = df.iloc[ -188 ][ 'close' ]
price_189_close = df.iloc[ -189 ][ 'close' ]
price_190_close = df.iloc[ -190 ][ 'close' ]











    

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
acc_ma12_29 = acc_ma12_29_1 / 12
acc_ma12_30_1 = price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close
acc_ma12_30 = acc_ma12_30_1 / 12


acc_ma12_31_1 = price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close
acc_ma12_31 = acc_ma12_31_1 / 12
acc_ma12_32_1 = price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close
acc_ma12_32 = acc_ma12_32_1 / 12
acc_ma12_33_1 = price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close
acc_ma12_33 = acc_ma12_33_1 / 12
acc_ma12_34_1 = price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close
acc_ma12_34 = acc_ma12_34_1 / 12
acc_ma12_35_1 = price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close
acc_ma12_35 = acc_ma12_35_1 / 12

acc_ma12_36_1 = price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close
acc_ma12_36 = acc_ma12_36_1 / 12
acc_ma12_37_1 = price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close
acc_ma12_37 = acc_ma12_37_1 / 12
acc_ma12_38_1 = price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close
acc_ma12_38 = acc_ma12_38_1 / 12
acc_ma12_39_1 = price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close
acc_ma12_39 = acc_ma12_39_1 / 12
acc_ma12_40_1 = price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close
acc_ma12_40 = acc_ma12_40_1 / 12


acc_ma12_41_1 = price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close
acc_ma12_41 = acc_ma12_41_1 / 12
acc_ma12_42_1 = price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close
acc_ma12_42 = acc_ma12_42_1 / 12
acc_ma12_43_1 = price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close
acc_ma12_43 = acc_ma12_43_1 / 12
acc_ma12_44_1 = price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close
acc_ma12_44 = acc_ma12_44_1 / 12
acc_ma12_45_1 = price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close
acc_ma12_45 = acc_ma12_45_1 / 12

acc_ma12_46_1 = price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close
acc_ma12_46 = acc_ma12_46_1 / 12
acc_ma12_47_1 = price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close
acc_ma12_47 = acc_ma12_47_1 / 12
acc_ma12_48_1 = price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close
acc_ma12_48 = acc_ma12_48_1 / 12
acc_ma12_49_1 = price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close
acc_ma12_49 = acc_ma12_49_1 / 12
acc_ma12_50_1 = price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close
acc_ma12_50 = acc_ma12_50_1 / 12


acc_ma12_51_1 = price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close
acc_ma12_51 = acc_ma12_51_1 / 12
acc_ma12_52_1 = price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close
acc_ma12_52 = acc_ma12_52_1 / 12
acc_ma12_53_1 = price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close
acc_ma12_53 = acc_ma12_53_1 / 12
acc_ma12_54_1 = price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close
acc_ma12_54 = acc_ma12_54_1 / 12
acc_ma12_55_1 = price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close
acc_ma12_55 = acc_ma12_55_1 / 12

acc_ma12_56_1 = price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close
acc_ma12_56 = acc_ma12_56_1 / 12
acc_ma12_57_1 = price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close
acc_ma12_57 = acc_ma12_57_1 / 12
acc_ma12_58_1 = price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close
acc_ma12_58 = acc_ma12_58_1 / 12
acc_ma12_59_1 = price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close
acc_ma12_59 = acc_ma12_59_1 / 12
acc_ma12_60_1 = price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close
acc_ma12_60 = acc_ma12_60_1 / 12


acc_ma12_61_1 = price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close
acc_ma12_61 = acc_ma12_61_1 / 12
acc_ma12_62_1 = price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close
acc_ma12_62 = acc_ma12_62_1 / 12
acc_ma12_63_1 = price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close
acc_ma12_63 = acc_ma12_63_1 / 12
acc_ma12_64_1 = price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close
acc_ma12_64 = acc_ma12_64_1 / 12
acc_ma12_65_1 = price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close
acc_ma12_65 = acc_ma12_65_1 / 12

acc_ma12_66_1 = price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close
acc_ma12_66 = acc_ma12_66_1 / 12
acc_ma12_67_1 = price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close
acc_ma12_67 = acc_ma12_67_1 / 12
acc_ma12_68_1 = price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close
acc_ma12_68 = acc_ma12_68_1 / 12
acc_ma12_69_1 = price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close
acc_ma12_69 = acc_ma12_69_1 / 12
acc_ma12_70_1 = price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close
acc_ma12_70 = acc_ma12_70_1 / 12


acc_ma12_71_1 = price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close
acc_ma12_71 = acc_ma12_71_1 / 12
acc_ma12_72_1 = price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close
acc_ma12_72 = acc_ma12_72_1 / 12
acc_ma12_73_1 = price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close
acc_ma12_73 = acc_ma12_73_1 / 12
acc_ma12_74_1 = price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close
acc_ma12_74 = acc_ma12_74_1 / 12
acc_ma12_75_1 = price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close
acc_ma12_75 = acc_ma12_75_1 / 12

acc_ma12_76_1 = price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close
acc_ma12_76 = acc_ma12_76_1 / 12
acc_ma12_77_1 = price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close
acc_ma12_77 = acc_ma12_77_1 / 12
acc_ma12_78_1 = price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close
acc_ma12_78 = acc_ma12_78_1 / 12
acc_ma12_79_1 = price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close
acc_ma12_79 = acc_ma12_79_1 / 12
acc_ma12_80_1 = price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close
acc_ma12_80 = acc_ma12_80_1 / 12


acc_ma12_81_1 = price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close
acc_ma12_81 = acc_ma12_81_1 / 12
acc_ma12_82_1 = price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close
acc_ma12_82 = acc_ma12_82_1 / 12
acc_ma12_83_1 = price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close
acc_ma12_83 = acc_ma12_83_1 / 12
acc_ma12_84_1 = price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close
acc_ma12_84 = acc_ma12_84_1 / 12
acc_ma12_85_1 = price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close
acc_ma12_85 = acc_ma12_85_1 / 12

acc_ma12_86_1 = price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close
acc_ma12_86 = acc_ma12_86_1 / 12
acc_ma12_87_1 = price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close
acc_ma12_87 = acc_ma12_87_1 / 12
acc_ma12_88_1 = price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close
acc_ma12_88 = acc_ma12_88_1 / 12
acc_ma12_89_1 = price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close
acc_ma12_89 = acc_ma12_89_1 / 12
acc_ma12_90_1 = price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close
acc_ma12_90 = acc_ma12_90_1 / 12


acc_ma12_91_1 = price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close
acc_ma12_91 = acc_ma12_91_1 / 12
acc_ma12_92_1 = price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close
acc_ma12_92 = acc_ma12_92_1 / 12
acc_ma12_93_1 = price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close
acc_ma12_93 = acc_ma12_93_1 / 12
acc_ma12_94_1 = price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close
acc_ma12_94 = acc_ma12_94_1 / 12
acc_ma12_95_1 = price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close
acc_ma12_95 = acc_ma12_95_1 / 12

acc_ma12_96_1 = price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close
acc_ma12_96 = acc_ma12_96_1 / 12
acc_ma12_97_1 = price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close
acc_ma12_97 = acc_ma12_97_1 / 12
acc_ma12_98_1 = price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close
acc_ma12_98 = acc_ma12_98_1 / 12
acc_ma12_99_1 = price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close
acc_ma12_99 = acc_ma12_99_1 / 12
acc_ma12_100_1 = price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close
acc_ma12_100 = acc_ma12_100_1 / 12


acc_ma12_101_1 = price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close
acc_ma12_101 = acc_ma12_101_1 / 12
acc_ma12_102_1 = price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close
acc_ma12_102 = acc_ma12_102_1 / 12
acc_ma12_103_1 = price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close
acc_ma12_103 = acc_ma12_103_1 / 12
acc_ma12_104_1 = price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close
acc_ma12_104 = acc_ma12_104_1 / 12
acc_ma12_105_1 = price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close
acc_ma12_105 = acc_ma12_105_1 / 12

acc_ma12_106_1 = price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close
acc_ma12_106 = acc_ma12_106_1 / 12
acc_ma12_107_1 = price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close
acc_ma12_107 = acc_ma12_107_1 / 12
acc_ma12_108_1 = price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close
acc_ma12_108 = acc_ma12_108_1 / 12
acc_ma12_109_1 = price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close
acc_ma12_109 = acc_ma12_109_1 / 12
acc_ma12_110_1 = price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close
acc_ma12_110 = acc_ma12_110_1 / 12


acc_ma12_111_1 = price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close
acc_ma12_111 = acc_ma12_111_1 / 12
acc_ma12_112_1 = price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close
acc_ma12_112 = acc_ma12_112_1 / 12
acc_ma12_113_1 = price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close
acc_ma12_113 = acc_ma12_113_1 / 12
acc_ma12_114_1 = price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close
acc_ma12_114 = acc_ma12_114_1 / 12
acc_ma12_115_1 = price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close
acc_ma12_115 = acc_ma12_115_1 / 12

acc_ma12_116_1 = price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close
acc_ma12_116 = acc_ma12_116_1 / 12
acc_ma12_117_1 = price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close
acc_ma12_117 = acc_ma12_117_1 / 12
acc_ma12_118_1 = price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close
acc_ma12_118 = acc_ma12_118_1 / 12
acc_ma12_119_1 = price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close
acc_ma12_119 = acc_ma12_119_1 / 12
acc_ma12_120_1 = price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close
acc_ma12_120 = acc_ma12_120_1 / 12

acc_ma12_121_1 = price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close
acc_ma12_121 = acc_ma12_121_1 / 12
acc_ma12_122_1 = price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close
acc_ma12_122 = acc_ma12_122_1 / 12
acc_ma12_123_1 = price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close
acc_ma12_123 = acc_ma12_123_1 / 12
acc_ma12_124_1 = price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close
acc_ma12_124 = acc_ma12_124_1 / 12
acc_ma12_125_1 = price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close
acc_ma12_125 = acc_ma12_125_1 / 12

acc_ma12_126_1 = price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close
acc_ma12_126 = acc_ma12_126_1 / 12
acc_ma12_127_1 = price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close
acc_ma12_127 = acc_ma12_127_1 / 12
acc_ma12_128_1 = price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close
acc_ma12_128 = acc_ma12_128_1 / 12
acc_ma12_129_1 = price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close
acc_ma12_129 = acc_ma12_129_1 / 12
acc_ma12_130_1 = price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close
acc_ma12_130 = acc_ma12_130_1 / 12


acc_ma12_131_1 = price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close
acc_ma12_131 = acc_ma12_131_1 / 12
acc_ma12_132_1 = price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close
acc_ma12_132 = acc_ma12_132_1 / 12
acc_ma12_133_1 = price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close
acc_ma12_133 = acc_ma12_133_1 / 12
acc_ma12_134_1 = price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close
acc_ma12_134 = acc_ma12_134_1 / 12
acc_ma12_135_1 = price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close
acc_ma12_135 = acc_ma12_135_1 / 12

acc_ma12_136_1 = price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close
acc_ma12_136 = acc_ma12_136_1 / 12
acc_ma12_137_1 = price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close
acc_ma12_137 = acc_ma12_137_1 / 12
acc_ma12_138_1 = price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close
acc_ma12_138 = acc_ma12_138_1 / 12
acc_ma12_139_1 = price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close
acc_ma12_139 = acc_ma12_139_1 / 12
acc_ma12_140_1 = price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close
acc_ma12_140 = acc_ma12_140_1 / 12








# EMA - 단기 12 지수이동평균값 구하기
acc_e_ma12_139 = acc_ma12_140
acc_e_ma12_138 = ( price_139_close * ma12_sc )  + ( acc_e_ma12_139 * ( 1 - ma12_sc ) )
acc_e_ma12_137 = ( price_138_close * ma12_sc )  + ( acc_e_ma12_138 * ( 1 - ma12_sc ) )
acc_e_ma12_136 = ( price_137_close * ma12_sc )  + ( acc_e_ma12_137 * ( 1 - ma12_sc ) )
acc_e_ma12_135 = ( price_136_close * ma12_sc )  + ( acc_e_ma12_136 * ( 1 - ma12_sc ) )
acc_e_ma12_134 = ( price_135_close * ma12_sc )  + ( acc_e_ma12_135 * ( 1 - ma12_sc ) )
acc_e_ma12_133 = ( price_134_close * ma12_sc )  + ( acc_e_ma12_134 * ( 1 - ma12_sc ) )
acc_e_ma12_132 = ( price_133_close * ma12_sc )  + ( acc_e_ma12_133 * ( 1 - ma12_sc ) )
acc_e_ma12_131 = ( price_132_close * ma12_sc )  + ( acc_e_ma12_132 * ( 1 - ma12_sc ) )

acc_e_ma12_130 = ( price_131_close * ma12_sc )  + ( acc_e_ma12_131 * ( 1 - ma12_sc ) )
acc_e_ma12_129 = ( price_130_close * ma12_sc )  + ( acc_e_ma12_130 * ( 1 - ma12_sc ) )
acc_e_ma12_128 = ( price_129_close * ma12_sc )  + ( acc_e_ma12_129 * ( 1 - ma12_sc ) )
acc_e_ma12_127 = ( price_128_close * ma12_sc )  + ( acc_e_ma12_128 * ( 1 - ma12_sc ) )
acc_e_ma12_126 = ( price_127_close * ma12_sc )  + ( acc_e_ma12_127 * ( 1 - ma12_sc ) )
acc_e_ma12_125 = ( price_126_close * ma12_sc )  + ( acc_e_ma12_126 * ( 1 - ma12_sc ) )
acc_e_ma12_124 = ( price_125_close * ma12_sc )  + ( acc_e_ma12_125 * ( 1 - ma12_sc ) )
acc_e_ma12_123 = ( price_124_close * ma12_sc )  + ( acc_e_ma12_124 * ( 1 - ma12_sc ) )
acc_e_ma12_122 = ( price_123_close * ma12_sc )  + ( acc_e_ma12_123 * ( 1 - ma12_sc ) )
acc_e_ma12_121 = ( price_122_close * ma12_sc )  + ( acc_e_ma12_122 * ( 1 - ma12_sc ) )

acc_e_ma12_120 = ( price_121_close * ma12_sc )  + ( acc_e_ma12_121 * ( 1 - ma12_sc ) )
acc_e_ma12_119 = ( price_120_close * ma12_sc )  + ( acc_e_ma12_120 * ( 1 - ma12_sc ) )
acc_e_ma12_118 = ( price_119_close * ma12_sc )  + ( acc_e_ma12_119 * ( 1 - ma12_sc ) )
acc_e_ma12_117 = ( price_118_close * ma12_sc )  + ( acc_e_ma12_118 * ( 1 - ma12_sc ) )
acc_e_ma12_116 = ( price_117_close * ma12_sc )  + ( acc_e_ma12_117 * ( 1 - ma12_sc ) )
acc_e_ma12_115 = ( price_116_close * ma12_sc )  + ( acc_e_ma12_116 * ( 1 - ma12_sc ) )
acc_e_ma12_114 = ( price_115_close * ma12_sc )  + ( acc_e_ma12_115 * ( 1 - ma12_sc ) )
acc_e_ma12_113 = ( price_114_close * ma12_sc )  + ( acc_e_ma12_114 * ( 1 - ma12_sc ) )
acc_e_ma12_112 = ( price_113_close * ma12_sc )  + ( acc_e_ma12_113 * ( 1 - ma12_sc ) )
acc_e_ma12_111 = ( price_112_close * ma12_sc )  + ( acc_e_ma12_112 * ( 1 - ma12_sc ) )

acc_e_ma12_110 = ( price_111_close * ma12_sc )  + ( acc_e_ma12_111 * ( 1 - ma12_sc ) )
acc_e_ma12_109 = ( price_110_close * ma12_sc )  + ( acc_e_ma12_110 * ( 1 - ma12_sc ) )
acc_e_ma12_108 = ( price_109_close * ma12_sc )  + ( acc_e_ma12_109 * ( 1 - ma12_sc ) )
acc_e_ma12_107 = ( price_108_close * ma12_sc )  + ( acc_e_ma12_108 * ( 1 - ma12_sc ) )
acc_e_ma12_106 = ( price_107_close * ma12_sc )  + ( acc_e_ma12_107 * ( 1 - ma12_sc ) )
acc_e_ma12_105 = ( price_106_close * ma12_sc )  + ( acc_e_ma12_106 * ( 1 - ma12_sc ) )
acc_e_ma12_104 = ( price_105_close * ma12_sc )  + ( acc_e_ma12_105 * ( 1 - ma12_sc ) )
acc_e_ma12_103 = ( price_104_close * ma12_sc )  + ( acc_e_ma12_104 * ( 1 - ma12_sc ) )
acc_e_ma12_102 = ( price_103_close * ma12_sc )  + ( acc_e_ma12_103 * ( 1 - ma12_sc ) )
acc_e_ma12_101 = ( price_102_close * ma12_sc )  + ( acc_e_ma12_102 * ( 1 - ma12_sc ) )

acc_e_ma12_100 = ( price_101_close * ma12_sc )  + ( acc_e_ma12_101 * ( 1 - ma12_sc ) )
acc_e_ma12_99 = ( price_100_close * ma12_sc )  + ( acc_e_ma12_100 * ( 1 - ma12_sc ) )
acc_e_ma12_98 = ( price_99_close * ma12_sc )  + ( acc_e_ma12_99 * ( 1 - ma12_sc ) )
acc_e_ma12_97 = ( price_98_close * ma12_sc )  + ( acc_e_ma12_98 * ( 1 - ma12_sc ) )
acc_e_ma12_96 = ( price_97_close * ma12_sc )  + ( acc_e_ma12_97 * ( 1 - ma12_sc ) )
acc_e_ma12_95 = ( price_96_close * ma12_sc )  + ( acc_e_ma12_96 * ( 1 - ma12_sc ) )
acc_e_ma12_94 = ( price_95_close * ma12_sc )  + ( acc_e_ma12_95 * ( 1 - ma12_sc ) )
acc_e_ma12_93 = ( price_94_close * ma12_sc )  + ( acc_e_ma12_94 * ( 1 - ma12_sc ) )
acc_e_ma12_92 = ( price_93_close * ma12_sc )  + ( acc_e_ma12_93 * ( 1 - ma12_sc ) )
acc_e_ma12_91 = ( price_92_close * ma12_sc )  + ( acc_e_ma12_92 * ( 1 - ma12_sc ) )

acc_e_ma12_90 = ( price_91_close * ma12_sc )  + ( acc_e_ma12_91 * ( 1 - ma12_sc ) )
acc_e_ma12_89 = ( price_90_close * ma12_sc )  + ( acc_e_ma12_90 * ( 1 - ma12_sc ) )
acc_e_ma12_88 = ( price_89_close * ma12_sc )  + ( acc_e_ma12_89 * ( 1 - ma12_sc ) )
acc_e_ma12_87 = ( price_88_close * ma12_sc )  + ( acc_e_ma12_88 * ( 1 - ma12_sc ) )
acc_e_ma12_86 = ( price_87_close * ma12_sc )  + ( acc_e_ma12_87 * ( 1 - ma12_sc ) )
acc_e_ma12_85 = ( price_86_close * ma12_sc )  + ( acc_e_ma12_86 * ( 1 - ma12_sc ) )
acc_e_ma12_84 = ( price_85_close * ma12_sc )  + ( acc_e_ma12_85 * ( 1 - ma12_sc ) )
acc_e_ma12_83 = ( price_84_close * ma12_sc )  + ( acc_e_ma12_84 * ( 1 - ma12_sc ) )
acc_e_ma12_82 = ( price_83_close * ma12_sc )  + ( acc_e_ma12_83 * ( 1 - ma12_sc ) )
acc_e_ma12_81 = ( price_82_close * ma12_sc )  + ( acc_e_ma12_82 * ( 1 - ma12_sc ) )

acc_e_ma12_80 = ( price_81_close * ma12_sc )  + ( acc_e_ma12_81 * ( 1 - ma12_sc ) )
acc_e_ma12_79 = ( price_80_close * ma12_sc )  + ( acc_e_ma12_80 * ( 1 - ma12_sc ) )
acc_e_ma12_78 = ( price_79_close * ma12_sc )  + ( acc_e_ma12_79 * ( 1 - ma12_sc ) )
acc_e_ma12_77 = ( price_78_close * ma12_sc )  + ( acc_e_ma12_78 * ( 1 - ma12_sc ) )
acc_e_ma12_76 = ( price_77_close * ma12_sc )  + ( acc_e_ma12_77 * ( 1 - ma12_sc ) )
acc_e_ma12_75 = ( price_76_close * ma12_sc )  + ( acc_e_ma12_76 * ( 1 - ma12_sc ) )
acc_e_ma12_74 = ( price_75_close * ma12_sc )  + ( acc_e_ma12_75 * ( 1 - ma12_sc ) )
acc_e_ma12_73 = ( price_74_close * ma12_sc )  + ( acc_e_ma12_74 * ( 1 - ma12_sc ) )
acc_e_ma12_72 = ( price_73_close * ma12_sc )  + ( acc_e_ma12_73 * ( 1 - ma12_sc ) )
acc_e_ma12_71 = ( price_72_close * ma12_sc )  + ( acc_e_ma12_72 * ( 1 - ma12_sc ) )

acc_e_ma12_70 = ( price_71_close * ma12_sc )  + ( acc_e_ma12_71 * ( 1 - ma12_sc ) )
acc_e_ma12_69 = ( price_70_close * ma12_sc )  + ( acc_e_ma12_70 * ( 1 - ma12_sc ) )
acc_e_ma12_68 = ( price_69_close * ma12_sc )  + ( acc_e_ma12_69 * ( 1 - ma12_sc ) )
acc_e_ma12_67 = ( price_68_close * ma12_sc )  + ( acc_e_ma12_68 * ( 1 - ma12_sc ) )
acc_e_ma12_66 = ( price_67_close * ma12_sc )  + ( acc_e_ma12_67 * ( 1 - ma12_sc ) )
acc_e_ma12_65 = ( price_66_close * ma12_sc )  + ( acc_e_ma12_66 * ( 1 - ma12_sc ) )
acc_e_ma12_64 = ( price_65_close * ma12_sc )  + ( acc_e_ma12_65 * ( 1 - ma12_sc ) )
acc_e_ma12_63 = ( price_64_close * ma12_sc )  + ( acc_e_ma12_64 * ( 1 - ma12_sc ) )
acc_e_ma12_62 = ( price_63_close * ma12_sc )  + ( acc_e_ma12_63 * ( 1 - ma12_sc ) )
acc_e_ma12_61 = ( price_62_close * ma12_sc )  + ( acc_e_ma12_62 * ( 1 - ma12_sc ) )

acc_e_ma12_60 = ( price_61_close * ma12_sc )  + ( acc_e_ma12_61 * ( 1 - ma12_sc ) )
acc_e_ma12_59 = ( price_60_close * ma12_sc )  + ( acc_e_ma12_60 * ( 1 - ma12_sc ) )
acc_e_ma12_58 = ( price_59_close * ma12_sc )  + ( acc_e_ma12_59 * ( 1 - ma12_sc ) )
acc_e_ma12_57 = ( price_58_close * ma12_sc )  + ( acc_e_ma12_58 * ( 1 - ma12_sc ) )
acc_e_ma12_56 = ( price_57_close * ma12_sc )  + ( acc_e_ma12_57 * ( 1 - ma12_sc ) )
acc_e_ma12_55 = ( price_56_close * ma12_sc )  + ( acc_e_ma12_56 * ( 1 - ma12_sc ) )
acc_e_ma12_54 = ( price_55_close * ma12_sc )  + ( acc_e_ma12_55 * ( 1 - ma12_sc ) )
acc_e_ma12_53 = ( price_54_close * ma12_sc )  + ( acc_e_ma12_54 * ( 1 - ma12_sc ) )
acc_e_ma12_52 = ( price_53_close * ma12_sc )  + ( acc_e_ma12_53 * ( 1 - ma12_sc ) )
acc_e_ma12_51 = ( price_52_close * ma12_sc )  + ( acc_e_ma12_52 * ( 1 - ma12_sc ) )

acc_e_ma12_50 = ( price_51_close * ma12_sc )  + ( acc_e_ma12_51 * ( 1 - ma12_sc ) )
acc_e_ma12_49 = ( price_50_close * ma12_sc )  + ( acc_e_ma12_50 * ( 1 - ma12_sc ) )
acc_e_ma12_48 = ( price_49_close * ma12_sc )  + ( acc_e_ma12_49 * ( 1 - ma12_sc ) )
acc_e_ma12_47 = ( price_48_close * ma12_sc )  + ( acc_e_ma12_48 * ( 1 - ma12_sc ) )
acc_e_ma12_46 = ( price_47_close * ma12_sc )  + ( acc_e_ma12_47 * ( 1 - ma12_sc ) )
acc_e_ma12_45 = ( price_46_close * ma12_sc )  + ( acc_e_ma12_46 * ( 1 - ma12_sc ) )
acc_e_ma12_44 = ( price_45_close * ma12_sc )  + ( acc_e_ma12_45 * ( 1 - ma12_sc ) )
acc_e_ma12_43 = ( price_44_close * ma12_sc )  + ( acc_e_ma12_44 * ( 1 - ma12_sc ) )
acc_e_ma12_42 = ( price_43_close * ma12_sc )  + ( acc_e_ma12_43 * ( 1 - ma12_sc ) )
acc_e_ma12_41 = ( price_42_close * ma12_sc )  + ( acc_e_ma12_42 * ( 1 - ma12_sc ) )

acc_e_ma12_40 = ( price_41_close * ma12_sc )  + ( acc_e_ma12_41 * ( 1 - ma12_sc ) )
acc_e_ma12_39 = ( price_40_close * ma12_sc )  + ( acc_e_ma12_40 * ( 1 - ma12_sc ) )
acc_e_ma12_38 = ( price_39_close * ma12_sc )  + ( acc_e_ma12_39 * ( 1 - ma12_sc ) )
acc_e_ma12_37 = ( price_38_close * ma12_sc )  + ( acc_e_ma12_38 * ( 1 - ma12_sc ) )
acc_e_ma12_36 = ( price_37_close * ma12_sc )  + ( acc_e_ma12_37 * ( 1 - ma12_sc ) )
acc_e_ma12_35 = ( price_36_close * ma12_sc )  + ( acc_e_ma12_36 * ( 1 - ma12_sc ) )
acc_e_ma12_34 = ( price_35_close * ma12_sc )  + ( acc_e_ma12_35 * ( 1 - ma12_sc ) )
acc_e_ma12_33 = ( price_34_close * ma12_sc )  + ( acc_e_ma12_34 * ( 1 - ma12_sc ) )
acc_e_ma12_32 = ( price_33_close * ma12_sc )  + ( acc_e_ma12_33 * ( 1 - ma12_sc ) )
acc_e_ma12_31 = ( price_32_close * ma12_sc )  + ( acc_e_ma12_32 * ( 1 - ma12_sc ) )

acc_e_ma12_30 = ( price_31_close * ma12_sc )  + ( acc_e_ma12_31 * ( 1 - ma12_sc ) )
acc_e_ma12_29 = ( price_30_close * ma12_sc )  + ( acc_e_ma12_30 * ( 1 - ma12_sc ) )
acc_e_ma12_28 = ( price_29_close * ma12_sc )  + ( acc_e_ma12_29 * ( 1 - ma12_sc ) )
acc_e_ma12_27 = ( price_28_close * ma12_sc )  + ( acc_e_ma12_28 * ( 1 - ma12_sc ) )
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
acc_ma26_57_1 = acc_ma12_57_1  +  price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close
acc_ma26_57 = acc_ma26_57_1 / 26
acc_ma26_58_1 = acc_ma12_58_1  +  price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close
acc_ma26_58 = acc_ma26_58_1 / 26
acc_ma26_59_1 = acc_ma12_59_1  +  price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close
acc_ma26_59 = acc_ma26_59_1 / 26
acc_ma26_60_1 = acc_ma12_60_1  +  price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close
acc_ma26_60 = acc_ma26_60_1 / 26


acc_ma26_61_1 = acc_ma12_61_1  +  price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close
acc_ma26_61 = acc_ma26_61_1 / 26
acc_ma26_62_1 = acc_ma12_62_1  +  price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close
acc_ma26_62 = acc_ma26_62_1 / 26
acc_ma26_63_1 = acc_ma12_63_1  +  price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close
acc_ma26_63 = acc_ma26_63_1 / 26
acc_ma26_64_1 = acc_ma12_64_1  +  price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close
acc_ma26_64 = acc_ma26_64_1 / 26
acc_ma26_65_1 = acc_ma12_65_1  +  price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close
acc_ma26_65 = acc_ma26_65_1 / 26

acc_ma26_66_1 = acc_ma12_66_1  +  price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close
acc_ma26_66 = acc_ma26_66_1 / 26
acc_ma26_67_1 = acc_ma12_67_1  +  price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close
acc_ma26_67 = acc_ma26_67_1 / 26
acc_ma26_68_1 = acc_ma12_68_1  +  price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close
acc_ma26_68 = acc_ma26_68_1 / 26
acc_ma26_69_1 = acc_ma12_69_1  +  price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close
acc_ma26_69 = acc_ma26_69_1 / 26
acc_ma26_70_1 = acc_ma12_70_1  +  price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close
acc_ma26_70 = acc_ma26_70_1 / 26


acc_ma26_71_1 = acc_ma12_71_1  +  price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close
acc_ma26_71 = acc_ma26_71_1 / 26
acc_ma26_72_1 = acc_ma12_72_1  +  price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close
acc_ma26_72 = acc_ma26_72_1 / 26
acc_ma26_73_1 = acc_ma12_73_1  +  price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close
acc_ma26_73 = acc_ma26_73_1 / 26
acc_ma26_74_1 = acc_ma12_74_1  +  price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close
acc_ma26_74 = acc_ma26_74_1 / 26
acc_ma26_75_1 = acc_ma12_75_1  +  price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close
acc_ma26_75 = acc_ma26_75_1 / 26

acc_ma26_76_1 = acc_ma12_76_1  +  price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close
acc_ma26_76 = acc_ma26_76_1 / 26
acc_ma26_77_1 = acc_ma12_77_1  +  price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close
acc_ma26_77 = acc_ma26_77_1 / 26
acc_ma26_78_1 = acc_ma12_78_1  +  price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close
acc_ma26_78 = acc_ma26_78_1 / 26
acc_ma26_79_1 = acc_ma12_79_1  +  price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close
acc_ma26_79 = acc_ma26_79_1 / 26
acc_ma26_80_1 = acc_ma12_80_1  +  price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close
acc_ma26_80 = acc_ma26_80_1 / 26


acc_ma26_81_1 = acc_ma12_81_1  +  price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close
acc_ma26_81 = acc_ma26_81_1 / 26
acc_ma26_82_1 = acc_ma12_82_1  +  price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close
acc_ma26_82 = acc_ma26_82_1 / 26
acc_ma26_83_1 = acc_ma12_83_1  +  price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close
acc_ma26_83 = acc_ma26_83_1 / 26
acc_ma26_84_1 = acc_ma12_84_1  +  price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close
acc_ma26_84 = acc_ma26_84_1 / 26
acc_ma26_85_1 = acc_ma12_85_1  +  price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close
acc_ma26_85 = acc_ma26_85_1 / 26

acc_ma26_86_1 = acc_ma12_86_1  +  price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close
acc_ma26_86 = acc_ma26_86_1 / 26
acc_ma26_87_1 = acc_ma12_87_1  +  price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close
acc_ma26_87 = acc_ma26_87_1 / 26
acc_ma26_88_1 = acc_ma12_88_1  +  price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close
acc_ma26_88 = acc_ma26_88_1 / 26
acc_ma26_89_1 = acc_ma12_89_1  +  price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close
acc_ma26_89 = acc_ma26_89_1 / 26
acc_ma26_90_1 = acc_ma12_90_1  +  price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close
acc_ma26_90 = acc_ma26_90_1 / 26


acc_ma26_91_1 = acc_ma12_91_1  +  price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close
acc_ma26_91 = acc_ma26_91_1 / 26
acc_ma26_92_1 = acc_ma12_92_1  +  price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close
acc_ma26_92 = acc_ma26_92_1 / 26
acc_ma26_93_1 = acc_ma12_93_1  +  price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close
acc_ma26_93 = acc_ma26_93_1 / 26
acc_ma26_94_1 = acc_ma12_94_1  +  price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close
acc_ma26_94 = acc_ma26_94_1 / 26
acc_ma26_95_1 = acc_ma12_95_1  +  price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close
acc_ma26_95 = acc_ma26_95_1 / 26

acc_ma26_96_1 = acc_ma12_96_1  +  price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close
acc_ma26_96 = acc_ma26_96_1 / 26
acc_ma26_97_1 = acc_ma12_97_1  +  price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close
acc_ma26_97 = acc_ma26_97_1 / 26
acc_ma26_98_1 = acc_ma12_98_1  +  price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close
acc_ma26_98 = acc_ma26_98_1 / 26
acc_ma26_99_1 = acc_ma12_99_1  +  price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close
acc_ma26_99 = acc_ma26_99_1 / 26
acc_ma26_100_1 = acc_ma12_100_1  +  price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close
acc_ma26_100 = acc_ma26_100_1 / 26


acc_ma26_101_1 = acc_ma12_101_1  +  price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close
acc_ma26_101 = acc_ma26_101_1 / 26
acc_ma26_102_1 = acc_ma12_102_1  +  price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close
acc_ma26_102 = acc_ma26_102_1 / 26
acc_ma26_103_1 = acc_ma12_103_1  +  price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close
acc_ma26_103 = acc_ma26_103_1 / 26
acc_ma26_104_1 = acc_ma12_104_1  +  price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close
acc_ma26_104 = acc_ma26_104_1 / 26
acc_ma26_105_1 = acc_ma12_105_1  +  price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close
acc_ma26_105 = acc_ma26_105_1 / 26

acc_ma26_106_1 = acc_ma12_106_1  +  price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close
acc_ma26_106 = acc_ma26_106_1 / 26
acc_ma26_107_1 = acc_ma12_107_1  +  price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close
acc_ma26_107 = acc_ma26_107_1 / 26
acc_ma26_108_1 = acc_ma12_108_1  +  price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close
acc_ma26_108 = acc_ma26_108_1 / 26
acc_ma26_109_1 = acc_ma12_109_1  +  price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close
acc_ma26_109 = acc_ma26_109_1 / 26
acc_ma26_110_1 = acc_ma12_110_1  +  price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close
acc_ma26_110 = acc_ma26_110_1 / 26


acc_ma26_111_1 = acc_ma12_111_1  +  price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close
acc_ma26_111 = acc_ma26_111_1 / 26
acc_ma26_112_1 = acc_ma12_112_1  +  price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close
acc_ma26_112 = acc_ma26_112_1 / 26
acc_ma26_113_1 = acc_ma12_113_1  +  price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close
acc_ma26_113 = acc_ma26_113_1 / 26
acc_ma26_114_1 = acc_ma12_114_1  +  price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close
acc_ma26_114 = acc_ma26_114_1 / 26
acc_ma26_115_1 = acc_ma12_115_1  +  price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close
acc_ma26_115 = acc_ma26_115_1 / 26

acc_ma26_116_1 = acc_ma12_116_1  +  price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close
acc_ma26_116 = acc_ma26_116_1 / 26
acc_ma26_117_1 = acc_ma12_117_1  +  price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close
acc_ma26_117 = acc_ma26_117_1 / 26
acc_ma26_118_1 = acc_ma12_118_1  +  price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close
acc_ma26_118 = acc_ma26_118_1 / 26
acc_ma26_119_1 = acc_ma12_119_1  +  price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close
acc_ma26_119 = acc_ma26_119_1 / 26
acc_ma26_120_1 = acc_ma12_120_1  +  price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close
acc_ma26_120 = acc_ma26_120_1 / 26


acc_ma26_121_1 = acc_ma12_121_1  +  price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close
acc_ma26_121 = acc_ma26_121_1 / 26
acc_ma26_122_1 = acc_ma12_122_1  +  price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close
acc_ma26_122 = acc_ma26_122_1 / 26
acc_ma26_123_1 = acc_ma12_123_1  +  price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close
acc_ma26_123 = acc_ma26_123_1 / 26
acc_ma26_124_1 = acc_ma12_124_1  +  price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close
acc_ma26_124 = acc_ma26_124_1 / 26
acc_ma26_125_1 = acc_ma12_125_1  +  price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close
acc_ma26_125 = acc_ma26_125_1 / 26

acc_ma26_126_1 = acc_ma12_126_1  +  price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close
acc_ma26_126 = acc_ma26_126_1 / 26
acc_ma26_127_1 = acc_ma12_127_1  +  price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close
acc_ma26_127 = acc_ma26_127_1 / 26
acc_ma26_128_1 = acc_ma12_128_1  +  price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close
acc_ma26_128 = acc_ma26_128_1 / 26
acc_ma26_129_1 = acc_ma12_129_1  +  price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close
acc_ma26_129 = acc_ma26_129_1 / 26
acc_ma26_130_1 = acc_ma12_130_1  +  price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close
acc_ma26_130 = acc_ma26_130_1 / 26


acc_ma26_131_1 = acc_ma12_131_1  +  price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close
acc_ma26_131 = acc_ma26_131_1 / 26
acc_ma26_132_1 = acc_ma12_132_1  +  price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close
acc_ma26_132 = acc_ma26_132_1 / 26
acc_ma26_133_1 = acc_ma12_133_1  +  price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close
acc_ma26_133 = acc_ma26_133_1 / 26
acc_ma26_134_1 = acc_ma12_134_1  +  price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close
acc_ma26_134 = acc_ma26_134_1 / 26
acc_ma26_135_1 = acc_ma12_135_1  +  price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close
acc_ma26_135 = acc_ma26_135_1 / 26

acc_ma26_136_1 = acc_ma12_136_1  +  price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close
acc_ma26_136 = acc_ma26_136_1 / 26
acc_ma26_137_1 = acc_ma12_137_1  +  price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close + price_163_close
acc_ma26_137 = acc_ma26_137_1 / 26
acc_ma26_138_1 = acc_ma12_138_1  +  price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close + price_163_close + price_164_close
acc_ma26_138 = acc_ma26_138_1 / 26
acc_ma26_139_1 = acc_ma12_139_1  +  price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close + price_163_close + price_164_close + price_165_close
acc_ma26_139 = acc_ma26_139_1 / 26
acc_ma26_140_1 = acc_ma12_140_1  +  price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close + price_163_close + price_164_close + price_165_close + price_166_close
acc_ma26_140 = acc_ma26_140_1 / 26








# EMA - 장기 26 지수이동평균값 구하기
acc_e_ma26_139 = acc_ma26_140
acc_e_ma26_138 = ( price_139_close * ma26_sc )  + ( acc_e_ma26_139 * ( 1 - ma26_sc ) )
acc_e_ma26_137 = ( price_138_close * ma26_sc )  + ( acc_e_ma26_138 * ( 1 - ma26_sc ) )
acc_e_ma26_136 = ( price_137_close * ma26_sc )  + ( acc_e_ma26_137 * ( 1 - ma26_sc ) )
acc_e_ma26_135 = ( price_136_close * ma26_sc )  + ( acc_e_ma26_136 * ( 1 - ma26_sc ) )
acc_e_ma26_134 = ( price_135_close * ma26_sc )  + ( acc_e_ma26_135 * ( 1 - ma26_sc ) )
acc_e_ma26_133 = ( price_134_close * ma26_sc )  + ( acc_e_ma26_134 * ( 1 - ma26_sc ) )
acc_e_ma26_132 = ( price_133_close * ma26_sc )  + ( acc_e_ma26_133 * ( 1 - ma26_sc ) )
acc_e_ma26_131 = ( price_132_close * ma26_sc )  + ( acc_e_ma26_132 * ( 1 - ma26_sc ) )

acc_e_ma26_130 = ( price_131_close * ma26_sc )  + ( acc_e_ma26_131 * ( 1 - ma26_sc ) )
acc_e_ma26_129 = ( price_130_close * ma26_sc )  + ( acc_e_ma26_130 * ( 1 - ma26_sc ) )
acc_e_ma26_128 = ( price_129_close * ma26_sc )  + ( acc_e_ma26_129 * ( 1 - ma26_sc ) )
acc_e_ma26_127 = ( price_128_close * ma26_sc )  + ( acc_e_ma26_128 * ( 1 - ma26_sc ) )
acc_e_ma26_126 = ( price_127_close * ma26_sc )  + ( acc_e_ma26_127 * ( 1 - ma26_sc ) )
acc_e_ma26_125 = ( price_126_close * ma26_sc )  + ( acc_e_ma26_126 * ( 1 - ma26_sc ) )
acc_e_ma26_124 = ( price_125_close * ma26_sc )  + ( acc_e_ma26_125 * ( 1 - ma26_sc ) )
acc_e_ma26_123 = ( price_124_close * ma26_sc )  + ( acc_e_ma26_124 * ( 1 - ma26_sc ) )
acc_e_ma26_122 = ( price_123_close * ma26_sc )  + ( acc_e_ma26_123 * ( 1 - ma26_sc ) )
acc_e_ma26_121 = ( price_122_close * ma26_sc )  + ( acc_e_ma26_122 * ( 1 - ma26_sc ) )

acc_e_ma26_120 = ( price_121_close * ma26_sc )  + ( acc_e_ma26_121 * ( 1 - ma26_sc ) )
acc_e_ma26_119 = ( price_120_close * ma26_sc )  + ( acc_e_ma26_120 * ( 1 - ma26_sc ) )
acc_e_ma26_118 = ( price_119_close * ma26_sc )  + ( acc_e_ma26_119 * ( 1 - ma26_sc ) )
acc_e_ma26_117 = ( price_118_close * ma26_sc )  + ( acc_e_ma26_118 * ( 1 - ma26_sc ) )
acc_e_ma26_116 = ( price_117_close * ma26_sc )  + ( acc_e_ma26_117 * ( 1 - ma26_sc ) )
acc_e_ma26_115 = ( price_116_close * ma26_sc )  + ( acc_e_ma26_116 * ( 1 - ma26_sc ) )
acc_e_ma26_114 = ( price_115_close * ma26_sc )  + ( acc_e_ma26_115 * ( 1 - ma26_sc ) )
acc_e_ma26_113 = ( price_114_close * ma26_sc )  + ( acc_e_ma26_114 * ( 1 - ma26_sc ) )
acc_e_ma26_112 = ( price_113_close * ma26_sc )  + ( acc_e_ma26_113 * ( 1 - ma26_sc ) )
acc_e_ma26_111 = ( price_112_close * ma26_sc )  + ( acc_e_ma26_112 * ( 1 - ma26_sc ) )

acc_e_ma26_110 = ( price_111_close * ma26_sc )  + ( acc_e_ma26_111 * ( 1 - ma26_sc ) )
acc_e_ma26_109 = ( price_110_close * ma26_sc )  + ( acc_e_ma26_110 * ( 1 - ma26_sc ) )
acc_e_ma26_108 = ( price_109_close * ma26_sc )  + ( acc_e_ma26_109 * ( 1 - ma26_sc ) )
acc_e_ma26_107 = ( price_108_close * ma26_sc )  + ( acc_e_ma26_108 * ( 1 - ma26_sc ) )
acc_e_ma26_106 = ( price_107_close * ma26_sc )  + ( acc_e_ma26_107 * ( 1 - ma26_sc ) )
acc_e_ma26_105 = ( price_106_close * ma26_sc )  + ( acc_e_ma26_106 * ( 1 - ma26_sc ) )
acc_e_ma26_104 = ( price_105_close * ma26_sc )  + ( acc_e_ma26_105 * ( 1 - ma26_sc ) )
acc_e_ma26_103 = ( price_104_close * ma26_sc )  + ( acc_e_ma26_104 * ( 1 - ma26_sc ) )
acc_e_ma26_102 = ( price_103_close * ma26_sc )  + ( acc_e_ma26_103 * ( 1 - ma26_sc ) )
acc_e_ma26_101 = ( price_102_close * ma26_sc )  + ( acc_e_ma26_102 * ( 1 - ma26_sc ) )

acc_e_ma26_100 = ( price_101_close * ma26_sc )  + ( acc_e_ma26_101 * ( 1 - ma26_sc ) )
acc_e_ma26_99 = ( price_100_close * ma26_sc )  + ( acc_e_ma26_100 * ( 1 - ma26_sc ) )
acc_e_ma26_98 = ( price_99_close * ma26_sc )  + ( acc_e_ma26_99 * ( 1 - ma26_sc ) )
acc_e_ma26_97 = ( price_98_close * ma26_sc )  + ( acc_e_ma26_98 * ( 1 - ma26_sc ) )
acc_e_ma26_96 = ( price_97_close * ma26_sc )  + ( acc_e_ma26_97 * ( 1 - ma26_sc ) )
acc_e_ma26_95 = ( price_96_close * ma26_sc )  + ( acc_e_ma26_96 * ( 1 - ma26_sc ) )
acc_e_ma26_94 = ( price_95_close * ma26_sc )  + ( acc_e_ma26_95 * ( 1 - ma26_sc ) )
acc_e_ma26_93 = ( price_94_close * ma26_sc )  + ( acc_e_ma26_94 * ( 1 - ma26_sc ) )
acc_e_ma26_92 = ( price_93_close * ma26_sc )  + ( acc_e_ma26_93 * ( 1 - ma26_sc ) )
acc_e_ma26_91 = ( price_92_close * ma26_sc )  + ( acc_e_ma26_92 * ( 1 - ma26_sc ) )

acc_e_ma26_90 = ( price_91_close * ma26_sc )  + ( acc_e_ma26_91 * ( 1 - ma26_sc ) )
acc_e_ma26_89 = ( price_90_close * ma26_sc )  + ( acc_e_ma26_90 * ( 1 - ma26_sc ) )
acc_e_ma26_88 = ( price_89_close * ma26_sc )  + ( acc_e_ma26_89 * ( 1 - ma26_sc ) )
acc_e_ma26_87 = ( price_88_close * ma26_sc )  + ( acc_e_ma26_88 * ( 1 - ma26_sc ) )
acc_e_ma26_86 = ( price_87_close * ma26_sc )  + ( acc_e_ma26_87 * ( 1 - ma26_sc ) )
acc_e_ma26_85 = ( price_86_close * ma26_sc )  + ( acc_e_ma26_86 * ( 1 - ma26_sc ) )
acc_e_ma26_84 = ( price_85_close * ma26_sc )  + ( acc_e_ma26_85 * ( 1 - ma26_sc ) )
acc_e_ma26_83 = ( price_84_close * ma26_sc )  + ( acc_e_ma26_84 * ( 1 - ma26_sc ) )
acc_e_ma26_82 = ( price_83_close * ma26_sc )  + ( acc_e_ma26_83 * ( 1 - ma26_sc ) )
acc_e_ma26_81 = ( price_82_close * ma26_sc )  + ( acc_e_ma26_82 * ( 1 - ma26_sc ) )

acc_e_ma26_80 = ( price_81_close * ma26_sc )  + ( acc_e_ma26_81 * ( 1 - ma26_sc ) )
acc_e_ma26_79 = ( price_80_close * ma26_sc )  + ( acc_e_ma26_80 * ( 1 - ma26_sc ) )
acc_e_ma26_78 = ( price_79_close * ma26_sc )  + ( acc_e_ma26_79 * ( 1 - ma26_sc ) )
acc_e_ma26_77 = ( price_78_close * ma26_sc )  + ( acc_e_ma26_78 * ( 1 - ma26_sc ) )
acc_e_ma26_76 = ( price_77_close * ma26_sc )  + ( acc_e_ma26_77 * ( 1 - ma26_sc ) )
acc_e_ma26_75 = ( price_76_close * ma26_sc )  + ( acc_e_ma26_76 * ( 1 - ma26_sc ) )
acc_e_ma26_74 = ( price_75_close * ma26_sc )  + ( acc_e_ma26_75 * ( 1 - ma26_sc ) )
acc_e_ma26_73 = ( price_74_close * ma26_sc )  + ( acc_e_ma26_74 * ( 1 - ma26_sc ) )
acc_e_ma26_72 = ( price_73_close * ma26_sc )  + ( acc_e_ma26_73 * ( 1 - ma26_sc ) )
acc_e_ma26_71 = ( price_72_close * ma26_sc )  + ( acc_e_ma26_72 * ( 1 - ma26_sc ) )

acc_e_ma26_70 = ( price_71_close * ma26_sc )  + ( acc_e_ma26_71 * ( 1 - ma26_sc ) )
acc_e_ma26_69 = ( price_70_close * ma26_sc )  + ( acc_e_ma26_70 * ( 1 - ma26_sc ) )
acc_e_ma26_68 = ( price_69_close * ma26_sc )  + ( acc_e_ma26_69 * ( 1 - ma26_sc ) )
acc_e_ma26_67 = ( price_68_close * ma26_sc )  + ( acc_e_ma26_68 * ( 1 - ma26_sc ) )
acc_e_ma26_66 = ( price_67_close * ma26_sc )  + ( acc_e_ma26_67 * ( 1 - ma26_sc ) )
acc_e_ma26_65 = ( price_66_close * ma26_sc )  + ( acc_e_ma26_66 * ( 1 - ma26_sc ) )
acc_e_ma26_64 = ( price_65_close * ma26_sc )  + ( acc_e_ma26_65 * ( 1 - ma26_sc ) )
acc_e_ma26_63 = ( price_64_close * ma26_sc )  + ( acc_e_ma26_64 * ( 1 - ma26_sc ) )
acc_e_ma26_62 = ( price_63_close * ma26_sc )  + ( acc_e_ma26_63 * ( 1 - ma26_sc ) )
acc_e_ma26_61 = ( price_62_close * ma26_sc )  + ( acc_e_ma26_62 * ( 1 - ma26_sc ) )

acc_e_ma26_60 = ( price_61_close * ma26_sc )  + ( acc_e_ma26_61 * ( 1 - ma26_sc ) )
acc_e_ma26_59 = ( price_60_close * ma26_sc )  + ( acc_e_ma26_60 * ( 1 - ma26_sc ) )
acc_e_ma26_58 = ( price_59_close * ma26_sc )  + ( acc_e_ma26_59 * ( 1 - ma26_sc ) )
acc_e_ma26_57 = ( price_58_close * ma26_sc )  + ( acc_e_ma26_58 * ( 1 - ma26_sc ) )
acc_e_ma26_56 = ( price_57_close * ma26_sc )  + ( acc_e_ma26_57 * ( 1 - ma26_sc ) )
acc_e_ma26_55 = ( price_56_close * ma26_sc )  + ( acc_e_ma26_56 * ( 1 - ma26_sc ) )
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
print( "macd값" )
print( "========== ========== ========== ========== ==========" )
acc_macd_ok_1 = acc_e_ma12_1 - acc_e_ma26_1
print( f"e_macd_ok_1 ( { acc_macd_ok_1 } ) =  acc_e_ma12_1 ( { acc_e_ma12_1 } ) - acc_e_ma26_1 ( { acc_e_ma26_1 } )" )

acc_macd_ok_2 = acc_e_ma12_2 - acc_e_ma26_2
print( f"e_macd_ok_2 ( { acc_macd_ok_2 } ) =  acc_e_ma12_2 ( { acc_e_ma12_2 } ) - acc_e_ma26_2 ( { acc_e_ma26_2 } )" )

acc_macd_ok_3 = acc_e_ma12_3 - acc_e_ma26_3
print( f"e_macd_ok_3 ( { acc_macd_ok_3 } ) =  acc_e_ma12_3 ( { acc_e_ma12_3 } ) - acc_e_ma26_3 ( { acc_e_ma26_3 } )" )

acc_macd_ok_4 = acc_e_ma12_4 - acc_e_ma26_4
print( f"e_macd_ok_4 ( { acc_macd_ok_4 } ) =  acc_e_ma12_4 ( { acc_e_ma12_4 } ) - acc_e_ma26_4 ( { acc_e_ma26_4 } )" )

acc_macd_ok_5 = acc_e_ma12_5 - acc_e_ma26_5
print( f"e_macd_ok_5 ( { acc_macd_ok_5 } ) =  acc_e_ma12_5 ( { acc_e_ma12_5 } ) - acc_e_ma26_5 ( { acc_e_ma26_5 } )" )

acc_macd_ok_6 = acc_e_ma12_6 - acc_e_ma26_6
print( f"e_macd_ok_6 ( { acc_macd_ok_6 } ) =  acc_e_ma12_6 ( { acc_e_ma12_6 } ) - acc_e_ma26_6 ( { acc_e_ma26_6 } )" )

acc_macd_ok_7 = acc_e_ma12_7 - acc_e_ma26_7
print( f"e_macd_ok_7 ( { acc_macd_ok_7 } ) =  acc_e_ma12_7 ( { acc_e_ma12_7 } ) - acc_e_ma26_7 ( { acc_e_ma26_7 } )" )

acc_macd_ok_8 = acc_e_ma12_8 - acc_e_ma26_8
print( f"e_macd_ok_8 ( { acc_macd_ok_8 } ) =  acc_e_ma12_8 ( { acc_e_ma12_8 } ) - acc_e_ma26_8 ( { acc_e_ma26_8 } )" )

acc_macd_ok_9 = acc_e_ma12_9 - acc_e_ma26_9
print( f"e_macd_ok_9 ( { acc_macd_ok_9 } ) =  acc_e_ma12_9 ( { acc_e_ma12_9 } ) - acc_e_ma26_9 ( { acc_e_ma26_9 } )" )

acc_macd_ok_10 = acc_e_ma12_10 - acc_e_ma26_10
print( f"e_macd_ok_10 ( { acc_macd_ok_10 } ) =  acc_e_ma12_10 ( { acc_e_ma12_10 } ) - acc_e_ma26_10 ( { acc_e_ma26_10 } )" )

acc_macd_ok_11 = acc_e_ma12_11 - acc_e_ma26_11
print( f"e_macd_ok_11 ( { acc_macd_ok_11 } ) =  acc_e_ma12_11 ( { acc_e_ma12_11 } ) - acc_e_ma26_11 ( { acc_e_ma26_11 } )" )

acc_macd_ok_12 = acc_e_ma12_12 - acc_e_ma26_12
print( f"e_macd_ok_12 ( { acc_macd_ok_12 } ) =  acc_e_ma12_12 ( { acc_e_ma12_12 } ) - acc_e_ma26_12 ( { acc_e_ma26_12 } )" )

acc_macd_ok_13 = acc_e_ma12_13 - acc_e_ma26_13
print( f"e_macd_ok_13 ( { acc_macd_ok_13 } ) =  acc_e_ma12_13 ( { acc_e_ma12_13 } ) - acc_e_ma26_13 ( { acc_e_ma26_13 } )" )

acc_macd_ok_14 = acc_e_ma12_14 - acc_e_ma26_14
print( f"e_macd_ok_14 ( { acc_macd_ok_14 } ) =  acc_e_ma12_14 ( { acc_e_ma12_14 } ) - acc_e_ma26_14 ( { acc_e_ma26_14 } )" )

acc_macd_ok_15 = acc_e_ma12_15 - acc_e_ma26_15
print( f"e_macd_ok_15 ( { acc_macd_ok_15 } ) =  acc_e_ma12_15 ( { acc_e_ma12_15 } ) - acc_e_ma26_15 ( { acc_e_ma26_15 } )" )

acc_macd_ok_16 = acc_e_ma12_16 - acc_e_ma26_16
print( f"e_macd_ok_16 ( { acc_macd_ok_16 } ) =  acc_e_ma12_16 ( { acc_e_ma12_16 } ) - acc_e_ma26_16 ( { acc_e_ma26_16 } )" )

acc_macd_ok_17 = acc_e_ma12_17 - acc_e_ma26_17
print( f"e_macd_ok_17 ( { acc_macd_ok_17 } ) =  acc_e_ma12_17 ( { acc_e_ma12_17 } ) - acc_e_ma26_17 ( { acc_e_ma26_17 } )" )
print()





print( "시그널값" )
print( "========== ========== ========== ========== ==========" )
# signal = macd 9일선, macd값의 9이평선.
# + 는 0선 이상, - 는 0선 이하
acc_signal_1 = ( acc_macd_ok_1 + acc_macd_ok_2 + acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 ) / 9
print( f"acc_signal_1 = ( { acc_signal_1 } )" )

acc_signal_2 = ( acc_macd_ok_2 + acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 ) / 9
print( f"acc_signal_2 = ( { acc_signal_2 } )" )

acc_signal_3 = ( acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 ) / 9
print( f"acc_signal_3 = ( { acc_signal_3 } )" )

acc_signal_4 = ( acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 ) / 9
print( f"acc_signal_4 = ( { acc_signal_4 } )" )

acc_signal_5 = ( acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 ) / 9
print( f"acc_signal_5 = ( { acc_signal_5 } )" )

acc_signal_6 = ( acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 ) / 9
print( f"acc_signal_6 = ( { acc_signal_6 } )" )

acc_signal_7 = ( acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 ) / 9
print( f"acc_signal_7 = ( { acc_signal_7 } )" )

acc_signal_8 = ( acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 + acc_macd_ok_16 ) / 9
print( f"acc_signal_8 = ( { acc_signal_8 } )" )

acc_signal_9 = ( acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 + acc_macd_ok_16 + acc_macd_ok_17 ) / 9
print( f"acc_signal_9 = ( { acc_signal_9 } )" )

print()

# 최종값
# macd - 시그널 = + 는 골든크로스, - 는 데드크로스
print( "[최종] 간격 = macd - 시그널" )
print( "========== ========== ========== ========== ==========" )
acc_macd1 = acc_macd_ok_1 - acc_signal_1
print( f"acc_macd1 ( { acc_macd1 } ) = acc_macd_ok_1 ( { acc_macd_ok_1 } ) - acc_signal_1 ( { acc_signal_1 } )" )
acc_macd2 = acc_macd_ok_2 - acc_signal_2
print( f"acc_macd2 ( { acc_macd2 } ) = acc_macd_ok_2 ( { acc_macd_ok_2 } ) - acc_signal_2 ( { acc_signal_2 } )" )
acc_macd3 = acc_macd_ok_3 - acc_signal_3
print( f"acc_macd3 ( { acc_macd3 } ) = acc_macd_ok_3 ( { acc_macd_ok_3 } ) - acc_signal_3 ( { acc_signal_3 } )" )
acc_macd4 = acc_macd_ok_4 - acc_signal_4
print( f"acc_macd4 ( { acc_macd4 } ) = acc_macd_ok_4 ( { acc_macd_ok_4 } ) - acc_signal_4 ( { acc_signal_4 } )" )
acc_macd5 = acc_macd_ok_5 - acc_signal_5
print( f"acc_macd5 ( { acc_macd5 } ) = acc_macd_ok_5 ( { acc_macd_ok_5 } ) - acc_signal_5 ( { acc_signal_5 } )" )
acc_macd6 = acc_macd_ok_6 - acc_signal_6
print( f"acc_macd6 ( { acc_macd6 } ) = acc_macd_ok_6 ( { acc_macd_ok_6 } ) - acc_signal_6 ( { acc_signal_6 } )" )
acc_macd7 = acc_macd_ok_7 - acc_signal_7
print( f"acc_macd7 ( { acc_macd7 } ) = acc_macd_ok_7 ( { acc_macd_ok_7 } ) - acc_signal_7 ( { acc_signal_7 } )" )
acc_macd8 = acc_macd_ok_8 - acc_signal_8
print( f"acc_macd8 ( { acc_macd8 } ) = acc_macd_ok_8 ( { acc_macd_ok_8 } ) - acc_signal_8 ( { acc_signal_8 } )" )
acc_macd9 = acc_macd_ok_9 - acc_signal_9
print( f"acc_macd9 ( { acc_macd9 } ) = acc_macd_ok_9 ( { acc_macd_ok_9 } ) - acc_signal_9 ( { acc_signal_9 } )" )
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

print( "========== ========== ==========" )
print( "       선 물  잔 고  조 회" )
print( "========== ========== ==========" )
print()

balance = binance.fetch_balance()
print( "보유코인" )
pprint.pprint( balance[ 'total' ] )
pprint.pprint( balance[ 'total' ][ 'USDT' ] )
pprint.pprint( balance[ 'total' ][ 'BTC' ] )
print()

print( "포지션" )
positions = balance[ 'info' ][ 'positions' ]
print()

for position in positions:
    if position[ 'symbol' ] == "BTCUSDT":
        pprint.pprint( position )

        btc_position_amt = float( position[ 'positionAmt' ] )
        print( f"현재 포지션은 ? { btc_position_amt }" )
        print( f"진입한 btc코인의 변수타입은? { type( btc_position_amt ) }" )




        if btc_position_amt > 0:
            print( "1. 현재 롱포지션 진입상태" )
            btc_position_1 = 1

        elif btc_position_amt == 0:
            print( "2. 현재 포지션 진입을 안한상태" )
            btc_position_1 = 0

        elif btc_position_amt < 0:
            print( "3. 현재 숏포지션 진입상태" )
            btc_position_1 = -1

        btc_future_leverage = int( position[ 'leverage' ] )
        print( f"현재 레버리지의 변수타입은? { type( btc_future_leverage ) }" )



print()
print()






###################
# 선물 현재가 조회 #
###################
print( "========== ========== ==========" )
print( "      선 물  현 재 가  조 회" )
print( "========== ========== ==========" )
print()

btc = binance.fetch_ticker( "BTC/USDT" )
pprint.pprint( float( btc[ 'last' ] ) )
print( f"BTC/USDT 현재가 = { btc[ 'last' ] }" )
print()
print()



######################
# 거래가능한 USDT 갯수 #
######################
print( "========== ========== ==========" )
print( "        거래가능한 BTC 갯수" )
print( "========== ========== ==========" )
print()
balance = binance.fetch_balance()
usdt = float( balance[ 'total' ][ 'USDT' ] )
print( f"보유 USDT = { usdt }" )
print( f"보유 USDT 의 변수타입은? { type( usdt ) }" )

btc = binance.fetch_ticker( symbol = "BTC/USDT" )
cur_price = float( btc[ 'last' ] )
print( f"BTC 종가의 변수타입은? { type( cur_price ) }" )
amount_1 = cal_amount( usdt, cur_price )
print( f"보유 USDT로 BTC 거래가능한 갯수 = { amount_1 }" )
print( f"보유 USDT로 BTC 거래가능한 갯수의 변수타입은? { type( amount_1 ) }" )
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






























































#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+

# 포지션 진입 최대 usdt 금액
usdt_trade_MAX_price = 1100

#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+


# 현재 레버리지 배율 10 배
#btc_leverage = 10  # 현재 레버리지 설정값
btc_leverage = btc_future_leverage  # 레버리지 가져옴

if btc_leverage > 1:   # 레버리지 비율이 1 초과면 
    btc_leverage_1 = btc_leverage - 1  # 진입시 사용할 레버리지 배율
elif btc_leverage <= 1:   # 레버리지 비율이 1 이하이면 
    btc_leverage_1 = 1  # 진입시 사용할 레버리지 배율


#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+


print( f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" )
print( f"0-1. 재시작시 포지션 유지중이면" )
print()
print( f"0-2. 현재 macd 코드는? btc_mode = { btc_mode }" )
print()
print( f"0-3-1. 현재 거래중인 코인갯수는? btc_position_amt = { btc_position_amt }" )
print( f"0-3-2. 진입한 btc코인의 변수타입은? { type( btc_position_amt ) }" )
print( f"0-3-3. 현재 거래중인 코인의 포지션 코드는? btc_position_1 = { btc_position_1 }" )

if btc_position_amt > 0:
    print( "0-3-4. 현재 롱포지션 진입상태" )
    btc_position_1 = 1

elif btc_position_amt == 0:
    print( "0-3-5. 현재 포지션 진입을 안한상태" )
    btc_position_1 = 0

elif btc_position_amt < 0:
    print( "0-3-6. 현재 숏포지션 진입상태" )
    btc_position_1 = -1

print()
print( f"0-4-1. 현재 설정된 레버리지 배율은 btc_leverage = { btc_leverage }" )
print( f"0-4-2. 진입시 설정될 레버리지 배율은 btc_leverage_1 = { btc_leverage_1 }" )
print( f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" )





################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################




print()
print( "----- =====  거래 시작 ===== -----" )
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

#    if now.hour == 1 or now.hour == 5 or now.hour == 9 or now.hour == 13 or now.hour == 17 or now.hour == 21:
    if now.minute == 1:
        time.sleep(5)

        print()
        print()
        print( "-=-=-=-=-=- ********** -=-=-=-=-=- ********** -=-=-=-=-=-" )
        print( f"[ 현재시간 : {now} ]   -   시작" )
        print( "-=-=-=-=-=- ********** -=-=-=-=-=- ********** -=-=-=-=-=-" )
        print()








        btc = exchange.fetch_ohlcv(
            symbol = symbol1,
            timeframe = '1h', 
            since = None, 
            limit = 200
        )

        df = pd.DataFrame( data = btc, columns = [ 'datetime', 'open', 'high', 'low', 'close', 'volume' ] )
        df[ 'datetime' ] = pd.to_datetime( df[ 'datetime' ], unit = 'ms' )
        df.set_index( 'datetime', inplace = True )





        # 종가받기 200개
        print( "========== 1시간봉 종가 받기 ==========" )
        print()
        # 0은 아무것도 아님.
        price_0_close = df.iloc[ 0 ][ 'close' ]
        #price_0_time = df.iloc[ 0 ][ 'datetime' ]

        # -1은 현재가.
        price_1_close = df.iloc[ -1 ][ 'close' ]

        ########################################
        # -2는 1시간전 종가. 여기부터 macd 계산.
        price_2_close = df.iloc[ -2 ][ 'close' ]
        price_3_close = df.iloc[ -3 ][ 'close' ]
        price_4_close = df.iloc[ -4 ][ 'close' ]
        price_5_close = df.iloc[ -5 ][ 'close' ]
        price_6_close = df.iloc[ -6 ][ 'close' ]
        price_7_close = df.iloc[ -7 ][ 'close' ]
        price_8_close = df.iloc[ -8 ][ 'close' ]
        price_9_close = df.iloc[ -9 ][ 'close' ]
        price_10_close = df.iloc[ -10 ][ 'close' ]

        price_11_close = df.iloc[ -11 ][ 'close' ]
        price_12_close = df.iloc[ -12 ][ 'close' ]
        price_13_close = df.iloc[ -13 ][ 'close' ]
        price_14_close = df.iloc[ -14 ][ 'close' ]
        price_15_close = df.iloc[ -15 ][ 'close' ]
        price_16_close = df.iloc[ -16 ][ 'close' ]
        price_17_close = df.iloc[ -17 ][ 'close' ]
        price_18_close = df.iloc[ -18 ][ 'close' ]
        price_19_close = df.iloc[ -19 ][ 'close' ]
        price_20_close = df.iloc[ -20 ][ 'close' ]

        price_21_close = df.iloc[ -21 ][ 'close' ]
        price_22_close = df.iloc[ -22 ][ 'close' ]
        price_23_close = df.iloc[ -23 ][ 'close' ]
        price_24_close = df.iloc[ -24 ][ 'close' ]
        price_25_close = df.iloc[ -25 ][ 'close' ]
        price_26_close = df.iloc[ -26 ][ 'close' ]
        price_27_close = df.iloc[ -27 ][ 'close' ]
        price_28_close = df.iloc[ -28 ][ 'close' ]
        price_29_close = df.iloc[ -29 ][ 'close' ]
        price_30_close = df.iloc[ -30 ][ 'close' ]

        price_31_close = df.iloc[ -31 ][ 'close' ]
        price_32_close = df.iloc[ -32 ][ 'close' ]
        price_33_close = df.iloc[ -33 ][ 'close' ]
        price_34_close = df.iloc[ -34 ][ 'close' ]
        price_35_close = df.iloc[ -35 ][ 'close' ]
        price_36_close = df.iloc[ -36 ][ 'close' ]
        price_37_close = df.iloc[ -37 ][ 'close' ]
        price_38_close = df.iloc[ -38 ][ 'close' ]
        price_39_close = df.iloc[ -39 ][ 'close' ]
        price_40_close = df.iloc[ -40 ][ 'close' ]

        price_41_close = df.iloc[ -41 ][ 'close' ]
        price_42_close = df.iloc[ -42 ][ 'close' ]
        price_43_close = df.iloc[ -43 ][ 'close' ]
        price_44_close = df.iloc[ -44 ][ 'close' ]
        price_45_close = df.iloc[ -45 ][ 'close' ]
        price_46_close = df.iloc[ -46 ][ 'close' ]
        price_47_close = df.iloc[ -47 ][ 'close' ]
        price_48_close = df.iloc[ -48 ][ 'close' ]
        price_49_close = df.iloc[ -49 ][ 'close' ]
        price_50_close = df.iloc[ -50 ][ 'close' ]

        price_51_close = df.iloc[ -51 ][ 'close' ]
        price_52_close = df.iloc[ -52 ][ 'close' ]
        price_53_close = df.iloc[ -53 ][ 'close' ]
        price_54_close = df.iloc[ -54 ][ 'close' ]
        price_55_close = df.iloc[ -55 ][ 'close' ]
        price_56_close = df.iloc[ -56 ][ 'close' ]
        price_57_close = df.iloc[ -57 ][ 'close' ]
        price_58_close = df.iloc[ -58 ][ 'close' ]
        price_59_close = df.iloc[ -59 ][ 'close' ]
        price_60_close = df.iloc[ -60 ][ 'close' ]

        price_61_close = df.iloc[ -61 ][ 'close' ]
        price_62_close = df.iloc[ -62 ][ 'close' ]
        price_63_close = df.iloc[ -63 ][ 'close' ]
        price_64_close = df.iloc[ -64 ][ 'close' ]
        price_65_close = df.iloc[ -65 ][ 'close' ]
        price_66_close = df.iloc[ -66 ][ 'close' ]
        price_67_close = df.iloc[ -67 ][ 'close' ]
        price_68_close = df.iloc[ -68 ][ 'close' ]
        price_69_close = df.iloc[ -69 ][ 'close' ]
        price_70_close = df.iloc[ -70 ][ 'close' ]

        price_71_close = df.iloc[ -71 ][ 'close' ]
        price_72_close = df.iloc[ -72 ][ 'close' ]
        price_73_close = df.iloc[ -73 ][ 'close' ]
        price_74_close = df.iloc[ -74 ][ 'close' ]
        price_75_close = df.iloc[ -75 ][ 'close' ]
        price_76_close = df.iloc[ -76 ][ 'close' ]
        price_77_close = df.iloc[ -77 ][ 'close' ]
        price_78_close = df.iloc[ -78 ][ 'close' ]
        price_79_close = df.iloc[ -79 ][ 'close' ]
        price_80_close = df.iloc[ -80 ][ 'close' ]

        price_81_close = df.iloc[ -81 ][ 'close' ]
        price_82_close = df.iloc[ -82 ][ 'close' ]
        price_83_close = df.iloc[ -83 ][ 'close' ]
        price_84_close = df.iloc[ -84 ][ 'close' ]
        price_85_close = df.iloc[ -85 ][ 'close' ]
        price_86_close = df.iloc[ -86 ][ 'close' ]
        price_87_close = df.iloc[ -87 ][ 'close' ]
        price_88_close = df.iloc[ -88 ][ 'close' ]
        price_89_close = df.iloc[ -89 ][ 'close' ]
        price_90_close = df.iloc[ -90 ][ 'close' ]

        price_91_close = df.iloc[ -91 ][ 'close' ]
        price_92_close = df.iloc[ -92 ][ 'close' ]
        price_93_close = df.iloc[ -93 ][ 'close' ]
        price_94_close = df.iloc[ -94 ][ 'close' ]
        price_95_close = df.iloc[ -95 ][ 'close' ]
        price_96_close = df.iloc[ -96 ][ 'close' ]
        price_97_close = df.iloc[ -97 ][ 'close' ]
        price_98_close = df.iloc[ -98 ][ 'close' ]
        price_99_close = df.iloc[ -99 ][ 'close' ]
        price_100_close = df.iloc[ -100 ][ 'close' ]

        price_101_close = df.iloc[ -101 ][ 'close' ]
        price_102_close = df.iloc[ -102 ][ 'close' ]
        price_103_close = df.iloc[ -103 ][ 'close' ]
        price_104_close = df.iloc[ -104 ][ 'close' ]
        price_105_close = df.iloc[ -105 ][ 'close' ]
        price_106_close = df.iloc[ -106 ][ 'close' ]
        price_107_close = df.iloc[ -107 ][ 'close' ]
        price_108_close = df.iloc[ -108 ][ 'close' ]
        price_109_close = df.iloc[ -109 ][ 'close' ]
        price_110_close = df.iloc[ -110 ][ 'close' ]

        price_111_close = df.iloc[ -111 ][ 'close' ]
        price_112_close = df.iloc[ -112 ][ 'close' ]
        price_113_close = df.iloc[ -113 ][ 'close' ]
        price_114_close = df.iloc[ -114 ][ 'close' ]
        price_115_close = df.iloc[ -115 ][ 'close' ]
        price_116_close = df.iloc[ -116 ][ 'close' ]
        price_117_close = df.iloc[ -117 ][ 'close' ]
        price_118_close = df.iloc[ -118 ][ 'close' ]
        price_119_close = df.iloc[ -119 ][ 'close' ]
        price_120_close = df.iloc[ -120 ][ 'close' ]

        price_121_close = df.iloc[ -121 ][ 'close' ]
        price_122_close = df.iloc[ -122 ][ 'close' ]
        price_123_close = df.iloc[ -123 ][ 'close' ]
        price_124_close = df.iloc[ -124 ][ 'close' ]
        price_125_close = df.iloc[ -125 ][ 'close' ]
        price_126_close = df.iloc[ -126 ][ 'close' ]
        price_127_close = df.iloc[ -127 ][ 'close' ]
        price_128_close = df.iloc[ -128 ][ 'close' ]
        price_129_close = df.iloc[ -129 ][ 'close' ]
        price_130_close = df.iloc[ -130 ][ 'close' ]

        price_131_close = df.iloc[ -131 ][ 'close' ]
        price_132_close = df.iloc[ -132 ][ 'close' ]
        price_133_close = df.iloc[ -133 ][ 'close' ]
        price_134_close = df.iloc[ -134 ][ 'close' ]
        price_135_close = df.iloc[ -135 ][ 'close' ]
        price_136_close = df.iloc[ -136 ][ 'close' ]
        price_137_close = df.iloc[ -137 ][ 'close' ]
        price_138_close = df.iloc[ -138 ][ 'close' ]
        price_139_close = df.iloc[ -139 ][ 'close' ]
        price_140_close = df.iloc[ -140 ][ 'close' ]

        price_141_close = df.iloc[ -141 ][ 'close' ]
        price_142_close = df.iloc[ -142 ][ 'close' ]
        price_143_close = df.iloc[ -143 ][ 'close' ]
        price_144_close = df.iloc[ -144 ][ 'close' ]
        price_145_close = df.iloc[ -145 ][ 'close' ]
        price_146_close = df.iloc[ -146 ][ 'close' ]
        price_147_close = df.iloc[ -147 ][ 'close' ]
        price_148_close = df.iloc[ -148 ][ 'close' ]
        price_149_close = df.iloc[ -149 ][ 'close' ]
        price_150_close = df.iloc[ -150 ][ 'close' ]

        price_151_close = df.iloc[ -151 ][ 'close' ]
        price_152_close = df.iloc[ -152 ][ 'close' ]
        price_153_close = df.iloc[ -153 ][ 'close' ]
        price_154_close = df.iloc[ -154 ][ 'close' ]
        price_155_close = df.iloc[ -155 ][ 'close' ]
        price_156_close = df.iloc[ -156 ][ 'close' ]
        price_157_close = df.iloc[ -157 ][ 'close' ]
        price_158_close = df.iloc[ -158 ][ 'close' ]
        price_159_close = df.iloc[ -159 ][ 'close' ]
        price_160_close = df.iloc[ -160 ][ 'close' ]

        price_161_close = df.iloc[ -161 ][ 'close' ]
        price_162_close = df.iloc[ -162 ][ 'close' ]
        price_163_close = df.iloc[ -163 ][ 'close' ]
        price_164_close = df.iloc[ -164 ][ 'close' ]
        price_165_close = df.iloc[ -165 ][ 'close' ]
        price_166_close = df.iloc[ -166 ][ 'close' ]
        price_167_close = df.iloc[ -167 ][ 'close' ]
        price_168_close = df.iloc[ -168 ][ 'close' ]
        price_169_close = df.iloc[ -169 ][ 'close' ]
        price_170_close = df.iloc[ -170 ][ 'close' ]

        price_171_close = df.iloc[ -171 ][ 'close' ]
        price_172_close = df.iloc[ -172 ][ 'close' ]
        price_173_close = df.iloc[ -173 ][ 'close' ]
        price_174_close = df.iloc[ -174 ][ 'close' ]
        price_175_close = df.iloc[ -175 ][ 'close' ]
        price_176_close = df.iloc[ -176 ][ 'close' ]
        price_177_close = df.iloc[ -177 ][ 'close' ]
        price_178_close = df.iloc[ -178 ][ 'close' ]
        price_179_close = df.iloc[ -179 ][ 'close' ]
        price_180_close = df.iloc[ -180 ][ 'close' ]

        price_181_close = df.iloc[ -181 ][ 'close' ]
        price_182_close = df.iloc[ -182 ][ 'close' ]
        price_183_close = df.iloc[ -183 ][ 'close' ]
        price_184_close = df.iloc[ -184 ][ 'close' ]
        price_185_close = df.iloc[ -185 ][ 'close' ]
        price_186_close = df.iloc[ -186 ][ 'close' ]
        price_187_close = df.iloc[ -187 ][ 'close' ]
        price_188_close = df.iloc[ -188 ][ 'close' ]
        price_189_close = df.iloc[ -189 ][ 'close' ]
        price_190_close = df.iloc[ -190 ][ 'close' ]











            

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
        acc_ma12_29 = acc_ma12_29_1 / 12
        acc_ma12_30_1 = price_31_close + price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close
        acc_ma12_30 = acc_ma12_30_1 / 12


        acc_ma12_31_1 = price_32_close + price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close
        acc_ma12_31 = acc_ma12_31_1 / 12
        acc_ma12_32_1 = price_33_close + price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close
        acc_ma12_32 = acc_ma12_32_1 / 12
        acc_ma12_33_1 = price_34_close + price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close
        acc_ma12_33 = acc_ma12_33_1 / 12
        acc_ma12_34_1 = price_35_close + price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close
        acc_ma12_34 = acc_ma12_34_1 / 12
        acc_ma12_35_1 = price_36_close + price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close
        acc_ma12_35 = acc_ma12_35_1 / 12

        acc_ma12_36_1 = price_37_close + price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close
        acc_ma12_36 = acc_ma12_36_1 / 12
        acc_ma12_37_1 = price_38_close + price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close
        acc_ma12_37 = acc_ma12_37_1 / 12
        acc_ma12_38_1 = price_39_close + price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close
        acc_ma12_38 = acc_ma12_38_1 / 12
        acc_ma12_39_1 = price_40_close + price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close
        acc_ma12_39 = acc_ma12_39_1 / 12
        acc_ma12_40_1 = price_41_close + price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close
        acc_ma12_40 = acc_ma12_40_1 / 12


        acc_ma12_41_1 = price_42_close + price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close
        acc_ma12_41 = acc_ma12_41_1 / 12
        acc_ma12_42_1 = price_43_close + price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close
        acc_ma12_42 = acc_ma12_42_1 / 12
        acc_ma12_43_1 = price_44_close + price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close
        acc_ma12_43 = acc_ma12_43_1 / 12
        acc_ma12_44_1 = price_45_close + price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close
        acc_ma12_44 = acc_ma12_44_1 / 12
        acc_ma12_45_1 = price_46_close + price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close
        acc_ma12_45 = acc_ma12_45_1 / 12

        acc_ma12_46_1 = price_47_close + price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close
        acc_ma12_46 = acc_ma12_46_1 / 12
        acc_ma12_47_1 = price_48_close + price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close
        acc_ma12_47 = acc_ma12_47_1 / 12
        acc_ma12_48_1 = price_49_close + price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close
        acc_ma12_48 = acc_ma12_48_1 / 12
        acc_ma12_49_1 = price_50_close + price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close
        acc_ma12_49 = acc_ma12_49_1 / 12
        acc_ma12_50_1 = price_51_close + price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close
        acc_ma12_50 = acc_ma12_50_1 / 12


        acc_ma12_51_1 = price_52_close + price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close
        acc_ma12_51 = acc_ma12_51_1 / 12
        acc_ma12_52_1 = price_53_close + price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close
        acc_ma12_52 = acc_ma12_52_1 / 12
        acc_ma12_53_1 = price_54_close + price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close
        acc_ma12_53 = acc_ma12_53_1 / 12
        acc_ma12_54_1 = price_55_close + price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close
        acc_ma12_54 = acc_ma12_54_1 / 12
        acc_ma12_55_1 = price_56_close + price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close
        acc_ma12_55 = acc_ma12_55_1 / 12

        acc_ma12_56_1 = price_57_close + price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close
        acc_ma12_56 = acc_ma12_56_1 / 12
        acc_ma12_57_1 = price_58_close + price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close
        acc_ma12_57 = acc_ma12_57_1 / 12
        acc_ma12_58_1 = price_59_close + price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close
        acc_ma12_58 = acc_ma12_58_1 / 12
        acc_ma12_59_1 = price_60_close + price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close
        acc_ma12_59 = acc_ma12_59_1 / 12
        acc_ma12_60_1 = price_61_close + price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close
        acc_ma12_60 = acc_ma12_60_1 / 12


        acc_ma12_61_1 = price_62_close + price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close
        acc_ma12_61 = acc_ma12_61_1 / 12
        acc_ma12_62_1 = price_63_close + price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close
        acc_ma12_62 = acc_ma12_62_1 / 12
        acc_ma12_63_1 = price_64_close + price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close
        acc_ma12_63 = acc_ma12_63_1 / 12
        acc_ma12_64_1 = price_65_close + price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close
        acc_ma12_64 = acc_ma12_64_1 / 12
        acc_ma12_65_1 = price_66_close + price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close
        acc_ma12_65 = acc_ma12_65_1 / 12

        acc_ma12_66_1 = price_67_close + price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close
        acc_ma12_66 = acc_ma12_66_1 / 12
        acc_ma12_67_1 = price_68_close + price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close
        acc_ma12_67 = acc_ma12_67_1 / 12
        acc_ma12_68_1 = price_69_close + price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close
        acc_ma12_68 = acc_ma12_68_1 / 12
        acc_ma12_69_1 = price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close
        acc_ma12_69 = acc_ma12_69_1 / 12
        acc_ma12_70_1 = price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close
        acc_ma12_70 = acc_ma12_70_1 / 12


        acc_ma12_71_1 = price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close
        acc_ma12_71 = acc_ma12_71_1 / 12
        acc_ma12_72_1 = price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close
        acc_ma12_72 = acc_ma12_72_1 / 12
        acc_ma12_73_1 = price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close
        acc_ma12_73 = acc_ma12_73_1 / 12
        acc_ma12_74_1 = price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close
        acc_ma12_74 = acc_ma12_74_1 / 12
        acc_ma12_75_1 = price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close
        acc_ma12_75 = acc_ma12_75_1 / 12

        acc_ma12_76_1 = price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close
        acc_ma12_76 = acc_ma12_76_1 / 12
        acc_ma12_77_1 = price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close
        acc_ma12_77 = acc_ma12_77_1 / 12
        acc_ma12_78_1 = price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close
        acc_ma12_78 = acc_ma12_78_1 / 12
        acc_ma12_79_1 = price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close
        acc_ma12_79 = acc_ma12_79_1 / 12
        acc_ma12_80_1 = price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close
        acc_ma12_80 = acc_ma12_80_1 / 12


        acc_ma12_81_1 = price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close
        acc_ma12_81 = acc_ma12_81_1 / 12
        acc_ma12_82_1 = price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close
        acc_ma12_82 = acc_ma12_82_1 / 12
        acc_ma12_83_1 = price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close
        acc_ma12_83 = acc_ma12_83_1 / 12
        acc_ma12_84_1 = price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close
        acc_ma12_84 = acc_ma12_84_1 / 12
        acc_ma12_85_1 = price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close
        acc_ma12_85 = acc_ma12_85_1 / 12

        acc_ma12_86_1 = price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close
        acc_ma12_86 = acc_ma12_86_1 / 12
        acc_ma12_87_1 = price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close
        acc_ma12_87 = acc_ma12_87_1 / 12
        acc_ma12_88_1 = price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close
        acc_ma12_88 = acc_ma12_88_1 / 12
        acc_ma12_89_1 = price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close
        acc_ma12_89 = acc_ma12_89_1 / 12
        acc_ma12_90_1 = price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close
        acc_ma12_90 = acc_ma12_90_1 / 12


        acc_ma12_91_1 = price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close
        acc_ma12_91 = acc_ma12_91_1 / 12
        acc_ma12_92_1 = price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close
        acc_ma12_92 = acc_ma12_92_1 / 12
        acc_ma12_93_1 = price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close
        acc_ma12_93 = acc_ma12_93_1 / 12
        acc_ma12_94_1 = price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close
        acc_ma12_94 = acc_ma12_94_1 / 12
        acc_ma12_95_1 = price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close
        acc_ma12_95 = acc_ma12_95_1 / 12

        acc_ma12_96_1 = price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close
        acc_ma12_96 = acc_ma12_96_1 / 12
        acc_ma12_97_1 = price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close
        acc_ma12_97 = acc_ma12_97_1 / 12
        acc_ma12_98_1 = price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close
        acc_ma12_98 = acc_ma12_98_1 / 12
        acc_ma12_99_1 = price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close
        acc_ma12_99 = acc_ma12_99_1 / 12
        acc_ma12_100_1 = price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close
        acc_ma12_100 = acc_ma12_100_1 / 12


        acc_ma12_101_1 = price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close
        acc_ma12_101 = acc_ma12_101_1 / 12
        acc_ma12_102_1 = price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close
        acc_ma12_102 = acc_ma12_102_1 / 12
        acc_ma12_103_1 = price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close
        acc_ma12_103 = acc_ma12_103_1 / 12
        acc_ma12_104_1 = price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close
        acc_ma12_104 = acc_ma12_104_1 / 12
        acc_ma12_105_1 = price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close
        acc_ma12_105 = acc_ma12_105_1 / 12

        acc_ma12_106_1 = price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close
        acc_ma12_106 = acc_ma12_106_1 / 12
        acc_ma12_107_1 = price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close
        acc_ma12_107 = acc_ma12_107_1 / 12
        acc_ma12_108_1 = price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close
        acc_ma12_108 = acc_ma12_108_1 / 12
        acc_ma12_109_1 = price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close
        acc_ma12_109 = acc_ma12_109_1 / 12
        acc_ma12_110_1 = price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close
        acc_ma12_110 = acc_ma12_110_1 / 12


        acc_ma12_111_1 = price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close
        acc_ma12_111 = acc_ma12_111_1 / 12
        acc_ma12_112_1 = price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close
        acc_ma12_112 = acc_ma12_112_1 / 12
        acc_ma12_113_1 = price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close
        acc_ma12_113 = acc_ma12_113_1 / 12
        acc_ma12_114_1 = price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close
        acc_ma12_114 = acc_ma12_114_1 / 12
        acc_ma12_115_1 = price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close
        acc_ma12_115 = acc_ma12_115_1 / 12

        acc_ma12_116_1 = price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close
        acc_ma12_116 = acc_ma12_116_1 / 12
        acc_ma12_117_1 = price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close
        acc_ma12_117 = acc_ma12_117_1 / 12
        acc_ma12_118_1 = price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close
        acc_ma12_118 = acc_ma12_118_1 / 12
        acc_ma12_119_1 = price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close
        acc_ma12_119 = acc_ma12_119_1 / 12
        acc_ma12_120_1 = price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close
        acc_ma12_120 = acc_ma12_120_1 / 12

        acc_ma12_121_1 = price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close
        acc_ma12_121 = acc_ma12_121_1 / 12
        acc_ma12_122_1 = price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close
        acc_ma12_122 = acc_ma12_122_1 / 12
        acc_ma12_123_1 = price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close
        acc_ma12_123 = acc_ma12_123_1 / 12
        acc_ma12_124_1 = price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close
        acc_ma12_124 = acc_ma12_124_1 / 12
        acc_ma12_125_1 = price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close
        acc_ma12_125 = acc_ma12_125_1 / 12

        acc_ma12_126_1 = price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close
        acc_ma12_126 = acc_ma12_126_1 / 12
        acc_ma12_127_1 = price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close
        acc_ma12_127 = acc_ma12_127_1 / 12
        acc_ma12_128_1 = price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close
        acc_ma12_128 = acc_ma12_128_1 / 12
        acc_ma12_129_1 = price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close
        acc_ma12_129 = acc_ma12_129_1 / 12
        acc_ma12_130_1 = price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close
        acc_ma12_130 = acc_ma12_130_1 / 12


        acc_ma12_131_1 = price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close
        acc_ma12_131 = acc_ma12_131_1 / 12
        acc_ma12_132_1 = price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close
        acc_ma12_132 = acc_ma12_132_1 / 12
        acc_ma12_133_1 = price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close
        acc_ma12_133 = acc_ma12_133_1 / 12
        acc_ma12_134_1 = price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close
        acc_ma12_134 = acc_ma12_134_1 / 12
        acc_ma12_135_1 = price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close
        acc_ma12_135 = acc_ma12_135_1 / 12

        acc_ma12_136_1 = price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close
        acc_ma12_136 = acc_ma12_136_1 / 12
        acc_ma12_137_1 = price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close
        acc_ma12_137 = acc_ma12_137_1 / 12
        acc_ma12_138_1 = price_139_close + price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close
        acc_ma12_138 = acc_ma12_138_1 / 12
        acc_ma12_139_1 = price_140_close + price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close
        acc_ma12_139 = acc_ma12_139_1 / 12
        acc_ma12_140_1 = price_141_close + price_142_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close
        acc_ma12_140 = acc_ma12_140_1 / 12








        # EMA - 단기 12 지수이동평균값 구하기
        acc_e_ma12_139 = acc_ma12_140
        acc_e_ma12_138 = ( price_139_close * ma12_sc )  + ( acc_e_ma12_139 * ( 1 - ma12_sc ) )
        acc_e_ma12_137 = ( price_138_close * ma12_sc )  + ( acc_e_ma12_138 * ( 1 - ma12_sc ) )
        acc_e_ma12_136 = ( price_137_close * ma12_sc )  + ( acc_e_ma12_137 * ( 1 - ma12_sc ) )
        acc_e_ma12_135 = ( price_136_close * ma12_sc )  + ( acc_e_ma12_136 * ( 1 - ma12_sc ) )
        acc_e_ma12_134 = ( price_135_close * ma12_sc )  + ( acc_e_ma12_135 * ( 1 - ma12_sc ) )
        acc_e_ma12_133 = ( price_134_close * ma12_sc )  + ( acc_e_ma12_134 * ( 1 - ma12_sc ) )
        acc_e_ma12_132 = ( price_133_close * ma12_sc )  + ( acc_e_ma12_133 * ( 1 - ma12_sc ) )
        acc_e_ma12_131 = ( price_132_close * ma12_sc )  + ( acc_e_ma12_132 * ( 1 - ma12_sc ) )

        acc_e_ma12_130 = ( price_131_close * ma12_sc )  + ( acc_e_ma12_131 * ( 1 - ma12_sc ) )
        acc_e_ma12_129 = ( price_130_close * ma12_sc )  + ( acc_e_ma12_130 * ( 1 - ma12_sc ) )
        acc_e_ma12_128 = ( price_129_close * ma12_sc )  + ( acc_e_ma12_129 * ( 1 - ma12_sc ) )
        acc_e_ma12_127 = ( price_128_close * ma12_sc )  + ( acc_e_ma12_128 * ( 1 - ma12_sc ) )
        acc_e_ma12_126 = ( price_127_close * ma12_sc )  + ( acc_e_ma12_127 * ( 1 - ma12_sc ) )
        acc_e_ma12_125 = ( price_126_close * ma12_sc )  + ( acc_e_ma12_126 * ( 1 - ma12_sc ) )
        acc_e_ma12_124 = ( price_125_close * ma12_sc )  + ( acc_e_ma12_125 * ( 1 - ma12_sc ) )
        acc_e_ma12_123 = ( price_124_close * ma12_sc )  + ( acc_e_ma12_124 * ( 1 - ma12_sc ) )
        acc_e_ma12_122 = ( price_123_close * ma12_sc )  + ( acc_e_ma12_123 * ( 1 - ma12_sc ) )
        acc_e_ma12_121 = ( price_122_close * ma12_sc )  + ( acc_e_ma12_122 * ( 1 - ma12_sc ) )

        acc_e_ma12_120 = ( price_121_close * ma12_sc )  + ( acc_e_ma12_121 * ( 1 - ma12_sc ) )
        acc_e_ma12_119 = ( price_120_close * ma12_sc )  + ( acc_e_ma12_120 * ( 1 - ma12_sc ) )
        acc_e_ma12_118 = ( price_119_close * ma12_sc )  + ( acc_e_ma12_119 * ( 1 - ma12_sc ) )
        acc_e_ma12_117 = ( price_118_close * ma12_sc )  + ( acc_e_ma12_118 * ( 1 - ma12_sc ) )
        acc_e_ma12_116 = ( price_117_close * ma12_sc )  + ( acc_e_ma12_117 * ( 1 - ma12_sc ) )
        acc_e_ma12_115 = ( price_116_close * ma12_sc )  + ( acc_e_ma12_116 * ( 1 - ma12_sc ) )
        acc_e_ma12_114 = ( price_115_close * ma12_sc )  + ( acc_e_ma12_115 * ( 1 - ma12_sc ) )
        acc_e_ma12_113 = ( price_114_close * ma12_sc )  + ( acc_e_ma12_114 * ( 1 - ma12_sc ) )
        acc_e_ma12_112 = ( price_113_close * ma12_sc )  + ( acc_e_ma12_113 * ( 1 - ma12_sc ) )
        acc_e_ma12_111 = ( price_112_close * ma12_sc )  + ( acc_e_ma12_112 * ( 1 - ma12_sc ) )

        acc_e_ma12_110 = ( price_111_close * ma12_sc )  + ( acc_e_ma12_111 * ( 1 - ma12_sc ) )
        acc_e_ma12_109 = ( price_110_close * ma12_sc )  + ( acc_e_ma12_110 * ( 1 - ma12_sc ) )
        acc_e_ma12_108 = ( price_109_close * ma12_sc )  + ( acc_e_ma12_109 * ( 1 - ma12_sc ) )
        acc_e_ma12_107 = ( price_108_close * ma12_sc )  + ( acc_e_ma12_108 * ( 1 - ma12_sc ) )
        acc_e_ma12_106 = ( price_107_close * ma12_sc )  + ( acc_e_ma12_107 * ( 1 - ma12_sc ) )
        acc_e_ma12_105 = ( price_106_close * ma12_sc )  + ( acc_e_ma12_106 * ( 1 - ma12_sc ) )
        acc_e_ma12_104 = ( price_105_close * ma12_sc )  + ( acc_e_ma12_105 * ( 1 - ma12_sc ) )
        acc_e_ma12_103 = ( price_104_close * ma12_sc )  + ( acc_e_ma12_104 * ( 1 - ma12_sc ) )
        acc_e_ma12_102 = ( price_103_close * ma12_sc )  + ( acc_e_ma12_103 * ( 1 - ma12_sc ) )
        acc_e_ma12_101 = ( price_102_close * ma12_sc )  + ( acc_e_ma12_102 * ( 1 - ma12_sc ) )

        acc_e_ma12_100 = ( price_101_close * ma12_sc )  + ( acc_e_ma12_101 * ( 1 - ma12_sc ) )
        acc_e_ma12_99 = ( price_100_close * ma12_sc )  + ( acc_e_ma12_100 * ( 1 - ma12_sc ) )
        acc_e_ma12_98 = ( price_99_close * ma12_sc )  + ( acc_e_ma12_99 * ( 1 - ma12_sc ) )
        acc_e_ma12_97 = ( price_98_close * ma12_sc )  + ( acc_e_ma12_98 * ( 1 - ma12_sc ) )
        acc_e_ma12_96 = ( price_97_close * ma12_sc )  + ( acc_e_ma12_97 * ( 1 - ma12_sc ) )
        acc_e_ma12_95 = ( price_96_close * ma12_sc )  + ( acc_e_ma12_96 * ( 1 - ma12_sc ) )
        acc_e_ma12_94 = ( price_95_close * ma12_sc )  + ( acc_e_ma12_95 * ( 1 - ma12_sc ) )
        acc_e_ma12_93 = ( price_94_close * ma12_sc )  + ( acc_e_ma12_94 * ( 1 - ma12_sc ) )
        acc_e_ma12_92 = ( price_93_close * ma12_sc )  + ( acc_e_ma12_93 * ( 1 - ma12_sc ) )
        acc_e_ma12_91 = ( price_92_close * ma12_sc )  + ( acc_e_ma12_92 * ( 1 - ma12_sc ) )

        acc_e_ma12_90 = ( price_91_close * ma12_sc )  + ( acc_e_ma12_91 * ( 1 - ma12_sc ) )
        acc_e_ma12_89 = ( price_90_close * ma12_sc )  + ( acc_e_ma12_90 * ( 1 - ma12_sc ) )
        acc_e_ma12_88 = ( price_89_close * ma12_sc )  + ( acc_e_ma12_89 * ( 1 - ma12_sc ) )
        acc_e_ma12_87 = ( price_88_close * ma12_sc )  + ( acc_e_ma12_88 * ( 1 - ma12_sc ) )
        acc_e_ma12_86 = ( price_87_close * ma12_sc )  + ( acc_e_ma12_87 * ( 1 - ma12_sc ) )
        acc_e_ma12_85 = ( price_86_close * ma12_sc )  + ( acc_e_ma12_86 * ( 1 - ma12_sc ) )
        acc_e_ma12_84 = ( price_85_close * ma12_sc )  + ( acc_e_ma12_85 * ( 1 - ma12_sc ) )
        acc_e_ma12_83 = ( price_84_close * ma12_sc )  + ( acc_e_ma12_84 * ( 1 - ma12_sc ) )
        acc_e_ma12_82 = ( price_83_close * ma12_sc )  + ( acc_e_ma12_83 * ( 1 - ma12_sc ) )
        acc_e_ma12_81 = ( price_82_close * ma12_sc )  + ( acc_e_ma12_82 * ( 1 - ma12_sc ) )

        acc_e_ma12_80 = ( price_81_close * ma12_sc )  + ( acc_e_ma12_81 * ( 1 - ma12_sc ) )
        acc_e_ma12_79 = ( price_80_close * ma12_sc )  + ( acc_e_ma12_80 * ( 1 - ma12_sc ) )
        acc_e_ma12_78 = ( price_79_close * ma12_sc )  + ( acc_e_ma12_79 * ( 1 - ma12_sc ) )
        acc_e_ma12_77 = ( price_78_close * ma12_sc )  + ( acc_e_ma12_78 * ( 1 - ma12_sc ) )
        acc_e_ma12_76 = ( price_77_close * ma12_sc )  + ( acc_e_ma12_77 * ( 1 - ma12_sc ) )
        acc_e_ma12_75 = ( price_76_close * ma12_sc )  + ( acc_e_ma12_76 * ( 1 - ma12_sc ) )
        acc_e_ma12_74 = ( price_75_close * ma12_sc )  + ( acc_e_ma12_75 * ( 1 - ma12_sc ) )
        acc_e_ma12_73 = ( price_74_close * ma12_sc )  + ( acc_e_ma12_74 * ( 1 - ma12_sc ) )
        acc_e_ma12_72 = ( price_73_close * ma12_sc )  + ( acc_e_ma12_73 * ( 1 - ma12_sc ) )
        acc_e_ma12_71 = ( price_72_close * ma12_sc )  + ( acc_e_ma12_72 * ( 1 - ma12_sc ) )

        acc_e_ma12_70 = ( price_71_close * ma12_sc )  + ( acc_e_ma12_71 * ( 1 - ma12_sc ) )
        acc_e_ma12_69 = ( price_70_close * ma12_sc )  + ( acc_e_ma12_70 * ( 1 - ma12_sc ) )
        acc_e_ma12_68 = ( price_69_close * ma12_sc )  + ( acc_e_ma12_69 * ( 1 - ma12_sc ) )
        acc_e_ma12_67 = ( price_68_close * ma12_sc )  + ( acc_e_ma12_68 * ( 1 - ma12_sc ) )
        acc_e_ma12_66 = ( price_67_close * ma12_sc )  + ( acc_e_ma12_67 * ( 1 - ma12_sc ) )
        acc_e_ma12_65 = ( price_66_close * ma12_sc )  + ( acc_e_ma12_66 * ( 1 - ma12_sc ) )
        acc_e_ma12_64 = ( price_65_close * ma12_sc )  + ( acc_e_ma12_65 * ( 1 - ma12_sc ) )
        acc_e_ma12_63 = ( price_64_close * ma12_sc )  + ( acc_e_ma12_64 * ( 1 - ma12_sc ) )
        acc_e_ma12_62 = ( price_63_close * ma12_sc )  + ( acc_e_ma12_63 * ( 1 - ma12_sc ) )
        acc_e_ma12_61 = ( price_62_close * ma12_sc )  + ( acc_e_ma12_62 * ( 1 - ma12_sc ) )

        acc_e_ma12_60 = ( price_61_close * ma12_sc )  + ( acc_e_ma12_61 * ( 1 - ma12_sc ) )
        acc_e_ma12_59 = ( price_60_close * ma12_sc )  + ( acc_e_ma12_60 * ( 1 - ma12_sc ) )
        acc_e_ma12_58 = ( price_59_close * ma12_sc )  + ( acc_e_ma12_59 * ( 1 - ma12_sc ) )
        acc_e_ma12_57 = ( price_58_close * ma12_sc )  + ( acc_e_ma12_58 * ( 1 - ma12_sc ) )
        acc_e_ma12_56 = ( price_57_close * ma12_sc )  + ( acc_e_ma12_57 * ( 1 - ma12_sc ) )
        acc_e_ma12_55 = ( price_56_close * ma12_sc )  + ( acc_e_ma12_56 * ( 1 - ma12_sc ) )
        acc_e_ma12_54 = ( price_55_close * ma12_sc )  + ( acc_e_ma12_55 * ( 1 - ma12_sc ) )
        acc_e_ma12_53 = ( price_54_close * ma12_sc )  + ( acc_e_ma12_54 * ( 1 - ma12_sc ) )
        acc_e_ma12_52 = ( price_53_close * ma12_sc )  + ( acc_e_ma12_53 * ( 1 - ma12_sc ) )
        acc_e_ma12_51 = ( price_52_close * ma12_sc )  + ( acc_e_ma12_52 * ( 1 - ma12_sc ) )

        acc_e_ma12_50 = ( price_51_close * ma12_sc )  + ( acc_e_ma12_51 * ( 1 - ma12_sc ) )
        acc_e_ma12_49 = ( price_50_close * ma12_sc )  + ( acc_e_ma12_50 * ( 1 - ma12_sc ) )
        acc_e_ma12_48 = ( price_49_close * ma12_sc )  + ( acc_e_ma12_49 * ( 1 - ma12_sc ) )
        acc_e_ma12_47 = ( price_48_close * ma12_sc )  + ( acc_e_ma12_48 * ( 1 - ma12_sc ) )
        acc_e_ma12_46 = ( price_47_close * ma12_sc )  + ( acc_e_ma12_47 * ( 1 - ma12_sc ) )
        acc_e_ma12_45 = ( price_46_close * ma12_sc )  + ( acc_e_ma12_46 * ( 1 - ma12_sc ) )
        acc_e_ma12_44 = ( price_45_close * ma12_sc )  + ( acc_e_ma12_45 * ( 1 - ma12_sc ) )
        acc_e_ma12_43 = ( price_44_close * ma12_sc )  + ( acc_e_ma12_44 * ( 1 - ma12_sc ) )
        acc_e_ma12_42 = ( price_43_close * ma12_sc )  + ( acc_e_ma12_43 * ( 1 - ma12_sc ) )
        acc_e_ma12_41 = ( price_42_close * ma12_sc )  + ( acc_e_ma12_42 * ( 1 - ma12_sc ) )

        acc_e_ma12_40 = ( price_41_close * ma12_sc )  + ( acc_e_ma12_41 * ( 1 - ma12_sc ) )
        acc_e_ma12_39 = ( price_40_close * ma12_sc )  + ( acc_e_ma12_40 * ( 1 - ma12_sc ) )
        acc_e_ma12_38 = ( price_39_close * ma12_sc )  + ( acc_e_ma12_39 * ( 1 - ma12_sc ) )
        acc_e_ma12_37 = ( price_38_close * ma12_sc )  + ( acc_e_ma12_38 * ( 1 - ma12_sc ) )
        acc_e_ma12_36 = ( price_37_close * ma12_sc )  + ( acc_e_ma12_37 * ( 1 - ma12_sc ) )
        acc_e_ma12_35 = ( price_36_close * ma12_sc )  + ( acc_e_ma12_36 * ( 1 - ma12_sc ) )
        acc_e_ma12_34 = ( price_35_close * ma12_sc )  + ( acc_e_ma12_35 * ( 1 - ma12_sc ) )
        acc_e_ma12_33 = ( price_34_close * ma12_sc )  + ( acc_e_ma12_34 * ( 1 - ma12_sc ) )
        acc_e_ma12_32 = ( price_33_close * ma12_sc )  + ( acc_e_ma12_33 * ( 1 - ma12_sc ) )
        acc_e_ma12_31 = ( price_32_close * ma12_sc )  + ( acc_e_ma12_32 * ( 1 - ma12_sc ) )

        acc_e_ma12_30 = ( price_31_close * ma12_sc )  + ( acc_e_ma12_31 * ( 1 - ma12_sc ) )
        acc_e_ma12_29 = ( price_30_close * ma12_sc )  + ( acc_e_ma12_30 * ( 1 - ma12_sc ) )
        acc_e_ma12_28 = ( price_29_close * ma12_sc )  + ( acc_e_ma12_29 * ( 1 - ma12_sc ) )
        acc_e_ma12_27 = ( price_28_close * ma12_sc )  + ( acc_e_ma12_28 * ( 1 - ma12_sc ) )
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
        acc_ma26_57_1 = acc_ma12_57_1  +  price_70_close + price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close
        acc_ma26_57 = acc_ma26_57_1 / 26
        acc_ma26_58_1 = acc_ma12_58_1  +  price_71_close + price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close
        acc_ma26_58 = acc_ma26_58_1 / 26
        acc_ma26_59_1 = acc_ma12_59_1  +  price_72_close + price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close
        acc_ma26_59 = acc_ma26_59_1 / 26
        acc_ma26_60_1 = acc_ma12_60_1  +  price_73_close + price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close
        acc_ma26_60 = acc_ma26_60_1 / 26


        acc_ma26_61_1 = acc_ma12_61_1  +  price_74_close + price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close
        acc_ma26_61 = acc_ma26_61_1 / 26
        acc_ma26_62_1 = acc_ma12_62_1  +  price_75_close + price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close
        acc_ma26_62 = acc_ma26_62_1 / 26
        acc_ma26_63_1 = acc_ma12_63_1  +  price_76_close + price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close
        acc_ma26_63 = acc_ma26_63_1 / 26
        acc_ma26_64_1 = acc_ma12_64_1  +  price_77_close + price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close
        acc_ma26_64 = acc_ma26_64_1 / 26
        acc_ma26_65_1 = acc_ma12_65_1  +  price_78_close + price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close
        acc_ma26_65 = acc_ma26_65_1 / 26

        acc_ma26_66_1 = acc_ma12_66_1  +  price_79_close + price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close
        acc_ma26_66 = acc_ma26_66_1 / 26
        acc_ma26_67_1 = acc_ma12_67_1  +  price_80_close + price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close
        acc_ma26_67 = acc_ma26_67_1 / 26
        acc_ma26_68_1 = acc_ma12_68_1  +  price_81_close + price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close
        acc_ma26_68 = acc_ma26_68_1 / 26
        acc_ma26_69_1 = acc_ma12_69_1  +  price_82_close + price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close
        acc_ma26_69 = acc_ma26_69_1 / 26
        acc_ma26_70_1 = acc_ma12_70_1  +  price_83_close + price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close
        acc_ma26_70 = acc_ma26_70_1 / 26


        acc_ma26_71_1 = acc_ma12_71_1  +  price_84_close + price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close
        acc_ma26_71 = acc_ma26_71_1 / 26
        acc_ma26_72_1 = acc_ma12_72_1  +  price_85_close + price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close
        acc_ma26_72 = acc_ma26_72_1 / 26
        acc_ma26_73_1 = acc_ma12_73_1  +  price_86_close + price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close
        acc_ma26_73 = acc_ma26_73_1 / 26
        acc_ma26_74_1 = acc_ma12_74_1  +  price_87_close + price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close
        acc_ma26_74 = acc_ma26_74_1 / 26
        acc_ma26_75_1 = acc_ma12_75_1  +  price_88_close + price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close
        acc_ma26_75 = acc_ma26_75_1 / 26

        acc_ma26_76_1 = acc_ma12_76_1  +  price_89_close + price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close
        acc_ma26_76 = acc_ma26_76_1 / 26
        acc_ma26_77_1 = acc_ma12_77_1  +  price_90_close + price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close
        acc_ma26_77 = acc_ma26_77_1 / 26
        acc_ma26_78_1 = acc_ma12_78_1  +  price_91_close + price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close
        acc_ma26_78 = acc_ma26_78_1 / 26
        acc_ma26_79_1 = acc_ma12_79_1  +  price_92_close + price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close
        acc_ma26_79 = acc_ma26_79_1 / 26
        acc_ma26_80_1 = acc_ma12_80_1  +  price_93_close + price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close
        acc_ma26_80 = acc_ma26_80_1 / 26


        acc_ma26_81_1 = acc_ma12_81_1  +  price_94_close + price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close
        acc_ma26_81 = acc_ma26_81_1 / 26
        acc_ma26_82_1 = acc_ma12_82_1  +  price_95_close + price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close
        acc_ma26_82 = acc_ma26_82_1 / 26
        acc_ma26_83_1 = acc_ma12_83_1  +  price_96_close + price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close
        acc_ma26_83 = acc_ma26_83_1 / 26
        acc_ma26_84_1 = acc_ma12_84_1  +  price_97_close + price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close
        acc_ma26_84 = acc_ma26_84_1 / 26
        acc_ma26_85_1 = acc_ma12_85_1  +  price_98_close + price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close
        acc_ma26_85 = acc_ma26_85_1 / 26

        acc_ma26_86_1 = acc_ma12_86_1  +  price_99_close + price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close
        acc_ma26_86 = acc_ma26_86_1 / 26
        acc_ma26_87_1 = acc_ma12_87_1  +  price_100_close + price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close
        acc_ma26_87 = acc_ma26_87_1 / 26
        acc_ma26_88_1 = acc_ma12_88_1  +  price_101_close + price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close
        acc_ma26_88 = acc_ma26_88_1 / 26
        acc_ma26_89_1 = acc_ma12_89_1  +  price_102_close + price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close
        acc_ma26_89 = acc_ma26_89_1 / 26
        acc_ma26_90_1 = acc_ma12_90_1  +  price_103_close + price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close
        acc_ma26_90 = acc_ma26_90_1 / 26


        acc_ma26_91_1 = acc_ma12_91_1  +  price_104_close + price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close
        acc_ma26_91 = acc_ma26_91_1 / 26
        acc_ma26_92_1 = acc_ma12_92_1  +  price_105_close + price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close
        acc_ma26_92 = acc_ma26_92_1 / 26
        acc_ma26_93_1 = acc_ma12_93_1  +  price_106_close + price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close
        acc_ma26_93 = acc_ma26_93_1 / 26
        acc_ma26_94_1 = acc_ma12_94_1  +  price_107_close + price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close
        acc_ma26_94 = acc_ma26_94_1 / 26
        acc_ma26_95_1 = acc_ma12_95_1  +  price_108_close + price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close
        acc_ma26_95 = acc_ma26_95_1 / 26

        acc_ma26_96_1 = acc_ma12_96_1  +  price_109_close + price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close
        acc_ma26_96 = acc_ma26_96_1 / 26
        acc_ma26_97_1 = acc_ma12_97_1  +  price_110_close + price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close
        acc_ma26_97 = acc_ma26_97_1 / 26
        acc_ma26_98_1 = acc_ma12_98_1  +  price_111_close + price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close
        acc_ma26_98 = acc_ma26_98_1 / 26
        acc_ma26_99_1 = acc_ma12_99_1  +  price_112_close + price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close
        acc_ma26_99 = acc_ma26_99_1 / 26
        acc_ma26_100_1 = acc_ma12_100_1  +  price_113_close + price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close
        acc_ma26_100 = acc_ma26_100_1 / 26


        acc_ma26_101_1 = acc_ma12_101_1  +  price_114_close + price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close
        acc_ma26_101 = acc_ma26_101_1 / 26
        acc_ma26_102_1 = acc_ma12_102_1  +  price_115_close + price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close
        acc_ma26_102 = acc_ma26_102_1 / 26
        acc_ma26_103_1 = acc_ma12_103_1  +  price_116_close + price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close
        acc_ma26_103 = acc_ma26_103_1 / 26
        acc_ma26_104_1 = acc_ma12_104_1  +  price_117_close + price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close
        acc_ma26_104 = acc_ma26_104_1 / 26
        acc_ma26_105_1 = acc_ma12_105_1  +  price_118_close + price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close
        acc_ma26_105 = acc_ma26_105_1 / 26

        acc_ma26_106_1 = acc_ma12_106_1  +  price_119_close + price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close
        acc_ma26_106 = acc_ma26_106_1 / 26
        acc_ma26_107_1 = acc_ma12_107_1  +  price_120_close + price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close
        acc_ma26_107 = acc_ma26_107_1 / 26
        acc_ma26_108_1 = acc_ma12_108_1  +  price_121_close + price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close
        acc_ma26_108 = acc_ma26_108_1 / 26
        acc_ma26_109_1 = acc_ma12_109_1  +  price_122_close + price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close
        acc_ma26_109 = acc_ma26_109_1 / 26
        acc_ma26_110_1 = acc_ma12_110_1  +  price_123_close + price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close
        acc_ma26_110 = acc_ma26_110_1 / 26


        acc_ma26_111_1 = acc_ma12_111_1  +  price_124_close + price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close
        acc_ma26_111 = acc_ma26_111_1 / 26
        acc_ma26_112_1 = acc_ma12_112_1  +  price_125_close + price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close
        acc_ma26_112 = acc_ma26_112_1 / 26
        acc_ma26_113_1 = acc_ma12_113_1  +  price_126_close + price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close
        acc_ma26_113 = acc_ma26_113_1 / 26
        acc_ma26_114_1 = acc_ma12_114_1  +  price_127_close + price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close
        acc_ma26_114 = acc_ma26_114_1 / 26
        acc_ma26_115_1 = acc_ma12_115_1  +  price_128_close + price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close
        acc_ma26_115 = acc_ma26_115_1 / 26

        acc_ma26_116_1 = acc_ma12_116_1  +  price_129_close + price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close
        acc_ma26_116 = acc_ma26_116_1 / 26
        acc_ma26_117_1 = acc_ma12_117_1  +  price_130_close + price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close
        acc_ma26_117 = acc_ma26_117_1 / 26
        acc_ma26_118_1 = acc_ma12_118_1  +  price_131_close + price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close
        acc_ma26_118 = acc_ma26_118_1 / 26
        acc_ma26_119_1 = acc_ma12_119_1  +  price_132_close + price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close
        acc_ma26_119 = acc_ma26_119_1 / 26
        acc_ma26_120_1 = acc_ma12_120_1  +  price_133_close + price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close
        acc_ma26_120 = acc_ma26_120_1 / 26


        acc_ma26_121_1 = acc_ma12_121_1  +  price_134_close + price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close
        acc_ma26_121 = acc_ma26_121_1 / 26
        acc_ma26_122_1 = acc_ma12_122_1  +  price_135_close + price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close
        acc_ma26_122 = acc_ma26_122_1 / 26
        acc_ma26_123_1 = acc_ma12_123_1  +  price_136_close + price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close
        acc_ma26_123 = acc_ma26_123_1 / 26
        acc_ma26_124_1 = acc_ma12_124_1  +  price_137_close + price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close
        acc_ma26_124 = acc_ma26_124_1 / 26
        acc_ma26_125_1 = acc_ma12_125_1  +  price_138_close + price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close
        acc_ma26_125 = acc_ma26_125_1 / 26

        acc_ma26_126_1 = acc_ma12_126_1  +  price_139_close + price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close
        acc_ma26_126 = acc_ma26_126_1 / 26
        acc_ma26_127_1 = acc_ma12_127_1  +  price_140_close + price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close
        acc_ma26_127 = acc_ma26_127_1 / 26
        acc_ma26_128_1 = acc_ma12_128_1  +  price_141_close + price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close
        acc_ma26_128 = acc_ma26_128_1 / 26
        acc_ma26_129_1 = acc_ma12_129_1  +  price_142_close + price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close
        acc_ma26_129 = acc_ma26_129_1 / 26
        acc_ma26_130_1 = acc_ma12_130_1  +  price_143_close + price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close
        acc_ma26_130 = acc_ma26_130_1 / 26


        acc_ma26_131_1 = acc_ma12_131_1  +  price_144_close + price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close
        acc_ma26_131 = acc_ma26_131_1 / 26
        acc_ma26_132_1 = acc_ma12_132_1  +  price_145_close + price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close
        acc_ma26_132 = acc_ma26_132_1 / 26
        acc_ma26_133_1 = acc_ma12_133_1  +  price_146_close + price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close
        acc_ma26_133 = acc_ma26_133_1 / 26
        acc_ma26_134_1 = acc_ma12_134_1  +  price_147_close + price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close
        acc_ma26_134 = acc_ma26_134_1 / 26
        acc_ma26_135_1 = acc_ma12_135_1  +  price_148_close + price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close
        acc_ma26_135 = acc_ma26_135_1 / 26

        acc_ma26_136_1 = acc_ma12_136_1  +  price_149_close + price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close
        acc_ma26_136 = acc_ma26_136_1 / 26
        acc_ma26_137_1 = acc_ma12_137_1  +  price_150_close + price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close + price_163_close
        acc_ma26_137 = acc_ma26_137_1 / 26
        acc_ma26_138_1 = acc_ma12_138_1  +  price_151_close + price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close + price_163_close + price_164_close
        acc_ma26_138 = acc_ma26_138_1 / 26
        acc_ma26_139_1 = acc_ma12_139_1  +  price_152_close + price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close + price_163_close + price_164_close + price_165_close
        acc_ma26_139 = acc_ma26_139_1 / 26
        acc_ma26_140_1 = acc_ma12_140_1  +  price_153_close + price_154_close + price_155_close + price_156_close + price_157_close + price_158_close + price_159_close + price_160_close + price_161_close + price_162_close + price_163_close + price_164_close + price_165_close + price_166_close
        acc_ma26_140 = acc_ma26_140_1 / 26








        # EMA - 장기 26 지수이동평균값 구하기
        acc_e_ma26_139 = acc_ma26_140
        acc_e_ma26_138 = ( price_139_close * ma26_sc )  + ( acc_e_ma26_139 * ( 1 - ma26_sc ) )
        acc_e_ma26_137 = ( price_138_close * ma26_sc )  + ( acc_e_ma26_138 * ( 1 - ma26_sc ) )
        acc_e_ma26_136 = ( price_137_close * ma26_sc )  + ( acc_e_ma26_137 * ( 1 - ma26_sc ) )
        acc_e_ma26_135 = ( price_136_close * ma26_sc )  + ( acc_e_ma26_136 * ( 1 - ma26_sc ) )
        acc_e_ma26_134 = ( price_135_close * ma26_sc )  + ( acc_e_ma26_135 * ( 1 - ma26_sc ) )
        acc_e_ma26_133 = ( price_134_close * ma26_sc )  + ( acc_e_ma26_134 * ( 1 - ma26_sc ) )
        acc_e_ma26_132 = ( price_133_close * ma26_sc )  + ( acc_e_ma26_133 * ( 1 - ma26_sc ) )
        acc_e_ma26_131 = ( price_132_close * ma26_sc )  + ( acc_e_ma26_132 * ( 1 - ma26_sc ) )

        acc_e_ma26_130 = ( price_131_close * ma26_sc )  + ( acc_e_ma26_131 * ( 1 - ma26_sc ) )
        acc_e_ma26_129 = ( price_130_close * ma26_sc )  + ( acc_e_ma26_130 * ( 1 - ma26_sc ) )
        acc_e_ma26_128 = ( price_129_close * ma26_sc )  + ( acc_e_ma26_129 * ( 1 - ma26_sc ) )
        acc_e_ma26_127 = ( price_128_close * ma26_sc )  + ( acc_e_ma26_128 * ( 1 - ma26_sc ) )
        acc_e_ma26_126 = ( price_127_close * ma26_sc )  + ( acc_e_ma26_127 * ( 1 - ma26_sc ) )
        acc_e_ma26_125 = ( price_126_close * ma26_sc )  + ( acc_e_ma26_126 * ( 1 - ma26_sc ) )
        acc_e_ma26_124 = ( price_125_close * ma26_sc )  + ( acc_e_ma26_125 * ( 1 - ma26_sc ) )
        acc_e_ma26_123 = ( price_124_close * ma26_sc )  + ( acc_e_ma26_124 * ( 1 - ma26_sc ) )
        acc_e_ma26_122 = ( price_123_close * ma26_sc )  + ( acc_e_ma26_123 * ( 1 - ma26_sc ) )
        acc_e_ma26_121 = ( price_122_close * ma26_sc )  + ( acc_e_ma26_122 * ( 1 - ma26_sc ) )

        acc_e_ma26_120 = ( price_121_close * ma26_sc )  + ( acc_e_ma26_121 * ( 1 - ma26_sc ) )
        acc_e_ma26_119 = ( price_120_close * ma26_sc )  + ( acc_e_ma26_120 * ( 1 - ma26_sc ) )
        acc_e_ma26_118 = ( price_119_close * ma26_sc )  + ( acc_e_ma26_119 * ( 1 - ma26_sc ) )
        acc_e_ma26_117 = ( price_118_close * ma26_sc )  + ( acc_e_ma26_118 * ( 1 - ma26_sc ) )
        acc_e_ma26_116 = ( price_117_close * ma26_sc )  + ( acc_e_ma26_117 * ( 1 - ma26_sc ) )
        acc_e_ma26_115 = ( price_116_close * ma26_sc )  + ( acc_e_ma26_116 * ( 1 - ma26_sc ) )
        acc_e_ma26_114 = ( price_115_close * ma26_sc )  + ( acc_e_ma26_115 * ( 1 - ma26_sc ) )
        acc_e_ma26_113 = ( price_114_close * ma26_sc )  + ( acc_e_ma26_114 * ( 1 - ma26_sc ) )
        acc_e_ma26_112 = ( price_113_close * ma26_sc )  + ( acc_e_ma26_113 * ( 1 - ma26_sc ) )
        acc_e_ma26_111 = ( price_112_close * ma26_sc )  + ( acc_e_ma26_112 * ( 1 - ma26_sc ) )

        acc_e_ma26_110 = ( price_111_close * ma26_sc )  + ( acc_e_ma26_111 * ( 1 - ma26_sc ) )
        acc_e_ma26_109 = ( price_110_close * ma26_sc )  + ( acc_e_ma26_110 * ( 1 - ma26_sc ) )
        acc_e_ma26_108 = ( price_109_close * ma26_sc )  + ( acc_e_ma26_109 * ( 1 - ma26_sc ) )
        acc_e_ma26_107 = ( price_108_close * ma26_sc )  + ( acc_e_ma26_108 * ( 1 - ma26_sc ) )
        acc_e_ma26_106 = ( price_107_close * ma26_sc )  + ( acc_e_ma26_107 * ( 1 - ma26_sc ) )
        acc_e_ma26_105 = ( price_106_close * ma26_sc )  + ( acc_e_ma26_106 * ( 1 - ma26_sc ) )
        acc_e_ma26_104 = ( price_105_close * ma26_sc )  + ( acc_e_ma26_105 * ( 1 - ma26_sc ) )
        acc_e_ma26_103 = ( price_104_close * ma26_sc )  + ( acc_e_ma26_104 * ( 1 - ma26_sc ) )
        acc_e_ma26_102 = ( price_103_close * ma26_sc )  + ( acc_e_ma26_103 * ( 1 - ma26_sc ) )
        acc_e_ma26_101 = ( price_102_close * ma26_sc )  + ( acc_e_ma26_102 * ( 1 - ma26_sc ) )

        acc_e_ma26_100 = ( price_101_close * ma26_sc )  + ( acc_e_ma26_101 * ( 1 - ma26_sc ) )
        acc_e_ma26_99 = ( price_100_close * ma26_sc )  + ( acc_e_ma26_100 * ( 1 - ma26_sc ) )
        acc_e_ma26_98 = ( price_99_close * ma26_sc )  + ( acc_e_ma26_99 * ( 1 - ma26_sc ) )
        acc_e_ma26_97 = ( price_98_close * ma26_sc )  + ( acc_e_ma26_98 * ( 1 - ma26_sc ) )
        acc_e_ma26_96 = ( price_97_close * ma26_sc )  + ( acc_e_ma26_97 * ( 1 - ma26_sc ) )
        acc_e_ma26_95 = ( price_96_close * ma26_sc )  + ( acc_e_ma26_96 * ( 1 - ma26_sc ) )
        acc_e_ma26_94 = ( price_95_close * ma26_sc )  + ( acc_e_ma26_95 * ( 1 - ma26_sc ) )
        acc_e_ma26_93 = ( price_94_close * ma26_sc )  + ( acc_e_ma26_94 * ( 1 - ma26_sc ) )
        acc_e_ma26_92 = ( price_93_close * ma26_sc )  + ( acc_e_ma26_93 * ( 1 - ma26_sc ) )
        acc_e_ma26_91 = ( price_92_close * ma26_sc )  + ( acc_e_ma26_92 * ( 1 - ma26_sc ) )

        acc_e_ma26_90 = ( price_91_close * ma26_sc )  + ( acc_e_ma26_91 * ( 1 - ma26_sc ) )
        acc_e_ma26_89 = ( price_90_close * ma26_sc )  + ( acc_e_ma26_90 * ( 1 - ma26_sc ) )
        acc_e_ma26_88 = ( price_89_close * ma26_sc )  + ( acc_e_ma26_89 * ( 1 - ma26_sc ) )
        acc_e_ma26_87 = ( price_88_close * ma26_sc )  + ( acc_e_ma26_88 * ( 1 - ma26_sc ) )
        acc_e_ma26_86 = ( price_87_close * ma26_sc )  + ( acc_e_ma26_87 * ( 1 - ma26_sc ) )
        acc_e_ma26_85 = ( price_86_close * ma26_sc )  + ( acc_e_ma26_86 * ( 1 - ma26_sc ) )
        acc_e_ma26_84 = ( price_85_close * ma26_sc )  + ( acc_e_ma26_85 * ( 1 - ma26_sc ) )
        acc_e_ma26_83 = ( price_84_close * ma26_sc )  + ( acc_e_ma26_84 * ( 1 - ma26_sc ) )
        acc_e_ma26_82 = ( price_83_close * ma26_sc )  + ( acc_e_ma26_83 * ( 1 - ma26_sc ) )
        acc_e_ma26_81 = ( price_82_close * ma26_sc )  + ( acc_e_ma26_82 * ( 1 - ma26_sc ) )

        acc_e_ma26_80 = ( price_81_close * ma26_sc )  + ( acc_e_ma26_81 * ( 1 - ma26_sc ) )
        acc_e_ma26_79 = ( price_80_close * ma26_sc )  + ( acc_e_ma26_80 * ( 1 - ma26_sc ) )
        acc_e_ma26_78 = ( price_79_close * ma26_sc )  + ( acc_e_ma26_79 * ( 1 - ma26_sc ) )
        acc_e_ma26_77 = ( price_78_close * ma26_sc )  + ( acc_e_ma26_78 * ( 1 - ma26_sc ) )
        acc_e_ma26_76 = ( price_77_close * ma26_sc )  + ( acc_e_ma26_77 * ( 1 - ma26_sc ) )
        acc_e_ma26_75 = ( price_76_close * ma26_sc )  + ( acc_e_ma26_76 * ( 1 - ma26_sc ) )
        acc_e_ma26_74 = ( price_75_close * ma26_sc )  + ( acc_e_ma26_75 * ( 1 - ma26_sc ) )
        acc_e_ma26_73 = ( price_74_close * ma26_sc )  + ( acc_e_ma26_74 * ( 1 - ma26_sc ) )
        acc_e_ma26_72 = ( price_73_close * ma26_sc )  + ( acc_e_ma26_73 * ( 1 - ma26_sc ) )
        acc_e_ma26_71 = ( price_72_close * ma26_sc )  + ( acc_e_ma26_72 * ( 1 - ma26_sc ) )

        acc_e_ma26_70 = ( price_71_close * ma26_sc )  + ( acc_e_ma26_71 * ( 1 - ma26_sc ) )
        acc_e_ma26_69 = ( price_70_close * ma26_sc )  + ( acc_e_ma26_70 * ( 1 - ma26_sc ) )
        acc_e_ma26_68 = ( price_69_close * ma26_sc )  + ( acc_e_ma26_69 * ( 1 - ma26_sc ) )
        acc_e_ma26_67 = ( price_68_close * ma26_sc )  + ( acc_e_ma26_68 * ( 1 - ma26_sc ) )
        acc_e_ma26_66 = ( price_67_close * ma26_sc )  + ( acc_e_ma26_67 * ( 1 - ma26_sc ) )
        acc_e_ma26_65 = ( price_66_close * ma26_sc )  + ( acc_e_ma26_66 * ( 1 - ma26_sc ) )
        acc_e_ma26_64 = ( price_65_close * ma26_sc )  + ( acc_e_ma26_65 * ( 1 - ma26_sc ) )
        acc_e_ma26_63 = ( price_64_close * ma26_sc )  + ( acc_e_ma26_64 * ( 1 - ma26_sc ) )
        acc_e_ma26_62 = ( price_63_close * ma26_sc )  + ( acc_e_ma26_63 * ( 1 - ma26_sc ) )
        acc_e_ma26_61 = ( price_62_close * ma26_sc )  + ( acc_e_ma26_62 * ( 1 - ma26_sc ) )

        acc_e_ma26_60 = ( price_61_close * ma26_sc )  + ( acc_e_ma26_61 * ( 1 - ma26_sc ) )
        acc_e_ma26_59 = ( price_60_close * ma26_sc )  + ( acc_e_ma26_60 * ( 1 - ma26_sc ) )
        acc_e_ma26_58 = ( price_59_close * ma26_sc )  + ( acc_e_ma26_59 * ( 1 - ma26_sc ) )
        acc_e_ma26_57 = ( price_58_close * ma26_sc )  + ( acc_e_ma26_58 * ( 1 - ma26_sc ) )
        acc_e_ma26_56 = ( price_57_close * ma26_sc )  + ( acc_e_ma26_57 * ( 1 - ma26_sc ) )
        acc_e_ma26_55 = ( price_56_close * ma26_sc )  + ( acc_e_ma26_56 * ( 1 - ma26_sc ) )
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
        print( "macd값" )
        print( "========== ========== ========== ========== ==========" )
        acc_macd_ok_1 = acc_e_ma12_1 - acc_e_ma26_1
        print( f"e_macd_ok_1 ( { acc_macd_ok_1 } ) =  acc_e_ma12_1 ( { acc_e_ma12_1 } ) - acc_e_ma26_1 ( { acc_e_ma26_1 } )" )

        acc_macd_ok_2 = acc_e_ma12_2 - acc_e_ma26_2
        print( f"e_macd_ok_2 ( { acc_macd_ok_2 } ) =  acc_e_ma12_2 ( { acc_e_ma12_2 } ) - acc_e_ma26_2 ( { acc_e_ma26_2 } )" )

        acc_macd_ok_3 = acc_e_ma12_3 - acc_e_ma26_3
        print( f"e_macd_ok_3 ( { acc_macd_ok_3 } ) =  acc_e_ma12_3 ( { acc_e_ma12_3 } ) - acc_e_ma26_3 ( { acc_e_ma26_3 } )" )

        acc_macd_ok_4 = acc_e_ma12_4 - acc_e_ma26_4
        print( f"e_macd_ok_4 ( { acc_macd_ok_4 } ) =  acc_e_ma12_4 ( { acc_e_ma12_4 } ) - acc_e_ma26_4 ( { acc_e_ma26_4 } )" )

        acc_macd_ok_5 = acc_e_ma12_5 - acc_e_ma26_5
        print( f"e_macd_ok_5 ( { acc_macd_ok_5 } ) =  acc_e_ma12_5 ( { acc_e_ma12_5 } ) - acc_e_ma26_5 ( { acc_e_ma26_5 } )" )

        acc_macd_ok_6 = acc_e_ma12_6 - acc_e_ma26_6
        print( f"e_macd_ok_6 ( { acc_macd_ok_6 } ) =  acc_e_ma12_6 ( { acc_e_ma12_6 } ) - acc_e_ma26_6 ( { acc_e_ma26_6 } )" )

        acc_macd_ok_7 = acc_e_ma12_7 - acc_e_ma26_7
        print( f"e_macd_ok_7 ( { acc_macd_ok_7 } ) =  acc_e_ma12_7 ( { acc_e_ma12_7 } ) - acc_e_ma26_7 ( { acc_e_ma26_7 } )" )

        acc_macd_ok_8 = acc_e_ma12_8 - acc_e_ma26_8
        print( f"e_macd_ok_8 ( { acc_macd_ok_8 } ) =  acc_e_ma12_8 ( { acc_e_ma12_8 } ) - acc_e_ma26_8 ( { acc_e_ma26_8 } )" )

        acc_macd_ok_9 = acc_e_ma12_9 - acc_e_ma26_9
        print( f"e_macd_ok_9 ( { acc_macd_ok_9 } ) =  acc_e_ma12_9 ( { acc_e_ma12_9 } ) - acc_e_ma26_9 ( { acc_e_ma26_9 } )" )

        acc_macd_ok_10 = acc_e_ma12_10 - acc_e_ma26_10
        print( f"e_macd_ok_10 ( { acc_macd_ok_10 } ) =  acc_e_ma12_10 ( { acc_e_ma12_10 } ) - acc_e_ma26_10 ( { acc_e_ma26_10 } )" )

        acc_macd_ok_11 = acc_e_ma12_11 - acc_e_ma26_11
        print( f"e_macd_ok_11 ( { acc_macd_ok_11 } ) =  acc_e_ma12_11 ( { acc_e_ma12_11 } ) - acc_e_ma26_11 ( { acc_e_ma26_11 } )" )

        acc_macd_ok_12 = acc_e_ma12_12 - acc_e_ma26_12
        print( f"e_macd_ok_12 ( { acc_macd_ok_12 } ) =  acc_e_ma12_12 ( { acc_e_ma12_12 } ) - acc_e_ma26_12 ( { acc_e_ma26_12 } )" )

        acc_macd_ok_13 = acc_e_ma12_13 - acc_e_ma26_13
        print( f"e_macd_ok_13 ( { acc_macd_ok_13 } ) =  acc_e_ma12_13 ( { acc_e_ma12_13 } ) - acc_e_ma26_13 ( { acc_e_ma26_13 } )" )

        acc_macd_ok_14 = acc_e_ma12_14 - acc_e_ma26_14
        print( f"e_macd_ok_14 ( { acc_macd_ok_14 } ) =  acc_e_ma12_14 ( { acc_e_ma12_14 } ) - acc_e_ma26_14 ( { acc_e_ma26_14 } )" )

        acc_macd_ok_15 = acc_e_ma12_15 - acc_e_ma26_15
        print( f"e_macd_ok_15 ( { acc_macd_ok_15 } ) =  acc_e_ma12_15 ( { acc_e_ma12_15 } ) - acc_e_ma26_15 ( { acc_e_ma26_15 } )" )

        acc_macd_ok_16 = acc_e_ma12_16 - acc_e_ma26_16
        print( f"e_macd_ok_16 ( { acc_macd_ok_16 } ) =  acc_e_ma12_16 ( { acc_e_ma12_16 } ) - acc_e_ma26_16 ( { acc_e_ma26_16 } )" )

        acc_macd_ok_17 = acc_e_ma12_17 - acc_e_ma26_17
        print( f"e_macd_ok_17 ( { acc_macd_ok_17 } ) =  acc_e_ma12_17 ( { acc_e_ma12_17 } ) - acc_e_ma26_17 ( { acc_e_ma26_17 } )" )
        print()





        print( "시그널값" )
        print( "========== ========== ========== ========== ==========" )
        # signal = macd 9일선, macd값의 9이평선.
        # + 는 0선 이상, - 는 0선 이하
        acc_signal_1 = ( acc_macd_ok_1 + acc_macd_ok_2 + acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 ) / 9
        print( f"acc_signal_1 = ( { acc_signal_1 } )" )

        acc_signal_2 = ( acc_macd_ok_2 + acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 ) / 9
        print( f"acc_signal_2 = ( { acc_signal_2 } )" )

        acc_signal_3 = ( acc_macd_ok_3 + acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 ) / 9
        print( f"acc_signal_3 = ( { acc_signal_3 } )" )

        acc_signal_4 = ( acc_macd_ok_4 + acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 ) / 9
        print( f"acc_signal_4 = ( { acc_signal_4 } )" )

        acc_signal_5 = ( acc_macd_ok_5 + acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 ) / 9
        print( f"acc_signal_5 = ( { acc_signal_5 } )" )

        acc_signal_6 = ( acc_macd_ok_6 + acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 ) / 9
        print( f"acc_signal_6 = ( { acc_signal_6 } )" )

        acc_signal_7 = ( acc_macd_ok_7 + acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 ) / 9
        print( f"acc_signal_7 = ( { acc_signal_7 } )" )

        acc_signal_8 = ( acc_macd_ok_8 + acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 + acc_macd_ok_16 ) / 9
        print( f"acc_signal_8 = ( { acc_signal_8 } )" )

        acc_signal_9 = ( acc_macd_ok_9 + acc_macd_ok_10 + acc_macd_ok_11 + acc_macd_ok_12 + acc_macd_ok_13 + acc_macd_ok_14 + acc_macd_ok_15 + acc_macd_ok_16 + acc_macd_ok_17 ) / 9
        print( f"acc_signal_9 = ( { acc_signal_9 } )" )

        print()

        # 최종값
        # macd - 시그널 = + 는 골든크로스, - 는 데드크로스
        print( "[최종] 간격 = macd - 시그널" )
        print( "========== ========== ========== ========== ==========" )
        acc_macd1 = acc_macd_ok_1 - acc_signal_1
        print( f"acc_macd1 ( { acc_macd1 } ) = acc_macd_ok_1 ( { acc_macd_ok_1 } ) - acc_signal_1 ( { acc_signal_1 } )" )
        acc_macd2 = acc_macd_ok_2 - acc_signal_2
        print( f"acc_macd2 ( { acc_macd2 } ) = acc_macd_ok_2 ( { acc_macd_ok_2 } ) - acc_signal_2 ( { acc_signal_2 } )" )
        acc_macd3 = acc_macd_ok_3 - acc_signal_3
        print( f"acc_macd3 ( { acc_macd3 } ) = acc_macd_ok_3 ( { acc_macd_ok_3 } ) - acc_signal_3 ( { acc_signal_3 } )" )
        acc_macd4 = acc_macd_ok_4 - acc_signal_4
        print( f"acc_macd4 ( { acc_macd4 } ) = acc_macd_ok_4 ( { acc_macd_ok_4 } ) - acc_signal_4 ( { acc_signal_4 } )" )
        acc_macd5 = acc_macd_ok_5 - acc_signal_5
        print( f"acc_macd5 ( { acc_macd5 } ) = acc_macd_ok_5 ( { acc_macd_ok_5 } ) - acc_signal_5 ( { acc_signal_5 } )" )
        acc_macd6 = acc_macd_ok_6 - acc_signal_6
        print( f"acc_macd6 ( { acc_macd6 } ) = acc_macd_ok_6 ( { acc_macd_ok_6 } ) - acc_signal_6 ( { acc_signal_6 } )" )
        acc_macd7 = acc_macd_ok_7 - acc_signal_7
        print( f"acc_macd7 ( { acc_macd7 } ) = acc_macd_ok_7 ( { acc_macd_ok_7 } ) - acc_signal_7 ( { acc_signal_7 } )" )
        acc_macd8 = acc_macd_ok_8 - acc_signal_8
        print( f"acc_macd8 ( { acc_macd8 } ) = acc_macd_ok_8 ( { acc_macd_ok_8 } ) - acc_signal_8 ( { acc_signal_8 } )" )
        acc_macd9 = acc_macd_ok_9 - acc_signal_9
        print( f"acc_macd9 ( { acc_macd9 } ) = acc_macd_ok_9 ( { acc_macd_ok_9 } ) - acc_signal_9 ( { acc_signal_9 } )" )
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

        print( f"acc_macd_select = {acc_macd_select }" )
        print()

        time.sleep(1)







        print( "========== MACD 계산 ==========" )
        print()




        print( f"acc_macd_select = { acc_macd_select }" )


        # macd 설정
        if acc_macd_select == 1 or acc_macd_select == 3:    # 1, 3 은 골든크로스
            # 골든크로스
            now_macd = 1
            print( f"btc_mode = 1 -> 골든크로스" )
        elif acc_macd_select == 2 or acc_macd_select == 4:  # 2, 4 는 데드크로스
            # 데드크로스
            now_macd = -1
            print( f"btc_mode = -1 -> 데드크로스" )

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
        print( "========== ========== ==========" )
        print( "       선 물  잔 고  조 회" )
        print( "========== ========== ==========" )
        print()

        balance = binance.fetch_balance()
        print( "보유코인" )
        pprint.pprint( balance[ 'total' ] )
        #pprint.pprint( balance[ 'total' ][ 'USDT' ] )
        #pprint.pprint( balance[ 'total' ][ 'BTC' ] )
        print( "포지션" )
        positions = balance[ 'info' ][ 'positions' ]

        for position in positions:
            if position[ 'symbol' ] == "BTCUSDT":
                pprint.pprint( position )

                btc_position_amt = float( position[ 'positionAmt' ] )
                print( f"현재 포지션은 ? { btc_position_amt }" )
                print( f"현재 포지션의 변수타입은? { type( btc_position_amt ) }" )


                if btc_position_amt > 0:
                    print( "1. 현재 롱포지션 진입상태" )
                    btc_position_1 = 1

                elif btc_position_amt == 0:
                    print( "2. 현재 포지션 진입을 안한상태" )
                    btc_position_1 = 0

                elif btc_position_amt < 0:
                    print( "3. 현재 숏포지션 진입상태" )
                    btc_position_1 = -1
                
                # 레버리지 값 가져옴
                btc_future_leverage = int( position[ 'leverage' ] )
                btc_leverage = btc_future_leverage

                if btc_leverage > 1:   # 레버리지 비율이 1 초과면 
                    btc_leverage_1 = btc_leverage - 1  # 진입시 사용할 레버리지 배율
                elif btc_leverage <= 1:   # 레버리지 비율이 1 이하이면 
                    btc_leverage_1 = 1  # 진입시 사용할 레버리지 배율

                    

        print( f"현재 내 포지션 코드는? btc_position = { btc_position_1 }" )
        print()


        print( f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" )
        print( f"1-1. 현재시간 포지션 유지중이면" )
        print( f"     값." )
        print( f"1-2-1. 이전 macd 코드는? btc_mode = {btc_mode}" )
        print( f"1-2-2. 현재 macd 코드는? btc_macd = {now_macd}" )
        print()
        print( f"1-3-1. 현재 거래중인 코인갯수는? btc_position_amt = { btc_position_amt }" )
        print( f"1-3-2. 진입한 btc코인의 변수타입은? { type( btc_position_amt ) }" )
        print( f"1-3-3. 현재 거래중인 코인의 포지션 코드는? btc_position_1 = { btc_position_1 }" )

        if btc_position_amt > 0:
            print( "1-3-4. 현재 롱포지션 진입상태" )
            btc_position_1 = 1

        elif btc_position_amt == 0:
            print( "1-3-5. 현재 포지션 진입을 안한상태" )
            btc_position_1 = 0

        elif btc_position_amt < 0:
            print( "1-3-6. 현재 숏포지션 진입상태" )
            btc_position_1 = -1
        print()
        print( f"1-4-1. 현재 설정된 레버리지 배율은 btc_leverage = { btc_leverage }" )
        print( f"1-4-2. 진입시 설정될 레버리지 배율은 btc_leverage_1 = { btc_leverage_1 }" )
        print( f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" )
        print()
        print()

        time.sleep(1)

        





        
        




        # macd 조건문
        if btc_mode == 1:   # 이전 macd코드가 1은 골든크로스
            if now_macd == 1:    # 현재 macd코드가 1은 골든크로스
                print( "골든크로스 -> 골든크로스" )

            elif now_macd == -1:  # 현재 macd코드가 -1은 데드크로스
                print( "골든크로스 -> 데드크로스" )
                # 포지션 정리
                print( "1-1. 롱 포지션 정리" )
                print( f"1-2. 롱 포지션 정리할 코인 갯수 = { btc_position_amt }" )
                print( f"1-2. 롱 포지션 정리할 코인 갯수의 변수타입은? { type( btc_position_amt ) }" )
                print( f"1-3. 포지션 코드 = { btc_position_1 }" )

                # 롱 포지션 정리
                if btc_position_1 == 1:   # 롱 포지션 정리
                    if btc_position_amt != 0:
                        order = binance.create_market_sell_order( symbol = "BTC/USDT", amount = btc_position_amt )
                        print( "1-3. 롱 포지션 정리완료" )

                        time.sleep(1)

                        # 무 포지션으로 코드 변경
                        btc_position_1 = 0
                        print( f"1-4. btc_position_1 = { btc_position_1 } 무 포지션으로 변경" )
                
                # 숏 포지션 진입
                if btc_position_1 == 0:   # 무 포지션 상태
                    balance = binance.fetch_balance()
                    usdt = float( balance[ 'total' ][ 'USDT' ] )
                    print( f"2-1. 보유 USDT = { usdt }" )
                    print( f"2-1. 보유 USDT 의 변수타입은? { type( usdt ) }" )

                    btc = binance.fetch_ticker( symbol = "BTC/USDT" )
                    cur_price = float( btc[ 'last' ] )
                    print( f"2-1. BTC 종가의 변수타입은? { type( cur_price ) }" )
                    #amount_1 = float( cal_amount( usdt, cur_price ) )

                    # 보유금액 조건문.
                    if amount_1 > usdt_trade_MAX_price:
                        print( f"2-1-1. 1,100usdt 초과. △" )

                        usdt = 1000
                        amount_1 = float( cal_amount( usdt, cur_price ) )
                        print( f"2-1-2. 진입할 1배 금액. { amount_1 }usdt" )
                        print( f"2-1-3. 진입할 btc코인의 변수타입은? { type( amount_1 ) }" )

                        # btc_leverage_1 진입 레버리지 배율
                        amount_1_1 = amount_1 * ( btc_leverage_1 + 1 )
                        print( f"2-1-4. 진입할 { btc_leverage_1 + 1 }배 총 금액. { amount_1_1 }usdt" )
                        print( f"2-1-4. 진입할 총코인의 변수타입은? { type( amount_1_1 ) }" )

                    else:
                        print( f"2-1-5. 1,100usdt 이하. ▼" )

                        amount_1 = float( cal_amount( usdt, cur_price ) )
                        print( f"2-1-6. 진입할 1배 btc 코인 - { amount_1 }" )
                        print( f"2-1-7. 진입할 btc코인의 변수타입은? { type( amount_1 ) }" )

                        # btc_leverage_1 진입 레버리지 배율
                        amount_1_1 = amount_1 * btc_leverage_1
                        print( f"2-1-8. 진입할 { btc_leverage_1 }배 총 btc 코인 - { amount_1_1 }" )
                        print( f"2-1-8. 진입할 총코인의 변수타입은? { type( amount_1_1 ) }" )
                    
                    
                    print( "2-2. 숏 포지션 진입" )
                    print( f"2-3. 숏 포지션 진입할 코인 갯수 = { amount_1_1 }" )
                    order = binance.create_market_sell_order( symbol = "BTC/USDT", amount = amount_1_1 )
                    print( "2-4. 숏 포지션 진입완료" )

                    # 숏 포지션 진입시 들어간 코인 갯수
                    print( f"2-5. 진입코인갯수 저장 btc_position_amt = { amount_1_1 }" )

                    time.sleep(1)

                # macd 코드 변경 - 이전 macd 인 btc_mode 에 입력
                btc_mode = -1
                print( f"1, 2. 거래후 btc_macd = -1 -> 데드크로스" )
                # 포지션 숏으로 코드 변경
                btc_position_1 = -1
                print( f"1, 2. 거래후 btc_position_1 = -1 -> 숏 포지션" )

        elif btc_mode == -1:    # 이전 macd코드가 -1은 데드크로스
            if now_macd == 1:    # 현재 macd코드가 1은 골든크로스
                print( "데드크로스 -> 골든크로스" )
                # 포지션 정리
                print( "3-1. 숏 포지션 정리" )
                print( f"3-2. 숏 포지션 정리할 코인 갯수 = { btc_position_amt }" )
                print( f"3-2. 숏 포지션 정리할 코인의 변수타입은? { type( btc_position_amt ) }" )
                print( f"3-3. 포지션 코드 = { btc_position_1 }" )

                # 숏 포지션 정리
                if btc_position_1 == -1:   # 숏 포지션 정리
                    if btc_position_amt != 0:
                        print( "3-3-0. 숏 포지션 정리하기 전 테스트용" )

                        print( f"3-3-1. 포지션 코인을 음수에서 양수로 바꾸기 전 = { btc_position_amt }" )
                        print( "3-3-1. 포지션 코인이 음수이면 양수로 바꿔쭌다." )  

                        if btc_position_amt < 0:    # 포지션 코인이 음수이면 양수로 바꿔준다.
                            btc_position_amt = -( btc_position_amt )
                            print( f"3-3-1. 포지션 코인을 음수에서 양수로 바꾼 후 = { btc_position_amt }" )
                            print( f"3-3-1. 포지션 코인의 변수타입은? { type( btc_position_amt ) }" )

                        print( "3-3-2. 숏포지션 정리전." )
                        order = binance.create_market_buy_order( symbol = "BTC/USDT", amount = btc_position_amt )

                        print( "3-3-3. 숏 포지션 정리완료" )

                        time.sleep(1)
                    
                    # 무 포지션으로 코드 변경
                    btc_position_1 = 0
                    print( f"3-4. btc_position = { btc_position_1 } 무 포지션으로 변경" )
                    
                
                # 롱 포지션 진입
                if btc_position_1 == 0:   # 무 포지션 상태
                    balance = binance.fetch_balance()
                    usdt = float( balance[ 'total' ][ 'USDT' ] )
                    print( f"4-1. 보유 USDT = { usdt }" )
                    print( f"4-1. 보유 USDT 의 변수타입은? { type( usdt ) }" )

                    btc = binance.fetch_ticker(symbol = "BTC/USDT")
                    cur_price = float( btc['last'] )
                    print( f"4-1. BTC 종가의 변수타입은? { type( cur_price ) }" )
                    #amount_1 = float( cal_amount( usdt, cur_price ) )

                    # 보유금액 조건문.
                    if usdt > usdt_trade_MAX_price:
                        print( f"4-1-1. 1,100usdt 초과. △" )

                        usdt = 1000
                        amount_1 = float( cal_amount( usdt, cur_price ) )
                        print( f"4-1-2. 진입할 1배 btc코인. { amount_1 }btc" )
                        print( f"4-1-3. 진입할 btc코인의 변수타입은? { type( amount_1 ) }" )

                        # btc_leverage_1 진입 레버리지 배율
                        amount_1_1 = amount_1 * ( btc_leverage_1 + 1 )
                        print( f"4-1-4. 진입할 { btc_leverage_1 + 1 }배 총 금액. { amount_1_1 }usdt" )
                        print( f"4-1-4. 진입할 총코인의 변수타입은? { type( amount_1_1 ) }" )

                    else:
                        print( f"4-1-5. 1,100usdt 이하. ▼" )

                        amount_1 = float( cal_amount( usdt, cur_price ) )
                        print( f"4-1-6. 진입할 1배 btc 코인 - { amount_1 }" )
                        print( f"4-1-7. 진입할 btc코인의 변수타입은? { type( amount_1 ) }" )

                        # btc_leverage_1 진입 레버리지 배율
                        amount_1_1 = amount_1 * btc_leverage_1
                        print( f"4-1-8. 진입할 { btc_leverage_1 }배 총 btc 코인 - { amount_1_1 }" )
                        print( f"4-1-8. 진입할 총코인의 변수타입은? { type( amount_1_1 ) }" )


                    print( "4-2. 롱 포지션 진입" )
                    print( f"4-3. 롱 포지션 진입할 코인 갯수 = { amount_1_1 }" )
                    order = binance.create_market_buy_order( symbol = "BTC/USDT", amount = amount_1_1 )
                    print( "4-4. 롱 포지션 진입완료" )


                    # 롱 포지션 진입시 들어간 코인 갯수
                    print( f"4-5. 진입코인갯수 저장 btc_position_amt = { amount_1_1 }" )

                    time.sleep(1)
                
                # macd 코드 변경
                btc_mode = 1
                print( f"3, 4. 거래후 btc_macd = 1 -> 골든크로스" )
                # 포지션 롱으로 코드 변경
                btc_position_1 = 1
                print( f"3, 4. 거래후 btc_position = 1 -> 롱 포지션" )

            elif now_macd == -1:  # 현재 macd코드가 -1은 데드크로스
                print( "데드크로스 -> 데드크로스" )

            

        ######################
        # 매수/롱 포지션 진입 #
        ######################
        #order = binance.creat_market_buy_order( symbol = "BTC/USDT", amount = amount_1 )


        ######################
        # 매수/롱 포지션 정리 #
        ######################
        #order = binance.creat_market_sell_order( symbol = "BTC/USDT", amount = amount_1 )

        ################################################################################################################################################################

        ################################################################################################################################################################


        print( "" )
        print( "-=-=-=-=-=- ********** -=-=-=-=-=- ********** -=-=-=-=-=-" )
        print( f"[ 현재시간 : {now} ]   -   종료")
        print( "-=-=-=-=-=- ********** -=-=-=-=-=- ********** -=-=-=-=-=-" )
        print( "" )
        print( "" )



        # 60초 딜레이.
        time.sleep(60)


            