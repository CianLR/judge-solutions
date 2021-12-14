
let maybe_read_line () =
  try Some(read_line ())
  with End_of_file -> None

let rec read_input () =
  match maybe_read_line () with
  | Some(l) -> l :: read_input ()
  | None -> []

let line_to_point l =
  let [x; y] = List.map int_of_string (String.split_on_char ',' l) in
  (x, y)

let line_to_command l =
  Scanf.sscanf l "fold along %c=%d" (fun c d -> (c, d))

let rec split_input l =
  match l with
  | [] -> ([], [])
  | h::t ->
      if String.length h == 0 then
        ([], t)
      else
        let (f, s) = split_input t in
        (h::f, s)

let fold_x xfold point =
  let (x, y) = point in
  if x < xfold then (x, y) else
  (xfold - (x - xfold), y)

let get_unique =
  List.fold_left (fun a v -> if List.mem v a then a else v::a) []

let () =
  let input = read_input () in
  let (pts, cmds) = split_input input in
  let points = List.map line_to_point pts in
  let commands = List.map line_to_command cmds in
  let (_, d) = List.hd commands in
  let folded = get_unique (List.map (fold_x d) points) in
  Printf.printf "%d\n" (List.length folded)
