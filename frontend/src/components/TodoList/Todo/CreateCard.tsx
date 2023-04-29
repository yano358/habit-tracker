import { TextField } from "@mui/material";
import { useState } from "react";

interface Props {
  onAdd: (title: string) => void;
}

const CreateTodoCard = ({ onAdd }: Props) => {
const [title, setTitle] = useState("");

  return (
    <TextField
      value={title}
      onChange={(e) => setTitle(e.target.value)}
      onBlur={() => {onAdd(title)}}
    />
  );
};

export default CreateTodoCard;
