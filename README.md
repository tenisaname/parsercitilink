# Парсер магазин Ситилинк
Данный проект поможет вам выгрузить данные (название и цену)

Для этого замените переменную url
```python
url = "https://www.citilink.ru/catalog/noutbuki//"
```
Также замените ссылку на сhromedriver
```python
driver = webdriver.Chrome(service=ChromeService(executable_path='C:\\Users\\user\\Desktop\\ParserCitilink\\chromedriver.exe'),options=options)
```
И option
```python
options.add_argument(r"--user-data-dir=C:\\path\\to\\chrome\\user\\data")
```
