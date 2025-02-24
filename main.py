from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# Caminho para o WebDriver
# service_home= Service(r"C:\Users\Intel\Downloads\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_home)
service = Service(r"C:\Users\pietro.abrahamian\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# URL do site
driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")


wait = WebDriverWait(driver, 10) #salva na variavel WAIT a ação de esperar 10s
botao_login = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn-standard call-to-action']"))) #indica que tem q usar o tempo de espera até o elemento aparecer na tela, ai sim localiar ele 
botao_login.click() # clica no botao que foi armazena na variavel acima

email = wait.until(EC.visibility_of_element_located((By.ID, "email"))) 
email.send_keys("pietroabrahamian2021@gmail.com")
# email.send_keys("pietroabrahamian2018@gmail.com")
email.send_keys(Keys.RETURN)

senha = wait.until(EC.visibility_of_element_located((By.ID, "password")))
senha.send_keys("2007Pietr@")
senha.send_keys(Keys.RETURN)

try:
    seguranca = driver.find_element(By.ID, "secureBtn")
    seguranca.click()
except Exception as e:
    codigo = driver.find_element(By.ID, "btnSendCode")
    codigo.click()

input("Faça o que precisa agora e dps pressione enter para voltar a funcionar")

dme = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ut-tile-content-graphic-info")))
dme.click()

dme_melhoria = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Upgrades']")))
dme_melhoria.click()

dme_bronze_diaria = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Daily Bronze Upgrade']")))
dme_bronze_diaria.click()


def montagem_automatica_bronze_diaria():
    #cria o template para criar o time
    template_SBC = wait.until(EC.visibility_of_element_located((By.ID, "edit-template")))
    template_SBC.click()
    template_add = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Add']")))
    template_add.click()
    untradeables_only = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Untradeables Only']")))
    untradeables_only.click()
    sbc_storage = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='SBC Storage']")))
    sbc_storage.click()
    position_players = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Ignore Players Positions']")))
    position_players.click()
    quality = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Quality']")))
    quality.click()
    quality_bronze = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='Bronze']")))
    quality_bronze.click()
    template_save = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Save']")))
    template_save.click()
    #volta para a pagina inicial de Melhoria
    voltar = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ut-navigation-button-control")))
    voltar.click()
    # entra de novo na melhoria de bronze diaria
    dme_bronze_diaria = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Daily Bronze Upgrade']")))
    dme_bronze_diaria.click()
    # usa o template já feito
    use_template = wait.until(EC.visibility_of_element_located((By.ID, "use-template")))
    use_template.click()
    time.sleep(5)
    submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Submit']")))
    submit.click()
    claim = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Claim Rewards']")))
    claim.click()
    

def build_bronze_diaria():
    # entra de novo na melhoria de bronze diaria
    dme_bronze_diaria = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Daily Bronze Upgrade']")))
    dme_bronze_diaria.click()
    # usa o template já feito
    use_template = wait.until(EC.visibility_of_element_located((By.ID, "use-template")))
    use_template.click()
    time.sleep(5)
    submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Submit']")))
    submit.click()
    claim = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Claim Rewards']")))
    claim.click()

# def bronze_diario():
#     carta_vazia = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "small player item ut-item-loading empty has-chemistry-breakdown droppable")))
#     carta_vazia.click()
#     add_player = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Add Player']")))
#     add_player.click()
#     quality = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Quality']")))
#     quality.click()
#     quality_bronze = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='Bronze']")))
#     quality_bronze.click()
#     x = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "flat ut-search-filter-control--row-button")))
#     x.click()
#     search = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Search']")))
#     search.click()
#     add = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ut-image-button-control btnAction add")))
#     add.click()
#     submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Submit']")))
#     submit.click()

# bronze_diario()
try:
    montagem_automatica_bronze_diaria()
    build_bronze_diaria()
    build_bronze_diaria()
