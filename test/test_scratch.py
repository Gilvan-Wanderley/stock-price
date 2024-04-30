from src.scratch.scratch import companies_SandP500

class TestScratchCompaniesSandP500:
    def setup_method(self) -> None:
        self.df = companies_SandP500()
        self.columns = ['Symbol', 'Security', 'GICS Sector',
                'GICS Sub-Industry', 'Headquarters Location',
                'Date added', 'CIK', 'Founded']

    def test_row_companies_SandP500(self):
        assert len(self.df) == 503

    def test_columns_companies_SandP500(self): 
        assert len(self.df.columns) == 8

    def test_columns_name_companies_SandP500(self): 
        for label in self.columns:
            assert label in self.df.columns
