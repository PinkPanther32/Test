import price_info

def test_total_cost_shopping():
    
    expected_result = 46.75
    
    result = price_info.total_cost_shopping()
    
    assert expected_result == result
    
def test_cost_of_fruits():
    
    expected_result = 12.0
    
    result = price_info.cost_of_fruits('apple', 10)
    
    assert result == expected_result