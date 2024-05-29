from hstest import StageTest, dynamic_test, CheckResult,TestedProgram,WrongAnswer
import transformers
import os

class CNNFineTuningTest(StageTest):
    @dynamic_test
    def test_finetuning(self):
        try:
            pr = TestedProgram()
            result = pr.start()
            #test for the stdout content(added to put only put emphasis on the arguements)
            if "trainingarguments" not in result.lower().strip():
                raise WrongAnswer("Make sure to print the training arguments using 'print('training_args', training_args)'")
            try:
                #test whether the finetuned model is trained properly
                model = transformers.BartForConditionalGeneration.from_pretrained("fine-tuned-bart")
                tokenizer = transformers.BartTokenizer.from_pretrained("fine-tuned-bart")
            except Exception as e:
                raise WrongAnswer(f"Error loading the saved model or tokenizer: {str(e)}")

            return CheckResult.correct()
        except Exception as e:
            raise WrongAnswer(f"An error occurred during testing: {str(e)}")


if __name__ == '__main__':
    CNNFineTuningTest().run_tests()