except Exception as e:
    
    def montagem_automatica_silver_diaria():
        dme_silver_diaria = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Daily Silver Upgrade']")))
        dme_silver_diaria.click()
        #cria o template para criar o time
        template_SBC = wait.until(EC.visibility_of_element_located((By.ID, "edit-template")))
        template_SBC.click()
        template_add = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Add']")))
        template_add.click()
        untradeables_only = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Untradeables Only']")))
        untradeables_only.click()
        sbc_storage = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='SBC Storage']")))
        sbc_storage.click()
        position_players = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Ignore Players Positions']")))
        position_players.click()
        quality = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Quality']")))
        quality.click()
        quality_silver = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='Silver']")))
        quality_silver.click()
        template_save = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Save']")))
        template_save.click()
        #volta para a pagina inicial de Melhoria
        voltar = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ut-navigation-button-control")))
        voltar.click()
        # entra de novo na melhoria de silver diaria
        dme_silver_diaria = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Daily Silver Upgrade']")))
        dme_silver_diaria.click()
        # usa o template já feito
        use_template = wait.until(EC.visibility_of_element_located((By.ID, "use-template")))
        use_template.click()
        time.sleep(5)
        submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Submit']")))
        submit.click()
        claim = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Claim Rewards']")))
        claim.click()
        

    def build_silver_diaria():
        # entra de novo na melhoria de silver diaria
        dme_silver_diaria = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Daily Silver Upgrade']")))
        dme_silver_diaria.click()
        # usa o template já feito
        use_template = wait.until(EC.visibility_of_element_located((By.ID, "use-template")))
        use_template.click()
        time.sleep(5)
        submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Submit']")))
        submit.click()
        claim = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Claim Rewards']")))
        claim.click()


    try:
        montagem_automatica_silver_diaria()
        build_silver_diaria()
        build_silver_diaria()
    except Exception as e:
        def montagem_automatica_gold_diaria():
            # Entra no DME - Ouro Diaria
            dme_gold_diaria= wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Daily Gold Upgrade']")))
            dme_gold_diaria.click()

            # começa o desafio bronze
            start_chellenge = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Start Challenge']")))
            start_chellenge.click()

            #cria o template para criar o time bronze
            template_SBC = wait.until(EC.visibility_of_element_located((By.ID, "edit-template")))
            template_SBC.click()
            template_add = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Add']")))
            template_add.click()
            untradeables_only = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Untradeables Only']")))
            untradeables_only.click()
            sbc_storage = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='SBC Storage']")))
            sbc_storage.click()
            position_players = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Ignore Players Positions']")))
            position_players.click()
            quality = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Quality']")))
            quality.click()
            quality_silver = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='Bronze']")))
            quality_silver.click()
            template_save = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Save']")))
            template_save.click()

            #volta para a pagina de escolher o chellenge
            voltar = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ut-navigation-button-control")))
            voltar.click()

            # entra de novo na melhoria de silver diaria
            start_chellenge.click()

            # usa o template já feito
            use_template = wait.until(EC.visibility_of_element_located((By.ID, "use-template")))
            use_template.click()

            #clica em submit para terminar a criação do time
            time.sleep(5)
            submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Submit']")))
            submit.click()

            #recolhe a recompensa
            claim = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Claim Rewards']")))
            claim.click()


            # prata

            # inicia o chellenge prata
            start_chellenge.click()

            #cria o template para criar o time prata
            template_SBC = wait.until(EC.visibility_of_element_located((By.ID, "edit-template")))
            template_SBC.click()
            template_add = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Add']")))
            template_add.click()
            untradeables_only = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Untradeables Only']")))
            untradeables_only.click()
            sbc_storage = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='SBC Storage']")))
            sbc_storage.click()
            position_players = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Ignore Players Positions']")))
            position_players.click()
            quality = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Quality']")))
            quality.click()
            quality_silver = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='Silver']")))
            quality_silver.click()
            template_save = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Save']")))
            template_save.click()

            #volta para a pagina de escolha do chellenge
            voltar.click()
            
            # entra de novo na melhoria de silver diaria
            start_chellenge.click()

            # usa o template já feito
            use_template = wait.until(EC.visibility_of_element_located((By.ID, "use-template")))
            use_template.click()

            #clica em submit para terminar a criação do time
            time.sleep(5)
            submit.click()

            #recolhe a recompensa
            claim.click()
            time.sleep(3)
            claim.click()




        def build_gold_diaria():

            # entra de novo na melhoria de gold diaria
            dme_gold_diaria = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Daily Gold Upgrade']")))
            dme_gold_diaria.click()

            # começa o desafio bronze
            start_chellenge = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Start Challenge']")))
            start_chellenge.click()

            # usa o template já feito
            use_template = wait.until(EC.visibility_of_element_located((By.ID, "use-template")))
            use_template.click()

            #clica em submit para terminar a criação do time
            time.sleep(5)
            submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Submit']")))
            submit.click()
            claim.click()

            # entra de novo na melhoria de silver diaria
            dme_gold_diaria.click()
            # usa o template já feito
            use_template.click()
            time.sleep(5)
            submit.click()

            #recolhe a recompensa
            claim = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Claim Rewards']")))
            claim.click()

            #volta para a pagina de escolher o chellenge
            voltar = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ut-navigation-button-control")))
            voltar.click()

            # prata

            # inicia o chellenge prata
            start_chellenge.click()

            #usa o template criado
            use_template.click()

            #clica em submit para terminar a criação do time
            time.sleep(5)
            submit.click()


            #recolhe a recompensa
            claim.click()
            time.sleep(3)
            claim.click()

        montagem_automatica_gold_diaria()
        build_gold_diaria()
        build_gold_diaria()
        build_gold_diaria()
        



time.sleep(3600)

