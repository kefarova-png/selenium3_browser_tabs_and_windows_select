#  Импортируем необходимые библиотеки и модули
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#  Chrome. Создаём переменную для опций браузера
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver. Chrome (
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

#  Открываем вебдрайвером ссылку
base_url = 'https://demoqa.com/browser-windows'
driver.get(base_url)
driver.set_window_size(1080, 1080)
time.sleep(3)
print('Загрузилась первая вкладка первого окна')

#  Найдем и нажмем кнопку [Новая вкладка]
driver.find_element (By.XPATH,"//button[@id='tabButton']").click()  #  Открыли новую вкладку
print("Открыли вторую вкладку")
time.sleep(1)
driver.switch_to.window (driver.window_handles [1])  #  Перейдём во 2-ую вкладку 1-го окна
print('Переключились во вторую вкладку')
time.sleep(3)
driver.switch_to.window (driver.window_handles[0])  #  Перейдём в 1-ую вкладка 1-го окна
print('Переключились в первую вкладку')
time.sleep(5)

#  Найдем и нажмем кнопку [Новое окно]
driver.find_element (By.XPATH,"//button[@id='windowButton']").click()  #  Открыли новое окно
print("Открыли второе окно")
time.sleep(1)
driver.switch_to.window (driver.window_handles [2])  #  Перейдём во 2-е окно (по счету -- третья страничка)
print('Переключились во второе окно')
time.sleep(3)

#  Вернемся в 1-ое окно
driver.switch_to.window (driver.window_handles[1])  #  Перейдём во 2-ую вкладку 1-го окна
print('Переключились в первое окно, вкладка 2')
time.sleep(3)
driver.switch_to.window (driver.window_handles[0])  #  Перейдём в 1-ую вкладка 1-го окна
print('Переключились в первое окно, вкладка 1')
time.sleep(3)

#  Вернемся в 2-ое окно для его закрытия
driver.switch_to.window (driver.window_handles[2])  #  Перейдём во 2-ую вкладку 1-го окна
print('Переключились во второе окно для его закрытия')
time.sleep(3)
driver.close()  #  Закрываем второе окно

#  Вернемся в первое окно для закрытия 1-ой и 2-ой вкладок
driver.switch_to.window (driver.window_handles[0])  #  Перейдём в 1-ую вкладку 1-го окна
print('Переключились во вкладку 1 первого окна для её закрытия')
time.sleep(3)
driver.close()  #  Закрываем в первом окне вкладку 2
driver.switch_to.window (driver.window_handles[0])  #  Перейдём в оставшуюся уже 1-ую вкладку (бывшую 2-ую) 1-го окна
print('Переключились в единственную вкладку первого окна для её закрытия')
time.sleep(3)
driver.close()  #  Закрываем в первом окне вкладку 1
