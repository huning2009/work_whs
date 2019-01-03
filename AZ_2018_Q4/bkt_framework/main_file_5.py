import sys

sys.path.append('/mnt/mfs')

from work_whs.loc_lib.pre_load import *
import work_whs.AZ_2018_Q4.bkt_framework.bkt_base_import_script as bkt_base


class KeyFun:
    @staticmethod
    def load_daily_data(file_name, xinx, xnms, sector_df):
        load_path = '/mnt/mfs/DAT_EQT/EM_Funda/daily/'
        tmp_df = bt.AZ_Load_csv(os.path.join(load_path, file_name + '.csv'))
        tmp_df = tmp_df.reindex(index=xinx, columns=xnms) * sector_df
        target_df = bt.AZ_Row_zscore(tmp_df, cap=5)
        return target_df

    @staticmethod
    def load_filter_data(filter_name, xinx, xnms, sector_df, if_only_long):
        load_path = '/mnt/mfs/dat_whs/data/new_factor_data_v2/'
        target_df = pd.read_pickle(os.path.join(load_path, filter_name + '.pkl')).reindex(index=xinx, columns=xnms)
        if if_only_long:
            target_df = target_df[target_df > 0]
        return target_df

    @staticmethod
    def row_extre(raw_df, sector_df, percent):
        raw_df = raw_df * sector_df
        target_df = raw_df.rank(axis=1, pct=True)
        target_df[target_df >= 1 - percent] = 1
        target_df[target_df <= percent] = -1
        target_df[(target_df > percent) & (target_df < 1 - percent)] = 0
        return target_df

    def create_mix_factor(self, name_1, name_2, xinx, xnms, sector_df, if_only_long, percent):
        factor_1 = self.load_daily_data(name_1, xinx, xnms, sector_df)
        factor_2 = self.load_daily_data(name_2, xinx, xnms, sector_df)
        score_df_1 = bt.AZ_Row_zscore(factor_1, cap=5)
        score_df_2 = bt.AZ_Row_zscore(factor_2, cap=5)
        mix_df = score_df_1 + score_df_2
        target_df = self.row_extre(mix_df, sector_df, percent)
        if if_only_long:
            target_df = target_df[target_df > 0]
        return target_df


def main_fun(time_para_dict, sector_name, hold_time, if_only_long):
    root_path = '/mnt/mfs/DAT_EQT'
    if_save = True
    if_new_program = True

    begin_date = pd.to_datetime('20100101')
    cut_date = pd.to_datetime('20160401')
    end_date = pd.to_datetime('20180901')
    lag = 2
    return_file = ''

    if_hedge = True
    # if_only_long = False

    if sector_name.startswith('market_top_300plus'):
        if_weight = 1
        ic_weight = 0

    elif sector_name.startswith('market_top_300to800plus'):
        if_weight = 0
        ic_weight = 1

    else:
        if_weight = 0.5
        ic_weight = 0.5

    para_set = [root_path, if_save, if_new_program, begin_date, cut_date, end_date, time_para_dict,
                sector_name, hold_time, lag, return_file, if_hedge, if_only_long, if_weight, ic_weight]

    key_fun = KeyFun()

    main_model = bkt_base.FactorTest(key_fun, *para_set)

    my_factor_list = [
        'lsgg_num_df_5',
        'lsgg_num_df_20',
        'lsgg_num_df_60',
        'bulletin_num_df',
        'news_num_df_5',
        'news_num_df_20',
        'news_num_df_60',
        'staff_changes',
        'funds',
        'meeting_decide',
        'restricted_shares',
        'son_company',
        'suspend',
        'shares',
        'bar_num_7_df',
        'bar_num_12_df',
        'ab_ab_pre_rec.csv',
        'ab_grossprofit.csv',
        'ab_inventory.csv',
        'ab_others_rec.csv',
        'ab_rec.csv',
        'ab_sale_mng_exp.csv'
    ]

    filter_list = [
        'ADOSC_5_10_0',
        'ADOSC_60_120_0',
        'ADX_10_20_10',
        'ADX_140_20_10',
        'ADX_40_20_10',
        'MFI_10_70_30',
        'MFI_40_70_30',
        'MFI_140_70_30',
        'AROON_10_80',
        'AROON_140_80',
        'BBANDS_10_1.5',
        'BBANDS_20_1.5',
        'MACD_20_60_18',
        'MACD_12_26_9',
        'MA_LINE_10_5',
        'MA_LINE_160_60',
        'MFI_100_70_30',
        'MFI_20_70_30',
        'RSI_100_10',
        'RSI_200_30',
        'WILLR_100_40',
        'WILLR_100_30',
        'WILLR_10_30',
        'WILLR_140_30',
        'WILLR_200_30',
        'WILLR_20_30',
    ]

    pool_num = 25
    suffix_name = os.path.basename(__file__).split('.')[0][-1]
    main_model.main_test_fun(filter_list, my_factor_list, my_factor_list,
                             pool_num=pool_num, suffix_name=suffix_name, old_file_name='')


