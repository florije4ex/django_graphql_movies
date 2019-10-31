# Usage

## url
`https://stackabuse.com/building-a-graphql-api-with-django/`

## workflow
```text
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata movies
python manage.py runserver
```

## queries

查询所有actor
```text
query getActors {
  actors {
    id
    name
  }
}
```

查询单个movie
```text
query getMovie {
  movie(id: 1) {
    id
    title
    actors {
      id
      name
    }
  }
}
```

## mutations

添加actor
```text
mutation createActor {
  createActor(input: {
    name: "Tom Hanks"
  }) {
    ok
    actor {
      id
      name
    }
  }
}
```

添加movie
```text
mutation createMovie {
  createMovie(input: {
    title: "Cast Away",
    actors: [
      {
        id: 3
      }
    ]
    year: 1999
  }) {
    ok
    movie{
      id
      title
      actors {
        id
        name
      }
      year
    }
  }
}
```

修改movie
```text
mutation updateMovie {
  updateMovie(id: 2, input: {
    title: "Cast Away",
    actors: [
      {
        id: 3
      }
    ]
    year: 2000
  }) {
    ok
    movie{
      id
      title
      actors {
        id
        name
      }
      year
    }
  }
}
```

## http post request
```text
curl -X POST -H "Content-Type: application/json" --data '{ "query": "{ actors { name } }" }' http://127.0.0.1:8000/graphql/

will return value:

{"data":{"actors":[{"name":"Michael B. Jordan"},{"name":"Sylvester Stallone"},{"name":"Tom Hanks"}]}}boqings-MacBook-Pro:~ boqingfu$
```