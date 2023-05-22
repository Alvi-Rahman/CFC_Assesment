import pytest
from controllers.privacy_policy_controller import PrivacyPolicyWordCountController


class TestPrivacyPolicyWordCountController:
    @pytest.fixture
    def privacy_policy_word_count_controller(self):
        """
        Fixture for creating an instance of PrivacyPolicyWordCountController for testing.
        """
        return PrivacyPolicyWordCountController()

    def test_get_privacy_policy_word_count(self, privacy_policy_word_count_controller):
        """
        Test case for the __get_privacy_policy_word_count method of PrivacyPolicyWordCountController.

        Tests the behavior of retrieving the word frequency count of the privacy policy and returning a tuple.

        Args:
            privacy_policy_word_count_controller (PrivacyPolicyWordCountController): Instance of PrivacyPolicyWordCountController.
        """
        flag, privacy_policy_word_count = privacy_policy_word_count_controller._PrivacyPolicyWordCountController__get_privacy_policy_word_count()
        assert isinstance(flag, bool)
        assert isinstance(privacy_policy_word_count, dict)

    def test_write_privacy_policy_word_count(self, privacy_policy_word_count_controller):
        """
        Test case for the __write_privacy_policy_word_count method of PrivacyPolicyWordCountController.

        Tests the behavior of writing the privacy policy word frequency count to a JSON file and returning a message.

        Args:
            privacy_policy_word_count_controller (PrivacyPolicyWordCountController): Instance of PrivacyPolicyWordCountController.
        """
        message = privacy_policy_word_count_controller._PrivacyPolicyWordCountController__write_privacy_policy_word_count()
        assert isinstance(message, str)

    def test_main(self, privacy_policy_word_count_controller):
        """
        Test case for the main method of PrivacyPolicyWordCountController.

        Tests the behavior of the main entry point that orchestrates the word counting and writing process.

        Args:
            privacy_policy_word_count_controller (PrivacyPolicyWordCountController): Instance of PrivacyPolicyWordCountController.
        """
        message = privacy_policy_word_count_controller.main()
        assert isinstance(message, str)
