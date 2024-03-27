const JWTHelper = require('../jwt/JWTHelper');

module.exports = async (req, res, next) => {
	try{
		if (req.cookies.jwt === undefined) {
			if(!req.is('application/json')) return res.redirect('/');
			return res.status(401).json({ status: 'unauthorized', message: 'Authentication required!' });
		}
		let data = await JWTHelper.decode(req.cookies.jwt);
		req.data = {
			id: data.id,
			role: data.role ? data.role : "guest",
			email : data.email
		}
		next();
	} catch(e) {
		(e);
		return res.status(500).send('Internal server error');
	}
}