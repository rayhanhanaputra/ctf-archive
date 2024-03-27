const sqlite = require('sqlite-async');
const crypto = require('crypto')
const { v4 } = require('uuidv4');

class Database {
	constructor(db_file) {
		this.db_file = db_file;
		this.db = undefined;
	}
	
	async connect() {
		this.db = await sqlite.open(this.db_file);
	}

	async migrate() {
		return this.db.exec(`
            DROP TABLE IF EXISTS users;

            CREATE TABLE IF NOT EXISTS users (
                id         UUID NOT NULL PRIMARY KEY,
                email   VARCHAR(255) NOT NULL UNIQUE,
                password   VARCHAR(255) NOT NULL,
				reward	   INTEGER DEFAULT 0,
				token	   VARCHAR(255),
				claimed    INTEGER DEFAULT 0
            );

            DROP TABLE IF EXISTS opinions;

            CREATE TABLE IF NOT EXISTS opinions (
                id         INTEGER      NOT NULL PRIMARY KEY AUTOINCREMENT,
				email VARCHAR(255),
                user_id  VARCHAR(255),
                content    VARCHAR(255) NOT NULL,
                allowed   INTEGER      NOT NULL DEFAULT 0,
                created_at TIMESTAMP    DEFAULT CURRENT_TIMESTAMP,
				FOREIGN KEY (user_id) REFERENCES users(id)
            );
			INSERT INTO users (id,email,password) VALUES ('c336ea38-c5ea-4a80-9167-b35b5e1ec7c8','admin@email.com','heheh');
			INSERT INTO opinions (user_id, email, content, allowed) VALUES
			('c336ea38-c5ea-4a80-9167-b35b5e1ec7c8', 'GreenLover42', 'I believe pollution is a serious global issue that needs immediate attention.', 1),
			('c336ea38-c5ea-4a80-9167-b35b5e1ec7c8', 'EcoChampion99', 'Renewable energy sources are the future, and we should invest more in them.', 1),
			('c336ea38-c5ea-4a80-9167-b35b5e1ec7c8', 'NatureGuardian23', 'Its crucial to reduce our carbon footprint and adopt sustainable practices.', 1),
			('c336ea38-c5ea-4a80-9167-b35b5e1ec7c8', 'EarthDefender77', 'The government should implement stricter environmental regulations.', 1),
			('c336ea38-c5ea-4a80-9167-b35b5e1ec7c8', 'BiodiversityAdvocate', 'Im concerned about the loss of biodiversity and its impact on ecosystems.', 1),
			('c336ea38-c5ea-4a80-9167-b35b5e1ec7c8', 'GreenEducationPro', 'We need to educate people about the importance of conservation and protecting the environment.', 1),
			('c336ea38-c5ea-4a80-9167-b35b5e1ec7c8', 'PlasticFreeCampaigner', 'Plastic pollution is a major environmental problem; we should use less plastic.', 1),
			('c336ea38-c5ea-4a80-9167-b35b5e1ec7c8', 'SustainableFashionista', 'The fashion industry should focus more on sustainable and ethical practices.', 1),
			('c336ea38-c5ea-4a80-9167-b35b5e1ec7c8', 'LocalFoodSupporter', 'Single-use plastics like straws and bags should be banned.', 1),
			('c336ea38-c5ea-4a80-9167-b35b5e1ec7c8', 'OrganicFarmingFan', 'Supporting local and organic farming can help reduce the carbon footprint of our food production.', 1);


        `);
	}

	async registerUser(user, pass) {
		return new Promise(async (resolve, reject) => {
			try {
				let randuuid = crypto.randomUUID()
				let query = await this.db.prepare('INSERT INTO users (id,email, password) VALUES (?,?,?)');
				resolve((await query.run(randuuid,user.toString(), pass)));
			} catch(e) {
				reject(e);
			}
		});
	}

	async loginUser(user, pass) {
		return new Promise(async (resolve, reject) => {
			try {
				let query = await this.db.prepare('SELECT id,email FROM users WHERE email = ? and password = ?');
				resolve(await query.get(user, pass));
			} catch(e) {
				reject(e);
			}
		});
	}

	async getUser(user) {
		return new Promise(async (resolve, reject) => {
			try {
				let query = await this.db.prepare('SELECT * FROM users WHERE id = ? LIMIT 1');
				resolve(await query.get(user));
			} catch(e) {
				reject(e);
			}
		});
	}

	async checkUser(user) {
		return new Promise(async (resolve, reject) => {
			try {
				let query = await this.db.prepare('SELECT email FROM users WHERE email = ?');
				let row = await query.get(user);
				resolve(row !== undefined);
			} catch(e) {
				reject(e);
			}
		});
	}

	async createOpinion(user_id, content) {
		return new Promise(async (resolve, reject) => {
			try {
				let query = await this.db.prepare('INSERT INTO opinions (user_id, content, allowed) VALUES (? , ?, 0)');
				resolve(await query.run(user_id, content));
			} catch(e) {
				reject(e);
			}
		});
	}

	async getOpinions() {
		return new Promise(async (resolve, reject) => {
			try {
				let query = await this.db.prepare('SELECT * FROM opinions WHERE allowed = ?');
				resolve(await query.all(1));
			} catch(e) {
				reject(e);
			}
		});
	}
	async getOpinion(userId){
		return new Promise(async (resolve, reject) => {
			try {
				let query = await this.db.prepare('SELECT * FROM opinions WHERE user_id = ?');
				resolve(await query.all(userId));
			} catch(e) {
				reject(e);
			}
		});
	}
	async generateReward(userId){
		return new Promise(async (resolve, reject) => {
			try {
				const key = "6T2Uz2IAkpFLscDpoWA7YWfb4R"+ (Math.floor(new Date().getTime()/100)).toString()
				const hash = crypto.createHash('sha256').update(key).digest('hex');
				let query = await this.db.prepare('UPDATE users SET token = ? WHERE id = ?');
				await query.run(hash,userId)
				resolve(hash);
			} catch(e) {
				reject(e);
			}
		});
	}
	async claimReward(userId){
		return new Promise(async (resolve, reject) => {
			try {
				let query = await this.db.prepare('UPDATE users SET reward = reward + 400 WHERE id = ?');
				resolve(await query.run(userId));
			} catch(e) {
				reject(e);
			}
		});
	}
	async setClaimed(userId){
		return new Promise(async (resolve, reject) => {
			try {
				let query = await this.db.prepare('UPDATE users SET claimed = 1 WHERE id = ?');
				resolve(await query.run(userId));
			} catch(e) {
				reject(e);
			}
		});
	}
	async deleteReward(userId){
		return new Promise(async (resolve, reject) => {
			try {
				let query = await this.db.prepare('UPDATE users SET reward = 0 WHERE id = ?');
				resolve(await query.run(userId));
			} catch(e) {
				reject(e);
			}
		});
	}
}

module.exports = Database;