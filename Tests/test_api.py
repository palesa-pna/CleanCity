import requests

BASE_URL = "https://cleancityqa.netlify.app/"

def test_homepage_loads():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_page_contains_clean_city():
    assert "Clean City" in requests.get(BASE_URL).text

def test_schedule_button_or_text_exists():
    html = requests.get(BASE_URL).text
    assert "Schedule" in html or "Book Pickup" in html
