//////  CLI
> npx create-next-app@latest .
> pnpm run dev
//////  SERVER COMPONENTS vs CLIENT COMPONENTS
- build on server exclusively
- no effects/hooks
- faster page loads
- default
- [server] tag, logs on TERMINAL
vs
- use client
- browser apis
///////// ROUTING
users/page.tsx
users/[id]/page.tsx

function Users({params}: {params: {id: string}}){
  const { id } = await params;
  return <h1>Product: {id}</h1>;
}
/////// PAGE GROUPS
(auth)/login/page.tsx    // login/ route, logical grouping
(auth)/register/page.tsx // only matters for organizing
////// METADATA
export const metadata:Metadata = { // inside layout.tsx
  title: "Create Next App",
  description: "Description of site"
};
/////// LAYOUTS: shared between multiple pages
src/app/layout.tsx -> basic layout for all pages
function RootLayout({children}: Readonly<{children: React.ReactNode;}>){
  return (
    <html lang="en">
      <body> {children} </body>
    </html>
  )
}

products/[id]/layout.tsx -> applies for all product pages
function ProductLayout({children}: {children: React.ReactNode}){
  return <div>
  	  <h2>Featured</h2>
  	  {children}
	</div>
}
////// LINK and ROUTER
<Link href="/">Home</Link> // uses nextjs router for navigation
import {usePathname, useRouter} from "next/navigation"
const pathname = usePathname(); // pathname === "/" "/about"
const router = useRouter();
router.push("/") // navigate programatically
//////////// ROUTE HANDLERS (api)
src/app/users/route.ts

export async function GET(){
  return Response.json(users);
}

export async function POST(request: Request){
  const user = await request.json();
  const newUser = createUser({id: 1, name: user.name});
  return new Response(JSON.stringify(newUser,{
    headers: {
      "Content-Type": "application/json"
    },
    status: 201,
  });
}

/users/[id]/route.ts

export async function GET(_request: Request, ctx: {params}: {params:{id:string}}){
  const {id} = await params;
  const user = users.find(user => user.id === id);
  return Response.json(user);
}

export async function PATH(){...}

///////// DATA FETCHING
// in server components you can users = await fetch('...') directly
// in client components only in useEffect

//////////// LOADING
app/users-server/loading.tsx
export default function Loading(){
  return <div> Loading users...</div>
}

app/users-server/error.tsx
"use client"
export default function Error({error}: {error: Error}){
  return <div>error fetching data </div>
}
//////////// SERVER ACTIONS: async functions on server, form, db, etc
app/mock-users/page.tsx

import {revalidatePath} from "next/cache";

async function MockUsers(){
  const res = await fetch("mockusers-endpoint");
  const users = await res.json();

  async function addUser(formData: FormData){
    "use server"
    const name = formData.get("name")
    const res = await fetch(
      "https://users",
      {
	method: "POST",
      	headers: {
        	"Content-Type": "application/json",
		Authorization: "Bearer PRIVATE_KEY",
      	},
      	body: JSON.stringify({name}),
      }
     );
     const newUser = await res.json();
     revalidatePath("/mock-users");
     console.log(newUser);
  }
  return <div>
    <form action={addUser}>
      <input type="text" name="name" required />
      <button> Add user </button>
   </form>
    <div>{users.map()}</div>
  </div>
////////// SUSPENSE AND STREAMING
export const dynamic = 'force-dynamic'; // disable component exported as static in order to run client interaction
await fetch(...,{ cache: "no-cache" }); // {next: { revalidate: 3600 }}
////////// MIDDLEWARE
app/middleware.ts

export function middleware(request: NextRequest){
  const isAuthenticated = false;
  if (!isAuthenticated){
    return NextResponse.redirect("/login");
  }
  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard", "/account"];
}
//////// PAGINATION

////////// CACHE

///////// AUTH

/*************************** ROUTER (WOUTER) *****************************/
<Link href="/users/1">Profile</Link>
<Redirect to="/logout" />

//////// COMPONENTS API ///////////////////
<Switch>
  <Route path="/about">About us</Route>
  <Route path="/contact"> <ContactForm /> </Route>
  <Route path="/users/:name">{(params)=> <div>Hello, {params.name}!</div></Route>
  <Route path="/profile" component={ProfilePage} />
  <Router base="/job">
    <Route path="/payments" component={PaymentsPage} />
  </Router>
  <Route> Rendered if anything matches </Route>
</Switch>

//////// HOOKS API //////////////
const [match, params] = useRoute("/users/:id");
const [location, setLocation] = useLocation(); // setLocation("/somewhere"), location = current page
const params = useParams(); //params.id for path="/user/:id"
navigate("/new-route") // navigate("/home", {replace: true});

/************************** ZUSTAND *************************************/
import {create} from 'zustand';

const useProfileStore = create(set => ({
  name: "Max",
  age: 33,
  changeName: (newName) => set(state => ({name: newName})),
  increaseAge: () => set(state=> ({age: state.age + 1})),
  unname: () => set({name: ""}),
}));

const completeState = useProfileStore();

const name = useProfileStore(state => state.name);
<p>{name}</p>

const changeName = useProfileStore(state => state.changeName);
<button onClick={()=> changeName("Pedro")}>Rename </button>

/************************* REACT QUERY ********************************/
const queryClient = new QueryClient();

<QueryClientProvider client={queryClient}>
  <App />
</QueryClient>

const [search, setSearch] = useState("");

const {data: todos, loading} = useQuery({
  queryFn: ()=> fetchDataFn(search),
  queryKey: ["todos", {search}],
  staleTime: Infinity, //or a valid numb of seconds. Don't refetch on mount if cached data exists
  cacheTime: 0, // remove caching functionallity
});

const queryClient = useQueryClient();

const {mutate, mutateAsync: addTodoMutation} = useMutation({
  mutationFn: addTodo,
  onSuccess: ()=>{
    queryClient.invalidateQueries(["todos"]);
  },
});

if (isLoading) return <div>Loading...</div>
<button onClick={async (evt) => await addTodoMutation({title})}>Add todo </button>

/************************ JEST **********************************/
import {render, fireEvent} from "@testing-library/react";
import Counter from "./MyComponent";

beforeAll(()=> recreateDb());
afterAll(()=> clearDb());
beforeEach(()=>...);
afterEach(()=>...);

describe(Counter, () =>{
  it("check initial value", () => {
    const initialValue = 0;
    const {getByTestId} = render(<Counter initial={initialValue} />);
    const count = getByTestId("count").innerText; // <p data-testid="count"> {{ count }} </p>
    expect(count).toEqual(initialValue);
  });

  it("check if button works", () => {
    const initialValue = 0;
    const {getByTestId, getByRole} = render(<Counter initial={initialValue} />);
    const button = getByRole("button", {name: "Increment"}); // <button> Increment </button>
    fireEvent.click(button);
    const count = getByTestId("count").innerText;
    expect(count).toEqual(initialValue);
  });
});

//////// REACT QUERY

//////// Zustand

