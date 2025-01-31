import pytest
import json
import os
from unittest.mock import patch, mock_open
from cli.ai_models import (
    load_models_api,
    update_models_api_json,
    api_key_model_selection,
    remove_model,
    configure_model,
    generate_output,
    create_json_file,
)

TEST_FILE = "test_models_api.json"


def setup_module(module):
    """Setup a test JSON file before running tests."""
    with open(TEST_FILE, "w") as f:
        json.dump({"gemini-1.5-flash": "test_api_key"}, f)


def teardown_module(module):
    """Remove the test JSON file after tests complete."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


@patch("ai_models_management.FILE_NAME", TEST_FILE)
def test_load_models_api():
    """Test loading API configurations."""
    data = load_models_api()
    assert data == {"gemini-1.5-flash": "test_api_key"}


@patch("ai_models_management.FILE_NAME", TEST_FILE)
def test_update_models_api_json():
    """Test updating API configurations."""
    update_models_api_json({"gemini-1.5-flash": "new_api_key"})
    with open(TEST_FILE, "r") as f:
        data = json.load(f)
    assert data["gemini-1.5-flash"] == "new_api_key"


@patch("ai_models_management.FILE_NAME", TEST_FILE)
def test_api_key_model_selection():
    """Test retrieving API key for a given model."""
    assert api_key_model_selection("gemini-1.5-flash") == "test_api_key"
    with pytest.raises(ValueError):
        api_key_model_selection("non_existent_model")


@patch("ai_models_management.FILE_NAME", TEST_FILE)
def test_remove_model():
    """Test removing a model from the configuration."""
    configure_model("test_model", "test_key")
    remove_model("test_model")
    with open(TEST_FILE, "r") as f:
        data = json.load(f)
    assert "test_model" not in data
    with pytest.raises(ValueError):
        remove_model("non_existent_model")


@patch("ai_models_management.FILE_NAME", TEST_FILE)
def test_configure_model():
    """Test adding or updating a model configuration."""
    configure_model("gemini-1.5-interactive", "new_test_key")
    with open(TEST_FILE, "r") as f:
        data = json.load(f)
    assert data["gemini-1.5-interactive"] == "new_test_key"


@patch("ai_models_management.FILE_NAME", TEST_FILE)
def test_create_json_file():
    """Test creating a new JSON file with default values."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    create_json_file()
    assert os.path.exists(TEST_FILE)
    with open(TEST_FILE, "r") as f:
        data = json.load(f)
    assert "gemini-1.5-flash" in data and data["gemini-1.5-flash"] is None


@patch("ai_models_management.genai.GenerativeModel")
@patch("ai_models_management.api_key_model_selection", return_value="test_api_key")
def test_generate_output(mock_api_key_selection, mock_model_class):
    """Test generating AI response."""
    mock_model_instance = mock_model_class.return_value
    mock_model_instance.generate_content.return_value.text = "Test response"

    response = generate_output("gemini-1.5-flash", "Hello AI")

    assert response == "Test response"
    mock_api_key_selection.assert_called_once_with("gemini-1.5-flash")
    mock_model_class.assert_called_once_with("gemini-1.5-flash")
