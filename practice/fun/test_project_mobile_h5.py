#!/usr/bin/python
# -*- coding: UTF-8 -*-
import constants as cs
import core.request as request
from common import tools as time
from common.tools import log as log

logging = log.get_log()


class TestProjectApi():
    def setup_class(self):
        pass

    # @pytest.mark.parametrize("path1", [" ", "/intro"])
    # def test_project_detail(self,gen_peoject, path1):
    #     #(project_id, project_code) = gen_peoject()
    #     path = "/h5/api/project/v1/"
    #     # code = transfer.id_to_code(gen_project)
    #     # print(cs.URL_MOBILE+"/h5/api/project/v1/"+code)
    #     res = resquest.api("get", cs.URL_MOBILE + path + gen_peoject[1] + path1, data.yaml=None, headers=headers)
    #     # print(res)
    #     assert res['data.yaml']['projectId'] == gen_peoject[0]
    def test_project_detail(self, gen_project):
        # code = transfer.id_to_code(gen_project)
        # print(cs.URL_MOBILE+"/h5/api/project/v1/"+code)
        res = request.api("get", cs.URL_MOBILE + "/h5/api/project/v1/" + gen_project[1], data=None,
                          headers=cs.headers_mobile)
        # print(gen_project[0])
        assert res['data.yaml']['projectId'] == gen_project[0] and res['data.yaml']['title'] == cs.TITLE

    def test_project_intro(self, gen_project):
        # code = transfer.id_to_code(gen_project)
        # print(cs.URL_MOBILE+"/h5/api/project/v1/"+code)
        res = request.api("get", cs.URL_MOBILE + "/h5/api/project/v1/" + gen_project[1] + "/intro", data=None,
                          headers=cs.headers_mobile)
        # print(gen_project[0])
        assert res['data.yaml']['projectId'] == gen_project[0] and res['data.yaml']['title'] == cs.TITLE

    def test_project_ranking_list(self, gen_project):
        # code = transfer.id_to_code(gen_project)
        # print(cs.URL_MOBILE+"/h5/api/project/v1/"+code)
        res = request.api("get", cs.URL_MOBILE + "/h5/api/project/v1/" + gen_project[1] + "/rankingList?offset=0",
                          data=None, headers=cs.headers_mobile)
        # print(gen_project[0])
        assert res['data.yaml']['myranking']["uid"] == cs.UID[0]

    def test_project_stat(self, gen_project):
        # code = transfer.id_to_code(gen_project)
        # print(cs.URL_MOBILE+"/h5/api/project/v1/"+code)
        res = request.api("get", cs.URL_MOBILE + "/h5/api/project/v1/" + gen_project[1] + "/stat",
                          data=None, headers=cs.headers_mobile)
        # print(gen_project[0])
        assert res['data.yaml']['totalTaskCount'] == gen_project[4]

    def test_project_checkin_status(self, gen_project):
        res = request.api("get", cs.URL_MOBILE + "/h5/api/checkin/v1/checkinStatus?beginDate=" + time.this_month_data()[
            0] + "&endDate=" + time.this_month_data()[1] + "&checkinCode=" + gen_project[3],
                          data=None, headers=cs.headers_mobile)
        assert res['data.yaml']['checkinUserTask']['uid'] == cs.UID[0]

    def test_project_checkin_detail(self, gen_project):
        res = request.api("get",
                          cs.URL_MOBILE + "/h5/api/checkin/v1/detail?checkinCode=" + gen_project[3] + "&statDate=" +
                          time.today_datetime()[2],
                          data=None, headers=cs.headers_mobile)
        assert res['data.yaml']['checkinCode'] == gen_project[3]

    # /h5/api/checkin/v1/detail?checkinCode=KCCxbtmKiCY&statDate=20201209
    def teardown_class(self):
        pass
