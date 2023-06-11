import pandas as pd
import Levenshtein

class SimpleChatBot:
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)

    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist() # 질문열만 뽑아 파이썬 리스트로 저장
        answers = data['A'].tolist()   # 답변열만 뽑아 파이썬 리스트로 저장
        return questions, answers

    def get_closest_question(self,input_sentence):
        min_distance = float("inf")    # 첨 거리를 무한대로 지정한다.
        for i in range(len(chatbot.questions)): #입력된 질문과 자료질문에서 최소거리 찾기
            distance = Levenshtein.distance(input_sentence, chatbot.questions[i])
            if distance < min_distance:
               min_distance = distance
               closest_idx = i
        return closest_idx
    


# CSV 파일 경로를 지정하세요.
filepath = 'ChatbotData.csv'

# 간단한 챗봇 인스턴스를 생성합니다.
chatbot = SimpleChatBot(filepath)

# '종료'라는 단어가 입력될 때까지 챗봇과의 대화를 반복합니다.
while True:
    input_sentence = input('You: ')
    if input_sentence == '종료':
        break
    idx = chatbot.get_closest_question(input_sentence)
    print(chatbot.questions[idx],'->',chatbot.answers[idx])


