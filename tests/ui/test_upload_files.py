import os
from pathlib import Path

import pytest


@pytest.mark.ui
class TestUploadFiles:
    PROJECT_ROOT = Path(__file__).resolve().parents[2]

    pdf_path = (
            PROJECT_ROOT / "src" / "test_data" / "Automation Testing Practice.pdf"
    )
    txt_path = (
            PROJECT_ROOT / "src" / "test_data" / "Test_file_1.txt")
    md_path = (
            PROJECT_ROOT / "src" / "test_data" / "DATA_DIR}/Test_file_2.md")

    def test_upload_single_file(self, web_element_practice_page):
        (web_element_practice_page
         .open_practice_page()
         .select_file_to_upload(self.pdf_path)
         .assert_file_selected("Automation Testing Practice.pdf"))
