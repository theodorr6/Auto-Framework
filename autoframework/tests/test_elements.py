from autoframework.poms.pages.elements_page import ElementsPage

def test_add_remove_elements(base_url, init_driver):
    """Test add and remove elements functionality."""
    elements_page = ElementsPage(base_url, init_driver)
    elements_page.open()

    print("[TEST] Act: add 2 elements")
    elements_page.add_elements(2)

    print("[TEST] Assert: verify 2 elements present")
    assert elements_page.count_delete_elements() == 2

    print("[TEST] Act: delete one element")
    elements_page.delete_element()

    print("[TEST] Assert: verify 1 element present")
    assert elements_page.count_delete_elements() == 1