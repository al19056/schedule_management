def planQuery(userID, orderDate):
    return [
        {
            "start": "2020-12-01T09:00",
            "end": "2020-12-01T15:00",
            "title": "外出",
            "planID": "123456",
        }
    ]


def planQueryMany(userID, orderDate):
    return [
        {
            "start": "2020-12-01T09:00",
            "end": "2020-12-01T15:00",
            "title": "外出",
            "planID": "123456",
        },
        {
            "start": "2020-09-01T09:00",
            "end": "2020-09-01T15:00",
            "title": "出張",
            "planID": "09876",
        },
    ]


def planQueryMonth(userID, orderDate):
    return [
        {
            "start": "2020-12-01T09:00",
            "end": "2020-12-01T15:00",
            "title": "外出",
            "planID": "123456",
        },
        {
            "start": "2020-09-01T09:00",
            "end": "2020-09-01T15:00",
            "title": "出張",
            "planID": "09876",
        },
    ]


def planQueryAll(userID):
    return [
        {
            "start": "2021-06-15T09:00",
            "end": "2021-06-15T15:00",
            "title": "予定1",
            "planID": "123456",
        },
        {
            "start": "2021-06-24T09:00",
            "end": "2021-06-24T15:00",
            "title": "予定2",
            "planID": "09876",
        },
        {
            "start": "2021-06-28T09:00",
            "end": "2021-06-28T15:00",
            "title": "予定3",
            "planID": "09876",
        },
    ]


def planEdit(userID, start, end, title, planID):
    return "newID"
