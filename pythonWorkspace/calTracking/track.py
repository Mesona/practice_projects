class CalorieTracker():
    import subprocess

    def __init__(f="history.txt"):
        self.file = f
        self.current_date = subprocess.getoutput(["date -I"])

    def add(calories, note):
        with open(self.file, "w+"):


def parser():
    import argparse

    parser = argparse.ArgumentParser(
            description=globals()["__doc__"],
            formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
            "file",
            default="history.txt",
            type=argparse.FileType("w+"),
            help="File to read from and write to",
    )

    parser.add_argument(
            "--count",
            default="today",
            help="Returns the amount of calories logged for the given day/week/month. Defaults to 'today'",
    )

    parser.add_argument(
            "--add",

    )

    #parser.add_argument(
    #        "add"



def main():
    args = parser().parge_args()
    # TODO: Build this out
    #return CalorieTracker
    ct = CalorieTracker(f="history.txt", calories, note)


if __name__ == "__main__":
    exit(main())
