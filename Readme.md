## What is API
Lets suppose our frontend is in React and backend is in Python so to communicate among themselves we will write API calls.

So we will decide the protocol and the data that we will be sharing/sending

API is to communicate among systems or among applications or servers

Via API calls we share data. Our only duty is to write API calls and we don't have to worry about how we will get the data, from where we will get the data, what will be the processing of it.

## From Sudo Code

API- Application Programming Interface
When piece of code has to interact with another piece of code we use API
Through API a piece of code can interact with another piece of code which could be running on same machine or another machine. it can be in same language or another

Through API you will mention what you have to do-
1) Send a data
2) Fetch a data
3) Do computation or Task? (Hence the programming)

Interface- mean abstraction

As we said via API one piece of code interact with another, ex- When we write comment in youtube video maybe the frontend is taking the comment and giving it to backend which could be in different server. Frontend is sending that via API calls we dont know how the backend is processing that API calls hence the abstraction.

So via API we are interacting to another code but we dont know how to implementation will work behind the scene.

### Advantages-
1) Communication- Two different app/code to interact
2) Abstract- Freedom of implementation. Ex- Instagram get follower API. So the implementation of the code can change but again we don't have to worry about the change.
3) Platform Agnostic- FrontEnd and BackEnd could be in different languages 

### Examples-
1) Private APIs- Hidden APIs (Application in a Phone making payment)
2) Public APIs- Available to everyone like Google Map API, Weather API
3) Web APIs- Superset of Private and Public. Application running on cloud can interact with each other (get follower, post pictures etc)
4) SDK/Library APIs- For thredding we can use lock, releaselock, fork, join.


API are the way on how your data move in the system, get in the system.

### Factors to look for while designing/making an API
1) API contracts- Deciding the end points that we have to call,methods that we have to use, format in which we will get the data. 
2) Documentation- 
3) Data Format-
4) Security- Why providing the API we are exposing our system in some way. So API security is of huge importance. Like someone can send huge amount of request and can bring down the system.

### Standard defined in industry while writing API
As per requirement and platform we use it.
1) RPC-
2) SOAP-
3) REST-

## Code Execution-
So we need requests library for the API call in python

So for that we need to execute-
```pip install requests```

If you dont have pip installed then-
```sudo apt update```
and then
```sudo apt install python3-pip```