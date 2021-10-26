import project2a as p2
import pytest

def test_odds_api(capfd):
	p2.get_current_matches()
	out, err = capfd.readouterr()
	assert err == "Odds API Call Succeeded\n"
