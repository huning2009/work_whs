import sys

sys.path.append('../..')
import loc_lib.b_t_box.get_data as gd
import loc_lib.b_t_box.choose_stock as cs
import pandas as pd
import time
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
import gc
import numpy as np
from multiprocessing import Pool
import os
import copy


def pcf(df):
    pcf_df = (df - df.shift(1)) / df.shift(1)
    pcf_df[(-0.2 > pcf_df) | (pcf_df > 0.2)] = 0
    return pcf_df


def path_create(target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)


def Sharpe(pnl):
    pnl = pd.DataFrame(pnl, columns=['pnl'])
    pnl_diff = (pnl - pnl.shift(1)).dropna()
    return ((16 * pnl_diff.mean()) / pnl_diff.std())[0]


# signal 生成
def signal_BBANDS(choose_price, n=15):
    # 5分钟级别的数据
    MA = choose_price.rolling(window=n).mean()
    STD = choose_price.rolling(window=n).std()
    signal = (choose_price - MA) / STD
    signal.fillna(0, inplace=True)
    return signal


# position生成
def position_1(signal, limit=1):
    signal[(signal >= -limit) & (signal <= limit)] = None
    signal[signal > limit] = 1
    signal[signal < -limit] = -1

    signal.fillna(method='ffill', inplace=True)
    signal.fillna(0, inplace=True)
    return signal


def sub_pos_2(k, hold_time, limit):
    x = 0
    k_c = np.array([0.] * len(k))
    while x < len(k):
        if k[x] > limit:
            k_c[x:x + hold_time] = -1
            x += hold_time
        elif k[x] < -limit:
            k_c[x:x + hold_time] = 1
            x += hold_time
        else:
            x += 1
    return k_c


def position_2(signal, hold_time=8, limit=1):
    position = signal.apply(sub_pos_2, args=(hold_time * 3, limit))
    return position


def trade_fun(position, choose_vwap, log_time):
    cost = 0.0005
    position_lag = position.shift(log_time)
    position_trade = position_lag.loc[choose_vwap.index]
    position_trade.iloc[-2:] = 0
    vwap_diff = choose_vwap.rolling(window=2).apply(lambda x: (x[-1] - x[0]) / x[0])
    day_pnl = sum((position_trade.shift(2) * vwap_diff).sum())
    day_trade = sum(position_trade.diff().abs().sum())
    # day_cost = day_trade * cost
    # day_pnl = day_pnl - day_cost
    return day_pnl, day_trade


def back_test_fun(vol_num, log_time, n, limit, stock_num):
    start = time.time()
    cost = 0.0005
    date_list = sorted(price.keys())
    pnl_list = [0.] * len(date_list)
    trade_list = [0] * len(date_list)
    for i_date in range(vol_num, len(date_list)):
        date = date_list[i_date]
        print(date)
        pre_price_data = pd.DataFrame()
        pre_turnover_data = pd.DataFrame()

        part_price = copy.deepcopy(price[date])
        part_vwap = copy.deepcopy(vwap[date])

        part_vwap.index = pd.to_datetime([date + ' ' + x for x in part_vwap.index])
        part_price.index = pd.to_datetime(part_price.index)
        today_stock = part_price.columns

        for i_vol in range(vol_num):
            back_date = date_list[i_date - 1 - i_vol]
            tmp_price_data = copy.deepcopy(price[back_date])
            tmp_turn_data = copy.deepcopy(volume[back_date])
            pre_price_data = pd.concat([pre_price_data, tmp_price_data], axis=0)
            pre_turnover_data = pd.concat([pre_turnover_data, tmp_turn_data], axis=0)
        # 根据波动率、交易量与股价选股 返回一个股票list
        # universe = cs.high_vol_stock(pre_price_data, pre_turnover_data, p_num=stock_num, t_num=300, v_num=500)
        try:
            universe = list(map(lambda x: 'SH' + x if x[0] == '6' else 'SZ' + x,
                                universe_df.loc[pd.to_datetime(date)].dropna().index.values))
        except:
            universe = []
        print(universe)
        # 筛选出的股票与当天开盘的股票求交集
        choose_stock = sorted(list(set(universe) & set(today_stock)))
        # 筛选股票的price和vwap
        choose_price = part_price[choose_stock]
        choose_vwap = part_vwap[choose_stock]
        # 每天信号和仓位生成
        signal = signal_BBANDS(choose_price, n)
        # position = position_2(signal, hold_time, limit)
        position = position_1(signal, limit)
        # 每天的交易函数
        pnl_list[i_date], trade_list[i_date] = trade_fun(position, choose_vwap, log_time)

    end = time.time()

    asset = np.cumsum(pnl_list)
    sharpe = Sharpe(asset)
    if abs(sharpe) >= 1.5 and \
            (abs(asset[-1]) - sum(trade_list) * cost) / (sum(trade_list) * cost / (0.001 * 7 * 250)) > 1.5:
        # 保存路径
        save_root_path = '/home/whs/Work/result/bbangs/bbangs_pos1'
        path_create(save_root_path)
        save_path = \
            'sharpe={},vol_num={},hold_time={},log_time={},n={},limit={},stock_num={},asset={},trade_cost={}.npy' \
                .format(sharpe, vol_num, hold_time, log_time, n, limit, stock_num, asset[-1], sum(trade_list) * cost)
        np.save(os.path.join(save_root_path, save_path), asset)
    print('*************************************************', '\n',
          'in the process:', os.getpid(), os.getppid(), '\n',
          vol_num, hold_time, n, limit, stock_num, '\n',
          'Processing Cost:{} second'.format(end - start), '\n',
          'sharpe={},vol_num={},hold_time={},log_time={},n={},limit={},stock_num={},asset={},trade_cost={}'
          .format(sharpe, vol_num, hold_time, log_time, n, limit, stock_num, asset[-1], sum(trade_list) * cost), '\n',
          asset, '\n',
          '*************************************************')

    if not os.path.exists(log_save_path):
        with open(log_save_path, "w") as f:
            f.write('{}_{}_{}_{}_{},Done\n'.format(vol_num, log_time, n, limit, stock_num))
    else:
        with open(log_save_path, "a") as f:
            f.write('{}_{}_{}_{}_{},Done\n'.format(vol_num, log_time, n, limit, stock_num))


