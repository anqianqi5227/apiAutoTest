from common.tools.gen_sign import gen_sign
from common.tools.time import gen_stamp_date_today_begin_time, gen_stamp_date_today_end_time, this_week_date_begin, \
    this_week_date_end, gen_timestamps_13, this_month_data_begin, this_month_data_end, today_datetime
import logging
def replace_function(func_name,func_param):

    """

    :param func_name: 函数名
    :param func_param: 函数参数
    :return: 函数执行完的结果值
    """
    try:
        if 'gen_timestamps_13' in func_name:
            func_value = gen_timestamps_13(func_param)
        elif 'gen_stamp_date_today_begin_time' in func_name:
            func_value = gen_stamp_date_today_begin_time()
        elif 'gen_stamp_date_today_end_time' in func_name:
            func_value = gen_stamp_date_today_end_time()
        elif 'this_week_date_begin' in func_name:
            func_value = this_week_date_begin()
        elif 'this_week_date_end' in func_name:
            func_value = this_week_date_end()
        elif 'this_month_data_begin' in func_name:
            func_value = this_month_data_begin
        elif 'this_month_data_end' in func_name:
            func_value = this_month_data_end()
        elif 'today_datetime' in func_name:
            func_value = today_datetime()
        elif 'gen_sign' in func_name:
            func_value = gen_sign(func_param)
        # elif 'code_to_id' in func_name:
        #     func_value = code_to_id(func_param)
        # elif 'id_to_code' in func_name:
        #     func_value = id_to_code(func_param)

        return func_value
    except Exception as e:
        logging.error('解析函数失败%s' % e)


