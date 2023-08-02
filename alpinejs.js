/****************** AlpineJS: 15/6/2 (attribs, props, methods) **************/
//Attributes: x- always on start, ex: x-data/x-bind

/* DATA:  state           */ data ="{open: false}" 
/* BIND:  binding         */ bind:class ="!open? 'hidden': ''" // shortcut :class
/* ON:    events          */ on:click="open != open" // shortcut: @click=".."
/* MODEL: 2 way binding   */ <div x-data="{search: ''}"> <input type="text" x-model="search"/></div>
/* INIT:   mount          */ init="date = new Date()"
/* EFFECT: reactivity     */ effect="console.log(open)"

/* TEXT:  textContent     */ text="new Date().getFullYear()"
/* HTML:  innerHTML       */ html="(await fetch('..')).data"
/* SHOW:  toggle visib    */ show="open"
/* TRANSITION: fading     */ transition

/* IF:     cond rendering */ <template x-if="open"> <div>....</div></template>
/* FOR:    loop           */ <template x-for="post in posts"> <h2 x-text="post.title" /> </template>

/* REF: ref to elem/$refs */ <input "text" x-ref="content"/> <btn x-on:click="navigator.clipboard.writeText($refs.content"/>
/* CLOAK: wait until init */ <div x-cloak/>
/* IGNORE: prevents init  */ <div x-ignore />

// Properties: $ always on start, ex: $store/$el

/* $ STORE: global store  */ x-text="$store.site.title"
/* $ EL: reference itself */ x-init="console.log($el)"
/* $ DISPATCH: custom evt */ <div x-on:notify=".."><button x-on:click="$dispatch('notify')"/></div> 
/* $ WATCH: cb data change*/ <div x-init="$watch('count', val => console.log(val))" />
/* $ REFS: refer dom elem */ <div x-init="$refs.button.remove()"> <button x-ref="button"/></div>
/* $ NEXTTICK: paint tick */ <div x-text="$nextTick(()=> console.log(new Date()))" />

//Methods: on module Alpine (Alpine.data/Alpine.store)

/* . DATA: Access to local state from JS script */ 
<div x-data="dropdown"/>
Alpine.data('dropdown', () => ({open: false, toggle(){ this.open != this.open }));

/* . STORE: Declare global store from JS script */
<button x-on:click="$store.notifications.notify('...')" />
Alpine.store('notifications', { items: [], notify(msg){ this.items.push(msg) }});


// Event Modifiers: ex: @click.prevent
.prevent  // preventDefault()
.stop	  // stopPropagation()
.outside  // listen for clicks outside of the element
.window   // register the evt listener on root window instead of element
.document // same as .window
.once     // handler called once
.debounce // .debounde.250ms by default. Call the evt after Xms from previous call
.throttle // same a .debounce but at fixed Xms intervals
.self     // call only if event originate on itself and not a child
.passive  // @touchstart.passive for optimizing performance on touch devices

// Transition helpers: ex: x-transition.duration.500ms

.duration.500ms
:enter.duration...
:leave.duration...
.delay.50ms
.opacitiy
.scale.80 // 80%, :enter.scale.80 or :leave.scale.80

// Transition classes: ex: x-transition:enter="transition ease-out duration-300" custom css classes
:enter //TODO: compress and add summary
:enter-start
:enter-end
:leave
:leave-start
:leave-end






/*============== EXTRA SECTIONS ===================== */
// Things that will use in rare circunstances so should pay little attention
/***** Modifiers ****************/
.camel    //listen for cammelCase events like customEvent instead of custom-event
.dot      // same as cammel with a dot: custom.event
.capture  // call the listener in the capture instead of bubbling

// TODO: Advanced topic to checkout later: ttps://alpinejs.dev/advanced/reactivity
