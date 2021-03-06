import sys

sys.path.append('/mnt/mfs')

from work_whs.loc_lib.pre_load import *


def save_fun(df, save_path, sep='|', check=False):
    df.to_csv(save_path, sep=sep)
    if check:
        test_save_path = '/mnt/mfs/dat_whs/EM_Funda/{}'.format(datetime.now().strftime('%Y%m%d'))
        bt.AZ_Path_create(test_save_path)
        df.to_csv(os.path.join(test_save_path, os.path.split(save_path)[-1]))


# def data_update():
#     def deal_fun(x):
#         return x.iloc[-1]
#
#     data = bt.AZ_Load_csv(f'{root_path}/EM_Funda/daily/R_SALEGOODSSERVICEREC_First.csv'
#                           , parse_dates=False)
#     upsample_df = bt.AZ_Load_csv(f'{root_path}/EM_Funda/LICO_FN_RGCASHFLOW/UpSampleDate_SALEGOODSSERVICEREC_First.csv'
#                                  , parse_dates=False)
#     a = upsample_df.stack()
#     b = data.stack()
#     c = pd.concat([a, b], axis=1)
#     d = c.reset_index()[['level_1', 0, 1]]
#     target_df = d.groupby([0, 'level_1'])[1].apply(deal_fun).unstack()


def get_totassets(root_path):
    TangAssets = bt.AZ_Load_csv(f'{root_path}/EM_Funda/daily/R_TangAssets_First.csv')
    TangAssets_TotAssets = bt.AZ_Load_csv(f'{root_path}/EM_Funda/daily/R_TangAssets_TotAssets_First.csv')
    return TangAssets / TangAssets_TotAssets


def norm_increase_fun(root_path):
    data = bt.AZ_Load_csv(f'{root_path}/EM_Funda/daily/R_SALEGOODSSERVICEREC_First.csv')
    target_df = data / data.shift(255)
    return target_df


def ab_inventory_fun(nif, totassets, root_path):
    INVENTORY_df = bt.AZ_Load_csv(f'{root_path}/EM_Funda/daily/R_INVENTORY_First.csv')
    target_df = (INVENTORY_df - INVENTORY_df.shift(255) * nif) / totassets * (-1)
    save_path = f'{root_path}/EM_Funda/dat_whs/ab_inventory.csv'
    save_fun(target_df, save_path, sep='|')


def ab_rec_fun(nif, totassets, root_path):
    ACCOUNTREC_df = bt.AZ_Load_csv(f'{root_path}/EM_Funda/daily/R_ACCOUNTREC_First.csv')
    ADVANCEPAY_df = bt.AZ_Load_csv(f'{root_path}/EM_Funda/daily/R_ADVANCEPAY_First.csv')
    tot_df = (ACCOUNTREC_df + ADVANCEPAY_df)
    target_df = (tot_df - tot_df.shift(255) * nif) / totassets * (-1)
    save_path = f'{root_path}/EM_Funda/dat_whs/ab_rec.csv'
    save_fun(target_df, save_path, sep='|')


def ab_others_rec_fun(nif, totassets, root_path):
    OTHERREC_df = bt.AZ_Load_csv(f'{root_path}/EM_Funda/daily/R_OTHERREC_First.csv')
    target_df = (OTHERREC_df - OTHERREC_df.shift(255) * nif) / totassets * (-1)
    save_path = f'{root_path}/EM_Funda/dat_whs/ab_others_rec.csv'
    save_fun(target_df, save_path, sep='|')


def ab_pre_rec_fun(nif, totassets, root_path):
    ADVANCERECEIVE_df = bt.AZ_Load_csv(f'{root_path}/EM_Funda/daily/R_ADVANCERECEIVE_First.csv')
    target_df = (ADVANCERECEIVE_df - ADVANCERECEIVE_df.shift(255) * nif) / totassets
    save_path = f'{root_path}/EM_Funda/dat_whs/ab_ab_pre_rec.csv'
    save_fun(target_df, save_path, sep='|')


def ab_sale_mng_exp_fun(nif, totassets, root_path):
    SALEEXP_df = bt.AZ_Load_csv(f'{root_path}/EM_Funda/daily/R_SALEEXP_First.csv')
    MANAGEEXP_s_df = bt.AZ_Load_csv(f'{root_path}/EM_Funda/daily/R_MANAGEEXP_s_First.csv')
    tot_df = MANAGEEXP_s_df + SALEEXP_df
    target_df = (tot_df - tot_df.shift(255) * nif) / totassets * (-1)
    save_path = f'{root_path}/EM_Funda/dat_whs/ab_sale_mng_exp.csv'
    save_fun(target_df, save_path, sep='|')


def ab_grossprofit_fun(nif, totassets, root_path):
    GrossProfit_df = bt.AZ_Load_csv(f'{root_path}/EM_Funda/daily/R_GrossProfit_First.csv')
    target_df = (GrossProfit_df - GrossProfit_df.shift(255) * nif) / totassets
    save_path = f'{root_path}/EM_Funda/dat_whs/ab_grossprofit.csv'
    save_fun(target_df, save_path, sep='|')


def main_fun(mod):
    if mod == 'pro':
        root_path = '/media/hdd1/DAT_EQT'
    elif mod == 'bkt':
        root_path = '/mnt/mfs/DAT_EQT'
    else:
        return -1
    a = time.time()
    nif = norm_increase_fun(root_path)
    totassets = get_totassets(root_path)

    ab_inventory_fun(nif, totassets, root_path)
    ab_rec_fun(nif, totassets, root_path)
    ab_others_rec_fun(nif, totassets, root_path)
    ab_pre_rec_fun(nif, totassets, root_path)
    ab_sale_mng_exp_fun(nif, totassets, root_path)
    ab_grossprofit_fun(nif, totassets, root_path)

    b = time.time()
    print(b - a)


if __name__ == '__main__':
    mod = 'pro'
    main_fun(mod)
