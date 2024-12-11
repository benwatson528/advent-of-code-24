from main.day11.plutonian_pebbles import solve

parse_input = lambda s: [int(x) for x in s.split()]


def test_p1_simple():
    assert solve(parse_input("125 17"), 25) == 55312


def test_p1_real():
    assert solve(parse_input("17639 47 3858 0 470624 9467423 5 188"), 25) == 203228


def test_p2_real():
    assert solve(parse_input("17639 47 3858 0 470624 9467423 5 188"), 75) == 240884656550923
