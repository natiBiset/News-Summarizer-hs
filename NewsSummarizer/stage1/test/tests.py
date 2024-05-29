from hstest import CheckResult, StageTest, dynamic_test,TestedProgram,WrongAnswer
import os
import re
import ast
from dataset import config

class CNNPreprocessingTest(StageTest):
    @dynamic_test
    def test_preprocessing(self):
        try:
            pr = TestedProgram()
            result = pr.start()
            
            #Check if the dataset is downloaded
            datasets_cache_dir = config.HF_DATASETS_CACHE
            dataset_name = "cnn_dailymail"
            dataset_dir = os.path.join(datasets_cache_dir, dataset_name)
            if not os.path.isdir(dataset_dir):
                raise WrongAnswer(f'The dataset {dataset_name} is not downloaded. Please download it before advancing to the next stage of the project.')
            try:
                data = ast.literal_eval(result)
            except:
                raise WrongAnswer("print the first item exactly as shown in the example")
                
            if re.search(r"[^a-z0-9\s\.,?!'\"\-()]", data):
                raise WrongAnswer("Make sure you are converting the text to lowercase correctly as well as removing all characters except letters, numbers, spaces, and basic punctuation '.', ',', '?', '!'")
            return CheckResult.correct()
        except Exception as e:
            raise WrongAnswer(f"An error occurred during testing: {str(e)}")


if __name__ == '__main__':
    CNNPreprocessingTest().run_tests()
