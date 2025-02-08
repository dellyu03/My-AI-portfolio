from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_mistralai import ChatMistralAI
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# 환경변수 로드
load_dotenv()

class WebChatBot:
    def __init__(self, urls):
        # Mistral API 키 확인
        self.mistral_api_key = os.getenv('MISTRAL_API_KEY')
        if not self.mistral_api_key:
            raise ValueError("MISTRAL_API_KEY가 환경 변수에 없습니다.")
        
        # User Agent 설정
        os.environ["USER_AGENT"] = "Mozilla/5.0"
        
        # 웹 페이지 로드 및 변환
        loader = AsyncHtmlLoader(urls)
        docs = loader.load()
        
        # HTML 변환
        bs_transformer = BeautifulSoupTransformer()
        docs_transformed = bs_transformer.transform_documents(docs)
        
        # 문서를 작은 청크로 분할
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        self.texts = text_splitter.split_documents(docs_transformed)
        
        # HuggingFace 임베딩 설정
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.vectorstore = FAISS.from_documents(self.texts, embeddings)
        
        # 대화 메모리 설정
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )
        
        # 프롬프트 템플릿 설정
        self.prompt_template = PromptTemplate(
            template="""Please answer the question using the following context:

Context: {context}

Question: {question}

When generating your response, please consider the following:
1. Answer accurately based on the given context.
2. Explain in Korean.
3. Please respond as if you are the author of this text.

답변:""",
            input_variables=["context", "question"]
        )
        
        # Mistral AI 모델 설정
        self.llm = ChatMistralAI(
            model="mistral-medium",
            temperature=0.1,
            max_tokens=512,
            mistral_api_key=self.mistral_api_key
        )
        
        # QA 체인 설정
        self.qa = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(),
            memory=self.memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": self.prompt_template}
        )
    
    def ask_question(self, question):
        # 질문에 대한 답변 생성
        response = self.qa({"question": question})
        return response['answer']

def main():
    # 웹 페이지 URL 목록
    urls = [
        "https://velog.io/@youjacha082/%EB%AA%A8%EB%8D%98-%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-Deep-Dive-%EA%B3%B5%EB%B6%80-Ch5-%ED%91%9C%ED%98%84%EC%8B%9D%EA%B3%BC-%EB%AC%B8",
    ]
    
    try:
        print("웹 페이지 로딩 중...")
        chatbot = WebChatBot(urls)
        
        # 대화 루프
        print("\n웹 페이지의 내용에 대해 질문해주세요 (종료하려면 'quit' 입력)")
        while True:
            question = input("\n질문: ")
            if question.lower() == 'quit':
                break
                
            try:
                answer = chatbot.ask_question(question)
                print("\n답변:", answer)
            except Exception as e:
                print(f"질문 처리 중 오류 발생: {str(e)}")
                
    except Exception as e:
        print(f"오류 발생: {str(e)}")

if __name__ == "__main__":
    main() 