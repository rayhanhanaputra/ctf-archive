const puppeteer = require('puppeteer');
const JWTHelper = require('./jwt/JWTHelper')
const browser_options = {
	executablePath: '/usr/bin/google-chrome',
	headless: true,
	args: [
		'--no-sandbox',
		'--disable-background-networking',
		'--disable-default-apps',
		'--disable-extensions',
		'--disable-gpu',
		'--disable-sync',
		'--disable-translate',
		'--hide-scrollbars',
		'--metrics-recording-only',
		'--mute-audio',
		'--no-first-run',
		'--safebrowsing-disable-auto-update'
	]
};
let token = JWTHelper.sign({ role:"admin" });
const cookies = [{
    'name': 'jwt',
    'value': token
}];

async function viewOpinion(userId){
	const browser = await puppeteer.launch(browser_options);
	const page = await browser.newPage();

	await page.goto('http://127.0.0.1:55213/');
	await page.setCookie(...cookies);

	await page.goto(`http://127.0.0.1:55213/check?id=${userId}`, {
		waitUntil: 'networkidle2'
	});

	await browser.close();
};

module.exports = { viewOpinion };