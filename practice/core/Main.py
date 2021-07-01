import os
import shutil
import subprocess
import pytest
import logging
from common.unit.initializeYamlFile import ini_yaml
from common.utils.logs import LogConfig
from common.script.writeCase import write_case
from common.script.writeCaseScript import write_caseScript
from common.utils.formatChange import formatChange
from common.utils.emailModel.runSendEmail import sendEailMock

root_path = os.path.split(os.path.realpath(__file__))[0]
xml_report_path = root_path + "\\report\\xml"
detail_report_path = root_path + "\\report\\detail_report"
summary_report_path = root_path + "\\report\\summary_report\\summary_report.html"
runConf_path = os.path.join(root_path, "config")

# 获取运行配置信息
runConfig_dict = ini_yaml(runConf_path, "runConfig")

case_level = runConfig_dict["case_level"]
if not case_level:
    case_level = ["blocker", "critical", "normal", "minor", "trivial"]
else:
    pass

product_version = runConfig_dict["product_version"]
if not product_version:
    product_version = []
else:
    pass

isRun_switch = runConfig_dict["isRun_switch"]
run_interval = runConfig_dict["run_interval"]
writeCase_switch = runConfig_dict["writeCase_switch"]

ProjectAndFunction_path = runConfig_dict["ProjectAndFunction_path"]
if not ProjectAndFunction_path:
    ProjectAndFunction_path = ""
else:
    pass

scan_path = runConfig_dict["scan_path"]
if not scan_path:
    scan_path = ""
else:
    pass

runTest_switch = runConfig_dict["runTest_switch"]
reruns = str(runConfig_dict["reruns"])
reruns_delay = str(runConfig_dict["reruns_delay"])
log = runConfig_dict["log"]


def batch(CMD):
    output, errors = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    outs = output.decode("utf-8")
    return outs


if __name__ == "__main__":
    try:
        LogConfig(root_path, log)

        if writeCase_switch == 1:
            # 根据har_path里的文件，自动生成用例文件yml和用例执行文件py，若已存在相关文件，则不再创建
            write_case(root_path, ProjectAndFunction_path)

        elif writeCase_switch == 2:
            write_caseScript(root_path, scan_path)

        else:
            logging.info("="*20+"本次测试自动生成测试用例功能已关闭！"+"="*20+"\n")

        if runTest_switch == 1:
            # 清空目录和文件
            email_target_dir = root_path + "/report/zip_report"  # 压缩文件保存路径
            shutil.rmtree(email_target_dir)
            if os.path.exists(summary_report_path):
                os.remove(summary_report_path)
            else:
                pass
            os.mkdir(email_target_dir)

            args = ["-k", runConfig_dict["Project"], "-m", runConfig_dict["markers"], "--maxfail=%s" % runConfig_dict["maxfail"],
                    "--durations=%s" % runConfig_dict["slowestNum"], "--reruns", reruns, "--reruns-delay", reruns_delay,
                    "--alluredir", xml_report_path, "--html=%s" % summary_report_path]

            test_result = pytest.main(args)   # 全部通过，返回0；有失败或者错误，则返回1

            cmd = "allure generate %s -o %s --clean" % (xml_report_path, detail_report_path)
            reportResult = batch(cmd)
            logging.debug("生成html的报告结果为：{}".format(reportResult))

            # 发送report到邮件
            emailFunction = runConfig_dict["emailSwitch"]
            if emailFunction == 1:

                if test_result == 0:
                    ReportResult = "测试通过！"
                else:
                    ReportResult = "测试不通过！"

                # 将字符中的反斜杠转成正斜杠
                fileUrl_PATH = root_path.replace("\\", "/")
                logging.debug("基础路径的反斜杠转成正斜杠为：{}".format(fileUrl_PATH))

                fileUrl = "file:///{}/report/summary_report/summary_report.html".format(fileUrl_PATH)
                logging.info("html测试报告的url为：{}".format(fileUrl))
                save_fn = r"{}\report\zip_report\summary_report.png".format(root_path)
                logging.debug("转成图片报告后保存的目标路径为：{}".format(save_fn))
                formatChange_obj = formatChange()
                formatChange_obj.html_to_image(fileUrl, save_fn)

                email_folder_dir = root_path + "/report/detail_report"  # 待压缩文件夹
                logging.debug("待压缩文件夹为：{}".format(email_folder_dir))
                sendEailMock_obj = sendEailMock()
                sendEailMock_obj.send_email(email_folder_dir, email_target_dir, runConfig_dict, ReportResult, save_fn)

            else:
                logging.info("="*20+"本次测试的邮件功能已关闭！"+"="*20+"\n")

        else:
            logging.info("="*20+"本次运行测试开关已关闭！"+"="*20+"\n")
    except Exception as err:
        logging.error("本次测试有异常为：{}".format(err))