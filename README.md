# <p align='center'>Python-translator</p>
# Description
```A python app to translate your text```

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
localhost:8000
```
### Method
```
POST
```
### Request body (raw json)
- Payload
```json
{
    "text":"The text to translate",
    "to_language":"the language to translate the text (ex: en, fr, mg, etc...)"
}
```
- Example
```json
{
    "text":"Wikipédia fournit tous ses contenus gratuitement, sans publicité, et sans recourir à l'exploitation des données personnelles de ses utilisateurs.",
    "to_language":"es"
}
```