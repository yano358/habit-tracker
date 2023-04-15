import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import type { Todo } from "$types/todos";

export const todosApi = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:3000" }),
  endpoints: (build) => ({
    getTodos: build.query<Todo[], void>({
      query: () => "/todos",
    }),
  }),
});
