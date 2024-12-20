/********************* CLI ******************/
$php -S localhost:8080  // run dev server

<?php
/************ VARIABLES ***************/
$name = "Max" // variables with $
$fullName = $name . " LastName" // concat string with .
$fullName = "$name LastName" // string templating
<?= $fullName ?> // different way to print
/*************** SHORTHAND SINTAX ***************/
$names = ["Pedrito", "Pablito", "Clavito"]
<?php foreach ($names as $name): ?>
  <?= $name ?>
<?php endforeach; ?>
/***************  BASIC SCRIPT *******************/
$name = "Max";
echo "Printing your name {$name}";
$username = $name ?? 'Guest'; // NULL COALESCING
$birthday = $birthday?->format('Y-m-d');

define(PI, 3.14); // CONSTANTS

var_dump("anything")
die()
echo "</pre>"
/************* DATA STRUCTURES *****************/
$names = array("Max", "Otto"); // ARRAY
$names = ["Max", "Otto"];
[$a, $b] = $names;
$myName = $names[0]

array_push($names, "Sergio");
$names[] = "Sergio"; // SHORTHAND push to array

$name_last  = array_pop($names); // "Sergio"
$name_first = array_shift($names); // "Max"
$names_rev  = array_reverse($names);
$count      = count($names);  // 3

$capitals = array("USA" => "Washington DC", "Uruguay" => "Montevideo"); // MAP
$myCapital = $capitals["Uruguay"]

$keys   = array_keys($capitals);
$values = array_values($capitals);
$flip   = array_flip($capitals);  // "Montevideo" => "Uruguay"

$other  = array_map(fn($thing) => $thing->id, $names);
in_array($thing, $array); // true or false
if (array_key_exists($key, $array)){...} // check if the key is defined

$filterList = array_filter($books, function ($book) { return $book["releaseYear"] > 1980;})

enum Status: int{ // Status::DRAFT
  case DRAFT;
  case ARCHIVED;
}
/*************** SUPER GLOBALS ******************/
$_GET, $_POST, $_SERVER
<form action="php-lang.php" method="post"> <input name="username" /></form>

htmspecialchars($_SERVER["PHP_SELF"]); // the current filename, avoid xss
$_SERVER["REQUEST_METHOD"] == "POST"
$_SERVER["REQUEST_URI"] === "/"

$allowed_ext = ["png", "jpg", "jpeg"]
$_FILES["upload"]; // enctype="multipart/formdata"  ["name"| "size" | "tmp_name"]
move_uploaded_file($file_tmp, $target_dir);

  $username = $_POST["username"];
?>


$resource_from_disk = file_get_contents(__DIR__ . '/../' . 'data.json');

parse_url($_SERVER['REQUEST_URI']); // ['path'=>..., 'query'=>...]
http_build_query($data); // concatenate a Dict in order to create a querystring
http_response_code(500); // returns the status code as result

call_user_func($my_func);
password_hash($password, PASSWORD_BCRYPT);

// LOGOUT
$_SESSION = [];
session_destroy();
$params = session_get_cookie_params();
setcookie('PHPSESSIONID', '', time()-3600, $params['path'], $params['domain'], $params['httponly']);
header("Location: /");
exit();


$root_folder = __DIR__ . "..";
extract($attrArray); // import symbols to current closure


$className = (new ReflextionClass($this))->getShortName();

