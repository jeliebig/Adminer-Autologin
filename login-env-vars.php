<?php

/** Autologin via environment variables
* @link https://www.adminer.org/plugins/#use
* @author Julian Liebig <je.liebig@web.de>
* @license https://www.gnu.org/licenses/gpl-2.0.html GNU General Public License, version 2 (or later)
*/
class AdminerLoginEnvVars {
	var $auth = array("driver" => "", "server" => "", "username" => "", "password" => "", "db" => "");

	function __construct() {
		$this->store_auth();
		if ($_SERVER["REQUEST_URI"] == "/") {
			$_POST["auth"] = $this->auth;
		}
	}

	function store_auth() {
		$this->auth["driver"] = getenv("ADMINER_DRIVER");
		$this->auth["server"] = getenv("ADMINER_SERVER");
		$this->auth["username"] = getenv("ADMINER_USERNAME");
		$this->auth["password"] = getenv("ADMINER_PASSWORD");
		$this->auth["db"] = getenv("ADMINER_DB");
	}

	function credentials() {
		return array($this->auth["server"], $this->auth["username"], $this->auth["password"]);
	}

	function login($login, $password) {
		return true;
	}

	function loginForm() {
		echo "Autologin is enabled.. You should not see this.<br>";
		// https://layton.fandom.com/wiki/Professor_Hershel_Layton
		echo "A true gentleman leaves no puzzle unsolved!";
	}
}
