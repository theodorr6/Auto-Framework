import pytest

def test_login_success(login_logout):
    """Test successful login."""

    print("[TEST] Arrange: have a logged-in session via fixture")
    home_page = login_logout

    print("[TEST] Assert: verify secure area is present")
    assert home_page.verify_secure_area_presence()

@pytest.mark.parametrize("invalid_param, fixture_name",
    [
    ("password", "login_invalid_pass"),
    ("username", "login_invalid_user")
])
def test_login_negative(request, invalid_param, fixture_name):
    """Test login with invalid password."""
    login_page = request.getfixturevalue(fixture_name)

    print("[TEST] Act: check for invalid credentials error element")
    error_element = login_page.get_presence_of_invalid_credentials_error(invalid_param)

    print("[TEST] Assert: error element should be present")
    assert error_element