//************** COOKIES ***********************/
<?php
  setcookie("cookie_key", "value", time() + (3000), "/");
  if (isset($_COOKIE["cookie_key"]){...}
  foreach($_COOKIE as $key => $value){...}
?>
/*************** SESSION ***********************/
  session_start();
  session_destroy();
  $_SESSION["username"] = "Max";

  header("Location: home.php"); // redirect
/************** EXCEPTIONS *********************/
  try{...} catch(exception_name){...}
  try{...} catch (Exception $e){...}
  throw new Exception("error");
/************** MATH ***************************/
  $positive = abs($x);
  $total    = round($x); // floor($x) | ceil($x)
  $sq       = pow($x, 2);
  $upper    = max($x, $y, $z); // min(...)
  $pi_val   = pi();
/************* CONTROL FLOW ********************/
<?php
  if (...){ } elseif (...) { } else { };

switch($grade){
  case "A": echo "pretty bad"; break
  default:  echo "oki doki"; break
}

$msg = match($status){
  200, 300 => null,
  400 => 'not found',
  500 => 'server error',
  default => 'unknown code',
}

for ($i = 0; $i < 10; $i++) { echo "{$i}"; }
foreach ($names as $name) {...}
foreach ($capitals as $key => $value){...}
while ($doing) {...}
yield $result; // GENERATORS


?>
/************ STD LIB ***************************/
<?php
isset() = TRUE if declared and not null
empty() = TRUE if not declared, null, false, ""

strcmp($username, "Max");
strlen($phone);
strpos($name, "x");
substr($username, 0, 3);
strtolower($name)
strtoupper($name)
trim($strinWithSpaces)
explode(" ", $pharagraph); // split
implode(" ", $pharagraph); // join
str_replace("-", "", $phone);

$username = filter_input(INPUT_POST, "username", FILTER_SANITIZE_SPECIAL_CHARS); // FILTER_SANITIZE_NUMBER_INT | SANITIZE_EMAIL | VALIDATE_INT
filter_var($value, FILTER_VALIDATE_EMAIL);

$password_hashed = password_hash($password, PASSWORD_DEFAULT); // bcrypt
password_verify($password, $password_hashed);

?>
/************ FUNCTIONS *************************/
<?php
  function printer(float $a, string $b): int|float{...} // Foo&Bar => intersection type
  function sum(...$nums) { return array_sum($nums);} // VARIADICS

  sum(1, ...$others); // SPREAD: $others=[2, 3], SUM(1, 2, 3)

  printer(a: 1.0, b: "yup"); // NAMED ARGUMENTS
?>

/************ FILE     **************************/
<?php
 $exists = file_exists($file);
 $file = fopen($filename, 'r');
 $line = fgets($file)
 $contents = fread($file, filesize($file));
 $fclose($file);
?>
/************ DATABASE **************************/
<?php
 $db_server = "localhost";
 $db_user = "root";
 $db_pass = "";
 $db_name = "my_db";
 $connection = mysqli_connect($db_server, $db_user, $db_pass, $db_name); // $connection


 $sql = "INSERT INTO users (username, password) VALUES (?, ?)";
 $result = mysqli_query($connection, $sql);
 if (mysqli_num_rows($result) > 0)
   while($row = mysqli_fetch_assoc($result)){...};

 mysqli_close($connection);

 // PDO
 $dsn = "mysql:host=localhost;port=3306;dbname=my_db;user=root;password=1234;charset=utf8mb4;"
 $pdo = new PDO($dsn, 'root', 'password', [PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,]);
 $statement = $pdo->prepare(MY_SQL_QUERY);
 $statement->execute();
 $results = $statement->fetchAll();

?>
/************* OOP *******************************/
declare(strict_types=1)

///  CLASS ///
class Transaction extends Paperwork implements Notify, Usable{ // readonly class Transaction | float readonly $amount
  public float $amount;  // ?float $amount
  private string $expired = "yeah";

  public function __construct(float $amount, string $description){
    parent::__construct($amount);
    $this->$amount = $amount;
  }

  public function __construct(public float $amount, public string $expired){} // PROMOTION
}

require_once './Transaction.php';

$transaction = new Transaction(10, "nop");
echo($transaction->amount);
var_dump($transaction);

////  TRAITS /////
trait Commentable{
  public function sayHi($name){ echo "Hi {$name}"; }
}

class Post{
  use Commentable;
}

///   ANONYMOUS CLASS ///
$app->setThing(new class implements Bla{ ... });
/************ IMPORTS ***************************/
include("header.html"); // include_once "something.php"
include("body.html");
include("footer.html");
/*********** NAMESPACES *****************************/
require "Item.php";
require "functions.php";

use App\Models\Admin\Item;  // namespace App\Models\Admin
use const App\Utils\MAX;
use function App\Utils\sayHello as saludate;
/************ AUTOLOAD *******************************/
spl_autoload_register(function ($class){// RUN when a class not required is used
  require "$class.php";		             // CLASS autoload
  require str_replace('\\', '/', $class) . '.php'); // NAMESPACE autoload
});
/*********** ANOTATIONS or DECORATORS ***************/
#[Route(Http::GET, '/hello/world')]
class HelloWorldController{
  public function __invoke(){
    return 'Hello world';
  }
}

function login($user, #[SensitiveParameter] $password){...}
/************ CURL **********************************/
$resource = curl_init("http://google.com");
curl_setopt($resource, CURLOPT_RETURNTRANSFER, true);
$result = curl_exec($resource);
$info   = curl_getinfo($resource); //curl_getinfo($resource, CURLINFO_HTTP_CODE);
curl_close($resource);
/************ JSON **********************************/
json_encode($php_map, OPTIONAL); // OPTIONAL = JSON_FORCE_OBJECT | JSON_PRETTY_PRINT
json_decode($json_string);
file_put_contents('data.json', $encoded_data);
$json_data = file_get_contents('data.json');
