from hstest import CheckResult, StageTest, dynamic_test,TestedProgram,WrongAnswer
import os
import re
from dataset import config

class NewsSummaryGenerationTest(StageTest):
    files_dict = {
        "news_data.json":"""{
    "articles": [
        {
            "title": "New Exoplanet Discovered in Nearby Star System",
            "content": "Astronomers have made an exciting discovery of a new exoplanet orbiting a star just 30 light-years away. The planet, named Kepler-452b, is located in the habitable zone of its star, making it a prime candidate for potential life. This discovery opens up new possibilities for studying exoplanetary atmospheres and searching for signs of extraterrestrial life. Kepler-452b is approximately 1.5 times the size of Earth and orbits its star in 385 days, putting it in the 'Goldilocks zone' where conditions may be just right for liquid water to exist. Researchers are eager to study this distant world further using advanced telescopes and spectroscopic analysis to determine its composition and potential habitability. The discovery of Kepler-452b represents a significant advancement in our understanding of planetary systems beyond our own and fuels the ongoing quest for discovering life elsewhere in the universe. The unique characteristics of Kepler-452b, such as its size, orbital period, and location within the habitable zone, make it a captivating target for future space missions and scientific exploration. Scientists anticipate that studying Kepler-452b will provide valuable insights into the diversity of exoplanets and the conditions necessary for life to thrive beyond Earth.",
            "source": "AstroNews",
            "author": "Dr. Astrid Johnson",
            "publishedAt": "2024-05-29T08:00:00Z"
        }
    ]
}"""
    }

    
    @dynamic_test(files=files_dict)
    def test_summary_generation(self):
        try:
            pr = TestedProgram()
            result = pr.start()
            if 'summary' in result.lower().strip():
                raise WrongAnswer("Print the processed data exactly the way shown in the example")
            return CheckResult.correct()
        
        except Exception as e:
            raise WrongAnswer(f"An error occurred during testing: {str(e)}")


if __name__ == "__main__":
    NewsSummaryGenerationTest().run_tests()
