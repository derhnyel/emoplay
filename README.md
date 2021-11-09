<h1 align="center">PLAYEMO</h1>

<p align="center">Playemo was built from the ground-up with Flask, a python tool that makes it easy for developers to build APIs.

Please don't hesitate to [file an issue](https://github.com/playemo/issues/new) if you see anything missing.</p>

{% hint style="info" %}
**Is Python your language of choice?** If so, we have a [fully-supported Python API client] that makes working with the playemo API an easy task!
{% endhint %}

## Use Cases

There are many reasons to use the playemo API. The most common use case is to predict the emotion of a person from a single photograph.
However, this can also be used as a facial detection engine which returns a cropped out image of the face detected in a single photograph.!

## Authorization

All API requests require the use of an API key

To authenticate an API request, you should provide your the `api_key=[API_KEY]` as a GET parameter to authorize yourself to the API. But note that this is likely to leave traces in things like your history, if accessing the API through a browser.

```http
GET /?api_key=12345678901234567890123456789012
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `api_key` | `string` | **Required**. Your Playemo API key |

## Responses

Many API endpoints return the JSON representation of the resources created or edited. However, if an invalid request is submitted, or some other error occurs, Playemo returns a JSON response in the following format:

```javascript
{
  "error" : string,
  "success" : bool,
  "result"    : string
}
```

The `error` attribute contains a message commonly used to indicate errors or, in the case of deleting a resource, success that the resource was properly deleted.

The `success` attribute describes if the transaction was successful or not.

The `result` attribute contains any other metadata associated with the response. This will be an escaped string containing JSON data.

## Status Codes

Playemo returns the following status codes in its API:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |

## Links

- [Repo](https://github.com/derhnyel/playemo_api "playemo_api Repo")

- [Live](<hhtps://emoplay.herokuapp.com> "Live View")

- [Bugs](https://github.com/derhnyel/playemo_api/issues "Issues Page")

- [API](<hhtps://emoplay.herokuapp.com> "API")

## Screenshots

![Home Page](/screenshots/1.png "Home Page")

## Available Commands

In the project directory, you can run:
`python--version" : "check python version"`,

Since tensorflow supports python 3.6 , i would advice you have python 3.6 ,3.5 or 3.4 installed on your machine.

### `pip install -r requirements.txt" : "required libaries installed"`,

This will install the the neccesarry libaries need to run the application on your machine. 
### `python app.py" : "python-scripts start"`,

The app is built using `Flask` so this command Runs the app in Development mode. Open [http://localhost:5000](http://localhost:5000) to view it in the browser. The page will reload if you make edits.
You will also see any lint errors in the console.


## Built With

- Python
- Flask
- Mtcnn
- TensorFlow
- Keras
- CSS
- HTML

## Future Updates

- [ ] Reliable Storage

## Author

**DERHNYEL**

- [Profile](https://github.com/derhnyel "Rohit jain")
- [Email](mailto:ejedenials@gmail.com?subject=Hi "Hi!")
- [Website](https://daniel-eje.herokuapp.com "Welcome")

## 🤝 Support

Contributions, issues, and feature requests are welcome!

Give a ⭐️ if you like this project!
