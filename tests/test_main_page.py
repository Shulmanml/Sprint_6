import pytest
from  data import Answers

class TestMainPage:
    @pytest.mark.parametrize(
        "q_num, expected_result",
        [
            (0, Answers.Answers_1),
            (1, Answers.Answers_2),
            (2, Answers.Answers_3),
            (3, Answers.Answers_4),
            (4, Answers.Answers_5),
            (5, Answers.Answers_6),
            (6, Answers.Answers_7),
            (7, Answers.Answers_8),

        ]
    )

    def test_answers(self, main_page, q_num, expected_result):
       result = main_page.click_to_question_and_get_answer_text(q_num)
       assert result == expected_result

    def test_clik_on_logo_samokat_redirect_on_main_page(self, main_page):
        main_page.click_on_logo_samokat()
        result = main_page.get_current_url()
        assert result == 'https://qa-scooter.praktikum-services.ru/'




