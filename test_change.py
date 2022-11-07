from change import ChangeItForMe


class TestChange:

    def test_calculate(self):
        changer = ChangeItForMe()

        assert changer.calculate(100) == [0, 0, 0, 0, 1]
        assert changer.calculate(25) == [0, 0, 0, 1, 0]
        assert changer.calculate(10) == [0, 0, 1, 0, 0]
        assert changer.calculate(5) == [0, 1, 0, 0, 0]
        assert changer.calculate(1) == [1, 0, 0, 0, 0]

        assert changer.calculate(141) == [1, 1, 1, 1, 1]
        assert changer.calculate(99) == [4, 0, 2, 3, 0]
        assert changer.calculate(207) == [2, 1, 0, 0, 2]

    def test_transact(self):
        changer = ChangeItForMe()

        assert changer.transact(20, 100) == [0, 1, 0, 3, 0]
        assert changer.transact(56, 100) == [4, 1, 1, 1, 0]
