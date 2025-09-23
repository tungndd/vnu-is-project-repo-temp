import pytest
from src.data_analysis.analysis import load_and_summarize_data

def test_load_and_summarize_data():
    # Giả sử có file data/test_data.csv với dữ liệu mẫu
    summary = load_and_summarize_data('data/test_data.csv')
    assert summary is not None  # Test cơ bản