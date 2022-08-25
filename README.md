# <p align='center'>Python-translator</p>
# Description
A light python api to translate your text.
Fork this repository if you want to use it on your local environment. Otherwise, you can try out the deployed url https://python-translator.herokuapp.com

# Getting started

## Prerequisites
### Packages
    - fastapi
    - translators
    - uvicorn

## Run the script
```
> uvicorn main:app --reload
```

## Usage
### Url
```
localhost:8000/translate
```
### Method
```
POST
```
### Request body (raw json)
#### Body payload
```json
{
    "text":"The text to translate",
    "to_language":"the language to translate the text to (ex: en, fr, mg, etc...)"
}
```
#### Example
- Request body
```json
{
    "text":"Wikipedia provides all its content for free, without advertising, and without using the exploitation of the personal data of its users.",
    "to_language":"fr"
}
```
- Response
    - Success status 200
    ```json
    {
        "from_language": "auto",
        "to_language": "fr",
        "translated": "Wikipedia fournit tout son contenu gratuitement, sans publicité, et sans utiliser l'exploitation des données personnelles de ses utilisateurs."
    }
    ```

# Deployed app
## Url : https://python-translator.herokuapp.com/translate
