# giornale

<img src="./giornale.png" width="45" height="40">

- [ ] Parse and persist RSS
	- [x] Parse data
	- [x] Store data in standard format
	- [ ] Set cadence of data parsing service
- [ ] Tokenise data
	- [ ] Create and persist tokens
	- [ ] POS tagging/token cleaning
- [ ] 'To English' service
	- [x] Get translation of ~tokens~ full phrases
	- [ ] Persist tokens and translations in standard format
- [ ] API
    - [x] Simple `GET` for local db translations
	- [x] Get exercise/bag of ~tokens &~ translations
	- [ ] Exercise as a first-class entity
	- [x] Basic React `giornale-frontend` consuming from `/exercise` endpoint
