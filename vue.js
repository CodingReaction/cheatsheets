/*********** Component declaration: SFC or single file component ************/
// Every component is composed of 3 parts: logic in script / things to render on template / css on style
<script setup lang="ts">
</script>

<template>
</template>

<style scoped lang="scss">
</style>

/************* Templating language ***************************/

// Dinamic props
<p> {{ name }} </p> // name declared in <script setup ...> Check reactivity section later
<div class="toggle-button"></div> // Don't need className [like React] for string class
<div :class="{'is-visible': isVisible, 'positive': count >= 0}"></div> // if isVisible is true then add is-visible class, if count >=0 then add count class
<input v-model="user.email" /> // two way data binding, the same as doing v-on:change + v-bind:name on the same sentence

// Directives of data/events
v-on:click="onClick()" // @click=".." // @click.prevent
v-bind:name=""	       // :name=".."
v-model                // explained above, two way data binding

// Conditional rendering and loops
<h1 v-if="awesome">Vue is awesome!</h1>    // if
<h1 v-else-if="count > 0"> Could be? </h1> // else if
<h1 v-else>Not so fast!</h1>		   // else
<h1 v-show="ok">Hello! </h1>		  // toggles the CSS display prop
<TodoItem v-for="todo in todos" :key="todo.id" :todo="todo" />

<template v-if="ok">
	<div>..</div>
	<div>..</div>
</template> // group elements

// Children (Slot or Outlet)
<MyApp>
  <template #default> <Todos /> </template> // passing <Todos /> as a children of <MyApp> with tag "default"
</MyApp>

<main> <slot name="default">Fallback content</slot> </main> // inside MyApp template declaration, render the passed children with tag "default"

// Attributes inheritance
"https://vuejs.org/guide/components/attrs.html#attribute-inheritance-on-multiple-root-nodes"

/**************** Prop drilling (passing props to children) ****************************/
const props = defineProps({ // first method
    name: {
        type: String,
	default: "Max",},
    onClick: {
        type: Function,
	default: () =>{}},
    todo: {
	type: Object as PropType<TodoType>,
	required: true},
});

type Props = {....}; // second method
const props = defineProps<Props>();
import type {TodoItemProps} from "./types";

/******************** Types validated on runtime *******************************************/
String | Number | Boolean | Array | Object | Date | Function | Symbol

/*********************** Event drilling (passing events to children and execute on parent) **********************/
const emit = defineEmits(["subscribe-news"]); //child emits
const handleSubmit = () => { emit("subscribe-news", extraData) };

<Form @subscribe-news="parentCallback" /> // parent listener

/***************** Reactivity *******************************/
import {ref, onMounted, type Ref, type PropType} from "vue";

const inputRef: Ref<HTMLInputElement | null> = ref(null); // DOM manipulation
onMounted(() =>{
    if (inputRef.value != null){
        inputRef.value.focus();
    }
});

const valueRef = ref(3); // valueRef.value to access from inside the <script /> // same as useState() in react
const myData = reactive<User>({name: "Max", age: 33}); // myData.name // also same as useState in react

/*************  Vue composables (TODO) ***********************/

/*************  Lifecycle events *****************************/
onMounted(() =>{});
onUpdated(()=>{});
watchEffect(() => { ...= title.value}); // watch also exists

/************* Global state management: Pinia lib ************/
// on store/todos.js
import {defineStore} from "pinia";
export const useTodosStore = defineStore("todos", {
	state: () => ({todos: []}), // declare your initial state
	actions: { //reducers
		addTodo(text){
			if (!text) return;
			this.todos.push({});
		}
	getters: { // optional part for returning the state with changes without mutating it
		filteredTodos(){
		    if (this.filter === "finished"){
			return this.todos.filter(todo => todo.isFinished);
		    }
		}
});

// Pinia usage from component itself
import {storeToRefs} from "pinia";
import {useTodosStore} from "./store/todos";
const {todos, addTodo} = storeToRefs(useStodosStore());


/******************** SPA Router: Vue router v4 *****************************/
npm install vue-router@4

<div id="app">
  <h1>Hello app</h1>
  <router-link to="/">Go to home</router-link>
  <router-link to="/about">Go to About</router-link>
  <router-view></router-view>
</div> // <router-link /> is an <a ..> tag that modifies the local history

const routes = [ // create a router file somewhere, most of time vue creates it for you
  { path: "/", component: Home},
  { path: "/about", component: About},
  {
     path: "/user/:id",
     name: "user",
     component: User,
     children: [          // /user/:id/profile
       {
         path: "profile",
	       component: UserProfile,
       }
     ],
  },
];

const router = VueRouter.createRouter({ // this part is almost automagically added by vue on project generation
  history: VueRouter.createWebHashHistory(),
  routes: routes
});
app.use(router);


router.beforeEach(async (to, from) => {  // wanna check if user is loged or redirect? easy!
  if (!isAuthenticated && to.name !== "Login") return {name: "Login"}
  //return false // cancels navigation intent
});

router.push("/about") //force nav inside component
router.push({path: "/about"});
router.push({name: "user", params: {username: "eduardo"}}); // /user/eduardo
router.push({path: "/register", query: {plan: "private"}}); // /register?plan=private
router.replace({path: "/home"});
router.go(1)
router.go(-1);

// Keep exploring on https://router.vuejs.org/guide/advanced/meta.html

/********************************* Catching (vue-query): TODO ***********************************************/

/********************* Testing Vitest ***************************/
import {describe, it, expect} from "vitest";

describe("#sum", () =>{
	it("returns 0 with no numbers", () =>{
		expect(sum()).toBe(0);
	})
	it("returns same number with one number", () =>{
		expect(sum(2)).toBe(3);
	}
});

// vue test utils use stub (npm install --save-dev @vue/test-utils)
// HappyDom and jsdom for dom testing
NotificationToast.test.js
import {moun} from "@vue/test-utils";
	import NotificationToast from "Notif.vue"
	import {describe, expect, test} from "vitest";

describe("Notification component", () =>{
  test("renders the correct style for error", () =>{
    const status = "error";
    const wrapper = mount(NotificationToast, {
        props: {status }});
    expect(wrapper.classes()).toEqual(expect.arrayContaining(["notification--error"]));
  }
  test("emits event when close button is clicked", async () =>{
    const wrapper = mount(NotificationToast, {
        data(){ return {clicked: false }}
    });
    const closeButton = wrapper.find("button");
    await closeButton.trigger("click")
    expect(wrapped.emitted()).toHaveProperty("clear-notification");
  });
}

/**************************** Testing Cypress: TODO **************************/

/**************************** Transitions: TODO ******************************/

/**************************** Popular libs: TODO *****************************/

