import os
import pytest
import allure
import shutil
import subprocess
from common.unit.initialize_yaml import ini_yaml
from common.script.write_case_script import write_case_script

root_path = os.path.split(os.path.realpath(__file__))[0]
xml_report_path = root_path + "/report/xml"
detail_report_path = root_path + "/report/detail_report"
summary_report_path = root_path + "/report/summary_report/summary_report.html"
runConf_path = os.path.join(root_path, "config")
# 获取当前运行信息
runConfig_dict = ini_yaml(runConf_path, 'run_config')
# 获取是否自动执行生成但接口执行脚本
writeCase_switch = runConfig_dict["writeCase_switch"]
# 获取当前扫描测试用例路径
scan_path = runConfig_dict["scan_path"]
if not scan_path:
    scan_path = ""
else:
    pass

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

runTest_switch = runConfig_dict["runTest_switch"]
reruns = str(runConfig_dict["reruns"])
print(reruns)
reruns_delay = str(runConfig_dict["reruns_delay"])


def batch(CMD):
    output, errors = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    out = output.decode('utf-8')
    return out


if __name__ == '__main__':

    if writeCase_switch == 2:
        write_case_script(root_path, scan_path)
    if runTest_switch == 1:
        args = ["-k", runConfig_dict["Project"],
                "--alluredir", xml_report_path, "--html=%s" % summary_report_path]

        test_result = pytest.main(args)
        cmd = "allure generate %s -o %s --clean" % (xml_report_path, detail_report_path)
        reportResult = batch(cmd)