time_para_dict = OrderedDict()

time_para_dict['time_para_1'] = [pd.to_datetime('20100101'), pd.to_datetime('20150101'),
                                 pd.to_datetime('20150401'), pd.to_datetime('20150701'),
                                 pd.to_datetime('20151001'), pd.to_datetime('20160101')]

time_para_dict['time_para_2'] = [pd.to_datetime('20110101'), pd.to_datetime('20160101'),
                                 pd.to_datetime('20160401'), pd.to_datetime('20160701'),
                                 pd.to_datetime('20161001'), pd.to_datetime('20170101')]

time_para_dict['time_para_3'] = [pd.to_datetime('20130101'), pd.to_datetime('20180101'),
                                 pd.to_datetime('20180401'), pd.to_datetime('20180701'),
                                 pd.to_datetime('20181001'), pd.to_datetime('20181001')]

time_para_dict['time_para_4'] = [pd.to_datetime('20130801'), pd.to_datetime('20180801'),
                                 pd.to_datetime('20181101'), pd.to_datetime('20181101'),
                                 pd.to_datetime('20181101'), pd.to_datetime('20181101')]

time_para_dict['time_para_5'] = [pd.to_datetime('20130901'), pd.to_datetime('20180901'),
                                 pd.to_datetime('20181101'), pd.to_datetime('20181101'),
                                 pd.to_datetime('20181101'), pd.to_datetime('20181101')]

time_para_dict['time_para_6'] = [pd.to_datetime('20131001'), pd.to_datetime('20181001'),
                                 pd.to_datetime('20181101'), pd.to_datetime('20181101'),
                                 pd.to_datetime('20181101'), pd.to_datetime('20181101')]

if __name__ == '__main__':

    if_only_long_list = [False, True]
    hold_time_list = [5, 20]
    sector_name_list = [
        'market_top_300plus',
        'market_top_300to800plus',

        'market_top_300plus_ind1.csv',
        'market_top_300plus_ind2.csv',
        'market_top_300plus_ind3.csv',
        'market_top_300plus_ind4.csv',
        'market_top_300plus_ind5.csv',
        'market_top_300plus_ind6.csv',
        'market_top_300plus_ind7.csv',
        'market_top_300plus_ind8.csv',
        'market_top_300plus_ind9.csv',
        'market_top_300plus_ind10.csv',
        'market_top_300to800plus_ind1.csv',
        'market_top_300to800plus_ind2.csv',
        'market_top_300to800plus_ind3.csv',
        'market_top_300to800plus_ind4.csv',
        'market_top_300to800plus_ind5.csv',
        'market_top_300to800plus_ind6.csv',
        'market_top_300to800plus_ind7.csv',
        'market_top_300to800plus_ind8.csv',
        'market_top_300to800plus_ind9.csv',
        'market_top_300to800plus_ind10.csv',
    ]

    for if_only_long, hold_time, sector_name in list(product(if_only_long_list, hold_time_list, sector_name_list)):
        # print(sector_name, hold_time, if_only_long)
        main_fun(time_para_dict, sector_name, hold_time, if_only_long)
