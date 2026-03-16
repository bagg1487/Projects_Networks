import requests
import json

PROJECT_CODE = "comments-s14"

def build_payload(query: str, variables: dict = None) -> dict:
    """
    Формирует payload для GraphQL запроса.
    
    Args:
        query: Строка с GraphQL запросом
        variables: Словарь с переменными
    
    Returns:
        dict: Словарь в формате GraphQL
    """
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    return payload


def main():
    """Основная функция клиента."""
    url = "http://localhost:8138/graphql"
    
    print("=== QUERY: получение комментариев ===")
    
    query = """
    query {
      comments {
        id
        text
        author
        createdAt
      }
    }
    """
    
    response = requests.post(
        url,
        json=build_payload(query),
        headers={"Content-Type": "application/json"}
    )
    
    result = response.json()
    
    if "errors" in result:
        print("Ошибки:")
        for error in result["errors"]:
            print(f"  - {error['message']}")
    else:
        print("Комментарии:")
        for comment in result["data"]["comments"]:
            print(f"  {comment['id']}: {comment['text']} (by {comment['author']})")
    
    print("\n=== MUTATION: создание комментария ===")
    
    mutation = """
    mutation {
      createComment(input: {
        text: "Новый комментарий",
        author: "s14"
      }) {
        id
        text
        author
        createdAt
      }
    }
    """
    
    response = requests.post(
        url,
        json=build_payload(mutation),
        headers={"Content-Type": "application/json"}
    )
    
    result = response.json()
    
    if "errors" in result:
        print("Ошибки:")
        for error in result["errors"]:
            print(f"  - {error['message']}")
    else:
        comment = result["data"]["createComment"]
        print("Создан комментарий:")
        print(f"  ID: {comment['id']}")
        print(f"  Текст: {comment['text']}")
        print(f"  Автор: {comment['author']}")
        print(f"  Дата: {comment['createdAt']}")


if __name__ == "__main__":
    main()