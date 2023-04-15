import { Stack } from "@mui/material";
import { useState } from "react";
import { Todo } from "$types/todos";
import CreateTodoCard from "./Todo/CreateCard";

const TodoList = () => {
  const [todos, setTodos] = useState<Todo[]>([]);

  const addTodo = (title: string) => {
    const newTodo: Todo = {
      id: todos.length + 1,
      title,
      completed: false,
    };
    setTodos([...todos, newTodo]);
  };

  return (
    <Stack direction={"column"} spacing={2}>
      {todos.map((todo) => (
        <div key={todo.id}>{todo.title}</div>
      ))}
      <CreateTodoCard onAdd={addTodo} />
    </Stack>
  );
};

export default TodoList;
