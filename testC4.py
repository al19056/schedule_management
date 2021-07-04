def taskQuery(userID, orderDate):
    return [
        {
            "due": "2020-12-01T09:00",
            "need": "7",
            "title": "英語",
            "taskID": "123456",
        }
    ]


def taskQueryMany(userID, orderDate):
    return [
        {
            "due": "2020-12-01T09:00",
            "need": "2",
            "title": "英語aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "taskID": "123456",
        },
        {
            "due": "2020-09-01T09:00",
            "need": "3",
            "title": "数学",
            "taskID": "09876",
        },
        {
            "due": "2020-12-01T09:00",
            "need": "2",
            "title": "英語",
            "taskID": "123456",
        },
        {
            "due": "2020-09-01T09:00",
            "need": "3",
            "title": "数学",
            "taskID": "09876",
        },
        {
            "due": "2020-12-01T09:00",
            "need": "2",
            "title": "英語",
            "taskID": "123456",
        },
        {
            "due": "2020-09-01T09:00",
            "need": "3",
            "title": "数学",
            "taskID": "09876",
        },
    ]


def taskQueryMonth(userID, orderDate):
    return [
        {
            "due": "2020-12-01T09:00",
            "need": "2",
            "title": "英語",
            "taskID": "123456",
        },
        {
            "due": "2020-09-01T09:00",
            "need": "3",
            "title": "数学",
            "taskID": "09876",
        },
    ]


def taskQueryAll(userID):
    return [
        {
            "due": "2021-06-17T09:00",
            "need": "7",
            "title": "外出",
            "taskID": "123456",
        },
        {
            "due": "2021-06-25T09:00",
            "need": "2",
            "title": "出張",
            "taskID": "09876",
        },
    ]


def taskEdit(userID, due, need, title, taskID):
    return "newID"
