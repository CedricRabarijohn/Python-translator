[deployed_url]: https://python-translator.herokuapp.com

# <p align='center'>⌨ Python-translator ⌨</p>

# Description

A light python api to translate your text.
Fork this repository if you want to use it on your local environment. Otherwise, you can try out the deployed url https://python-translator.herokuapp.com

## Prerequisites

### Packages

    - fastapi
    - translators
    - uvicorn

## Run the script

```
> uvicorn module.main:app --reload
```

# Usage

## ⭐⭐ V2 ⭐⭐

### ✅ Url

```
localhost:8000 (Or use https://python-translator.herokuapp.com to try out the deployed version ready to go !)
```

### ✅ EndPoint

```
/v2/translate
```

### ✅ Method

```
POST
```

### ✅ Request body (raw json)

```json
{
  "texts": {
    "text1": "The first text to translate",
    "text2": "the second text to translate",
    "randomFieldName": "the third text to translate",
    "helloworld": "font icons for all projects, large or small"
  },
  "to_language": "fr"
}
```

### ✅ Response (status 200)

```json
{
  "from_language": "auto",
  "to_language": "fr",
  "translated": {
    "text1": "Le premier texte à traduire",
    "text2": "Le deuxième texte à traduire",
    "randomFieldName": "Le troisième texte à traduire",
    "helloworld": "icônes de police pour tous les projets, grands ou petits"
  }
}
```

## ⭐⭐ V1 ⭐⭐

### ✅ Url

```
localhost:8000 (Or use https://python-translator.herokuapp.com to try out the deployed version ready to go !)
```

### ✅ EndPoint

```
/v1/translate
```

### ✅ Method

```
POST
```

### ✅ Request body (raw json)

```json
{
  "text": "Wikipedia provides all its content for free, without advertising, and without using the exploitation of the personal data of its users.",
  "to_language": "fr"
}
```

### ✅ Response (status 200)

```json
{
  "from_language": "auto",
  "to_language": "fr",
  "translated": "Wikipedia fournit tout son contenu gratuitement, sans publicité, et sans utiliser l'exploitation des données personnelles de ses utilisateurs."
}
```
# Deployed api

## Url : https://python-translator.herokuapp.com
