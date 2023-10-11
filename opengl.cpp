#include <glad/glad.h>
#include <GLFW/glfw3.h> // -lglfw3 -lGL -lX11 -lptrread -lXrandr -lXi -ldl

// setup -> data -> VBO -> SHADERS -> render loop -> exit
int main(){
  // GLFW: setup window + opengl 3.3 core
  glfwInit();
  glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
  glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
  // GLFW: create window + set opengl context
  GLFWwindow *window = glfwCreateWindow(800, 600, "Title", NULL, NULL);
  if (window == NULL) { glfwTerminate(); return -1 };
  glfwMakeContextCurrent(window);
  // GLAD: init before any opengl call
  if (!gladLoadGLLoader((GLADloadproc) glfwGetProcAddress)) return -1;
  // Viewport: how much space of the window opengl gets for rendering?
  glViewport(0, 0, 800, 600); // from LB corner
  glfwSetFramebufferSizeCallback(window, framebuffer_size_callback); // callback for window resizing

  // VERTEX DATA

  float vertices[] = {
    -0.5f, -0.5f, 0.0f,
     0.5f, -0.5f, 0.0f,
     0.0f,  0.5f, 0.0f
  }; // up is positive

  // VBO: vertex buffer object: CREATE -> BIND -> LOAD DATA
  unsigned int VBO;
  glGenBuffers(1, &VBO); // 1. create
  glBindBuffer(GL_ARRAY_BUFFER, VBO); // 2. bind
  glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW); // 3. load data
  // GL_STREAM_DRAW:  - change | - usage
  // GL_STATIC_DRAW:  - change | + usage 
  // GL_DYNAMIC_DRAW: + change | + usage 

  const char *vertexShaderCode = "...";
  unsigned int vertexShader;
  vertexShader = glCreateShader(GL_VERTEX_SHADER); // 1.create
  glShaderSource(vertexShader, 1, &vertexShaderCode, NULL);
  glCompileShader(vertexShader);

  const char *fragmentShaderCode = "...";
  unsigned int fragmentShader; 
  fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
  glShaderSource(fragmentShader, 1, &gragmentShaderCode, NULL);
  glCompileShader(fragmentShader);

  unsigned int shaderProgram;
  shaderProgram = glCreateProgram();
  glAttachShader(shaderProgram, vertexShader);
  glAttachShader(shaderProgram, fragmentShader);
  glLinkProgram(shaderProgram);

  glUseProgram(shaderProgram);
  glDeleteShader(vertexShader);
  glDeleteShader(fragmentShader);
  
  // RENDER loop
  while (!glfwWindowShouldClose(window)){
    processInput(window);
    glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT); // also GL_DEPTH_BUFFER_BIT / GL_STENCIL_BUFFER_BIT
    glfwPollEvents(); // poll events
    glfwSwapBuffers(window); // draw
  }
  // Exit
  glfwTerminate();
  return 0;
}


/********************** CALLBACKS and extra functions ****************************/
void framebuffer_size_callback(GLFWwindow *window, int width, int height){ glViewport(0, 0, width, height); }
void processInput(GLFWwindow *window){ if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) glfwSetWindowShouldClose(window, true); }

/********************* VERTEX SHADER *********************************************/
#version 330 core // 1.version opengl
layout (location=0) in vec3 aPos; //2.input attribute

void main(){
	gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
}

/******************** FRAGMENT SHADER ********************************************/
#version 330 core
out vec4 FragColor;

void main(){
    FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);
}
