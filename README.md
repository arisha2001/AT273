
запустить тесты Allure: pytest --alluredir=allure-results (с выводом логов: pytest --alluredir=allure-results -s)

запустить отчет Allure: allure serve allure-results

pytest -n 4 --alluredir=allure-results

очистить кэш:
rm -rf .pytest_cache                   
rm -rf allure-results