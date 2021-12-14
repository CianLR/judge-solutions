
let maybe_read_line () =
  try Some(read_line ())
  with End_of_file -> None

let rec read_input () =
  match maybe_read_line () with
  | None -> []
  | Some(l) -> l :: read_input ()

let parse_line l =
  Scanf.sscanf l "%d,%d -> %d,%d" (fun a b c d -> (a, b, c, d))

let line_to_points (sx, sy, ex, ey) =
  if sx == ex then
    let (lo, hi) = if sy < ey then (sy, ey) else (ey, sy) in
    List.init ((hi - lo) + 1) (fun k -> (sx, lo + k))
  else if sy == ey then
    let (lo, hi) = if sx < ex then (sx, ex) else (ex, sx) in
    List.init ((hi - lo) + 1) (fun k -> (lo + k, sy))
  else
    []

let fill_hashtbl points =
  let grid = Hashtbl.create (List.length points) in
  List.iter (fun p -> Hashtbl.add grid p true) points;
  grid

let get_unique l =
  let grid = Hashtbl.create (List.length l) in
  let incl a v =
    match Hashtbl.find_opt grid v with
    | Some(_) -> a
    | None ->
        begin
          Hashtbl.add grid v true;
          v::a
        end
  in
  List.fold_left incl [] l

let is_dupe hash v =
  let bindings = Hashtbl.find_all hash v in
  (List.length bindings) > 1

let () =
  let input = read_input () in
  let lines = List.map parse_line input in
  let grouped_points = List.map line_to_points lines in
  let points = List.flatten grouped_points in
  let grid = fill_hashtbl points in
  let unq_points = get_unique points in
  let dupes = List.length (List.filter (is_dupe grid) unq_points) in
  Printf.printf "Dupes: %d\n" dupes;

