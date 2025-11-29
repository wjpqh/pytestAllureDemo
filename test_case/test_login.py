import os
from pathlib import Path

import allure
import pytest
from loguru import logger

from common.DataUtils import DataUtils

# Get the current script's file path
current_file = Path(__file__)

# Get the file name without extension
file_name = current_file.stem

@allure.epic('测试')
class TestBatchDeclare:



    @allure.feature('测试')
    @pytest.mark.parametrize("story,title,param1,param2,data",DataUtils.read_excel('/test_case_file/test_case.xls','测试用例'))
    def test(self,story,title,param1,param2,data):
        allure.dynamic.story(story)
        allure.dynamic.title(title)
        allure.dynamic.description(title)
        with allure.step("第一步 操作1"):
            logger.info(f"测试{param1}")
            logger.info(f"测试{param2}")
            assert True

        with allure.step("第二步 操作2"):
            logger.info(f"测试2{data}")
            assert True







if __name__ == '__main__':

    pytest.main(['-sv',f"{file_name}.py",'--alluredir=./allure/allure_json','--clean-alluredir'])
    os.system("allure generate ./allure/allure_json -o ./allure/allure_html --clean")
