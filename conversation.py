from social_interaction_cloud.abstract_connector import AbstractSICConnector
from social_interaction_cloud.action import ActionRunner
from social_interaction_cloud.basic_connector import BasicSICConnector
from social_interaction_cloud.detection_result_pb2 import DetectionResult

class Conversation:
    def __init__(self, sic, robot_present=False):
        self.action_runner = ActionRunner(sic)
        self.user_model = {"name": "", "age": -1}
        self.recognition_manager = {'attempt_success': False, 'attempt_number': 0, 'max_attempts': 2, 'intent_result': -1}
        self.robot_present = robot_present

    def introduce(self) -> None:
        self.action_runner.load_waiting_action('set_language', 'en-US')
        if self.robot_present:
            self.action_runner.load_waiting_action('wake_up')
        self.action_runner.run_loaded_actions()
        self.action_runner.run_waiting_action('say', 'Hello, world! I am Nao.')

    def end_conversation(self):
        self.action_runner.run_waiting_action('say', 'It was nice talking to you! Bye bye!')
        if self.robot_present:
            self.action_runner.run_waiting_action('rest')

    def ask_question(self, question: str = None, intent: str = None) -> int:
        while not self.recognition_manager['attempt_success'] and self.recognition_manager['attempt_number'] < self.recognition_manager['max_attempts']:
            # ask question
            self.action_runner.run_waiting_action('say', question)
            # wait for speech with dialogflow intent
            self.action_runner.run_waiting_action('speech_recognition', intent, 0, additional_callback=self.on_intent)
            if self.recognition_manager['intent_result'] == -1:
                return -1

        self.reset_recognition_management()
        return 1

    def tell_story_part(self, text) -> None:
        self.action_runner.run_waiting_action('say', text)

    def on_intent(self, detection_result: DetectionResult = None) -> None:
        if detection_result and len(detection_result.parameters) > 0:

            if detection_result.intent == 'answer_name':
                self.user_model['name'] = detection_result.parameters['name'].struct_value['name']
                self.recognition_manager['attempt_success'] = True
                self.recognition_manager['intent_result'] = 1

            elif detection_result.intent == 'answer_age':
                self.user_model['age'] = detection_result.parameters['age'].struct_value['amount']
                self.recognition_manager['attempt_success'] = True
                self.recognition_manager['intent_result'] = 1

            elif detection_result.intent == 'answer_decision':
                print(detection_result.parameters['decision'].string_value)
                self.user_model['decision'] = detection_result.parameters['decision'].string_value
                self.recognition_manager['attempt_success'] = True
                self.recognition_manager['intent_result'] = 1
            
            elif detection_result.intent == "stop":
                # self.end_conversation()
                self.recognition_manager['intent_result'] = -1

            else:
                self.recognition_manager['attempt_number'] += 1

        else:
            self.recognition_manager['attempt_number'] += 1

    def reset_recognition_management(self) -> None:
        self.recognition_manager.update({'attempt_success': False, 'attempt_number': 0})
