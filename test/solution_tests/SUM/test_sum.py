from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
    
    def test_for_positive(self):
        assert sum_solution.compute(3,5)== 8
        assert sum_solution.compute(999,999)== 1998
        
    def test_for_zero(self):
        assert sum_solution.compute(0,0)==0