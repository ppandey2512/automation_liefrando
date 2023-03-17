import pytest
import undetected_chromedriver as uc



class MyUC(uc.Chrome):
    def __del__(self):
        try:
            self.service.process.kill()
        except:  # noqa
            pass
        # self.quit()

@pytest.fixture()
def setup():
    driver = MyUC() 
    return driver