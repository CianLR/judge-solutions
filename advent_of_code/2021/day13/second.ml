
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

let fold_y yfold point =
  let (x, y) = point in
  if y < yfold then (x, y) else
  (x, yfold - (y - yfold))

let get_unique =
  List.fold_left (fun a v -> if List.mem v a then a else v::a) []

let fold points command =
  let (c, d) = command in
  let fold_func = if c == 'x' then fold_x else fold_y in
  get_unique (List.map (fold_func d) points)

let print_points points =
  let max_x = List.fold_left (fun a (x, _) -> if a > x then a else x) 0 points in
  let max_y = List.fold_left (fun a (_, y) -> if a > y then a else y) 0 points in
  for y = 0 to max_y do
    for x = 0 to max_x do
      Printf.printf (if List.mem (x, y) points then "#" else ".")
    done;
    Printf.printf "\n"
  done

let () =
  let input = read_input () in
  let (pts, cmds) = split_input input in
  let points = List.map line_to_point pts in
  let commands = List.map line_to_command cmds in
  let folded = List.fold_left fold points commands in
  print_points folded
