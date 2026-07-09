from abc import ABC, abstractmethod


class BaseVectorStore(ABC):

    @abstractmethod
    def build_index(self, embeddings):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def search(self, query_embedding, top_k):
        pass