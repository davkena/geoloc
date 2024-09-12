import subprocess

def test_single_city_state():
    """Test valid city and state input."""
    result = subprocess.run(["python", "geoloc_util.py", "Madison, WI"], capture_output=True, text=True)
    assert "Lat:" in result.stdout
    assert "Lon:" in result.stdout
    assert "Madison" in result.stdout


def test_single_zip():
    """Test valid zip code input."""
    result = subprocess.run(["python", "geoloc_util.py", "90210"], capture_output=True, text=True)
    assert "Lat:" in result.stdout
    assert "Lon:" in result.stdout


def test_multiple_inputs():
    """Test multiple valid inputs of city/state and zip code."""
    result = subprocess.run(["python", "geoloc_util.py", "Madison, WI", "90210"], capture_output=True, text=True)
    assert "Lat:" in result.stdout
    assert "Lon:" in result.stdout

def test_invalid_zip_code():
    """Test an invalid zip code."""
    result = subprocess.run(["python", "geoloc_util.py", "00000"], capture_output=True, text=True)
    assert "Could not find location" in result.stdout


def test_invalid_city_state():
    """Test an invalid city/state combination."""
    result = subprocess.run(["python", "geoloc_util.py", "FakeCity, ZZ"], capture_output=True, text=True)
    assert "Could not find location" in result.stdout


def test_empty_input():
    """Test empty input."""
    result = subprocess.run(["python", "geoloc_util.py", ""], capture_output=True, text=True)
    assert "Invalid input format for location" in result.stdout


def test_missing_comma_in_city_state():
    """Test city and state input without a comma."""
    result = subprocess.run(["python", "geoloc_util.py", "NewYork NY"], capture_output=True, text=True)
    assert "Invalid input format for location" in result.stdout


def test_multiple_valid_and_invalid_inputs():
    """Test a mix of valid and invalid inputs."""
    result = subprocess.run(["python", "geoloc_util.py", "Madison, WI", "00000", "90210", "FakeCity, ZZ"], capture_output=True, text=True)
    assert "Lat:" in result.stdout  
    assert "Could not find location" in result.stdout  