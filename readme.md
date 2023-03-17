# Liefrando automation


### Installation Method

pip install -r requirements.txt


### Test API using pytest

python3 -m pytest -v -s api/test_successful_calls.py
<br />
python3 -m pytest -v -s api/test_failed_auth.py


### Test WEB using pytest

python3 -m pytest -v -s web/tests/test_cases.py
