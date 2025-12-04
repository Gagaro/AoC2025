from pathlib import Path


class Runner:
    def __init__(self, input_path: Path):
        self.lines = input_path.read_text().splitlines()

    def run1(self):
        raise NotImplementedError()

    def run2(self):
        raise NotImplementedError()
