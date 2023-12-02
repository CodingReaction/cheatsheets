// CLI
npx create-next-app@latest .

//Routing and Navigation
// src/app --> all pages

page.tsx            // "/"
posts/[id]/page.tsx // "posts/3/"

// layout.tsx contains <Header /> { children } <Footer /> // children: React.ReactNode


export const metadata:Metadata = { // inside layout.tsx
  title: "Create Next App",
  description: "Description of site"
};

// COMPONENTS
<Link href={...}> // client side <a href...>
<Image src="..." width="50" height="50" />

export default async function MyServerComponent({params}){
    const response = await fetch(...);
    const data = await response.json();

    return <h1>...</h1>
}

// SERVER ACTIONS
const addPost = async (formData: FormData) => {
  "user server";

  await prisma.post.create({data: {title: formData.get("title") as string,}});
  revalidatePath("/posts"); // rerun the posts route
}

return <form action={addPost}> </form>

// inside the SubmitBtn component of the form
const {pending} = useFormStatus();

<button type="submit" disabled={pending} />

// SUSPENSE AND STREAMING

export const dynamic = 'force-dynamic'; // disable component exported as static in order to run client interaction
await fetch(...,{ cache: "no-cache" }); // {next: { revalidate: 3600 }}
//
// MIDDLEWARE
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

// React Query

// Zustand
