import os

def pytest_sessionstart(session):
    worker = os.environ.get('PYTEST_XDIST_WORKER', 'master')
    session.config.log_file = open(f"worker_{worker}_log.txt", "w")
    session.config.log_file.write(f"Session starts for worker: {worker}\n")

def pytest_runtest_logstart(nodeid):
    worker = os.environ.get('PYTEST_XDIST_WORKER', 'master')
    with open(f"worker_{worker}_log.txt", "a") as log_file:
        log_file.write(f"Starting test: {nodeid} on worker: {worker}\n")

def pytest_sessionfinish(session):
    worker = os.environ.get('PYTEST_XDIST_WORKER', 'master')
    with open(f"worker_{worker}_log.txt", "a") as log_file:
        log_file.write(f"Session ends for worker: {worker}\n")
    session.config.log_file.close()

