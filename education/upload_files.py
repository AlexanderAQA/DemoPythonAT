from pathlib import Path
from playwright.sync_api import Page, expect


UPLOAD_URL = "http://127.0.0.1:8000/upload"


def test_upload_single_file(page: Page, tmp_path: Path):
    # Подготавливаем тестовый файл
    file_path = tmp_path / "document.txt"
    file_path.write_text("Test file content", encoding="utf-8")

    # Открываем страницу загрузки
    page.goto(UPLOAD_URL)

    # Выбираем один файл
    file_input = page.locator('input[type="file"]')
    file_input.set_input_files(str(file_path))

    # Проверяем, что выбран правильный файл
    expect(file_input).to_have_value("C:\\fakepath\\document.txt")

    # Проверяем отображение имени файла в интерфейсе
    expect(page.get_by_text("document.txt")).to_be_visible()

    # Отправляем файл на сервер
    page.get_by_role("button", name="Загрузить").click()

    # Проверяем результат загрузки
    expect(page.get_by_text("Файл успешно загружен")).to_be_visible()


def test_upload_multiple_files(page: Page, tmp_path: Path):
    # Подготавливаем несколько файлов
    file_paths = [
        tmp_path / "document1.txt",
        tmp_path / "document2.txt",
        tmp_path / "document3.txt",
    ]

    for index, file_path in enumerate(file_paths, start=1):
        file_path.write_text(
            f"Content of document {index}",
            encoding="utf-8",
        )

    page.goto(UPLOAD_URL)

    # Выбираем сразу несколько файлов
    file_input = page.locator('input[type="file"]')
    file_input.set_input_files([str(path) for path in file_paths])

    # Проверяем количество выбранных файлов
    selected_files = file_input.evaluate(
        "(input) => Array.from(input.files, file => file.name)"
    )

    assert selected_files == [
        "document1.txt",
        "document2.txt",
        "document3.txt",
    ]

    # Проверяем, что имена отображаются в интерфейсе
    for file_path in file_paths:
        expect(page.get_by_text(file_path.name)).to_be_visible()

    # Отправляем файлы на сервер
    page.get_by_role("button", name="Загрузить").click()

    # Проверяем успешный результат
    expect(page.get_by_text("Все файлы успешно загружены")).to_be_visible()
