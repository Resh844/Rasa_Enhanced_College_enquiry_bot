# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionSetLanguage(Action):
    def name(self) -> Text:
        return "action_set_language"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        selected_language = tracker.get_slot("language")
        if selected_language == "English":
            dispatcher.utter_message(text="Great! We'll continue in English.")
        elif selected_language == "Kannada":
            dispatcher.utter_message(text="ಬಹಳ ಚೆನ್ನಾಗಿದೆ! ನಾವು ಕನ್ನಡದಲ್ಲಿ ಮುಂದುವರಿಸೋಣ.")
        else:
            dispatcher.utter_message(text="I'm sorry, I didn't understand. Let's continue in English.")
        
        return [SlotSet("language", selected_language)]


class ActionShowCourseDetails(Action):
    def name(self) -> Text:
        return "action_show_course_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course = tracker.get_slot("course")
        language = tracker.get_slot("language")

        courses_info = {
            "English": {
                "Computer Science": "The Computer Science course covers programming, data structures, and AI. Duration: 4 years.",
                "Information Science and Engineering": "The Information Science course focuses on data analysis and systems design. Duration: 4 years.",
                "ECE": "The Electronics and Communication Engineering course covers embedded systems and signal processing. Duration: 4 years.",
                "EEE": "The Electrical and Electronics Engineering course focuses on power systems and electronics. Duration: 4 years.",
                "AI & Data Science": "The AI & Data Science course focuses on machine learning and data analytics. Duration: 4 years.",
                "AI & ML": "The AI & Machine Learning course emphasizes advanced AI techniques. Duration: 4 years.",
                "Civil Engineering": "The Civil Engineering course covers construction and structural engineering. Duration: 4 years.",
                "Mechanical Engineering": "The Mechanical Engineering course focuses on mechanics and manufacturing. Duration: 4 years.",
                "CSE - AIML": "The CSE - AIML course integrates computer science with artificial intelligence and machine learning. Duration: 4 years.",
                "MBA": "The MBA program offers specializations in marketing, finance, and HR. Duration: 2 years."
            },
            "Kannada": {
                "Computer Science": "ಕಂಪ್ಯೂಟರ್ ಸೈನ್ಸ್ ಕೋರ್ಸ್ ಪ್ರೋಗ್ರಾಮಿಂಗ್, ಡೇಟಾ ಸ್ಟ್ರಕ್ಚರ್ಸ್ ಮತ್ತು AI ಅನ್ನು ಒಳಗೊಂಡಿರುತ್ತದೆ. ಅವಧಿ: 4 ವರ್ಷಗಳು.",
                "Information Science and Engineering": "ಮಾಹಿತಿ ವಿಜ್ಞಾನ ಮತ್ತು ಇಂಜಿನಿಯರಿಂಗ್ ಕೋರ್ಸ್ ಡೇಟಾ ವಿಶ್ಲೇಷಣೆ ಮತ್ತು ವ್ಯವಸ್ಥೆಗಳ ವಿನ್ಯಾಸದ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸುತ್ತದೆ. ಅವಧಿ: 4 ವರ್ಷಗಳು.",
                "ECE": "ಎಲೆಕ್ಟ್ರಾನಿಕ್ಸ್ ಮತ್ತು ಸಂವಹನ ಎಂಜಿನಿಯರಿಂಗ್ ಕೋರ್ಸ್ ಎಂಬೆಡೆಡ್ ಸಿಸ್ಟಮ್ಸ್ ಮತ್ತು ಸಿಗ್ನಲ್ ಪ್ರೊಸೆಸಿಂಗ್ ಅನ್ನು ಒಳಗೊಂಡಿರುತ್ತದೆ. ಅವಧಿ: 4 ವರ್ಷಗಳು.",
                "EEE": "ಎಲೆಕ್ಟ್ರಿಕಲ್ ಮತ್ತು ಎಲೆಕ್ಟ್ರಾನಿಕ್ಸ್ ಎಂಜಿನಿಯರಿಂಗ್ ಕೋರ್ಸ್ ಪವರ್ ಸಿಸ್ಟಮ್ಸ್ ಮತ್ತು ಎಲೆಕ್ಟ್ರಾನಿಕ್ಸ್ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸುತ್ತದೆ. ಅವಧಿ: 4 ವರ್ಷಗಳು.",
                "AI & Data Science": "AI ಮತ್ತು ಡೇಟಾ ಸೈನ್ಸ್ ಕೋರ್ಸ್ ಮೆಷಿನ್ ಲರ್ನಿಂಗ್ ಮತ್ತು ಡೇಟಾ ಅನಾಲಿಟಿಕ್ಸ್ ಅನ್ನು ಒಳಗೊಂಡಿರುತ್ತದೆ. ಅವಧಿ: 4 ವರ್ಷಗಳು.",
                "AI & ML": "AI ಮತ್ತು ಮೆಷಿನ್ ಲರ್ನಿಂಗ್ ಕೋರ್ಸ್ ಸುಧಾರಿತ AI ತಂತ್ರಗಳು ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸಿದೆ. ಅವಧಿ: 4 ವರ್ಷಗಳು.",
                "Civil Engineering": "ಸಿವಿಲ್ ಎಂಜಿನಿಯರಿಂಗ್ ಕೋರ್ಸ್ ನಿರ್ಮಾಣ ಮತ್ತು ಸಾಂರಚನಾತ್ಮಕ ಎಂಜಿನಿಯರಿಂಗ್ ಅನ್ನು ಒಳಗೊಂಡಿರುತ್ತದೆ. ಅವಧಿ: 4 ವರ್ಷಗಳು.",
                "Mechanical Engineering": "ಮೆಕಾನಿಕಲ್ ಎಂಜಿನಿಯರಿಂಗ್ ಕೋರ್ಸ್ ಮೆಕಾನಿಕ್ಸ್ ಮತ್ತು ತಯಾರಿಕೆ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸಿದೆ. ಅವಧಿ: 4 ವರ್ಷಗಳು.",
                "CSE - AIML": "CSE - AIML ಕೋರ್ಸ್ ಕಂಪ್ಯೂಟರ್ ಸೈನ್ಸ್ ಅನ್ನು ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಮತ್ತು ಮೆಷಿನ್ ಲರ್ನಿಂಗ್ ಜೊತೆಗೆ ಏಕೀಕರಿಸುತ್ತದೆ. ಅವಧಿ: 4 ವರ್ಷಗಳು.",
                "MBA": "MBA ಪ್ರೋಗ್ರಾಮ್ ಮಾರ್ಕೆಟಿಂಗ್, ಫೈನಾನ್ಸ್ ಮತ್ತು HR ನಲ್ಲಿ ವಿಶಿಷ್ಟತೆಗಳನ್ನು ನೀಡುತ್ತದೆ. ಅವಧಿ: 2 ವರ್ಷಗಳು."
            }
        }

        # Fetch course info based on language and course
        response = courses_info.get(language, {}).get(course, "I'm sorry, I don't have details about this course.")
        dispatcher.utter_message(text=response)
        return [SlotSet("course", course)]

