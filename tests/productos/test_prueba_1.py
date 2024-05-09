import pytest
@pytest.mark.marca1
def test_prueba():
  assert 1==1

@pytest.mark.marca1
def test_prueba2():
  assert 1==1

#Creo un fixture
@pytest.fixture(scope="session")
def fixture_1():
  print("Desde mi fixture antes")
  yield 1
  print("Desde mi fixture despues")

@pytest.mark.marca1
def test_prueba3(fixture_1):
  print("Desde mi test")
  variable = fixture_1
  assert variable==1

@pytest.mark.marca1
def test_prueba4(fixture_1):
  print("Desde mi test")
  variable = fixture_1
