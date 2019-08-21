import pytest

def pytest_runtest_setup():
    """Funkcja uruchamiana przed każdym przypadkiem testowym
     nie ważne czy test zostął wykonany, czy byl pominiety; wykonał się poprawnie lub by się nie powiódł

     Rzadko używane, bo służą do zaawansowanego konfigurowania i odpalania środowiska testowego - wszystkie hooki(haki)
     sa opisane w dokumentacji pytest

     Z reguły używany jest do trzymania fixture używanych w wielu plikach testowych"""
    print("Starting the test")


# Wszystkie zadeklarowane tutaj fixture są dostepne dla wszsytkich testw niezależnie od ich lokalizacji

@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Zabiera możliwosc wykonywania requestów z poziomu testów"""
    monkeypatch.delattr('requests.sessions.Session.request')

@pytest.fixture
def backend(tmpdir):
    temp_file = tmpdir.join('test.txt') #tworzenie pliku
    temp_file.write('') # inicjalizacja pliku - zapisywanie pustej linii
    return temp_file
