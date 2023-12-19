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
