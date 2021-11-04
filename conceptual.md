1. Important difference between Javascript and Python...
Python is back end/Javascript is front end
Python uses indentation to indicate scope, Javascript uses{} to indicate scope
2. test={"a":1, "b":2}  test.get("c") returns None
3. Unit testing is a small sized test to test individual functions
4. Integration tests are test designed to test multiple functions and their interactions with each other. 
5. The role of a web application framework like Flask is to help handle HTTP requests and URL mapping. Flask is a set of libraries and tools that helps build a web app+
6. Using a parameter in a URL route is better used for instances where the URL route is set and static based on a few options already created. Using query params is better when the webpage requested has to be dynamimc and based on what the user is trying to find.
7. The URL path created must contain "app.route('/test/<variable>).  The function must include test_item=*data structure that the item is stored in*[variable]
8. test_variable=request.args["query Param"]
9. request.data will get the body of the reuqest using Flask
10. Cookies are data entries that are send from the server to your browser to hold data to be passed back to the server as the user interacts with the page. The server may or may not do something with the cookies that are fed back. It can be things such as keeping a user logged in each time they refresh the page or keeping items in an online shopping card.
11. Session objects in Flask are constainers of data (like a cookie) that keeps that type of data structure passed, such as a list or a dict. They contain info for the current browser
12. Flask's jsonify feature turns data into the JSON form so it can be passed back and forth between front and back end applications such as python and javascript