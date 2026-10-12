from .topic import Topic
from .document import Document
from .category import Category


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def __find_object(obj_id, collection) -> Category|Topic|Document|None:
        return next((o for o in collection if o.id == obj_id), None)

    def __edit_object(self, obj_id, collection,*new_values):
        obj = self.__find_object(obj_id, collection)
        if obj:
            obj.edit(*new_values)

    def __delete_object(self, obj_id, collection) -> None:
        obj = self.__find_object(obj_id, collection)
        if obj:
            collection.remove(obj)

    def edit_category(self, category_id, new_name) ->None:
        self.__edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        self.__edit_object(topic_id, self.topics,  new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        self.__edit_object(document_id, self.documents, new_file_name)

    def delete_category(self, category_id):
        self.__delete_object(category_id, self.categories)

    def delete_topic(self, topic_id):
        self.__delete_object(topic_id, self.topics)

    def delete_document(self, document_id):
        self.__delete_object(document_id, self.documents)

    def get_document(self, document_id) -> Document:
        return self.__find_object(document_id, self.documents)

    def __repr__(self):
        return '\n'.join([d.__str__() for d in self.documents])