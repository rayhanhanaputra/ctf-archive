const express       = require('express');
const app           = express();
const path          = require('path');
const bodyParser    = require('body-parser');
const cookieParser  = require('cookie-parser');
const routes        = require('./routes');
const Database      = require('./database');
const nunjucks     = require('nunjucks');


const db = new Database('challenge.db');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cookieParser());

nunjucks.configure('views', {
	autoescape: true,
	express: app
});
app.use(function(req, res, next) {
	res.setHeader("Content-Security-Policy", "object-src 'none'; child-src 'none'; script-src 'self' https://cdn.jsdelivr.net")
	next();
});

app.set('views', './views');
app.use('/static', express.static(path.resolve('static')));

app.use(routes(db));

app.all('*', (req, res) => {
	return res.status(404).send({
		message: 'Page not Found'
	});
});

(async () => {
	await db.connect();
	await db.migrate();
	app.listen(55213, '0.0.0.0', () => console.log('Listening on port 55213'));
})();