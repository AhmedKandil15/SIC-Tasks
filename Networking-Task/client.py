import requests

BASE_URL = "http://localhost:5000"


def test_get_temp():
    res = requests.get(f"{BASE_URL}/temp")
    print(res.json())


def test_update_temp(new_temp):
    res = requests.post(f"{BASE_URL}/temp", json={"temperature": new_temp})
    print(res.json())


if __name__ == "__main__":
    test_get_temp()

    test_update_temp(29)

    test_get_temp()
