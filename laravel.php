<?php
/******************  CLI  ************************/
php artisan down --refresh=15 --render="errors::503"  #show maintance page during deployment
php artisan up

php artisan about		   #overview of app config
php artisan config:show database

php artisan config:cache           # Cache into single file (for deploy)
php artisan event:cache
php artisan route:cache
php artisan view:cache

php artisan route:list [-v] [-vv] [--path=api]

/****************** ENVIRONMENT VARIABLES ********/
$value = config('app.timezone')
env('APP_DEBUG', false)
$environment = Illuminate\Support\Facades\App::environment();
if (App::environment('production')){...}
if (App::environment(['local', 'staging'])){...}

/****************** SERVICE PROVIDERS ***********/
php artisan make:provider RiakServiceProvider

class RiakServiceProvider extends ServiceProvider{
  public function register():void{ // boot():void is called after all service providers registered
    $this->app->singleton(Connection::class, function (Application $app){
	return new Connection(config('riak'));}}}

public $bindings = [ ServerProvider::class => DigitalOceanServerProvider::class,];
public $singletons = [DowntimeNotifier::class => PingdomDowntimeNotifier::class,];

'providers' => ServiceProvider::defaultProviders()->merge([App\Providers\ComposerServiceProvider::class,])->toArray(), // config/app.php

/****************** FACADES ********************/
Defined in Illuminate\Support\Facade namespace

protected static function getFacadeAccessor():string{ // Cache::get()
  return 'cache';  // returns object within container using __callStatic()	
}

# Most important facades: https://laravel.com/docs/10.x/facades#facade-class-reference

/****************** ROUTER ***********************/
Route::get('/greeting', function() { return 'Hello';})->name('index');
Route::get('/users', function(Request $request){...});
Route::get('/posts/{post}', function (string $postId){...});
Route::get('/user/{name?}', function(?string $name = null){...});
Route::get('/user/{name}', ...)->where('name', '[A-Za-z]+'); //whereIn, whereAlphaNumeric, whereNumber
Route::get('/user', [UserController::class, 'index']);

Route::match(['get', 'post'], '/', function(){...});
Route::any('/', function(){...});
Route::fallback(function(){...});

Route::redirect('/here', '/there', OPTIONAL_STATUS_CODE);
Route::view('/welcome', 'welcome', OPTIONAL_CONTEXT_DICT);

Route::middleware(['first', 'second'])->group(function(){
  Route::get('/', function(){...});
});
Route::controller(OrderController::class)->group(function(){
  Route::get('/orders/{id}', 'show');
});

Route::domain('{account}.example.com')->group(function(){... use $account in nested route });
Route::name('admin.')->group(... Route::get('/users', ...)->name('users')); // Name = admin.users
Route::get('/ users/{user}', function (User $user){ return $user->email }); // type hint the $user!
Route::get('/users/{user}', [UserController::class, 'show']); // {user:username} to customize the key

Route::resource('photos', PhotoController::class)
	->only(['index', 'show'])
	->except(['create', 'store', 'update', 'destroy'])
	->withTrashed()
	->missing(function (Request $request){ return redirect(...);});
Route::resources(['photos' => PhotoController::class, 'posts' => PostController::class,]);
Route::apiResource('photos', PhotoController::class); // or photos.comments for /photos/{photo}/comments/{comment}
Route::singleton('profile', ProfileController::class);

$url = route('index', OPTIONAL_PARAMS_DICT);

return redirect()->route('index');
return redirect('form')->withInput() // withInput($request->except('password'))

if ($request->route()->named('profile')){...} // Inspecting the current route
$route = Route::current(); // ::currentRouteName(), ::currentRouteAction()

RateLimiter::for('api', function (Request $request){
  return Limit::perMinute(60)->by($request->user()?->id ?: $request->ip());});

/***************** MIDDLEWARE ********************/
php artisan make:middleware EnsureTOkenIsValid

public function handle(Request $request, Closure $next): Response{
  if ($request->input('token') !== 'my-secret-token'){ return redirect('home'); }}
   // perform action and call return $next($request): middleware before request handled
   // $response = $next($request), perform action and return $response: middleware after request handled

## GLOBAL REGISTER
add to $middleware prop on app/Http/Kernel.php
## ROUTES register
Route::get(...)->middleware(Authenticate::class);
Route::get(...)->middleare([First::class, Second::class]);
## ROUTES register with alias
add to $middlewareAliases = [ 'auth' => \App\Http\Middleware\Authenticate::class,]
Route::get(...)->middleware('auth'); // add parameter: "auth:tempUser"

Route::get(...)->withoutMiddleware(...)
Route::withoutMiddleware(...)->group(function(){ Route::get(...);});
Route::middleware(['web'])->group(function(){...});

$this->middleware('auth')->only('index')->except('store'); // can define on __construct() of Controller

/***************** CONTROLLERS *******************/
php artisan make:controller PhotoController [--model=Photo] [--resource] [--requests]
GET    /photos               index    photos.index
GET    /photos/create        create   photos.create
POST   /photos               store    photos.store
GET    /photos/{photo}       show     photos.show
GET    /photos/{photo}/edit  edit     photos.edit
PUT    /photos/{photo}       update   photos.update
PATCH
DELETE /photos/{photo}       destroy  photos.destroy

/*************** REQUEST ***********************/
$host   = $request->host();
$uri    = $request->path();
$url    = $request->url(); // ->fullUrl() for url with query string
$method = $reuqest->method();
$header = $request->header("X-Header-Name");
$token  = $request->bearerToken();
$cookie = $request->cookie('name');
$file   = $request->file('photo'); // $file = $request->photo;
$fileP  = $request->photo->path();
$fileEx = $request->photo->extension();
$pathSt = $request->photo->store('images', OPTIONAL_DISK_NAME); // 's3' for example
$pathSt = $request->photo->storeAs('images', 'filename.jpg');
$ipAddr = $request->ip();
$cTypes = $request->getAcceptableContentTypes();
$request->fullUrlWithQuery(['type' => 'phone']); // merge with type=phone
if ($request->is('admin/*')){...} // ->routeIs('admin.*')
if ($request->isMethod('post')){...}
if ($request->hasHeader('X-Header-Name')){...}
if ($request->accepts(['text/html', 'application/json']){...}
if ($request->expectsJson()){...}
if ($request->has('name')){...}
if ($request->hasAny(['name', 'email']){...}
if ($request->filled('name')){...}
if ($request->missing('name')){...}
if ($request->file('photo')->isValid()){...}

$request->whenHas('name', function (string $input){...});
$request->merge(['votes' => 0]);
$request->mergeIfMissing(['votes' => 0]);

$request->flash();
$request->flashOnly(['username', 'email']);
$request->flashExcept('password');

$username = $request->old('username'); // {{ old('username') }} in blade template


$input  = $request->all(); // from form
$input  = $request->collect(); // collect('users')->each(function (string $user){...});
$name   = $request->input('name', OPTIONAL_DEFAULT); // also input('products.0.name')
$input  = $request->input(); //valid also for json if content type is application/json
$name   = $request->query('name'); // from query string, same api as input()
$name   = $request->string('name')->trim(); // also ->boolean()/date()
$status = $request->enum('status', Status::class);
$input  = $request->only(['username', 'password']); // ->except(['credit_card'])

/************* RESPONSE *************************/
Route::get('/user/{user}', function(User $user){
  return "Hello world";
  return [1, 2, 3];
  return $user;
  return redirect('home/dashboard')
  return redirect()->route('login')
  return redirect()->route('profile', ['id' => 1])
  return redirect()->route('profile', [$user])
  return back()->withInput()
  return redirect()->action([UserController::class, 'index'], OPTIONAL_PARAMS_DICT)
  return redirect()->away('https://google.com')
  return redirect('dashboard')->with('status', 'Profile updated!') // {{ session('status') }}
  return response()->view('hello', $data, 200) // or use ->view(...)->with('name', 'Max')
  return response()->json(['name'=>'Max', 'state'=> 'SA')
  return response()->download($pathToFile, OPTIONAL_NAME, OPTIONAL_HEADERS)
  return response()->file($pathToFile, OPTIONAL_HEADERS)
  return response('hello world', 200)
	   ->cookie($cookie) // using $cookie = cookie('name', 'value', $minutes)
	   ->cookie('name', 'value', $duration, $path, $domain, $secure, $httpOnly)
           ->withoutCookie('name')
           ->header('Content-Type', 'text/plain')
   	   ->withHeaders([
		'X-Header-One' => 'Header Value'])

/************* CACHE *****************************/
$cached_thing = cache()->remember('CACHE DATA KEY', MINUTES TIME, function() use ($closure_data){
  return FILE FROM DISK or SOMETHING expensive;		
});

/************* VIEWS *****************************/
php artisan make:view greeting

#layout.blade.php
@yield('content')

#post.blade.php
@extends("layout.blade.php")
@section("content")  @endsection
@foreach ($users as $user)... @endforeach

@props(["name"])

/***************** FACADES **********************/
\Illuminate\Support\Facades\DB::listen(function ($query){
    logger($query->sql);
});

/***************** FACTORIES ********************/
User::truncate();
User::factory(QUANTITY_DEFAULT_1)->create();

/***************** BREEZE ***********************/
composer require laravel/breeze --dev
php artisan breeze:install
php artisan migrate
npm install
npm run dev


/***************** JEETSTREAM *******************/
TODO:

/****************** FORGE ***********************/
TODO:

/****************** VAPOR ***********************/
TODO:
