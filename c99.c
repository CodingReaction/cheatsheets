/****************** Libs ***************************/
<stddef.h> // NULL | size_t | offsetof
<stdio.h>
<stdbool.h>
<string.h>
<math.h>
<assert.h>
<time.h>
<unistd.h>
<sys/types.h>
<signal.h>

/******************* Basic types ********************/
bool | char | int | float | double | size_t

enum TaskStatus { finished, unfinished}; // Warning: enum in C = int value
enum TaskStatus myStatus = finished;
/******************* Formatted printing ***********/
printf("My age is %d", age); // %d is a fmt specifier
%d = Decimal //%i works for int, take care on scanf
%f = Float
%g = Double
%c = Char
%p = Pointer addr
%zd = Size of data
/****************** Special operators ************/
(int)32.1f  // casting
sizeof(t)   // sizeof(int) also works
& | << >>   // bitwise
a > b? 1: 2 // ternary
/**************** STRINGS */
srlen() | srtcpy(dest, src) | strcat(dest, src) | strcmp(str1, str2)
strchr(str, chr) strstr(str, str) // searching, NULL if not found
char *token = strtok(str, "_") // tokenizing while(token != NULL){ ...; token = strtok(NULL, "_");}
islower() | isupper() | isalpha()
toupper() | tolower()
atoi() | atof() | atol() // ascii to int, float, long
gets()
getline()
puts()

/***************** Structs ***********************/
typedef struct User { char name[40]; int age } User;
u = User{.name="Jorge", .age=21};
/**************** Unions ************************/


/****************** Pointers special ************/
const * int agePtr = &age; // const pointer, can't modify which thing points to
const int *agePtr = &age;  // const value pointer, can't modify the thing that points to

int *numPtr = (int*)malloc(19 * sizeof(int)); // (int*)calloc(19, sizeof(int))
int *numPtr = (int*)realloc(sizeof(int), 29); // changes the order
free(numPtr); //also numPtr=NULL;

/****************** FILES ***********************/
//////////////// OPEN
FILE *f = fopen("/path/to/file", "r|w|a"); // NULL if not found, w+|a+|r+ (w always truncate)
fclose(f);
//////////////// READ
while((c = fgetc(fp)) != EOF) printf("%c", c); // int c
if (fgets(strBuff, 60, f) != NULL) printf("%s", strBuff);
/////////////// WRITE

fputc('a', f);
fputs("Max\n", f);
///////////// MOVE
long pos = ftell(f);
fseek(f, offset, from_where); // SEEK_SET | SEEK_CUR | SEEK_END

/***************** ACCESS MODIFIERS ***********************/
extern int objCount; // global outside main, accesible by all the compilation units
static int moduleGlobal; // only accesible by current file
static int myLocalVar; // makes the var exists outside the lifetime of the scope

volatile int loc1; // the change will change its value (prevent optimizations)

/****************** MACROS *************************************/
#define PI 3.14

#define PRNT(a, b) \
	printf("value 1 = %d\n", a); \
	printf("value 2 = %d\n", b);

#define str(x) #x
printf("Hello , " str(testing) // printf("Hello, " "testing") // concats to printf("Hello testing");

#define TOKENCAT(x, y) x##y // TOKENCAT(O,K) replaced with OK

__FILE__
__LINE__
__func__
__DATE__
__TIME__
__STDC__


/********************** GENERAL UTILITIES **********************/
srand(time())
rand()
system(command_str);
getenv(env_var_str);
memcpy() | memmv()

/********************** DATE&TIME: TODO **********************/
/********************** SETJMP & LONGJMP ********************/

/************************ PROCESS **************************/
PROCESS: program in execution with own address space vs a thread with shared address space. Every process is independent from another
Hierarchy: a parent program launchs the process by a system call
ID: each progress is unique by a PID

int myPID = getpid();

INTERPROCESS COMMUNICATION WAYS:

PIPES (same process) first |> second |> third (one dir, half duplex)
NAMED PIPES (diff process, FIFO) first <|> second (bi dir, full duplex)
MSG QUEUE: first post on queue, second reads from queue (full duplex)
SHARED MEM: first shared mem with second
SOCKET: mostly over a network client server
SIGNALS: source sends signal (id by number) and dest process handle it

SIGNALS:

int sig = raise(sigID); // SIGSTOP
kill()
fork()
