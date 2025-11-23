import requests
import time
import sys

BASE_URL = "http://127.0.0.1:8000"

def test_api():
    print("Waiting for server to start...")
    for _ in range(10):
        try:
            response = requests.get(BASE_URL)
            if response.status_code == 200:
                print("Server is up!")
                break
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    else:
        print("Server failed to start.")
        sys.exit(1)

    # 1. Create a task
    print("\nTesting Create Task...")
    task_data = {"title": "Buy groceries", "description": "Milk, Eggs, Bread"}
    response = requests.post(f"{BASE_URL}/tasks", json=task_data)
    assert response.status_code == 201
    created_task = response.json()
    print(f"Created: {created_task}")
    task_id = created_task["id"]

    # 2. Get all tasks
    print("\nTesting Get All Tasks...")
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    tasks = response.json()
    print(f"Tasks: {tasks}")
    assert len(tasks) >= 1

    # 3. Get specific task
    print(f"\nTesting Get Task {task_id}...")
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    print(f"Task: {response.json()}")

    # 4. Update task
    print(f"\nTesting Update Task {task_id}...")
    update_data = {"title": "Buy groceries", "description": "Milk, Eggs, Bread, Cheese", "completed": True}
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    print(f"Updated: {response.json()}")

    # 5. Delete task
    print(f"\nTesting Delete Task {task_id}...")
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    print("Deleted.")

    # 6. Verify deletion
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 404
    print("Verification successful: Task not found.")

if __name__ == "__main__":
    try:
        test_api()
        print("\nALL TESTS PASSED!")
    except Exception as e:
        print(f"\nTEST FAILED: {e}")
        sys.exit(1)
