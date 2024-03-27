const bot            = require('../bot');
const express        = require('express');
const router         = express.Router();
const JWTHelper      = require('../jwt/JWTHelper');
const AuthMiddleware = require('../middleware/AuthMiddleware');
const { validationResult, check, email } = require('express-validator')

let db;

const response = data => ({ message: data });

router.get('/', (req, res) => {
	return res.render('index.html');
});

router.get('/home', AuthMiddleware, async(req,res)=>{
	return db.getUser(req.data.id)
		.then(user => {
			(user)
			if(user === undefined) return res.redirect('/');
			return db.getOpinions()
				.then(opinions => {
					res.render('home.html', { opinions,user });
				})
		})
	.catch(() => res.status(500).send(response('Something went wrong!')));
})

router.post('/api/login', check('email').isEmail(),async (req, res) => {
	const { email, password } = req.body;
	const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).send(response("Invalid Email or Password"));
    }
	if (email && password) {
		return db.loginUser(email.toString(), password)
			.then(user => {
				let token = JWTHelper.sign({ id: user.id, role:"guest",email: user.email});
				res.cookie('jwt', token, { maxAge: 2000000000000000 });
				return res.send(response('User authenticated successfully!'));
			})
			.catch(() => res.status(403).send(response('Invalid Email or Password!')));
	}
	return res.status(500).send(response('Missing parameters!'));
});

router.post('/api/register', check('email').isEmail(), async (req, res) => {
	const { email, password } = req.body;
	const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).send(response("Invalid Email or Password"));
    }
	if (email && password) {
		return db.checkUser(email.toString())
			.then(user => {
				if (user) return res.status(401).send(response('User already registered!'));
				return db.registerUser(email.toString(), password)
					.then(()  => res.send(response('User registered successfully!')))
			})
			.catch((err) => {
				res.send(response('Something went wrong!'))
		});
	}
	return res.status(401).send(response('Please fill out all the required fields!'));
});

router.get('/check',AuthMiddleware, async (req, res) => {
	if(req.ip != '127.0.0.1') return res.redirect('/');
	if(req.data.role !== "admin") return res.redirect('/');
	return db.getUser(req.query.id).then(user =>{
		return db.getOpinion(req.query.id)
		.then(opinions => {
			res.render('check.html',{opinions,user});
		})
		.catch(() => res.status(500).send(response('Something went wrong!')));
	})
});

router.get('/api/generate', AuthMiddleware, async(req,res)=>{
	if(req.ip !== '127.0.0.1') return res.redirect('/');
	return db.getUser(req.data.id).then(
		user =>{
			if (user === undefined) return res.redirect('/');
			if(user.token !== null){
				return res.send(response('Token have been generated for your account'))
			}
			return db.generateReward(req.data.id).then((token)=>{
				return res.send(response(`Token generated for account ${req.data.id} value:${token}`))
			}).catch(()=>{res.status(500).json({ error: 'Generate Failed' });})
		})
		.catch(()=>{res.status(500).json({ error: 'Generate Failed' });})
})
router.post('/api/addopinion', AuthMiddleware, async (req, res) => {
	const { content } = req.body;
	if(content){
		return db.createOpinion(req.data.id, content)
			.then(() => {
				bot.viewOpinion(req.data.id);
				res.send(response('Your opinion is being checked by admin'));
			});
	}
	return res.status(403).send(response('Empty content cannot be checked'));
})
router.get('/api/claim', AuthMiddleware, async(req,res)=>{
	return db.getUser(req.data.id).then(
		user =>{
			if (user === undefined) return res.redirect('/');
			if(user.token === req.query.token && user.claimed === 0){
				return db.claimReward(req.data.id).then(()=>{
					return db.setClaimed(req.data.id).then(()=>{
						return res.send(response(`Reward Claimed ${req.data.id}`))
					}).catch(()=>{res.status(500).json({ error: 'Something went wrong' });})
				}).catch(()=>{res.status(500).json({ error: 'Something went wrong' });})
			}
			return res.status(500).json({message: "You have claimed your reward"})
		})
})

router.post('/api/flag',AuthMiddleware, async (req, res) => {
	return db.getUser(req.data.id)
		.then(user => {
			if(user === undefined) return res.redirect('/');
			if(user.reward >= 999){
				return db.deleteReward(user.id).then(()=>{
					res.send(`You've done it here's your flag IFEST23{fake_flag_dont_try_it}`)
				}).catch(()=>{res.status(500).json({error: 'Something went wrong'})} )
			}
			return res.status(500).json({message: "Too bad, you don't have enough money"})
		})
	.catch(() => res.status(403).send(response('Something Went Wrong')));
});

router.get('/logout', (req, res) => {
	res.clearCookie('jwt');
	return res.redirect('/');
});

module.exports = database => { 
	db = database;
	return router;
};
