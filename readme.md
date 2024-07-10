Urls:
    Add Task:
        method: "POST"
        http://127.0.0.1:8000/

    Task List:
        method: "GET"
        http://127.0.0.1:8000/

    Sigle Task View:
        method: "GET"
        http://127.0.0.1:8000/<int:'id'>/
        
        if you want see the task with id = 3 url wiil be:
            http://127.0.0.1:8000/3/
    
    For mark as complete
        http://127.0.0.1:8000/3/complete

        this link will mark as  complete the task with id = 3
    
    Delete Task
        method:"DELETE"
                http://127.0.0.1:8000/<int:'id'>/


Thank you for Visiting my Project!
