
let maybe_read_int () =
  try Some(int_of_string (read_line ()))
  with End_of_file -> None

let rec read_ints () =
  match maybe_read_int () with
  | Some(line) -> line :: read_ints ()
  | None -> []

let rec ascending l =
  match l with
  | [] -> 0
  | _ :: [] -> 0
  | a :: b :: t ->
      let rest = ascending (b :: t) in
      if b > a then rest + 1 else rest

let () =
  let ints = read_ints () in
  Printf.printf "Answer: %d\n" (ascending ints)

