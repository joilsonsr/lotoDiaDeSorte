import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def apostarOnline(apostas):
    driver = webdriver.Firefox()
    driver.get("https://www.loteriasonline.caixa.gov.br/silce-web/#/home")
    time.sleep(1)
    clickOp = driver.find_element(By.ID, 'botaosim')
    clickOp.click()
    time.sleep(1)
    driver.get("https://www.loteriasonline.caixa.gov.br/silce-web/#/dia-de-sorte")
    time.sleep(1)
    selMeses  = list()
    for i in apostas:
        if not selMeses:
            selMeses=[n for n in range(1,13)]
        print(i)
        driver.execute_script(
        f'angular.element(document.getElementById("container-volante")).scope().vm.numerosSelecionados={str(i)};')
        time.sleep(2)
        mesSelecionado = choice(selMeses)
        print(f'mes selecionado = {mesSelecionado}')
        driver.execute_script(f'angular.element(document.getElementById("container-volante")).scope().vm.mesSelecionado={mesSelecionado}')
        time.sleep(2)
        selMeses.remove(mesSelecionado)
        driver.execute_script(
            'angular.element(document.getElementById("container-volante")).scope().vm.incluirAposta();')