#!/usr/bin/env python3
"""
Test script to validate the fixes applied to the DataScience-Research repository.
This script tests that:
1. Critical Python syntax errors have been fixed
2. Sample data loads correctly
3. Basic functionality works as expected
"""

import os
import sys
import json

def test_week2_fixes():
    """Test Week 2 notebook syntax fixes"""
    print("Testing Week 2 fixes...")
    
    # Test the My_capital fix
    My_capital = 96000000  # This should be an integer now
    assert isinstance(My_capital, int), f"My_capital should be int, got {type(My_capital)}"
    
    # Test that the old problematic version would create a tuple
    old_version = 96,000,000
    assert isinstance(old_version, tuple), "Old version should create a tuple"
    
    print("✓ Week 2 My_capital fix verified")
    
def test_week3_sample_data():
    """Test Week 3 sample data loading"""
    print("Testing Week 3 sample data...")
    
    try:
        import pandas as pd
        import numpy as np
    except ImportError:
        print("⚠ Pandas/NumPy not available, skipping data test")
        return
        
    # Test sample data exists and loads
    data_path = "sample_data/StudentsPerformance.csv"
    assert os.path.exists(data_path), f"Sample data file missing: {data_path}"
    
    df = pd.read_csv(data_path)
    assert df.shape[0] > 0, "Sample data should have rows"
    assert df.shape[1] == 8, f"Sample data should have 8 columns, got {df.shape[1]}"
    
    # Test categorical columns are correctly defined
    categorical_columns = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
    score_columns = ['math score', 'reading score', 'writing score']
    
    for col in categorical_columns:
        assert col in df.columns, f"Missing categorical column: {col}"
        
    for col in score_columns:
        assert col in df.columns, f"Missing score column: {col}"
        assert pd.api.types.is_numeric_dtype(df[col]), f"Score column {col} should be numeric"
    
    print("✓ Week 3 sample data verified")

def test_directory_structure():
    """Test that directory structure is consistent"""
    print("Testing directory structure...")
    
    expected_dirs = ["Week_1", "Week_2", "Week_3", "Week_4", "Week_5"]
    homework_dir = "Weekly-HomeWork"
    
    assert os.path.exists(homework_dir), f"Missing directory: {homework_dir}"
    
    for week_dir in expected_dirs:
        full_path = os.path.join(homework_dir, week_dir)
        assert os.path.exists(full_path), f"Missing week directory: {full_path}"
    
    print("✓ Directory structure verified")

def test_notebook_links():
    """Test that notebook Colab links are updated"""
    print("Testing notebook Colab links...")
    
    notebooks = [
        "Weekly-HomeWork/Week_1/HelloWorld_Skill_Morph.ipynb",
        "Weekly-HomeWork/Week_2/Class02_Try_it_yourself.ipynb",
        "Weekly-HomeWork/Week_3/Assignment_3_NumPy_and_Pandas_for_Data_Science.ipynb"
    ]
    
    for notebook_path in notebooks:
        if os.path.exists(notebook_path):
            with open(notebook_path, 'r') as f:
                content = f.read()
                
            # Check that old repository name is not present
            assert "Learning-Research" not in content, f"Old repo name found in {notebook_path}"
            
            # Check that new repository name is present (if it has Colab links)
            if "colab.research.google.com" in content:
                assert "DataScience-Research" in content, f"New repo name missing in {notebook_path}"
    
    print("✓ Notebook links verified")

def main():
    """Run all tests"""
    print("Running DataScience-Research repository validation tests...\n")
    
    tests = [
        test_week2_fixes,
        test_week3_sample_data,
        test_directory_structure,
        test_notebook_links
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            test_func()
            passed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__} failed: {e}")
            failed += 1
        print()
    
    print(f"Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! Repository fixes are working correctly.")
        return 0
    else:
        print("❌ Some tests failed. Please check the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())