def parameter_fun1():
    for vol_num in iter([2, 3, 4]):
        for n in iter([5, 10, 15]):
            for limit in iter([1.8, 2, 2.2, 2.4]):
                for stock_num in iter([50, 100, 200]):
                    yield vol_num, n, limit, stock_num


if __name__ == '__main__':
    begin_date = '20100101'
    end_date = '20170101'

    # 过去 天的波动率和交易量
    vol_num = 2
    # 持仓时间 个数据点
    hold_time = 8
    # 延迟时间 个数据点
    log_time = 1
    # bbangs参数
    n = 10
    limit = 2
    # 选股数量
    stock_num = 200
    global price, volume, vwap, log_save_path, universe_df

    # price, volume, vwap = gd.eqt_1mbar_data(begin_date, end_date)
    # price, volume, vwap = gd.eqt_5mbar_data(begin_date, end_date)

    data_load_path = '/media/hdd0/data/adj_data/equity/intraday/special'
    price = pd.read_pickle(os.path.join(data_load_path, 'close_5m_2010-2017.pkl'))
    volume = pd.read_pickle(os.path.join(data_load_path, 'volume_5m_2010-2017.pkl'))
    vwap = pd.read_pickle(os.path.join(data_load_path, 'vwap_5m_2010-2017.pkl'))
    # universe_df = pd.read_pickle('/media/hdd1/whs_data/adj_data/table14/TRAD_BT_DAILY/TRAD_BT_DAILY_TIME.pkl')
    # universe_df[universe_df == 0] = float('nan')
    universe_df = pd.read_pickle('/media/hdd1/whs_data/adj_data/table14/set_137001.pkl')
    log_save_path = "/home/whs/Work/result/bbangs/log_big_trade_bbangs_pos1.txt"

    back_test_fun(vol_num, log_time, n, limit, stock_num)
    # pool = Pool(6)
    #
    # if os.path.exists(log_save_path):
    #     log_df = pd.read_csv('log_save_path', sep=',', header=None, index_col=0)
    # else:
    #     log_df = float('nan')
    # for vol_num, n, limit, stock_num in parameter_fun1():
    #     if not np.isnan(log_df):
    #         if '{}_{}_{}_{}_{}'.format(vol_num, log_time, n, limit, stock_num) in log_df.index:
    #             # pool.apply_async(back_test_fun, args=(vol_num, hold_time, log_time, n, limit, stock_num,))
    #             continue
    #     pool.apply_async(back_test_fun, args=(vol_num, log_time, n, limit, stock_num))
    #
    # pool.close()
    # pool.join()
