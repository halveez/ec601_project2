import project2a as p2


def test_above_range(capfd):
    p2.input = lambda: "10000"
    p2.fighter_information_request()
    out, err = capfd.readouterr()

    assert err == "Invalid user input\n"


def test_below_range(capfd):
    p2.input = lambda: "0"
    p2.fighter_information_request()
    out, err = capfd.readouterr()

    assert err == "Invalid user input\n"

def test_within_range(capfd):
    p2.input = lambda: "1"
    p2.fighter_information_request()
    out, err = capfd.readouterr()

   assert out != "Invalid user input\n"

# Followed these guides for capturing error printing, simulating user inputs, etc.
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
# https://stackoverflow.com/questions/20507601/writing-a-pytest-function-for-checking-the-output-on-console-stdout
# https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call