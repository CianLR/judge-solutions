
let read_command () =
  try Some(Scanf.scanf "%s %d\n" (fun c v -> (c, v)))
  with End_of_file -> None

let rec read_commands () =
  match read_command () with
  | Some(line) -> line :: read_commands ()
  | None -> []

let apply_command (h, d, a) (ax, fx) =
  (h + fx, d + (a * fx), a + ax)

let rec convert_commands commands =
  match commands with
  | [] -> []
  | c :: t -> (
      match c with
      | ("forward", v) -> (0, v)
      | ("down", v) -> (v, 0)
      | ("up", v) -> (-v, 0)
      | _ -> (0, 0)) :: convert_commands t

let run commands =
  let mapped = convert_commands commands in
  List.fold_left apply_command (0, 0, 0) mapped

let () =
  let commands = read_commands () in
  let (h, d, _) = run commands in
  Printf.printf "Answer: %d\n" (h * d)

