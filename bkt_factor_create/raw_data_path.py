from collections import OrderedDict

base_data_dict = OrderedDict({
    'TVOL': 'EM_Funda/TRAD_SK_DAILY_JC/TVOL.csv',
    'TVALCNY': 'EM_Funda/TRAD_SK_DAILY_JC/TVALCNY.csv',
    'aadj_r': 'EM_Funda/DERIVED_14/aadj_r.csv',
    'TURNRATE': 'EM_Funda/TRAD_SK_DAILY_JC/TURNRATE.csv',

    'aadj_p': 'EM_Funda/DERIVED_14/aadj_p.csv',
    'aadj_p_OPEN': 'EM_Funda/DERIVED_14/aadj_p_OPEN.csv',
    'aadj_p_HIGH': 'EM_Funda/DERIVED_14/aadj_p_HIGH.csv',
    'aadj_p_LOW': 'EM_Funda/DERIVED_14/aadj_p_OPEN.csv',

    'PE_TTM': 'EM_Funda/TRAD_SK_REVALUATION/PE_TTM.csv',
    'PS_TTM': 'EM_Funda/TRAD_SK_REVALUATION/PS_TTM.csv',
    'PBLast': 'EM_Funda/TRAD_SK_REVALUATION/PBLast.csv',

    'RZMRE': 'EM_Funda/TRAD_MT_MARGIN/RZMRE.csv',
    'RZYE': 'EM_Funda/TRAD_MT_MARGIN/RZYE.csv',
    'RQMCL': 'EM_Funda/TRAD_MT_MARGIN/RQMCL.csv',
    'RQYE': 'EM_Funda/TRAD_MT_MARGIN/RQYE.csv',
    'RQYL': 'EM_Funda/TRAD_MT_MARGIN/RQYL.csv',
    'RQCHL': 'EM_Funda/TRAD_MT_MARGIN/RQCHL.csv',
    'RZCHE': 'EM_Funda/TRAD_MT_MARGIN/RZCHE.csv',

    'R_AssetDepSales_s_First': '',
    'R_CFOPS_s_First': '',
    'R_CFO_TotRev_s_First': '',
    'R_CFO_s_YOY_First': '',
    'R_Cashflow_s_YOY_First': '',
    'R_CostSales_s_First': '',
    'R_CurrentAssetsTurnover_QTTM': '',
    'R_DebtAssets_QTTM': '',
    'R_EBITDA_IntDebt_QTTM': '',
    'R_EBIT_sales_QTTM': '',
    'R_EPS_s_First': '',
    'R_EPS_s_YOY_First': '',
    'R_FCFTot_Y3YGR': '',
    'R_FairValChgPnL_s_First': '',
    'R_FairValChg_TotProfit_s_First': '',
    'R_FinExp_sales_s_First': '',
    'R_GSCF_sales_s_First': '',
    'R_LTDebt_WorkCap_QTTM': '',
    'R_MgtExp_sales_s_First': '',
    'R_NetAssets_s_POP_First': '',
    'R_NetAssets_s_YOY_First': '',
    'R_NetCashflowPS_s_First': '',
    'R_NetIncRecur_s_First': '',
    'R_NetInc_TotProfit_s_First': '',
    'R_NetInc_s_First': '',
    'R_NetMargin_s_YOY_First': '',
    'R_NetProfit_sales_s_First': '',
    'R_NetROA_TTM_First': '',
    'R_NetROA_s_First': '',
    'R_NonOperProft_TotProfit_s_First': '',
    'R_OPCF_NetInc_s_First': '',
    'R_OPCF_TotDebt_QTTM': '',
    'R_OPCF_sales_s_First': '',
    'R_OPEX_sales_TTM_First': '',
    'R_OPEX_sales_s_First': '',
    'R_OperCost_sales_s_First': '',
    'R_OperProfit_s_POP_First': '',
    'R_OperProfit_s_YOY_First': '',
    'R_OperProfit_sales_s_First': '',
    'R_ParentProfit_s_POP_First': '',
    'R_ParentProfit_s_YOY_First': '',
    'R_ROENetIncRecur_s_First': '',
    'R_ROE_s_First': '',
    'R_RecurNetProft_NetProfit_s_First': '',
    'R_RevenuePS_s_First': '',
    'R_RevenueTotPS_s_First': '',
    'R_Revenue_s_POP_First': '',
    'R_Revenue_s_YOY_First': '',
    'R_SUMLIAB_Y3YGR': '',
    'R_SalesCost_s_First': '',
    'R_SalesGrossMGN_QTTM': '',
    'R_SalesGrossMGN_s_First': '',
    'R_SalesNetMGN_s_First': '',
    'R_TangAssets_TotLiab_QTTM': '',
    'R_Tax_TotProfit_QTTM': '',
    'R_Tax_TotProfit_s_First': '',
    'R_TotAssets_s_YOY_First': '',
    'R_TotLiab_s_YOY_First': '',
    'R_TotRev_TTM_Y3YGR': '',
    'R_TotRev_s_POP_First': '',
    'R_TotRev_s_YOY_First': '',

    'R_TotRev_TTM_QTTM': '',
    'R_FinCf_TTM_QTTM': '',
    'R_GSCF_TTM_QTTM': '',
    'R_NetCf_TTM_QTTM': '',
    'R_OPCF_TTM_QTTM': '',
    'R_EBIT_TTM_QTTM': '',
    'R_WorkCapital_QTTM': '',
    'R_NetWorkCapital_QTTM': '',
    'R_TotRev_TTM_QSD4Y': '',
    'R_FinCf_TTM_QSD4Y': '',
    'R_GSCF_TTM_QSD4Y': '',
    'R_NetCf_TTM_QSD4Y': '',
    'R_OPCF_TTM_QSD4Y': '',
    'R_EBIT_TTM_QSD4Y': '',
    'R_WorkCapital_QSD4Y': '',
    'R_NetWorkCapital_QSD4Y': '',
    'R_NetIncRecur_QTTM': '',
    'R_NETPROFIT_QTTM': '',
    'R_OTHERCINCOME_QTTM': '',
    'R_AssetDepSales_QTTM': '',
    'R_ACCEPTINVREC_QTTM': '',
    'R_COMMPAY_QTTM': '',
    'R_CurrentLiabInt0_QTTM': '',
    'R_DEFERTAX_QTTM': '',
    'R_DIVIPAY_QTTM': '',
    'R_EMPLOYEEPAY_QTTM': '',
    'R_INCOMETAX_QTTM': '',
    'R_INVENTORY_QTTM': '',
    'R_TangAssets_QTTM': '',
    'R_TangAssets_First': '',
    'R_TotAssets_NBY_First': '',
    'R_ASSETOTHER_First': '',
    'R_SUMASSET_First': '',
    'R_IntDebt_First': '',
    'R_NetDebt_First': '',
    'R_TotCapital_First': '',
    'R_WorkCapital_First': '',
    'R_ROETrig_First': '',
    'R_ROEWRecur_First': '',
    'R_NetROA1_First': '',
    'R_TotProfit_EBIT_First': '',
    'R_OperProfit_sales_Y3YGR': '',
    'R_SalesGrossMGN_First': '',
    'R_SalesGrossMGN_s_Y3YGR': '',

    'stock_tab1_1': '/EM_Funda/dat_whs/stock_code_df_tab1_1',
    'stock_tab1_2': '/EM_Funda/dat_whs/stock_code_df_tab1_2',
    'stock_tab1_5': '/EM_Funda/dat_whs/stock_code_df_tab1_5',
    'stock_tab1_7': '/EM_Funda/dat_whs/stock_code_df_tab1_7',
    'stock_tab1_8': '/EM_Funda/dat_whs/stock_code_df_tab1_8',
    'stock_tab1_9': '/EM_Funda/dat_whs/stock_code_df_tab1_9',
    'stock_tab2_1': '/EM_Funda/dat_whs/stock_code_df_tab2_1',
    'stock_tab2_10': '/EM_Funda/dat_whs/stock_code_df_tab2_10',
    'stock_tab2_4': '/EM_Funda/dat_whs/stock_code_df_tab2_4',
    'stock_tab2_5': '/EM_Funda/dat_whs/stock_code_df_tab2_5',
    'stock_tab2_7': '/EM_Funda/dat_whs/stock_code_df_tab2_7',
    'stock_tab2_8': '/EM_Funda/dat_whs/stock_code_df_tab2_8',
    'stock_tab2_9': '/EM_Funda/dat_whs/stock_code_df_tab2_9',
    'stock_tab4_1': '/EM_Funda/dat_whs/stock_code_df_tab4_1',
    'stock_tab4_2': '/EM_Funda/dat_whs/stock_code_df_tab4_2',
    'stock_tab4_3': '/EM_Funda/dat_whs/stock_code_df_tab4_3',

    'lsgg_num_df_5': '/EM_Funda/dat_whs/lsgg_num_df_5.csv',
    'lsgg_num_df_20': '/EM_Funda/dat_whs/lsgg_num_df_20.csv',
    'lsgg_num_df_60': '/EM_Funda/dat_whs/lsgg_num_df_60.csv',
    'bulletin_num_df_5': '/EM_Funda/dat_whs/bulletin_num_df_5.csv',
    'bulletin_num_df_20': '/EM_Funda/dat_whs/bulletin_num_df_20.csv',
    'bulletin_num_df_60': '/EM_Funda/dat_whs/bulletin_num_df_60.csv',
    'news_num_df_5': '/EM_Funda/dat_whs/news_num_df_5.csv',
    'news_num_df_20': '/EM_Funda/dat_whs/news_num_df_20.csv',
    'news_num_df_60': '/EM_Funda/dat_whs/news_num_df_60.csv',
    'staff_changes': '/EM_Funda/dat_whs/staff_changes.csv',
    'funds': '/EM_Funda/dat_whs/funds.csv',
    'meeting_decide': '/EM_Funda/dat_whs/meeting_decide.csv',
    'restricted_shares': '/EM_Funda/dat_whs/restricted_shares.csv',
    'son_company': '/EM_Funda/dat_whs/son_company.csv',
    'suspend': '/EM_Funda/dat_whs/suspend.csv',
    'shares': '/EM_Funda/dat_whs/shares.csv',
    'bar_num_7_df': '/EM_Funda/dat_whs/bar_num_7_df.csv',
    'bar_num_12_df': '/EM_Funda/dat_whs/bar_num_12_df.csv',
    'buy_key_title__word': '/EM_Funda/dat_whs/buy_key_title__word.csv',
    'sell_key_title_word': '/EM_Funda/dat_whs/sell_key_title_word.csv',
    'buy_summary_key_word': '/EM_Funda/dat_whs/buy_summary_key_word.csv',
    'sell_summary_key_word': '/EM_Funda/dat_whs/sell_summary_key_word.csv',

    'ab_inventory': '/EM_Funda/dat_whs/ab_inventory.csv',
    'ab_rec': '/EM_Funda/dat_whs/ab_rec.csv',
    'ab_others_rec': '/EM_Funda/dat_whs/ab_others_rec.csv',
    'ab_ab_pre_rec': '/EM_Funda/dat_whs/ab_ab_pre_rec.csv',
    'ab_sale_mng_exp': '/EM_Funda/dat_whs/ab_sale_mng_exp.csv',
    'ab_grossprofit': '/EM_Funda/dat_whs/ab_grossprofit.csv',
})
