import csv
import os
from project import load_mapping, make_mapping, delete_temp


def test_load_mapping():

    with open("mapping.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([1, 2])
        writer.writerow([3, 4])

    result = load_mapping()

    assert result == [(1, 2), (3, 4)]


def test_make_mapping(monkeypatch):

    inputs = iter(["1-2", "3-4", "done"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = make_mapping()

    assert result == [(1, 2), (3, 4)]


def test_delete_temp():

    open("_temp_page_1.jpg", "w").close()
    open("_temp_page_2.jpg", "w").close()

    delete_temp()

    files = os.listdir()

    assert "_temp_page_1.jpg" not in files
    assert "_temp_page_2.jpg" not in files
