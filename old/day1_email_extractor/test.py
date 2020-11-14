from main import email_extractor

test_text = "This is a sample test with three emails dennis@gmail.com, " \
            "bob@gmail.com and jim@gmail.com"
test_text_results = ["dennis@gmail.com", "bob@gmail.com", "jim@gmail.com"]

negative_test = "this text contains no emails"
negative_test_results = []

test_case_1 = email_extractor(test_text)
assert test_case_1 == test_text_results, "Test case 1 failed"

test_case_2 = email_extractor(negative_test)
assert test_case_2 == negative_test_results, "Test case 2 failed"


