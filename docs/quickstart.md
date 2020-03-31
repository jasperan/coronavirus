# Quickstart

## Purpose

The purpose of this library is to get live coronavirus updates in Spain. The code is very simple. It is written in Python3 and main revolves around the _requests_ library, to get data from other websites, as well as _Flask_ as the web server environment.

## Dependencies

First of all, we need to install the dependencies for this project. We will need:

* Python3
* A virtual environment with _pip_ installed.

After we have this, we will install the dependencies by doing:

```python
pip install -r requirements.txt
```

This will install the Flask library and also an additional library, called _flask__cors_, to allow the use of Cross-origin domain requests (in case you want to install the web service in a different domain than your own website).

## Endpoints

1. GET ```/covid19```
	* Parameters: none
	* Response:
		```
			{
				"author":str(),
				"cases":str(),
				"deaths":str(),
				"recovered":str()
			}
		```
	* Response format: JSON
	* Example request: [Click here](http://jasperan.ninja:5555/covid19)
	* Example response:
		```
		{
			"author":"github.com/jasperan",
			"cases":"Total: 95923 (+7967 hoy)",
			"deaths":"Muertos: 8464 (+748 hoy)",
			"recovered":"Recuperados: 19259"
		}
		```