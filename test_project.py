# # from project import add_transaction, view_summary, calculate_balance
# # import csv
# # import os
# # import pytest

# # @pytest.fixture
# # def setup_teardown():
# #     # Setup
# #     with open("test_transactions.csv", "w", newline="") as file:
# #         writer = csv.writer(file)
# #         writer.writerow(["2023-01-01", "100.00", "Food"])
# #         writer.writerow(["2023-01-02", "50.00", "Transport"])

# #     yield "test_transactions.csv"

# #     # Teardown
# #     os.remove("test_transactions.csv")

# # def test_calculate_balance():
# #     transactions = [
# #         ["2023-01-01", "100.00", "Food"],
# #         ["2023-01-02", "50.00", "Transport"]
# #     ]
# #     assert calculate_balance(transactions) == 150.00

# # def test_add_transaction(tmpdir):
# #     file_path = tmpdir.join("test_transactions.csv")
# #     with open(file_path, "w", newline="") as file:
# #         writer = csv.writer(file)
# #         writer.writerow(["2023-01-01", "100.00", "Food"])

# #     # This would need mocking input() in a real test
# #     # add_transaction() would be tested via integration tests

# # def test_view_summary(capsys, setup_teardown):
# #     view_summary()
# #     captured = capsys.readouterr()
# #     assert "Total transactions: 2" in captured.out
# #     assert "Total amount: $150.00" in captured.out



# from project import add_transaction, view_summary, calculate_balance
# import csv
# import os
# import pytest

# @pytest.fixture
# def setup_teardown():
#     # Setup - create test file
#     test_filename = "test_transactions.csv"
#     with open(test_filename, "w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["2023-01-01", "100.00", "Food"])
#         writer.writerow(["2023-01-02", "50.00", "Transport"])

#     yield test_filename  # This value gets passed to tests

#     # Teardown - remove test file
#     os.remove(test_filename)

# def test_calculate_balance():
#     transactions = [
#         ["2023-01-01", "100.00", "Food"],
#         ["2023-01-02", "50.00", "Transport"]
#     ]
#     assert calculate_balance(transactions) == 150.00

# def test_add_transaction(tmpdir):
#     test_file = tmpdir.join("test_add.csv")
#     add_transaction(filename=str(test_file))

#     with open(test_file, "r") as file:
#         transactions = list(csv.reader(file))
#     assert len(transactions) == 1  # After one addition

# def test_view_summary(capsys, setup_teardown):
#     view_summary(filename=setup_teardown)
#     captured = capsys.readouterr()
#     assert "Total transactions: 2" in captured.out
#     assert "Total amount: $150.00" in captured.out
#     assert "Food: $100.00" in captured.out
#     assert "Transport: $50.00" in captured.out




from project import add_transaction, view_summary, calculate_balance
import csv
import os
import pytest

@pytest.fixture
def setup_teardown():
    # Setup
    test_filename = "test_transactions.csv"
    with open(test_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["2023-01-01", "100.00", "Food"])
        writer.writerow(["2023-01-02", "50.00", "Transport"])

    yield test_filename

    # Teardown
    if os.path.exists(test_filename):
        os.remove(test_filename)

def test_calculate_balance():
    transactions = [
        ["2023-01-01", "100.00", "Food"],
        ["2023-01-02", "50.00", "Transport"]
    ]
    assert calculate_balance(transactions) == 150.00

def test_add_transaction(tmpdir):
    test_file = tmpdir.join("test_add.csv")
    # Test with direct parameters (no input() needed)
    result = add_transaction(
        amount=75.50,
        category="Test",
        date="2023-01-03",
        filename=str(test_file)
    )
    assert result is True

    # Verify the file was written correctly
    with open(test_file, "r") as file:
        transactions = list(csv.reader(file))
    assert len(transactions) == 1
    assert transactions[0] == ["2023-01-03", "75.5", "Test"]

def test_view_summary(capsys, setup_teardown):
    view_summary(filename=setup_teardown)
    captured = capsys.readouterr()
    assert "Total transactions: 2" in captured.out
    assert "Total amount: $150.00" in captured.out
    assert "Food: $100.00" in captured.out
